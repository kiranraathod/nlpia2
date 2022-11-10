""" Utilities for manipulating asccidoc (asciidoctor) documents """
from nlpia.doctests import *
import nbformat as nbf
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell


def adoc2ipynb(filepath, dest_filepath):

    nb = new_notebook()
    cells = []
    cells.append(
        new_markdown_cell(f"#### {filepath}"),
        new_code_cell(f"""\
            >>> import pandas as pd
            >>> pd.options.display.max_columns = 3000
            """),
    code="""\
    %pylab inline
    hist(normal(size=2000), bins=50);"""

    nb['cells']=[nbf.v4.new_markdown_cell(text),
                   nbf.v4.new_code_cell(code)]
    fname='test.ipynb'

    with open(fname, 'w') as f:
        nbf.write(nb, f)
