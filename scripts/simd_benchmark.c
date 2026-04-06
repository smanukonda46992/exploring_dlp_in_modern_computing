#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#ifdef __AVX2__
#include <immintrin.h>
#endif

static double now_seconds(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec * 1e-9;
}

static void scalar_add(const float *a, const float *b, float *out, size_t n) {
    for (size_t i = 0; i < n; i++) {
        out[i] = a[i] + b[i];
    }
}

#ifdef __AVX2__
static void avx2_add(const float *a, const float *b, float *out, size_t n) {
    size_t i = 0;
    for (; i + 8 <= n; i += 8) {
        __m256 va = _mm256_loadu_ps(a + i);
        __m256 vb = _mm256_loadu_ps(b + i);
        __m256 vr = _mm256_add_ps(va, vb);
        _mm256_storeu_ps(out + i, vr);
    }
    for (; i < n; i++) {
        out[i] = a[i] + b[i];
    }
}
#endif

int main(void) {
    const size_t n = 1 << 24;

    float *a = (float *)malloc(n * sizeof(float));
    float *b = (float *)malloc(n * sizeof(float));
    float *s = (float *)malloc(n * sizeof(float));
    float *v = (float *)malloc(n * sizeof(float));

    if (!a || !b || !s || !v) {
        fprintf(stderr, "Allocation failed\n");
        return 1;
    }

    for (size_t i = 0; i < n; i++) {
        a[i] = (float)(i % 1000) * 0.001f;
        b[i] = (float)(i % 2000) * 0.002f;
    }

    double t0 = now_seconds();
    scalar_add(a, b, s, n);
    double t1 = now_seconds();

    printf("=== SIMD Instruction Set Benchmark (AVX2) ===\n");
    printf("Elements: %zu\n", n);
    printf("Scalar time: %.6f s\n", t1 - t0);

#ifdef __AVX2__
    double t2 = now_seconds();
    avx2_add(a, b, v, n);
    double t3 = now_seconds();

    size_t bad = 0;
    for (size_t i = 0; i < n; i++) {
        if (fabsf(s[i] - v[i]) > 1e-6f) {
            bad++;
            break;
        }
    }

    printf("AVX2 time: %.6f s\n", t3 - t2);
    printf("Speedup: %.2fx\n", (t1 - t0) / (t3 - t2));
    printf("Validation: %s\n", bad ? "FAILED" : "PASSED");
#else
    printf("AVX2 not enabled in this build. Recompile with -mavx2 on x86_64.\n");
#endif

    free(a);
    free(b);
    free(s);
    free(v);

    return 0;
}
