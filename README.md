# RouteIQ - Data Science Project

## Project Overview
This repository is used for Data Science sprint milestones. It currently contains environment verification notes and a notebook proving disciplined use of Markdown and Code cells.

## Current Milestone Artifact

### Notebook Cell Discipline (Implemented)
- **Notebook file**: `notebooks/notebook_cell_discipline.ipynb`
- **Purpose**: Demonstrate clear separation of explanation and execution
- **Included structure**:
  - Markdown title/purpose cell
  - Two Markdown explanation cells
  - Two Code cells with simple Python commands
  - Executed outputs saved in notebook

### Why This Matters
- Markdown cells make notebooks readable for reviewers and collaborators.
- Code cells stay focused on execution.
- Clear Markdown-to-Code alignment reduces confusion during handoff and grading.

## How To Validate Notebook Structure
Use the project verification script to check notebook requirements automatically:

```powershell
python verify_setup.py --notebook-only
```

Validate a custom notebook path:

```powershell
python verify_setup.py --notebook notebooks/notebook_cell_discipline.ipynb --notebook-only
```

## Video Walkthrough Checklist (~2 Minutes)
- Open `notebooks/notebook_cell_discipline.ipynb`
- Scroll through the notebook structure
- Execute one Code cell
- Render/show one Markdown cell
- Convert one cell between Code and Markdown
- Explain when to use Code vs Markdown
- Explain how separation improves readability and review quality

## Scenario Talking Points (Mandatory)
If explanations are written only as code comments and there are no Markdown cells:
- Readability drops because intent is hidden inside executable blocks
- Collaboration slows because reviewers must parse code to understand narrative
- Execution and explanation become tightly mixed, which increases maintenance cost
- The fix is to move narrative into Markdown sections and keep Code cells execution-only

## Resources
- [Anaconda Documentation](https://docs.anaconda.com/)
- [Python Documentation](https://docs.python.org/3/)
- [Jupyter Documentation](https://docs.jupyter.org/)

---
*Last Updated: April 9, 2026*
*Milestone Status: Notebook structure proof added*
