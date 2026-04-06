#!/usr/bin/env python3
"""Simple vector-architecture style simulation for DLP analysis."""

from __future__ import annotations

import math
import time

import numpy as np


def scalar_add(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    out = np.empty_like(a)
    for i in range(len(a)):
        out[i] = a[i] + b[i]
    return out


def vector_add(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a + b


def simulate_vector_cycles(length: int, lanes: int, startup_cycles: int = 12) -> int:
    # Simplified model: one vector instruction startup + issue per lane group.
    return startup_cycles + math.ceil(length / lanes)


def main() -> None:
    n = 5_000_000
    lanes = 8

    a = np.random.rand(n).astype(np.float32)
    b = np.random.rand(n).astype(np.float32)

    t0 = time.perf_counter()
    scalar = scalar_add(a, b)
    t1 = time.perf_counter()

    t2 = time.perf_counter()
    vector = vector_add(a, b)
    t3 = time.perf_counter()

    assert np.allclose(scalar, vector)

    scalar_time = t1 - t0
    vector_time = t3 - t2
    speedup = scalar_time / vector_time if vector_time > 0 else float("inf")

    scalar_cycles_model = n
    vector_cycles_model = simulate_vector_cycles(n, lanes)

    print("=== Vector Architecture Simulation ===")
    print(f"Vector length (N): {n}")
    print(f"Assumed vector lanes: {lanes}")
    print(f"Scalar execution time: {scalar_time:.6f} s")
    print(f"Vectorized execution time: {vector_time:.6f} s")
    print(f"Measured speedup: {speedup:.2f}x")
    print(f"Model scalar cycles: {scalar_cycles_model}")
    print(f"Model vector cycles: {vector_cycles_model}")
    print(f"Model speedup: {scalar_cycles_model / vector_cycles_model:.2f}x")


if __name__ == "__main__":
    main()
