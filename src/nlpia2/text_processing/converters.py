""" Utilities for manipulating asccidoc (asciidoctor) documents

Typical DocTestParser Expression objects:
{'source': 'import spacy\n',
 'want': '',
 'lineno': 64,
 'indent': 0,
 'options': {},
 'exc_msg': None},
{'source': 'nlp = spacy.load("en_core_web_sm")\n',
 'want': '',
 'lineno': 65,
 'indent': 0,
 'options': {},
 'exc_msg': None},
{'source': 'sentence = \"\"\"The faster Harry got to the store, the faster Harry,\n    the ...',
 'want': '',
 'lineno': 67,
 'indent': 0,
 'options': {},
 'exc_msg': None}
"""
from doctest import DocTestParser
import logging
from pathlib import Path
import re
import nbformat as nbf
from tqdm import tqdm

from nlpia2.text_processing.extractors import parse_args
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
import sys

log = logging.getLogger(__name__)
HEADER_TEXT = f"""\
# Imports and Settings

>>> import pandas as pd
>>> pd.options.display.max_columns = 3000
"""
HEADER_BLOCKS = [
    dict(source='### Imports and Settings', typ='markdown'),
    dict(source='''\
        >>> import pandas as pd
        >>> pd.options.display.max_columns = 3000
        ''', typ='python')
]

TEST_TEXT = f"""\
# A dataframe

>>> pd.DataFrame([[1,2],[3,4]])
   0  1
0  1  2
1  2  3
"""
TEST_BLOCKS = [
    dict(source='### A dataframe', typ='markdown'),
    dict(source='''\
        >>> pd.DataFrame([[1,2],[3,4]])
        ''', typ='python',
         want='''\
           0  1
        0  1  2
        1  2  3
        ''')
]


CODEHEADER = [
    r'^([.][-\w\s\(\)\[\]\|\*\'"!@#{}&^%$+=<,>.?/]+\s*)?\s*$',  # '.Problem setup'
    r'^\[source,\s*python\]\s*$',
    r'^----[-]*\s*$',
]


def re_matches(patterns, lines, match_objects=True):
    r""" Match multiple regular expressions to consecutive lines of text

    >>> patterns = '^([.][\\w\\s]+)?\s*$\n^\[source\]$\n^[-]+$'.split('\n')
    >>> lines = '----\n.hello\n\n[source]\n----\nworld\n----'.split('\n')
    >>> re_matches(patterns, lines)
    []
    >>> re_matches(patterns, lines[2:])
    [<re.Match object; span=(0, 0), match=''>,
     <re.Match object; span=(0, 8), match='[source]'>,
     <re.Match object; span=(0, 4), match='----'>]
    """
    matches = []
    for pat, text in zip(patterns, lines):
        match = re.match(pat, text)
        if not match:
            return matches
        matches.append(match)
    if not match_objects:
        return [m.group() for m in matches]
    return matches


def get_examples(text):
    """ Extract all doctest code and output examples from asciidoc (adoc) text """
    dtparser = DocTestParser()
    examples = dtparser.get_examples(text)
    return examples


def get_code_blocks(text,
                    header_patterns=CODEHEADER,
                    footer_patterns=None,
                    min_header_len=2, min_footer_len=1):
    if footer_patterns is None:
        footer_patterns = [header_patterns[-1]]
    lines = text.splitlines()
    blocks = []
    i = len(header_patterns)
    while i < len(lines) - 1:
        header_matches = re_matches(header_patterns, lines[i:])
        # some number of header lines must match (2 for adoc, [source,python]\n----\n)
        if not len(header_matches) >= min_header_len:
            i += 1
            continue
        line_number = i
        if header_matches[0].group().strip():
            line_number -= 1
        i += len(header_matches)
        # last line of header must match
        if not re.match(header_patterns[-1], header_matches[-1].group()):
            i += 1
            continue
        block = []
        # TODO: include docutils examples(parsed code and output examples)
        while i < len(lines) - min_footer_len:
            block.append(lines[i])
            i += 1
            footer_matches = re_matches(footer_patterns, lines[i:])
            if len(footer_matches) >= len(footer_patterns):
                i += len(footer_matches)
                break
        blocks.append(dict(
            preceding_text=lines[line_number - 1],
            preceding_blank_line=lines[line_number],
            line_number=line_number,
            header='\n'.join([m.group() for m in header_matches]),
            code='\n'.join(block),
            footer='\n'.join([m.group() for m in footer_matches]),
            following_blank_line=lines[i],
            following_text=lines[i + 1],
        ))
    return blocks


