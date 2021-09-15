from graphviz import Graph
import shutil
from pathlib import Path

REPO_DIR = Path(__file__).resolve().absolute().parent.parent.parent
IMAGE_DIR = REPO_DIR / 'manuscript' / 'images'

print()
print('-' * 70)
print(Path(__file__).name)

# TODO: get this text from the .yml file in nlpia-manuscript/code/data/ or qary/src/qary/data/nlpia/
BOOK_THIEF_TEXT = ("Reading 'The Shoulder Shrug' between two and three o'clock each morning, "
                   "post-nightmare, or during the afternoon, in the basement.")
BOOK_THIEF_TEXT = ("Trust me, though, the words were on their way, and when "
                   "they arrived, Liesel would hold them in her hands like "
                   "the clouds, and she would wring them out, like the rain.")


def get_text_bigrams(text=BOOK_THIEF_TEXT, tokenizer=str.split, num_tokens=8):
    tokens = tokenizer(text)
    return list(zip(tokens[:-1], tokens[1:]))[:num_tokens]


def draw_text_tokens(edges, name='draw-text-tokenx-graphviz', formats=['png', 'svg']):
    print('edges: ')
    print(edges)
    g = Graph(name)
    g.attr(rankdir='LR')
    g.attr('node', shape='box')
    for e in edges:
        g.edge(e[0], e[1])
    for f in formats:
        destfilename = f'{name}.{f}'
        g.render(filename=name, cleanup=1, view=0, format=f)
        dest = IMAGE_DIR / Path('ch02') / destfilename
        print('Destination path for draw_text_tokens():')
        print(dest)
        try:
            dest.resolve().absolute().unlink()
            print('overwriting existing file')
        except FileNotFoundError:
            print('creating new file')
        shutil.move(destfilename, str(dest.resolve().absolute()))
    return g

# !firefox text-NLU-vector.svg


if __name__ == '__main__':
    bigrams = get_text_bigrams(BOOK_THIEF_TEXT)
    draw_text_tokens(edges=bigrams, name='book-thief-split')
    print('-' * 70)
    print()
