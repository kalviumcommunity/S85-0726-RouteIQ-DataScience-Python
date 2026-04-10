#!/usr/bin/env python3
"""
Setup Verification Script for Python and Anaconda Installation
This script verifies that all components are working correctly.
"""

import sys
import subprocess
import os
import json
import argparse

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

def validate_notebook_structure(notebook_path):
    """Validate notebook structure for Markdown/Code cell discipline milestone."""
    print("\n" + "="*60)
    print("NOTEBOOK STRUCTURE VERIFICATION")
    print("="*60)

    if not os.path.exists(notebook_path):
        print(f"FAILED: Notebook not found at {notebook_path}")
        return {
            "Notebook Exists": {"success": False, "output": f"Missing file: {notebook_path}"}
        }

    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook = json.load(f)
    except Exception as e:
        print(f"FAILED: Could not read notebook JSON ({e})")
        return {
            "Notebook Exists": {"success": True, "output": notebook_path},
            "Notebook JSON Parse": {"success": False, "output": str(e)}
        }

    cells = notebook.get("cells", [])
    markdown_cells = [c for c in cells if c.get("cell_type") == "markdown"]
    code_cells = [c for c in cells if c.get("cell_type") == "code"]
    executed_code_cells = [c for c in code_cells if c.get("execution_count") is not None]

    first_is_markdown = bool(cells) and cells[0].get("cell_type") == "markdown"
    has_markdown_before_each_code = True
    for idx, cell in enumerate(cells):
        if cell.get("cell_type") == "code":
            if idx == 0 or cells[idx - 1].get("cell_type") != "markdown":
                has_markdown_before_each_code = False
                break

    results = {
        "Notebook Exists": {"success": True, "output": notebook_path},
        "Notebook JSON Parse": {"success": True, "output": "Valid JSON"},
        "Title Cell Is Markdown": {"success": first_is_markdown, "output": str(first_is_markdown)},
        "At Least Two Markdown Cells": {
            "success": len(markdown_cells) >= 2,
            "output": f"Found {len(markdown_cells)} markdown cells"
        },
        "At Least Two Code Cells": {
            "success": len(code_cells) >= 2,
            "output": f"Found {len(code_cells)} code cells"
        },
        "All Code Cells Executed": {
            "success": len(executed_code_cells) == len(code_cells) and len(code_cells) > 0,
            "output": f"Executed {len(executed_code_cells)} of {len(code_cells)} code cells"
        },
        "Markdown Precedes Code Cells": {
            "success": has_markdown_before_each_code,
            "output": str(has_markdown_before_each_code)
        }
    }

    for test_name, result in results.items():
        status = "PASS" if result["success"] else "FAIL"
        print(f"[{status}] {test_name}: {result['output']}")

    return results

