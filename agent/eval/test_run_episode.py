"""CPU-only checks of run_episode.py: full runs follow the evaluator's lifetime, not smoke assertions.

Run from the repository root: python -m unittest agent.eval.test_run_episode
"""
import asyncio
import contextlib
import io
from pathlib import Path
import signal
from types import SimpleNamespace
import tempfile
import unittest
from unittest.mock import Mock, patch

from . import run_episode as runner
from .serve_agent_only import handle_connection


class RunnerTests(unittest.TestCase):
    def test_full_has_no_smoke_hooks_or_outcome_checks(self):
        for exit_code in (0, 1):
            with self.subTest(exit_code=exit_code), tempfile.TemporaryDirectory() as directory:
                output=Path(directory)/'run'
                server=Mock(pid=101);server.poll.return_value=None
                native=Mock(pid=102,returncode=exit_code);native.poll.return_value=exit_code
                stdout=io.StringIO()
                with patch.object(runner.sys,'argv',['runner','--full','--native-python','python',
                        '--output',str(output),'--port','0']), \
                     patch.dict(runner.os.environ,{'OPENAI_API_KEY':'unit-test-only'}), \
                     patch.object(runner.os,'sched_getaffinity',return_value={0},create=True), \
                     patch.object(runner.subprocess,'Popen',side_effect=[server,native]) as popen, \
                     patch.object(runner.subprocess,'check_output',side_effect=lambda *args,**kwargs:
                                  'test-commit' if kwargs.get('text') else b''), \
                     patch.object(runner.urllib.request,'urlopen'), contextlib.redirect_stdout(stdout):
                    with self.assertRaisesRegex(RuntimeError,'No native scored result'):
                        runner.main()
                env=popen.call_args_list[0].kwargs['env']
                self.assertEqual(env['B1K_AGENT_TEST_EARLY_TURN'],'0')
                self.assertEqual(env['B1K_AGENT_SMOKE'],'0')
                self.assertEqual(env['B1K_AGENT_EXIT_ON_DISCONNECT'],'1')
                self.assertNotIn('OPENAI_API_KEY',popen.call_args_list[1].kwargs['env'])
                self.assertIn('FULL_RUN_CLOSED',stdout.getvalue())
                self.assertIn(f'"native_returncode": {exit_code}',stdout.getvalue())
                self.assertNotIn('SMOKE_PASS',stdout.getvalue())
                self.assertFalse((output/'SMOKE-RESULT.json').exists())
                self.assertFalse((output/'forks').exists())  # no fork/resume count required

    def test_wait_stops_on_connection_close_or_native_exit(self):
        with patch.object(runner.time,'sleep') as sleep:
            runner.wait_for_evaluator(Mock(poll=Mock(return_value=None)),Mock(poll=Mock(return_value=0)))
            runner.wait_for_evaluator(Mock(poll=Mock(return_value=1)),Mock())
            sleep.assert_not_called()

    def test_full_wait_reports_wall_time_limit(self):
        native=Mock()
        native.poll.return_value=None
        server=Mock()
        server.poll.return_value=None
        with patch.object(runner.time,'monotonic',side_effect=[0,7201]), \
             patch.object(runner.time,'sleep') as sleep:
            self.assertTrue(runner.wait_for_evaluator(native,server,7200))
        sleep.assert_not_called()

    def test_full_timeout_closes_native_before_policy_and_records_interruption(self):
        with tempfile.TemporaryDirectory() as directory:
            output=Path(directory)/'run'
            server=Mock(pid=101,returncode=None)
            server.poll.return_value=None
            native=Mock(pid=102,returncode=None)
            native.poll.return_value=None
            native.wait.side_effect=lambda **kwargs:setattr(native,'returncode',0)
            stdout=io.StringIO()
            with patch.object(runner.sys,'argv',['runner','--full','--native-python','python',
                    '--output',str(output),'--port','0']), \
                 patch.dict(runner.os.environ,{'OPENAI_API_KEY':'unit-test-only'}), \
                 patch.object(runner.os,'sched_getaffinity',return_value={0},create=True), \
                 patch.object(runner.subprocess,'Popen',side_effect=[server,native]), \
                 patch.object(runner.subprocess,'check_output',side_effect=lambda *args,**kwargs:
                              'test-commit' if kwargs.get('text') else b''), \
                 patch.object(runner.urllib.request,'urlopen'), \
                 patch.object(runner,'wait_for_evaluator',return_value=True), \
                 patch.object(runner,'record_interruption') as record, \
                 contextlib.redirect_stdout(stdout):
                runner.main()
            native.send_signal.assert_called_once_with(signal.SIGINT)
            server.send_signal.assert_called_once_with(signal.SIGTERM)
            record.assert_called_once()
            self.assertIn('FULL_RUN_INTERRUPTED',stdout.getvalue())

    def test_runtime_finishing_after_shutdown_is_closed(self):
        import threading
        from .serve_agent_only import close_all, tracked_runtime
        active, stop = [], threading.Event()
        class Fake:
            closed = 0
            def __init__(self, entry, epoch, config):
                if entry == 'race':
                    close_all(active, stop)        # shutdown lands while this runtime is still starting
            def close(self):
                self.closed += 1
        Tracked = tracked_runtime(Fake, active, stop)
        with self.assertRaises(RuntimeError):
            Tracked('race', 'e', {})
        self.assertEqual(len(active), 1); self.assertGreaterEqual(active[0].closed, 1)
        with self.assertRaises(RuntimeError):     # nothing new starts after shutdown
            Tracked('next', 'e', {})
        self.assertEqual(len(active), 1)

    def test_connection_shutdown_is_full_only(self):
        async def check():
            async def handler(_):pass
            for full in (False,True):
                stopped=asyncio.Event()
                await handle_connection(SimpleNamespace(_handler=handler),None,stopped,full)
                self.assertEqual(stopped.is_set(),full)
        asyncio.run(check())


if __name__=='__main__':unittest.main()
