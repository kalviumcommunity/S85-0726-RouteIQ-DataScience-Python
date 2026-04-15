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

## Current Milestone: Python Data Types Fundamentals

### Files Created for This Milestone
- `data_types_fundamentals.py` - Comprehensive demonstration of numeric and string data types
- `video_demo_script.py` - Simplified script optimized for 2-minute video recording

### Key Concepts Demonstrated
- **Numeric Data Types**: Integers, floats, arithmetic operations, division behavior
- **String Data Types**: Creation, manipulation, concatenation, formatting
- **Type Mixing & Conversion**: Safe conversion between types, error handling
- **Type Inspection**: Using `type()` and `isinstance()` for debugging
- **Common Pitfalls**: Division differences, float precision, string immutability

### Video Recording Instructions
1. Open `video_demo_script.py` in your code editor
2. Start screen recording software
3. Run: `python video_demo_script.py`
4. Explain each section as it appears (numeric types, strings, type mixing, inspection)
5. Highlight key takeaways at the end

### Running the Scripts
```bash
# Comprehensive demonstration
python data_types_fundamentals.py

# Video demonstration (recommended for recording)
python video_demo_script.py
```

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