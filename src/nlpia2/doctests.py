import re
import doctest
from pathlib import Path
from doctest import DocTestParser
import tempfile

try:
    DATA_DIR = Path(__file__).parent / 'data'
except NameError:
    DATA_DIR = Path.cwd()

assert DATA_DIR.is_dir()

DEFAULT_DIR = Path('/home/hobs/code/tangibleai/nlpia-manuscript/manuscript/adoc')
DEFAULT_FILENAME = 'Chapter 03 -- Math with Words (TF-IDF Vectors).adoc'
DEFAULT_OPTIONFLAGS = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE


def extract_code_lines(filepath=DEFAULT_DIR / DEFAULT_FILENAME, with_metadata=True):
    expressions = extract_expressions(filepath=filepath)
    if with_metadata:
        return [vars(ex) for ex in expressions]
    return [ex.source for ex in expressions]


def extract_expressions(filepath=DEFAULT_DIR / DEFAULT_FILENAME):
    text = Path(filepath).open('rt').read()
    dtparser = DocTestParser()
    return dtparser.get_examples(text)


def expressions_to_doctests(expressions, prompt='>>> ', ellipsis='... ', comment=''):
    # expressions = extract_expressions(filepath=filepath)

    prompt = prompt or ''
    if prompt and prompt[-1] != ' ':
        prompt += ' '
    if not isinstance(prompt, str):
        prompt = '>>> '

    ellipsis = ellipsis or ''
    if ellipsis and ellipsis[-1] != ' ':
        ellipsis += ' '
    if not isinstance(ellipsis, str):
        ellipsis = '... '

    comment = comment or ''
    if not isinstance(comment, str):
        comment = '# '
    if comment and comment[-1] != ' ':
        comment += ' '
    blocks = ['']

    for exp in expressions:
        lines = exp.source.splitlines()
        if exp.source.strip() and len(lines) == 1:
            blocks[-1] += prompt + exp.source
        else:
            blocks[-1] += prompt + lines[0] + '\n'
            for line in lines[1:]:
                blocks[-1] += ellipsis + lines[0] + '\n'

        if exp.want:
            blocks[-1] += comment + exp.want
            blocks.append('')


def extract_code_file(filename=DEFAULT_FILENAME, basedir=DEFAULT_DIR, destfile=None):
    filename = Path(DEFAULT_FILENAME)
    basedir = Path(DEFAULT_DIR)
    filepath = basedir / filename
    destfile = destfile or filepath.with_suffix('.adoc.py')
    lines = extract_code_lines(filepath=filepath)
    if destfile:
        with Path(destfile).open('wt') as fout:
            fout.writelines(lines)
    return ''.join(lines)


def test_file(filename=DEFAULT_FILENAME, basedir=DEFAULT_DIR, adoc=True,
              optionflags=DEFAULT_OPTIONFLAGS,
              name=None,
              verbose=False,
              package=None, module_relative=False,
              **kwargs):
    filename = Path(filename)
    if name is None:
        name = filename.name
    if package:
        module_relative = True
        basedir = '.'
    basedir = Path(basedir)
    filepath = basedir / filename
    if not module_relative:
        assert filepath.is_file()
    if adoc:
        with filepath.open() as fin:
            lines = fin.readlines()
            newlines = []
            for pair in zip(lines[:-1], lines[1:]):
                newlines.append(pair[0])
                if not re.match(r'\s*\[\s*source\s*,\s*python\s*\]\s*', pair[0]):
                    if re.match(r'\s*[-]{4,80}\s*', pair[1]):
                        newlines.append('\n')
            newlines.append(lines[-1])
        fp, filepath = tempfile.mkstemp(text=True)
        filepath = Path(filepath)
        with filepath.open('wt') as fout:
            fout.writelines(newlines)
    results = doctest.testfile(str(filepath),
                               name=name,
                               module_relative=module_relative, package=package,
                               optionflags=optionflags, verbose=verbose,
                               **kwargs)
    filepath.unlink()
    return results


def extract_code_files(glob='*.adoc', adocdir=DEFAULT_DIR, destdir=None):
    adocdir = Path(adocdir)
    if destdir is None:
        destdir = adocdir.parent / 'py'
    destdir = Path(destdir)
    destdir.mkdir(exist_ok=True)
    destpaths = []
    for p in adocdir.glob(glob):
        destfile = (destdir / p.name).with_suffix('.adoc.py')
        print(f"{p} => {destfile}")
        code = extract_code_file(filename=p.name, basedir=p.parent)
        with destfile.open('wt') as fout:
            fout.write(code)
        destpaths.append(destfile)
    return destpaths


if __name__ == '__main__':
    if input('Extract python from all manuscript/adoc files? ').lower()[0] == 'y':
        filepaths = extract_code_files()
        print(filepaths)
