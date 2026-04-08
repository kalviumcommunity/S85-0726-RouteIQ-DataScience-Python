#!/usr/bin/env python3
"""
Setup Verification Script for Python and Anaconda Installation
This script verifies that all components are working correctly.
"""

import sys
import subprocess
import os

def run_command(command, description):
    """Run a command and return the result."""
    print(f"\n{'='*50}")
    print(f"Testing: {description}")
    print(f"Command: {command}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print(f"SUCCESS: {description}")
            print(f"Output:\n{result.stdout}")
            return True, result.stdout.strip()
        else:
            print(f"FAILED: {description}")
            print(f"Error:\n{result.stderr}")
            return False, result.stderr.strip()
            
    except subprocess.TimeoutExpired:
        print(f"TIMEOUT: {description}")
        return False, "Command timed out"
    except Exception as e:
        print(f"ERROR: {description} - {str(e)}")
        return False, str(e)

def verify_python():
    """Verify Python installation."""
    print("\n" + "="*60)
    print("PYTHON INSTALLATION VERIFICATION")
    print("="*60)
    
    tests = [
        ("python --version", "Python Version Check"),
        ("python -c \"import sys; print('Executable:', sys.executable)\"", "Python Executable Location"),
        ("python -c \"import math; print('Math module OK')\"", "Math Module Test"),
        ("python -c \"import os; print('OS module OK')\"", "OS Module Test"),
        ("python -c \"import json; print('JSON module OK')\"", "JSON Module Test"),
    ]
    
    results = {}
    for command, description in tests:
        success, output = run_command(command, description)
        results[description] = {"success": success, "output": output}
    
    return results

def verify_anaconda():
    """Verify Anaconda/Conda installation."""
    print("\n" + "="*60)
    print("ANACONDA INSTALLATION VERIFICATION")
    print("="*60)
    
    tests = [
        ("conda --version", "Conda Version Check"),
        ("conda info", "Conda Information"),
        ("conda info --envs", "Conda Environments"),
        ("conda list", "Installed Packages"),
    ]
    
    results = {}
    for command, description in tests:
        success, output = run_command(command, description)
        results[description] = {"success": success, "output": output}
    
    return results

def verify_data_science_packages():
    """Verify data science packages."""
    print("\n" + "="*60)
    print("DATA SCIENCE PACKAGES VERIFICATION")
    print("="*60)
    
    packages = [
        "numpy",
        "pandas", 
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "jupyter"
    ]
    
    results = {}
    for package in packages:
        command = f'python -c "import {package}; print(\'{package} OK\')"'
        success, output = run_command(command, f"{package} Import Test")
        results[package] = {"success": success, "output": output}
    
    return results

def test_jupyter():
    """Test Jupyter Notebook functionality."""
    print("\n" + "="*60)
    print("JUPYTER NOTEBOOK VERIFICATION")
    print("="*60)
    
    tests = [
        ("jupyter --version", "Jupyter Version Check"),
        ("jupyter notebook --version", "Jupyter Notebook Version"),
    ]
    
    results = {}
    for command, description in tests:
        success, output = run_command(command, description)
        results[description] = {"success": success, "output": output}
    
    return results

def generate_report(python_results, anaconda_results, ds_results, jupyter_results):
    """Generate a comprehensive verification report."""
    print("\n" + "="*80)
    print("VERIFICATION REPORT SUMMARY")
    print("="*80)
    
    all_results = {
        "Python": python_results,
        "Anaconda": anaconda_results,
        "Data Science Packages": ds_results,
        "Jupyter": jupyter_results
    }
    
    total_tests = 0
    passed_tests = 0
    
    for category, results in all_results.items():
        print(f"\n{category.upper()}:")
        print("-" * len(category))
        
        for test_name, result in results.items():
            status = "PASS" if result["success"] else "FAIL"
            print(f"  [{status}] {test_name}")
            total_tests += 1
            if result["success"]:
                passed_tests += 1
    
    print(f"\n{'='*80}")
    print(f"OVERALL RESULT: {passed_tests}/{total_tests} tests passed")
    print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
    
    if passed_tests == total_tests:
        print("STATUS: ALL TESTS PASSED - Setup is complete and functional!")
    else:
        print("STATUS: Some tests failed - Please review the output above")
    
    print("="*80)
    
    return passed_tests, total_tests

def main():
    """Main verification function."""
    print("Starting comprehensive Python and Anaconda setup verification...")
    print("This will test all components of your Data Science environment.")
    
    # Run all verifications
    python_results = verify_python()
    anaconda_results = verify_anaconda()
    ds_results = verify_data_science_packages()
    jupyter_results = test_jupyter()
    
    # Generate report
    passed, total = generate_report(python_results, anaconda_results, ds_results, jupyter_results)
    
    return passed, total

if __name__ == "__main__":
    try:
        passed, total = main()
        sys.exit(0 if passed == total else 1)
    except KeyboardInterrupt:
        print("\nVerification interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)
