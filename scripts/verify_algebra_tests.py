#!/usr/bin/env python3
"""Run the current five-version bundle checks for both algebra courses."""
import argparse
from pathlib import Path
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--render', action='store_true')
    args = parser.parse_args()
    for name in ('verify_tsm_practice_bundles.py', 'verify_math101_practice_bundles.py'):
        command = [sys.executable, str(Path(__file__).with_name(name))]
        if args.render:
            command.append('--render')
        subprocess.run(command, check=True)


if __name__ == '__main__':
    main()
