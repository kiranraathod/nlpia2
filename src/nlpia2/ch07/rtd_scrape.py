import requests
# ! pip instal html5lib_to_markdown
from html5lib_to_markdown.transformer import to_markdown  # , Transformer

resp = requests.get('https://readthedocs.org/search/?q=javascript')
btext = resp.content
text = resp.text

md = to_markdown(text)
