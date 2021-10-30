import os
import copy
from graphviz import Digraph, Graph
import yaml
import sys
from pathlib import Path
import shutil
import logging

log = logging.getLogger(__name__)


CODE_DIR = Path(__file__).resolve().absolute()
for i in range(4):
    if CODE_DIR.name in ['code', 'nlpia2']:
        break
    # print(f"NOT code dir: {CODE_DIR}")
    CODE_DIR = CODE_DIR.parent

REPO_DIR = CODE_DIR.parent
for i in range(4):
    if REPO_DIR.name in ['nlpia-manuscript', 'nlpia2']:
        break
    # print(f"not repo dir: {REPO_DIR}")
    REPO_DIR = REPO_DIR.parent

HOME_CODE_DIR = REPO_DIR.parent.parent
print(HOME_CODE_DIR)
assert HOME_CODE_DIR.name == 'code'
MANUSCRIPT_DIR = HOME_CODE_DIR / 'tangibleai' / 'nlpia-manuscript' / 'manuscript'
assert MANUSCRIPT_DIR.is_dir()
IMAGE_DIR = MANUSCRIPT_DIR / 'images'
assert IMAGE_DIR.is_dir()
SCRIPT_WORKING_DIR = os.getcwd()


FILEPATH = CODE_DIR / 'data' / 'nlp-applications-graphviz.yml'
ENGINE = 'sfdp'  # neato, fdp, sfdp, dot

CLASSES = dict(digraph=Digraph, graph=Graph)

# u = Digraph('unix', filename='unix.gv',
#             node_attr={'color': 'lightblue2', 'style': 'filled'})
ATTR = dict(
    # engine='fdp',
    rankdir='LR',
    # layout="neato",
    # size='6,6',
    #     nodesep=1,
    #     ranksep=1,
)
NODE_ATTR = dict(
    shape='plaintext')


def wrap_text(text, max_line_width=10):
    text = str(text)
    lines = []
    words = text.split()
    if len(text) < max_line_width:
        return text
    for i, w in enumerate(words):
        if len(w) < 3:
            if i:
                lines[-1] += f' {w}'
            else:
                if len(words) > 1:
                    words[i + 1] = f'{w} ' + words[i + 1]
                else:
                    lines.append(w)
        else:
            lines.append(w)
    return '\n'.join(lines)


def load_graphviz(filepath=FILEPATH, engine=ENGINE, attr=ATTR, node_attr=NODE_ATTR):
    filepath = str(filepath)
    with open(filepath) as fin:
        y = yaml.full_load(fin)
    attr = copy.deepcopy(dict(attr))
    node_attr = copy.deepcopy(node_attr)
    log.warning(f'yaml filepath: {filepath}')
    Klass = CLASSES[y.get('class', 'digraph').lower()]
    name = ''.join(str(filepath).split('.')[:-1])
    name = str(y.get('name') or name)
    engine = str(y.get('engine') or engine)
    log.warning(f'engine: {engine}')
    attr.update(y.get('attr', {}))
    node_attr.update(y.get('node_attr', {}))
    g = Klass(name, filename=name + '.gv',
              engine=engine, node_attr=node_attr)
    g.attr(**attr)
    # print(g)
    for i, node in enumerate(y.get('nodes', [])):
        label, kwargs = None, {}
        if isinstance(node, str):
            label = node
        elif len(node) == 1:
            label = str(node[0])
        elif len(node) == 2:
            if isinstance(node[1], dict):
                label = str(node[0])
                kwargs = dict(node[1])
            else:
                log.warning(f"Unable to parse node #{i}: {node}")
        if label is not None:
            # if label is just whitespace, then don't give it a box/oval/circle shape
            if not label.strip():
                kwargs.update({'shape': 'plaintext'})
            log.warning(f"{label}, {kwargs}")
            if len(kwargs):
                g.node(wrap_text(label), **kwargs)
            else:
                g.node(wrap_text(label))

    for e in y.get('edges', []):
        # print(e)
        if len(e) == 2:
            g.edge(wrap_text(e[0]), wrap_text(e[1]))
        elif len(e) == 3:
            if isinstance(e[2], str):
                e[2] = dict(label=wrap_text(e[2]))
            g.edge(wrap_text(e[0]), wrap_text(e[1]), **e[2])
    return g


if __name__ == '__main__':
    chnum = 'ch01' if len(sys.argv) < 3 else str(sys.argv[2])
    filepath = FILEPATH if len(sys.argv) < 2 else Path(sys.argv[1]).expanduser().resolve().absolute()
    g = load_graphviz(filepath=filepath)
    name = str(g.name)
    for ext in ['svg', 'png']:
        g.render(filename=name, cleanup=1, view=0, format=ext)
        # g.save()
        # g.view()

        dest = IMAGE_DIR / chnum / (name + '.' + ext)
        log.warning(f'svg filepath: {dest}')
        try:
            dest.resolve().absolute().unlink()
        except FileNotFoundError:
            pass
        shutil.move(name + '.' + ext, str(dest.resolve().absolute()))
    # g.view()
