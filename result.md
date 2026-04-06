# Results and Screenshot Evidence

Use this file to attach all required visual evidence for submission.

## Screenshot Checklist

- [ ] Environment setup (Python version, virtual environment activation)
- [ ] Vector simulation run output
- [ ] SIMD benchmark compile command and run output
- [ ] Loop-level parallelism run output
- [ ] GPU case study output (or clear note if GPU unavailable)
- [ ] At least one performance chart/table image

## Evidence Log Template

| ID | Requirement | Screenshot File | Description | Rubric Mapping |
|---|---|---|---|---|
| S1 | Configuration/setup | `screenshots/setup.png` | Python env and dependency install | Technical Accuracy, Clarity |
| S2 | Vector architecture simulation | `screenshots/vector_run.png` | Scalar vs vector timings and modeled speedup | Concepts, Depth |
| S3 | SIMD implementation | `screenshots/simd_compile_run.png` | Compile flags, AVX2/scalar timings, validation | Technical Accuracy, Depth |
| S4 | Loop-level parallelism | `screenshots/loop_parallel_run.png` | Serial vs parallel timing and speedup | Concepts, Depth |
| S5 | GPU case study | `screenshots/gpu_run.png` | CPU vs GPU timing (or GPU unavailable note) | Concepts, Critical Thinking |
| S6 | Performance visualization | `screenshots/performance_chart.png` | Consolidated comparison graph/table | Clarity, Depth |

## Recommended Chart Contents

Create one chart (or table screenshot) with:

- Scalar vs vectorized time for vector add
- Scalar vs SIMD time for C benchmark
- Serial vs parallel time for loop experiment
- CPU vs GPU time for matrix multiplication (if available)

## Notes for Final Submission

- Keep screenshot file names exactly as listed for clean traceability.
- If GPU is unavailable, include explicit terminal output proving fallback behavior.
- Ensure all numbers in `report.md` discussion match captured evidence.
