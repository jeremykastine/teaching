#!/usr/bin/env python3
"""Build five-version practice bundles and refresh the course resource pages."""
import sys
from build_practice_tests import *
import practice_math101 as M
import practice_tsm_finals as T

ASSESSMENTS=[
 ('TSM 098','98-arithmetic','Arithmetic Test',arithmetic98,8),
 ('TSM 098','98-polynomials','Polynomials Test',polynomials98,17),
 ('TSM 098','98-fractions','Fractions Test',fractions98,23),
 ('TSM 098','98-linear','Linear Equations and Linear Systems Test',linear98,34),
 ('TSM 098','98-final','Final Exam',lambda v:T.final('TSM 098',v),34),
 ('TSM 099','99-arithmetic','Arithmetic Test',arithmetic99,8),
 ('TSM 099','99-polynomials','Polynomials Test',polynomials99,17),
 ('TSM 099','99-rational','Rational Expressions Test',rational99,23),
 ('TSM 099','99-equations','Quadratic and Rational Equations Test',equations99,29),
 ('TSM 099','99-graphing','Graphing Test',graph99,34),
 ('TSM 099','99-final','Final Exam',lambda v:T.final('TSM 099',v),34),
 ('MATH 101','101-unit-1','Unit 1: Expressions, Equations, and Inequalities',M.unit1,2),
 ('MATH 101','101-unit-2','Unit 2: Functions and Their Graphs',M.unit2,4),
 ('MATH 101','101-unit-3','Unit 3: Polynomial, Rational, and Radical Functions',M.unit3,5),
 ('MATH 101','101-unit-4','Unit 4: Exponentials, Logarithms, and Systems',M.unit4,7),
 ('MATH 101','101-final','Final Exam',M.final,7),
]

def main():
    import argparse
    import subprocess
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', help='Accepted for compatibility; new IDs are random five-digit integers')
    parser.add_argument('--only', choices=[a[1] for a in ASSESSMENTS])
    parser.add_argument('--validate-only', action='store_true')
    args = parser.parse_args()
    scripts = Path(__file__).resolve().parent
    courses = ['tsm', 'math101'] if not args.only else ['math101' if args.only.startswith('101-') else 'tsm']
    for course in courses:
        name = f'verify_{course}_practice_bundles.py' if args.validate_only else f'build_{course}_practice_bundles.py'
        command = [sys.executable, str(scripts / name)]
        if args.only and not args.validate_only:
            command += ['--only', args.only]
        subprocess.run(command, check=True)


if __name__ == '__main__':
    main()
