from tqdm import tqdm
import gzip
import pandas as pd

"""
NELL Knowledge Graph schema:

1. entity: Canonical name of the entity part of the 'entity->relation->value' triple. NOT the literal string of NL seen by NELL in the text
2. relation: The canonical relation name between the entity and value. Category relations are named "generalizations".
3. value: Canonical name of the object or value in the 'entity->relation->value' triple. For category relations, this is the name of the category, otherwise it's an entity (noun phrase).
4. iteration: The point in NELL's life at which this category or relation instance was promoted to one that NELL beleives to be true. This is a non-negative integer indicating the number of iterations of bootstrapping NELL had gone through.
5. prob: A probabilistic confidence score for the belief.
6. source: A summary of the provenance for the belief indicating the set of learning subcomponents (CPL, SEAL, etc.) that had submitted this belief as being potentially true.
7. entities: The set of text strings that NELL has read that it believes can refer to the concept indicated in the Entity column.
8. values: For relations, the set of text strings that NELL has read that it believes can refer to the concept indicated in the Value column. For categories, this should be empty but may contain something spurious.
9. best_entities: Of the entity text strings, which str can best be used to describe the concept.
10. best_values: Of the value text strings, which str can best be used to describe the concept.
11. entity_categories: The full set of categories (which may be empty) to which NELL belives the concept indicated in the Entity column to belong.
12. value_categories: For relations, the full set of categories (which may be empty) to which NELL believes the concept indicated in the Value column to belong. For categories, this should be empty but may contain something spurious.
14. candidate_source: A free-form amalgamation of more specific provenance information describing the justification(s) NELL has for possibly believing this category or relation instance. 
"""

from .constants import BIGDATA_DIR
NELL_DIR = BIGDATA_DIR / 'nell'
NELL_DIR.mkdir(exist_ok=True, parents=True)
DEFAULT_PATH = NELL_DIR / 'NELL.08m.1115.esv.csv.gz'
DEFAULT_LAYOUT = 'spring'
DEFAULT_TOTAL = 3_000_000  # default number of rows expected


def read_nell_tsv(path=DEFAULT_PATH, total=DEFAULT_TOTAL, header=[0]):
    """ Read 13-column TSV containing facts/knowledge for a NELL triple, return DataFrame

    entity -> relation -> value(object)

    This will sometimes work (slowly, invisibly):    
    df = pd.read_csv(
        'http://rtw.ml.cmu.edu/resources/results/08m/NELL.08m.1115.esv.csv.gz',
        encoding='latin', sep='\t')
    """
    if isinstance(header, (list, tuple)):
        header = max([int(x) for x in header])
    if header is None or header is False or not isinstance(header, int):
        header = -1
    header = int(header) + 1
    lines = []
    with gzip.open(path) as fin:
        for i, line in enumerate(tqdm(fin, total=total)):
            if i < header:
                continue
            line = line.decode('latin')
            # print(i, len(line.split('\t')))
            lines.append(line.split('\t'))
    return pd.DataFrame(lines,
        columns=('entity relation value iteration prob source entities values '
            'best_entity_str best_value_str entity_categories value_categories '
            'candidate_source').split())


if __name__ == '__main__':
    df = read_nell_tsv(total=3_000_000)  # total=2_76X_XXX
