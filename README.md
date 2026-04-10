# RouteIQ - Data Science Project

## Project Overview
This repository is used for Data Science sprint milestones. It currently contains environment verification notes and a notebook proving disciplined use of Markdown and Code cells.

## Current Milestone Artifacts

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

### Kernel Control and Execution Discipline (Implemented)
- **Notebook file**: `notebooks/kernel_control_demo.ipynb`
- **Purpose**: Demonstrate execution order, interrupt behavior, kernel restart, and state rebuild
- **Included structure**:
  - Ordered code execution showing kernel state retention
  - Long-running cell intended for safe interrupt
  - Restart-and-rerun guidance with state check cell

### Why This Matters
- Kernel state can hide mistakes when cells run out of order.
- Interrupt prevents wasting time on unintended long execution.
- Restart and rerun from top validates notebooks are reproducible for collaborators.

## How To Validate Notebook Structure
Use the project verification script to check notebook requirements automatically:

```powershell
python verify_setup.py --notebook-only
```

Validate a custom notebook path:

```powershell
python verify_setup.py --notebook notebooks/notebook_cell_discipline.ipynb --notebook-only
```

Validate kernel-control notebook expectations:

```powershell
python verify_setup.py --kernel-only
python verify_setup.py --kernel-notebook notebooks/kernel_control_demo.ipynb --kernel-only
```

## Video Walkthrough Checklist (~2 Minutes)
- Open `notebooks/notebook_cell_discipline.ipynb`
- Scroll through the notebook structure
- Execute one Code cell
- Render/show one Markdown cell
- Convert one cell between Code and Markdown
- Explain when to use Code vs Markdown
- Explain how separation improves readability and review quality

## Kernel Control Video Checklist (~2 Minutes)
- Open `notebooks/kernel_control_demo.ipynb`
- Run the first two Code cells and explain retained state
- Start the long-running cell and interrupt it safely
- Restart kernel
- Rerun cells from the top
- Explain why restart-and-run-all prevents hidden state errors

## Scenario Talking Points (Mandatory)
If explanations are written only as code comments and there are no Markdown cells:
- Readability drops because intent is hidden inside executable blocks
- Collaboration slows because reviewers must parse code to understand narrative
- Execution and explanation become tightly mixed, which increases maintenance cost
- The fix is to move narrative into Markdown sections and keep Code cells execution-only

## Kernel Scenario Talking Points (Mandatory)
If someone gets undefined variable errors when running all cells:
- The notebook was likely authored using hidden kernel state from prior ad hoc runs.
- Cells may have been executed out of order, so dependencies were not explicit.
- Restarting clears hidden state and reveals missing setup/order issues.
- Rerunning all cells from top enforces reproducible execution order.

## Resources
- [Anaconda Documentation](https://docs.anaconda.com/)
- [Python Documentation](https://docs.python.org/3/)
- [Jupyter Documentation](https://docs.jupyter.org/)

---
*Last Updated: April 9, 2026*
*Milestone Status: Notebook structure and kernel control proofs added*
