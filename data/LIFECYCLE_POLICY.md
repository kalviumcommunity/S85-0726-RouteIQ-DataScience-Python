# Data Lifecycle Policy

This project enforces one-directional data flow:

1. `data/raw` (immutable inputs)
2. `data/processed` (derived datasets)
3. `outputs` (artifacts such as plots, reports, models)

## Principles

- Never overwrite raw source data.
- Keep processed data reproducible from raw data.
- Keep outputs separate from data inputs.
- Use clear and consistent names to reduce ambiguity.

## Anti-Patterns To Avoid

- Saving cleaned files back into `data/raw`
- Writing plots or model binaries into `data/raw` or `data/processed`
- Depending on output artifacts as pipeline inputs

Following this policy improves reproducibility, traceability, and trust.
