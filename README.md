# RouteIQ - Data Science Project

## Project Overview
This repository is used for Data Science sprint work. The current milestone validates that the local development environment is working consistently before project coding begins.

## Environment Verification Status

### Verified in Terminal (Current Session)
- **Operating System**: Windows 11
- **Python command**: Working
- **Python version output**: `Python 3.14.3`
- **Conda command**: Not currently recognized in PowerShell
- **Jupyter command**: Not currently recognized in PowerShell

### Evidence Log
```powershell
python --version
# Output: Python 3.14.3

conda --version
# Output: conda : The term 'conda' is not recognized ...

jupyter --version
# Output: jupyter : The term 'jupyter' is not recognized ...
```

## What Must Be Verified For Milestone Completion
The final PR must include successful proof for all of the following:
1. `python --version`
2. `conda --version`
3. Conda environment activation (`conda activate <env_name>`)
4. Jupyter launch (`jupyter notebook` or `jupyter lab`)
5. A Python cell execution inside Jupyter

## Commands To Finish Verification
Run these in **Anaconda Prompt** first (recommended), then in PowerShell after Conda initialization.

```powershell
conda --version
conda info --envs
conda create -n ds_sprint python=3.11 -y
conda activate ds_sprint
python --version
python -c "import sys; print(sys.executable)"
jupyter notebook
```

If Jupyter is missing in the environment:
```powershell
conda activate ds_sprint
conda install jupyter -y
jupyter notebook
```

## PowerShell Fix (If `conda` Is Not Found)
Initialize Conda for PowerShell:

```powershell
conda init powershell
```

Then close and reopen PowerShell and re-run:

```powershell
conda --version
jupyter --version
```

## Video Walkthrough Checklist (~2 Minutes)
- Show `python --version`
- Show `conda --version`
- Activate the Conda environment
- Launch Jupyter Notebook or JupyterLab
- Run one Python cell successfully
- Open your PR and point to the verification evidence
- Verbally explain the scenario: terminal Python works but Jupyter uses another interpreter

## Scenario Talking Points (For Video)
- Activate the intended environment before launching Jupyter.
- Confirm active interpreter with `python -c "import sys; print(sys.executable)"`.
- In Jupyter, verify/select the kernel tied to the same Conda environment.
- If imports fail, install packages in the active environment and restart kernel.
- Consistent environment + kernel prevents version mismatch and "works in terminal but not notebook" failures.

## Resources
- [Anaconda Documentation](https://docs.anaconda.com/)
- [Python Documentation](https://docs.python.org/3/)
- [Jupyter Documentation](https://docs.jupyter.org/)

---
*Last Updated: April 8, 2026*
*Setup Status: In Progress (Python verified, Conda/Jupyter pending in PowerShell)*
