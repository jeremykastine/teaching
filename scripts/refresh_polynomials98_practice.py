#!/usr/bin/env python3
"""Refresh only the three published TSM 098 polynomial practice forms.

Keep their existing public filenames/links; replace questions and source records
from the controlling current constructor without regenerating other assessments.
"""
import json
import random
from pathlib import Path
from build_practice_tests import ROOT, polynomials98
from algebra_test_layout import build

def main():
    source=ROOT/'tsm/practice-tests/source/assessments.json'
    manifest_path=ROOT/'tsm/practice-tests/manifest.json'
    report_path=ROOT/'101/practice-tests/source/build-report.json'
    assessments=json.loads(source.read_text())
    manifest=json.loads(manifest_path.read_text())
    report=json.loads(report_path.read_text())
    updated={}
    for a in assessments:
        if a['assessment']!='98-polynomials':continue
        a['questions']=polynomials98(a['practice']-1)
        random.SystemRandom().shuffle(a['questions'])
        a['version']=str(random.SystemRandom().randint(10000,99999))
        updated[a['file']]=build(a)
        for entry in manifest:
            if entry['file']==a['file']:entry['version']=a['version']
        print(a['file'],a['version'],flush=True)
    assert len(updated)==3
    source.write_text(json.dumps(assessments,indent=2))
    manifest_path.write_text(json.dumps(manifest,indent=2))
    report=[updated.get(Path(entry['file']).name,entry) for entry in report]
    report_path.write_text(json.dumps(report,indent=2))

if __name__=='__main__':main()
