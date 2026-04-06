#!/usr/bin/env python3
"""GPU DLP case study: matrix multiplication on CPU vs GPU (if available)."""

from __future__ import annotations

import time

import numpy as np


def run_cpu(n: int) -> float:
    a = np.random.rand(n, n).astype(np.float32)
    b = np.random.rand(n, n).astype(np.float32)
    t0 = time.perf_counter()
    _ = a @ b
    t1 = time.perf_counter()
    return t1 - t0


def run_gpu(n: int):
    try:
        import cupy as cp
    except Exception:
        return None, "CuPy not installed or CUDA runtime unavailable"

    a = cp.random.rand(n, n, dtype=cp.float32)
    b = cp.random.rand(n, n, dtype=cp.float32)

    cp.cuda.Stream.null.synchronize()
    t0 = time.perf_counter()
    _ = a @ b
    cp.cuda.Stream.null.synchronize()
    t1 = time.perf_counter()

    return (t1 - t0), None


def main() -> None:
    n = 1024

    cpu_time = run_cpu(n)
    gpu_time, err = run_gpu(n)

    print("=== GPU DLP Case Study: Matrix Multiplication ===")
    print(f"Matrix size: {n}x{n}")
    print(f"CPU (NumPy) time: {cpu_time:.6f} s")

    if err is not None:
        print(f"GPU run skipped: {err}")
        print("For full GPU evaluation, install CuPy and run on a CUDA-capable system.")
        return

    print(f"GPU (CuPy) time: {gpu_time:.6f} s")
    print(f"Speedup: {cpu_time / gpu_time:.2f}x")


if __name__ == "__main__":
    main()
