# Validation record

## Automated checks completed

Environment: Python 3.12.14, NumPy 2.3.5, Plotly 7.1.0, Streamlit 1.64.0.

`python -m unittest -v test_physics`: **11 tests passed**.

1. Crystal and detector frames are orthonormal, with proper handedness.
2. Specular centre hkl reproduces Bragg's law at multiple energies and l values.
3. All detector pixels lie on the elastic Ewald sphere after mapping.
4. Detector offsets survive ray/projection round trips.
5. Analytic rod intersections satisfy both the sphere and rod equations;
   captured points map back to their original q.
6. Zero miscut gives one geometric CTR, without duplicate parent-L hits.
7. Sub-rod spacing agrees with 2π / terrace width.
8. A 90° detector roll rotates image coordinates with the correct sign.
9. Doubling distance doubles spot offsets in millimetres.
10. The intensity grid is finite/nonnegative and the hkl derivative has rank 2.
11. Invalid top-surface incidence produces no physical captured intersections
    and a blank teaching image.

`python test_app.py`: **passed**.

- All five presets load and apply the intended sample/beam parameters.
- All four detector map modes execute.
- Aligning to (0,0,1) makes the target elastically accessible at detector centre.
- Invalid incidence displays the expected message.

The Streamlit local server started successfully. The static scientific preview
was generated from the same geometry core, rendered, and visually inspected.
The Plotly figures and self-contained HTML snapshot serialized successfully.

## Limits of verification

The interactive browser rendering was not screenshot-tested: a Chromium
runtime could not be downloaded in the execution environment. Streamlit's
AppTest executes the Python interface and widgets but does not validate WebGL
rendering, mouse gestures or browser layout. The included PNG is a separate
scientific preview, not a screenshot of the application. No Windows or macOS
machine was available to test the launch scripts.

This validates the implemented idealized geometry, not experimental calibration
or quantitative scattering intensities. The code has not been validated against
raw detector images, measured orientation matrices, structure factors or the
paper's complete roughness model. See README.md for all physics approximations.

## Default result for reproducibility

For the default oblique-step example, exact captured intersections are:

| Parent L | u (mm) | v (mm) |
|---:|---:|---:|
| -1 | 0.569 | -7.661 |
| 0 | 0.190 | -2.469 |
| 1 | -0.190 | 2.394 |
| 2 | -0.570 | 6.982 |

The detector spans ±9.6 mm in both axes. Even at symmetric centre l=0.5,
the spots are not exactly evenly spaced on the detector because the detector
samples the curved elastic shell. These are geometric centres; the teaching
brightness envelope can slightly shift an intensity maximum on a finite-width
rod. A captured geometric centre need not give an experimentally visible spot.
