#!/usr/bin/env python3
"""Compatibility entry point for a 20-version MSC 201 Unit 1 PDF export.

Usage: python stats/scripts/export_test_packets.py /absolute/output.pdf [saved.json]
All current presentation rules live in scripts/export_assessment_batches.py.
A saved record preserves its original questions, choice order, and identifiers.
"""
import sys,json,secrets
from pathlib import Path
from pypdf import PdfWriter
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from export_assessment_batches import stats_packet,stats_questions

def main():
    out=Path(sys.argv[1]).resolve();out.parent.mkdir(parents=True,exist_ok=True)
    records=json.loads(Path(sys.argv[2]).read_text()) if len(sys.argv)>2 else [dict(version=10000+secrets.randbelow(90000),seed=secrets.randbits(32)) for _ in range(20)]
    writer=PdfWriter()
    for record in records:
        if 'questions' not in record:record['questions']=stats_questions(1,record['seed'])
        a=dict(course='MSC 201',title='MSC 201 Unit 1 Test',version=str(record['version']),questions=record['questions'])
        reader,_,_,_=stats_packet(a);writer.append(reader,import_outline=False)
        if len(writer.pages)%2:writer.add_blank_page(width=612,height=792)
    writer.write(out);out.with_suffix('.json').write_text(json.dumps(records,indent=2)+'\n');print(out)
if __name__=='__main__':main()