def validate_kernel_control_notebook(notebook_path):
    """Validate notebook structure for kernel control milestone."""
    print("\n" + "="*60)
    print("KERNEL CONTROL NOTEBOOK VERIFICATION")
    print("="*60)

    if not os.path.exists(notebook_path):
        print(f"FAILED: Notebook not found at {notebook_path}")
        return {
            "Notebook Exists": {"success": False, "output": f"Missing file: {notebook_path}"}
        }

    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook = json.load(f)
    except Exception as e:
        print(f"FAILED: Could not read notebook JSON ({e})")
        return {
            "Notebook Exists": {"success": True, "output": notebook_path},
            "Notebook JSON Parse": {"success": False, "output": str(e)}
        }

    cells = notebook.get("cells", [])
    code_cells = [c for c in cells if c.get("cell_type") == "code"]
    markdown_cells = [c for c in cells if c.get("cell_type") == "markdown"]

    def cell_source_text(cell):
        src = cell.get("source", [])
        if isinstance(src, list):
            return "".join(src)
        return str(src)

    has_long_running_candidate = any(
        "time.sleep(" in cell_source_text(c) or "for i in range(1, 31)" in cell_source_text(c)
        for c in code_cells
    )
    has_interrupt_instruction = any(
        "Interrupt" in cell_source_text(c) or "interrupt" in cell_source_text(c)
        for c in markdown_cells
    )
    has_restart_instruction = any(
        "Restart" in cell_source_text(c) or "restart" in cell_source_text(c)
        for c in markdown_cells
    )
    has_state_check = any(
        "globals()" in cell_source_text(c) or "base_value" in cell_source_text(c)
        for c in code_cells
    )
    executed_count = sum(1 for c in code_cells if c.get("execution_count") is not None)

    results = {
        "Notebook Exists": {"success": True, "output": notebook_path},
        "Notebook JSON Parse": {"success": True, "output": "Valid JSON"},
        "At Least Three Code Cells": {
            "success": len(code_cells) >= 3,
            "output": f"Found {len(code_cells)} code cells"
        },
        "At Least Three Markdown Cells": {
            "success": len(markdown_cells) >= 3,
            "output": f"Found {len(markdown_cells)} markdown cells"
        },
        "Long-Running Cell Candidate Present": {
            "success": has_long_running_candidate,
            "output": str(has_long_running_candidate)
        },
        "Interrupt Guidance Present": {
            "success": has_interrupt_instruction,
            "output": str(has_interrupt_instruction)
        },
        "Restart Guidance Present": {
            "success": has_restart_instruction,
            "output": str(has_restart_instruction)
        },
        "Kernel State Check Present": {
            "success": has_state_check,
            "output": str(has_state_check)
        },
        "At Least Two Cells Executed": {
            "success": executed_count >= 2,
            "output": f"Executed {executed_count} code cells"
        }
    }

    for test_name, result in results.items():
        status = "PASS" if result["success"] else "FAIL"
        print(f"[{status}] {test_name}: {result['output']}")

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

def generate_notebook_report(notebook_results):
    """Generate summary report for notebook-only validation."""
    print("\n" + "="*80)
    print("NOTEBOOK VERIFICATION REPORT SUMMARY")
    print("="*80)

    total_tests = 0
    passed_tests = 0

    for test_name, result in notebook_results.items():
        status = "PASS" if result["success"] else "FAIL"
        print(f"  [{status}] {test_name}")
        total_tests += 1
        if result["success"]:
            passed_tests += 1

    print(f"\n{'='*80}")
    print(f"OVERALL RESULT: {passed_tests}/{total_tests} tests passed")
    print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
    if passed_tests == total_tests:
        print("STATUS: Notebook structure is review-ready.")
    else:
        print("STATUS: Notebook structure needs updates.")
    print("="*80)

    return passed_tests, total_tests

def main():
    """Main verification function."""
    parser = argparse.ArgumentParser(description="Environment and notebook verification utility.")
    parser.add_argument(
        "--notebook",
        default=os.path.join("notebooks", "notebook_cell_discipline.ipynb"),
        help="Notebook path for structure verification."
    )
    parser.add_argument(
        "--notebook-only",
        action="store_true",
        help="Run only notebook structure checks."
    )
    parser.add_argument(
        "--kernel-notebook",
        default=os.path.join("notebooks", "kernel_control_demo.ipynb"),
        help="Notebook path for kernel control verification."
    )
    parser.add_argument(
        "--kernel-only",
        action="store_true",
        help="Run only kernel control notebook checks."
    )
    args = parser.parse_args()

    if args.notebook_only:
        print("Starting notebook structure verification...")
        notebook_results = validate_notebook_structure(args.notebook)
        passed, total = generate_notebook_report(notebook_results)
        return passed, total

    if args.kernel_only:
        print("Starting kernel control notebook verification...")
        notebook_results = validate_kernel_control_notebook(args.kernel_notebook)
        passed, total = generate_notebook_report(notebook_results)
        return passed, total

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
