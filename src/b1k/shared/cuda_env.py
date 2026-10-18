"""Make XLA use the venv's ptxas (nvidia-cuda-nvcc wheel) instead of a system one that may not know the GPU
(e.g. Blackwell). On compute capability 10.x (B200/B300) jaxlib 0.5.x emits Triton GEMMs that ptxas rejects,
so GEMMs go to cuBLAS there. Call before the first compilation."""

import os
import pathlib
import subprocess


def ensure_packaged_ptxas() -> None:
    try:
        caps = subprocess.run(
            ["nvidia-smi", "--query-gpu=compute_cap", "--format=csv,noheader"], capture_output=True, text=True, timeout=10
        ).stdout.split()
    except Exception:
        caps = []
    flags = os.environ.get("XLA_FLAGS", "")
    if any(c.startswith("10.") for c in caps) and "xla_gpu_enable_triton_gemm" not in flags:
        os.environ["XLA_FLAGS"] = f"{flags} --xla_gpu_enable_triton_gemm=false".strip()
    try:
        import nvidia

        bin_dir = pathlib.Path(nvidia.__file__).resolve().parent / "cuda_nvcc" / "bin"
    except Exception:
        return
    if (bin_dir / "ptxas").exists() and str(bin_dir) not in os.environ.get("PATH", "").split(os.pathsep):
        os.environ["PATH"] = f"{bin_dir}{os.pathsep}{os.environ.get('PATH', '')}"
