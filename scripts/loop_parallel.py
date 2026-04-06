#!/usr/bin/env python3
"""Loop-level parallelism demo using serial and multiprocessing execution."""

from __future__ import annotations

import multiprocessing as mp
import time
from typing import Tuple

import numpy as np


def kernel(chunk: Tuple[np.ndarray, np.ndarray, float]) -> np.ndarray:
    x, y, alpha = chunk
    out = np.empty_like(x)
    for i in range(len(x)):
        out[i] = alpha * x[i] + y[i]
    return out


def serial_saxpy(x: np.ndarray, y: np.ndarray, alpha: float) -> np.ndarray:
    out = np.empty_like(x)
    for i in range(len(x)):
        out[i] = alpha * x[i] + y[i]
    return out


def parallel_saxpy(x: np.ndarray, y: np.ndarray, alpha: float, workers: int) -> np.ndarray:
    x_chunks = np.array_split(x, workers)
    y_chunks = np.array_split(y, workers)
    payload = [(xc, yc, alpha) for xc, yc in zip(x_chunks, y_chunks)]

    with mp.Pool(processes=workers) as pool:
        parts = pool.map(kernel, payload)
    return np.concatenate(parts)


def main() -> None:
    n = 8_000_000
    workers = max(2, mp.cpu_count() // 2)

    x = np.random.rand(n).astype(np.float32)
    y = np.random.rand(n).astype(np.float32)
    alpha = 2.75

    t0 = time.perf_counter()
    s = serial_saxpy(x, y, alpha)
    t1 = time.perf_counter()

    t2 = time.perf_counter()
    p = parallel_saxpy(x, y, alpha, workers)
    t3 = time.perf_counter()

    assert np.allclose(s, p)

    serial_time = t1 - t0
    parallel_time = t3 - t2
    speedup = serial_time / parallel_time if parallel_time > 0 else float("inf")

    print("=== Loop-Level Parallelism Experiment ===")
    print(f"Elements: {n}")
    print(f"Workers: {workers}")
    print(f"Serial time: {serial_time:.6f} s")
    print(f"Parallel time: {parallel_time:.6f} s")
    print(f"Speedup: {speedup:.2f}x")


if __name__ == "__main__":
    main()
