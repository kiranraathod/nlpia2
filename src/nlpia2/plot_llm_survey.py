# import re
from io import TextIOWrapper
from pathlib import Path

import numpy as np
import pandas as pd
from plotly.offline import plot as plot_html
import plotly.graph_objs as go
import seaborn as sns

import fitz  # pip install PyMuPDF
from matplotlib import pyplot as plt

sns.set_style('whitegrid')


LLM_PDF = '2303.18223 - A Survey of LLMs.pdf'
FORMFEED = chr(12)
FORMFEED_BYTE = FORMFEED.encode('utf8')



def extract_tables(pdf_path=LLM_PDF):
    """ FIXME: Only extracts a couple rows/columns """
    from tabula import read_pdf  # doesn't work well
    return read_pdf(pdf_path, pages="all")


def extract_text(pdf_path=LLM_PDF, write_file=True, page_sep=FORMFEED, header='', footer='\n\n' + '_'*80 + '\n\n'):
    doc = fitz.open(pdf_path)
    pages = []
    for page in doc:
        text = header or ''
        text += page.get_text()  # get plain text (is in UTF-8)
        text += footer or ''

        # blocks = page.get_text_blocks()
        pages.append(text)

    return (page_sep or '\n').join(pages)


LINK_ORG = {
    'T5': ('https://huggingface.co/t5-large', 'Google'),
    'mT5': ('https://https://huggingface.co/google/mt5-large', 'Google'),
    'PanGu-α': ('https://huggingface.co/sunzeyeah/pangu-13B', 'PCNL'),
    'CPM-2': ('https://huggingface.co/mymusise/CPM-GPT2', 'Tsinghua University'),
    'T0': ('https://huggingface.co/bigscience/T0', 'Hugging Face'),
    'GPT-NeoX-20B': ('https://huggingface.co/EleutherAI/gpt-neox-20b', 'EleutherAI'),
    'CodeGen': ('https://huggingface.co/Salesforce/codegen-16B-multi', 'Salesforce'),
    'Tk-Instruct': ('https://huggingface.co/allenai/tk-instruct-11b-def', 'AllenAI'),
    'UL2': ('https://huggingface.co/google/flan-ul2', 'Google'),
    'OPT': ('https://huggingface.co/facebook/opt-66b', 'Facebook'),
    'NLLB': ('https://huggingface.co/facebook/nllb-200-3.3B', 'Meta'),
    'BLOOM': ('https://huggingface.co/bigscience/bloom', 'Hugging Face'),
    'GLM-10b': ('https://huggingface.co/THUDM/glm-10b', 'Tsinghua University'),
    'GLM': ('https://huggingface.co/THUDM/glm-large-chinese', 'Tsinghua University'),
    'Flan-T5': ('https://huggingface.co/google/flan-t5-xxl', 'Google'),
    'mT0': ('https://huggingface.co/bigscience/bloomz', 'Hugging Face'),
    'Galactica-mini': ('https://huggingface.co/facebook/galactica-125m', 'Meta'),
    'Galactica-base': ('https://huggingface.co/facebook/galactica-1.3b', 'Meta'),
    'Galactica-standard': ('https://huggingface.co/facebook/galactica-6.7b', 'Meta'),
    'Galactica-large': ('https://huggingface.co/facebook/galactica-30b', 'Meta'),
    'Galactica-huge': ('https://huggingface.co/facebook/galactica-120b', 'Meta'),
    'Galactica': ('https://huggingface.co/facebook/galactica-120b', 'Meta'),
    'BLOOMZ': ('https://huggingface.co/bigscience/bloomz', 'Hugging Face'),
    'OPT-IML': ('https://huggingface.co/HuggingFaceH4/opt-iml-max-30b', 'Hugging Face'),
    'Pythia': ('https://github.com/EleutherAI/pythia', 'EleutherAI'),
    'LLaMA': ('https://github.com/juncongmoo/pyllama', 'Google'),
    'Vicuna': ('https://vicuna.lmsys.org/', 'Berkeley+CMU+Stanford+UCSD'),
    'Koala': ('https://vicuna.lmsys.org/', 'Berkeley'),
    'GShard': False,
    'GPT-3': False,
    'LaMDA': False,
    'HyperCLOVA': False,
    'Codex': False,
    'ERNIE 3.0': False,
    'Jurassic-1': False,
    'FLAN': False,
    'MT-NLG': False,
    'Yuan 1.0': False,
    'Anthropic': False,
    'WebGPT': False,
    'Gopher': False,
    'ERNIE 3.0 Titan': False,
    'GLaM': False,
    'InstructGPT': False,
    'AlphaCode': False,
    'Chinchilla': False,
    'PaLM': False,
    'Cohere': False,
    'YaLM': False,
    'AlexaTM': False,
    'Luminous': False,
    'Sparrow': False,
    'WeLM': False,
    'U-PaLM': False,
    'Flan-PaLM': False,
    'Flan-U-PaLM': False,
    'Alpaca': ('https://github.com/tatsu-lab/stanford_alpaca/', 'Stanford'),
    'GPT-4': False,
    'PanGU-Σ': False
}

