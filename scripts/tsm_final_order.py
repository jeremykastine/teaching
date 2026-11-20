"""Require an instructor-supplied position map for official TSM finals."""
import json
from pathlib import Path

MAP_PATH = Path(__file__).resolve().parents[1] / 'tsm/specifications/official-final-order.json'


def official_order(slug, path=MAP_PATH):
    if slug not in ('98-final', '99-final'):
        return None
    if not path.is_file():
        raise ValueError(
            f'{slug}: official final question order is unresolved. Supply the instructor-approved '
            'ten-position map in tsm/specifications/official-final-order.json; '
            'TSM_Test_Specs.md section 23 prohibits inferring it from institutional IDs or shuffling.')
    order = json.loads(path.read_text()).get(slug)
    if (not isinstance(order, list) or len(order) != 10
            or not all(isinstance(fid, str) for fid in order) or len(set(order)) != 10):
        raise ValueError(f'{slug}: an explicit list of ten distinct question IDs is required')
    return order


def arrange_official_final(slug, questions, order):
    if order is None:
        return questions
    indexed = {q['id']: q for q in questions}
    if len(indexed) != 10 or set(indexed) != set(order):
        raise ValueError(f'{slug}: question families do not match the approved final order')
    return [indexed[fid] for fid in order]
