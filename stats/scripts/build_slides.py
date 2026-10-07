#!/usr/bin/env python3
"""Build this course's portrait section PDFs and chapter index."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / 'scripts'))
from slide_builder import main

if __name__ == '__main__':
    main(ROOT)