def get_llm_sizes(readme='https://github.com/rucaibox/llmsurvey'):
    """ Scatterplot of LLM size vs release date """
    dfs = pd.read_html(readme)
    df = dfs[0]
    df.columns = 'Public Name Release Size Link'.split()
    df['Public'] = dfs[0]['Public'].str.lower().str.startswith('public')

    # Typo corrections, cleaning, estimation of missing values
    df['Name'] = df['Name'].replace({'Galatica': 'Galactica-huge'})
    df['Size'] = df['Size'].replace({'-': str(8*int(df['Size']['GPT-3']))})

    df.set_index('Name', inplace=True)
    if df.loc['GPT-4']['Size'] == '-':
        df['Size']['GPT-4'] = str(8*int(df['Size']['GPT-3']))
    df['Size'] = df['Size'].astype(int)
    return df


def plot_llm_sizes(df='https://github.com/rucaibox/llmsurvey',
        x='Release', y='Size', color=None, 
        dest='llm_sizes_scatter.html', display=False):
    """ Scatterplot of LLM size vs release date """
    if isinstance(df, (str, Path, TextIOWrapper)):
        df = get_llm_sizes(readme=df)
    if isinstance(df, (pd.DataFrame, dict)):
        x = df[x]
        y = df[y]
        if not isinstance(color, (None, list, tuple, pd.Series, np.ndarray)):
            color = df[color]
    df['color'] = 'r'
    df['color'][df['Open']] = 'g'
    if dest.lower().endswith('html'):
        scatter = go.Scatter(x=x, y=y, color=color)
        plot_html(scatter, show_link=False, validate=True, output_type='file', 
            filename=dest,
            image=None, image_width=800, image_height=600, 
            include_plotlyjs=True, include_mathjax=False,
            config=None, autoplay=True, animation_opts=None
            )
    else:
        scatter = df.plot(kind='scatter', x='Release', y='Size', color=df['color'])
        if display:
            plt.show()
    return scatter



"""
df.columns
df.columns[2] = 'Release'

plt.grid('on')
plt.show()

pip install plotly
from plotly.offline.offline import _plot_html
import plotly
plotly.offline.offline.plot?
plotly.offline.offline.plot?
from plotly.offline.offline import plot as _plot_html
from plotly.graph_objs import Scatter, Layout
from plotly.graph_objs.scatter import Marker
from plotly.graph_objs.layout import XAxis, YAxis
from nlpia2.constants import SRC_DATA_PATH

np = pd.np

PLOTLY_HTML = \"\"\"
<html>
  <head>
    <meta charset="utf-8" />
    <!-- <meta http-equiv="Content-Type" content="text/html; charset=utf-8"> -->
    <script type="text/javascript">
    {plotlyjs}
    </script>
  </head>
  <body>
    {plotlyhtml}
  </body>
</html>
\"\"\"

DEFAULT_PLOTLY_CONFIG = {
    'staticPlot': False,  # no interactivity, for export or image generation
    'workspace': False,  # we're in the workspace, so need toolbar etc
    'editable': False,  # we can edit titles, move annotations, etc
    'autosizable': False,  # plot will respect layout.autosize=true and infer its container size
    'fillFrame': False,  # if we DO autosize, do we fill the container or the screen?
    'scrollZoom': False,  # mousewheel or two-finger scroll zooms the plot
    'doubleClick': 'reset+autosize',  # double click interaction (false, 'reset', 'autosize' or 'reset+autosize')
    'showTips': True,  # new users see some hints about interactivity
    'showLink': True,  # link to open this plot in plotly
    'sendData': True,  # if we show a link, does it contain data or just link to a plotly file?
    'linkText': 'Edit chart',  # text appearing in the sendData link
    'displayModeBar': 'true',  # display the modebar (true, false, or 'hover')
    'displaylogo': False,  # add the plotly logo on the end of the modebar
    'plot3dPixelRatio': 2,  # increase the pixel ratio for 3D plot images
    'setBackground': 'opaque'  # fn to add the background color to a different container or 'opaque'
                               # to ensure there's white behind it
}
import os

from matplotlib import pyplot as plt
import seaborn as sns
sns.set_style?
sns.set_style('white grid')
sns.set_style('whitegrid')
from nlpia2 import constants
constants.SRC_DATA_DIR
pwd
import plotly.graph_objs as go

plot_html([go.Scatter(x=[1, 2, 3], y=[3, 2, 6])], filename='my-graph.html')
import plot.graph_objs as go

more my-graph.html
"""