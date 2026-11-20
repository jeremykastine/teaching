"""Regression checks for official-final ordering and missing-map behavior."""
import json
from pathlib import Path
import tempfile
import unittest

from tsm_final_order import official_order, arrange_official_final


class FinalOrderTests(unittest.TestCase):
    def test_missing_map_refuses_both_official_finals(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'absent.json'
            for slug in ('98-final', '99-final'):
                with self.assertRaisesRegex(ValueError, 'instructor-approved'):
                    official_order(slug, path)
            self.assertIsNone(official_order('98-diagnostic', path))
            self.assertIsNone(official_order('99-equations', path))

    def test_complete_map_reorders_whole_questions_and_keeps_content(self):
        # Synthetic IDs avoid inventing an official institutional position map.
        ids = [f'example-{i}' for i in range(10)]
        questions = [{'id': fid, 'rows': [{'answer': fid}]} for fid in reversed(ids)]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'order.json'
            path.write_text(json.dumps({'98-final': ids}))
            result = arrange_official_final('98-final', questions, official_order('98-final', path))
        self.assertEqual([q['id'] for q in result], ids)
        self.assertEqual([q['id'] for q in questions], list(reversed(ids)))
        self.assertEqual({id(q) for q in result}, {id(q) for q in questions})

    def test_incomplete_duplicate_or_mismatched_families_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'order.json'
            for invalid in ([], ['duplicate'] * 10, list(range(10))):
                path.write_text(json.dumps({'99-final': invalid}))
                with self.assertRaises(ValueError):
                    official_order('99-final', path)
        with self.assertRaisesRegex(ValueError, 'question families'):
            arrange_official_final('99-final', [{'id': 'wrong'}], [str(i) for i in range(10)])


if __name__ == '__main__':
    unittest.main()
