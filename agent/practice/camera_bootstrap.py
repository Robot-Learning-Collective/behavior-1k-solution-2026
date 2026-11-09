"""One bounded native annotator warm-up retry; never substitute intrinsics."""
def read_intrinsics(cameras, array, sim):
    def read():
        return [array(sensor.intrinsic_matrix).astype(float) for sensor in cameras]
    try:
        return read()
    except AssertionError as error:
        if 'intrinsic matrix for sensor:' not in str(error) or 'is degenerate!' not in str(error):
            raise
        before=sim.current_time
        print('CAMERA_INTRINSICS_WARMUP_RETRY native render x8; original assertion retained',flush=True)
        for _ in range(8):
            sim.render()
        if abs(sim.current_time-before)>1e-9:
            raise RuntimeError('Camera bootstrap render unexpectedly advanced physics') from error
        return read()  # Exactly one retry; original native assertion still applies.
