# Assignment 5: Exploring Data-Level Parallelism (DLP) in Modern Computing

This repository contains a submission-ready package designed to maximize rubric coverage for:
- Understanding of Concepts
- Technical Accuracy
- Depth of Analysis
- Clarity and Organization
- Critical Thinking and Future Insights

## Repository Structure

- [report.md](report.md): Full written report (Parts 1-5) with analysis and discussion.
- [result.md](result.md): Screenshot checklist and evidence log for submission.
- [scripts/vector_sim.py](scripts/vector_sim.py): Vector architecture simulation and speedup analysis.
- [scripts/simd_benchmark.c](scripts/simd_benchmark.c): Scalar vs AVX2 SIMD implementation for data-parallel addition.
- [scripts/loop_parallel.py](scripts/loop_parallel.py): Loop-level parallelism experiment (serial vs multiprocessing).
- [scripts/gpu_case_study.py](scripts/gpu_case_study.py): CPU vs GPU (CuPy) matrix multiplication case study.

## Quick Start

### 1) Python setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Run experiments

```bash
python3 scripts/vector_sim.py
python3 scripts/loop_parallel.py
python3 scripts/gpu_case_study.py
```

### 3) Compile and run SIMD benchmark

```bash
cc -O3 scripts/simd_benchmark.c -o simd_benchmark
./simd_benchmark
```

Optional AVX2 path on x86_64:

```bash
cc -O3 -mavx2 scripts/simd_benchmark.c -o simd_benchmark
./simd_benchmark
```

If AVX2 is unavailable (for example, Apple Silicon), the default build still runs scalar mode and reports that AVX2 is not enabled.

## What to Submit

1. `report.md` as the main written report.
2. All scripts under `scripts/`.
3. Screenshot evidence tracked in `result.md`.
4. Optional zipped folder with generated outputs/graphs.

## Screenshot Evidence Workflow

1. Run each experiment.
2. Capture terminal output and any generated plots.
3. Save images under `screenshots/` with clear names.
4. Update corresponding entries in `result.md`.

Suggested names:
- `screenshots/vector_run.png`
- `screenshots/simd_compile_run.png`
- `screenshots/loop_parallel_run.png`
- `screenshots/gpu_run.png`
- `screenshots/performance_chart.png`

## Grading Alignment

- Concepts and architecture explanations: `report.md` (Sections 1, 2, 3).
- Technical implementation evidence: scripts + screenshots in `result.md`.
- Performance and trade-off depth: `report.md` (Sections 4, 5, 6).
- Organization and clarity: README structure + explicit run steps.
- Future trends and critical insights: `report.md` (Section 7).
