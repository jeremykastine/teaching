#!/usr/bin/env python3
"""Check all built algebra PDFs against their saved assessment data."""
from pathlib import Path
import json
import pdfplumber
from algebra_test_layout import layouts, W, H, M, INNER, SPLIT, TOP

ROOT = Path(__file__).resolve().parents[1]

def normalized(text):
    return ' '.join(text.split())

def horizontal_rules(page, x1, x2):
    return sorted(round(line['top'], 2) for line in page.lines
                  if abs(line['x0']-x1)<.02 and abs(line['x1']-x2)<.02
                  and abs(line['top']-line['bottom'])<.02)

def verify(a, record):
    path = ROOT / record['file']
    assert path.is_file(), path
    expected = layouts(a)
    count = len(expected)
    key_start = record['starts']['key'] - 1
    assert record['test_pages'] == count
    assert key_start == count + count % 2 and key_start % 2 == 0
    assert record['key_columns'] == [len(expected[i:i+3]) for i in range(0,count,3)]
    assert sum(row['points'] for q in a['questions'] for row in q['rows']) == 100
    with pdfplumber.open(path) as pdf:
        assert len(pdf.pages) == record['pages'] == key_start + record['key_pages']
        for blank in pdf.pages[count:key_start]:
            assert not blank.chars and not blank.lines and not blank.rects and not blank.images
        for page_index, blocks in enumerate(expected):
            test = pdf.pages[page_index]
            key = pdf.pages[key_start + page_index//3]
            cols = record['key_columns'][page_index//3]
            col = page_index%3
            cw = INNER/cols
            x = M + col*cw
            assert horizontal_rules(test,M,W-M) == horizontal_rules(key,x,x+cw)
            assert horizontal_rules(test,SPLIT+6,W-M-6) == horizontal_rules(key,x+6,x+cw-6)
            text = key.extract_text()
            assert f'TEST PAGE {page_index+1}' in text
            y = TOP
            for block in blocks:
                for index,row in enumerate(block['rows']):
                    height = row['height']
                    points_test = test.crop((W-M-34,H-y+height-16,W-M,H-y+height))
                    points_key = key.crop((x+cw-34,H-y+height-16,x+cw,H-y+height))
                    assert normalized(points_test.extract_text() or '') == normalized(points_key.extract_text() or '')
                    assert [round(c['top'],2) for c in points_test.chars] == [round(c['top'],2) for c in points_key.chars]
                    if not row['graph']:
                        region = test.crop((SPLIT,H-y,W-M,H-y+height))
                        expected_text = ((str(block['num'])+'. ' if index==0 else '')
                                         + row['source']['label']+' '+str(row['source']['points'])+' pts')
                        assert normalized(region.extract_text() or '') == normalized(expected_text), (
                            path,page_index,block['num'],row['source']['label'],'unexpected response content')
                    y -= height
        for page in pdf.pages:
            assert float(page.width)==W and float(page.height)==H
            for char in page.chars:
                assert 35<=char['x0'] and char['x1']<=577 and 25<=char['top'] and char['bottom']<=772, (
                    path,'content outside print margins',char['text'])
    return count

def main():
    assessments=[]
    for folder in ('tsm','101'):
        assessments.extend(json.loads((ROOT/folder/'practice-tests/source/assessments.json').read_text()))
    report=json.loads((ROOT/'101/practice-tests/source/build-report.json').read_text())
    records={Path(record['file']).name:record for record in report}
    assert len(assessments)==len(records)==48
    pages={}
    for a in assessments:
        count=verify(a,records[a['file']]);pages[count]=pages.get(count,0)+1
        assert f'practice-tests/{a["file"]}' in (ROOT/a['folder']/'practice-tests.html').read_text()
    print(json.dumps({'verified':len(assessments),'student_page_counts':pages,
                      'checks':['100-point scoring','page-matching key columns','exact separator geometry',
                                'duplex blank pages','no hidden answers in response areas','print margins','index links']}))

if __name__=='__main__':main()
