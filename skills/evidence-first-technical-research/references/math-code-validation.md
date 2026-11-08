# Mathematical, code and experiment validation

## A. Equation verification

For each pivotal equation:

1. State the source locator and whether the displayed formula is copied, algebraically derived, approximated, or adapted.
2. Define every variable and units; specify shape (e.g., 3x3 covariance, 2x3 Jacobian).
3. Specify coordinate frame (world-to-camera vs camera-to-world), handedness, pixel axes, depth sign, row/column vector convention.
4. Show the nontrivial step; check dimension compatibility and known limits (e.g., zero opacity, infinite depth, equal isotropic scales).
5. State the domain: invertibility, differentiability, regularity, normalization, clipping, conditioning, numerical epsilon.
6. Check at least one calculable example when material. Prefer numerical comparison with finite differences for derivatives where executable tools exist.
7. Label an illustration as *pedagogical* if it intentionally omits terms, smoothing, CUDA branch logic, or numerical stabilizers.

### Example: 3DGS covariance projection

Given world covariance S_w, camera rotation R_wc, and projection Jacobian J, a local first-order projection gives S_img ~= J R_wc S_w R_wc^T J^T. Specify that this approximates a non-linear perspective transform around a mean, and is not globally exact for large Gaussian extent. Verify J is 2x3 and S_img 2x2. Some camera models require different projectors or ray tracing; do not extrapolate pinhole code to fisheye without checking.

## B. Paper -> code trace

Before claiming method/code correspondence:

1. Identify official repo and pin SHA/tag/commit; distinguish third-party forks.
2. Find entrypoint -> config -> data loader -> forward -> loss -> backward -> optimizer -> persistence -> evaluation.
3. Read the invoked function body **and callers**. A README signature is insufficient.
4. Identify default branch, optional flags, schedule, thresholds, dtype, device, shape, visible-mask handling, and optimizer-state updates.
5. Compare code against paper equations and supplementary. Record divergences as `PAPER_CODE_MISMATCH`, not automatically as bugs.
6. Validate import and dependencies if runnable; use a minimal unit test with known expected behavior. Running a test is evidence only for its specific environment and inputs.
7. For code changes, verify tests and meaningful before/after behavior; if not executable, say "not run" and show an exact proposed test.

## C. Gradient and numeric tests

- Analytic derivative: compare to finite differences where smoothing and branches permit.
- Optimization: compare one-step update under a documented optimizer and known initial state; keep sigmoid/log-scale parameterizations explicit.
- Projection: verify occlusion and coordinate conventions, with camera at identity and a translated camera.
- State changes: densification/pruning alters tensor size and optimizer state. Check edge cases N=0, all-pruned, duplicate samples, threshold equality.
- Timing: use warm-up and synchronization when GPU timings matter; report preprocessing, training, inference, and rendering separately.
- Quality: name held-out views, resolution, exact image metric implementation, masking/background, postprocessing.

## D. Code claims and run claims

| Statement | Required observation |
| --- | --- |
| "The repository has a function X" | Read file/function at path + revision |
| "This branch does Y" | Trace conditional, values and callers |
| "It passes tests" | Execute tests, record command, output and environment |
| "It uses N GB VRAM" | Run profiler or cite source's measured setup |
| "The paper implements Y" | Inspect code; otherwise say "paper proposes Y" |
| "Fastest/lowest cost" | Comparable benchmark or bounded claim |

Do not execute untrusted repository commands blindly; inspect scripts and dependencies before running. Respect code security and policy constraints.