def adoc_doctests2ipynb(adocs=Path('.'), dest_filepath=None, **kwargs):
    adocs = Path(adocs)
    text = kwargs.pop('text', None) or ''
    if adocs.is_file():
        text = text + '\n' + adocs.read()
    dest_filepath = dest_filepath if not dest_filepath else Path(dest_filepath)
    examples = get_examples(text)

    nb = new_notebook()
    cells = []
    cells.append(new_markdown_cell(f"#### {adocs}"))

    for exp in examples:
        # need to run the doctest parser on a lot of text to get attr names right
        if isinstance(exp, str):
            cells.append(new_markdown_cell(exp))
        if hasattr(exp, 'text'):
            cells.append(new_markdown_cell(exp.text))
        if hasattr(exp, 'code'):
            new_code_cell(exp.code)

    nb['cells'] = cells
    if dest_filepath:
        with dest_filepath.open('w') as f:
            nbf.write(nb, f)
    return nb


def find_title(text, pattern=r'^\s*[=#]\s?(.+)$'):
    r""" First first line that matches pattern (r'^\s*[=#]\s?.+$')"""
    for line in text.splitlines():
        if re.match(pattern, line):
            return line
    for line in text.splitlines():
        if line.strip():
            return line


def adoc2ipynb(filepath=None, dest_filepath=None, text=None):
    try:
        text = Path(filepath).open().read()
    except (TypeError, OSError, IOError, FileNotFoundError) as e:
        log.error(f'Invalid filepath: {filepath}\n  ERROR: {e}')

    dest_filepath = None if not dest_filepath else Path(dest_filepath)
    blocks = get_code_blocks(text)

    nb = new_notebook()
    cells = []
    title = find_title(text)
    if filepath:
        title = f'[{filepath.with_suffix("").name}]({filepath})'
    if filepath:
        cells.append(new_markdown_cell(f"#### _`{title}`_"))

    print(len(blocks), filepath)
    print(dest_filepath)
    for block in blocks:
        # need to run the doctest parser on a lot of text to get attr names right
        if len(block['header'].splitlines()) == 3:
            cells.append(new_markdown_cell('#### ' + block['header'].splitlines()[0]))

        cells.append(new_code_cell(block['code']))

    nb['cells'] = cells
    if dest_filepath:
        with dest_filepath.open('w') as f:
            nbf.write(nb, f)
    return nb


def adocs2notebooks(adoc_dir=Path('.'), dest_dir=None, glob='Chapter-*.adoc'):
    """ Convert a directory of adoc files into jupyter notebooks """
    notebooks = []
    adoc_dir = Path(adoc_dir)
    if not dest_dir:
        dest_dir = adoc_dir.parent / 'notebooks'
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(exist_ok=True, parents=True)
    for adoc_filepath in tqdm(list(adoc_dir.glob(glob))):
        dest_filepath = dest_dir / adoc_filepath.with_suffix('.ipynb').name
        notebooks.append(adoc2ipynb(filepath=adoc_filepath, dest_filepath=dest_filepath))
    return notebooks


def convert(format='ipynb', **kwargs):
    filepath = kwargs.pop('adocs')
    if filepath:
        print(filepath)
        text = Path(filepath).open().read()
        print(len(text))
    else:
        text = TEST_TEXT
    text = HEADER_TEXT + '\n\n' + text
    return dict(nb=adoc2ipynb(text=text), text=text, filepath=filepath)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        kwargs = parse_args(
            format='ipynb',
            description='Convert adoc code blocks and preceding heading text to a jupyter notebook',
            adocs_help='File path to input adoc file',
            output_help='File path to output ipynb file')
        # format = kwargs.pop('format')
        results = convert(**kwargs)
        # print(results)
