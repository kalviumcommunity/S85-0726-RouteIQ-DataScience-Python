# Python and Anaconda Setup Instructions

## Current System Status
- **Operating System**: Windows 11
- **Python Version**: 3.13.7 (already installed and verified)
- **Python Location**: C:\Python313\python.exe
- **Python Status**: Working correctly

## Anaconda Installation Steps

### Step 1: Download Anaconda
Since we encountered network issues with direct download, please download Anaconda manually:

1. **Visit the official Anaconda website**: https://www.anaconda.com/products/distribution
2. **Download the Windows version**: Anaconda3-2024.10-1-Windows-x86_64.exe
3. **Alternative download link**: https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Windows-x86_64.exe

### Step 2: Install Anaconda
1. **Run the installer** as Administrator (right-click and select "Run as administrator")
2. **Click Next** on the welcome screen
3. **Click "I Agree"** to the license agreement
4. **Choose installation type**:
   - Select "Just Me" (recommended for personal use)
5. **Choose installation location**:
   - Default: `C:\Users\<YourUsername>\anaconda3`
   - Or choose a custom location like `C:\anaconda3`
6. **Important**: Check the box that says **"Add Anaconda to my PATH environment variable"**
7. **Check the box** that says **"Register Anaconda as my default Python 3.x"**
8. **Click Install** and wait for installation to complete
9. **Click Next** on the "Thanks for installing Anaconda" screen
10. **Optional**: Uncheck the boxes for additional tutorials if you don't need them
11. **Click Finish** to complete installation

### Step 3: Verify Installation
After installation, open a **new** terminal/command prompt and run:

```bash
# Check conda version
conda --version

# Check Python version in Anaconda environment
python --version

# List conda environments
conda info --envs

# Check installed packages
conda list
```

### Step 4: Update Conda (Optional but Recommended)
```bash
conda update conda
conda update anaconda
```

### Step 5: Create a Data Science Environment (Optional)
```bash
# Create a new environment for data science
conda create -n ds_sprint python=3.11

# Activate the environment
conda activate ds_sprint

# Install essential data science packages
conda install numpy pandas matplotlib seaborn scikit-learn jupyter
```

## Troubleshooting

### If conda is not recognized after installation:
1. **Restart your computer** (this often resolves PATH issues)
2. **Add Anaconda to PATH manually**:
   - Go to Environment Variables (search in Windows Start menu)
   - Edit the PATH variable
   - Add: `C:\Users\<YourUsername>\anaconda3`
   - Add: `C:\Users\<YourUsername>\anaconda3\Scripts`
   - Add: `C:\Users\<YourUsername>\anaconda3\Library\bin`

### If Python conflicts occur:
- Use conda environments to isolate different Python versions
- Always activate the appropriate environment before working

## Verification Commands to Run After Installation

### Python Verification:
```bash
python --version
python -c "import sys; print('Python executable:', sys.executable)"
python -c "import math, os; print('Basic functionality: OK')"
```

### Anaconda Verification:
```bash
conda --version
conda info
conda list
```

### Environment Test:
```bash
# Test Jupyter Notebook
jupyter notebook --version

# Test basic data science packages
python -c "import numpy as np; import pandas as pd; print('Data Science packages: OK')"
```

## Next Steps
1. Complete Anaconda installation
2. Run verification commands
3. Create/update README.md with your setup details
4. Record a 2-minute video walkthrough showing your setup

## Notes
- Your existing Python 3.13.7 installation will remain intact
- Anaconda will create its own Python environment (typically Python 3.12)
- You can use both Python installations independently
- Conda environments help avoid package conflicts
