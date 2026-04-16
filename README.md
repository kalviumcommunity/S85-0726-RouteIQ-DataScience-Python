# RouteIQ - Data Science Sprint Repository

## Project Overview
This repository tracks milestone evidence for Data Science workflow discipline:
- notebook structure (Markdown vs Code separation)
- kernel management (interrupt/restart/rerun)
- data lifecycle organization (raw, processed, outputs)

## Current Milestone: Data Lifecycle Organization

### Implemented Folder Structure
- `data/raw` - original source data only (immutable)
- `data/processed` - cleaned/transformed data derived from raw
- `outputs` - artifacts such as plots, reports, and model files

### Governance Files Added
- `data/raw/README.md` - raw data immutability rules
- `data/processed/README.md` - processed data traceability rules
- `outputs/README.md` - output artifact storage rules
- `data/LIFECYCLE_POLICY.md` - one-directional data flow policy

### Why This Matters
- Protects raw data from accidental overwrites
- Preserves traceability from input to derived datasets
- Prevents contamination by separating outputs from inputs
- Improves reproducibility and collaboration quality

## Verification Commands

Validate notebook structure milestone:

```powershell
python verify_setup.py --notebook-only
```

Validate kernel control milestone:

```powershell
python verify_setup.py --kernel-only
```

Validate data lifecycle milestone:

```powershell
python verify_setup.py --data-only
```

## Data Lifecycle Video Walkthrough Checklist (~2 Minutes)
- Open `data/raw` and explain why raw data is read-only
- Open `data/processed` and explain derived/recreatable datasets
- Open `outputs` and explain artifacts belong here, not in data inputs
- Briefly open `data/LIFECYCLE_POLICY.md`
- Explain one-directional flow: raw -> processed -> outputs

## Mandatory Scenario Talking Points
If raw, processed, and outputs are mixed together:
- Teams can overwrite raw evidence and lose auditability
- It becomes unclear which files are inputs vs final results
- Reproducibility fails because derivation paths are ambiguous
- Fix by restoring strict folder separation and enforcing flow rules

## Existing Notebook Milestone Artifacts
- `notebooks/notebook_cell_discipline.ipynb`
- `notebooks/kernel_control_demo.ipynb`

## Resources
- [Anaconda Documentation](https://docs.anaconda.com/)
- [Python Documentation](https://docs.python.org/3/)
- [Jupyter Documentation](https://docs.jupyter.org/)

---
*Last Updated: April 15, 2026*
*Milestone Status: Data lifecycle organization proof added*





## Python Script

- Script location: src/main.py
- Purpose: Perform simple data analysis using Python
- Features:
  - Calculates sum and average
  - Prints outputs
  - Demonstrates basic data handling

## How to Run

```bash
python src/main.py



## Conditional Logic

This script demonstrates:

- Basic if statement
- if-else decision making
- if-elif-else for multiple conditions
- Logical operators (and, or, not)
- String comparisons

These are used to control program flow based on data.