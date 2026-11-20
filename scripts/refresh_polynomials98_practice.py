#!/usr/bin/env python3
"""Refresh the current five-version TSM 098 polynomial practice bundle."""
from pathlib import Path
import subprocess
import sys


if __name__ == '__main__':
    subprocess.run([sys.executable, str(Path(__file__).with_name('build_tsm_practice_bundles.py')),
                    '--only', '98-polynomials'], check=True)
