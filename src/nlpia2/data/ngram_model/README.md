# A character-based N-gram language model

### Build a small language model


A statistical model is a function that predicts something about the world. An language model is a function that predicts the next token for a particular language, usually a natural language like English. Language models can generate text that seems like it was written by a human, and large language models (LLMs) are so good at this, that huge companies and their billionaire investors have convinced the public that they are actually intelligent. In fact, the term "LLM" is now synonymous with "AI", even among smart professors that know better.

In this exercise you will build a small language model. Your model will be about will need a million times less data to generate interesting text. You definitely won't need to steal all the text on the Internet to get your language model working.  The example here downloads only 6 free and open source (FOS) Wikipedia pages about Python.  If you don't want to download them from wikipedia, you can find them here: gitlab.com

### References

1. [_Natural Language Processing in Action_](https://bookshop.org/p/books/natural-language-processing-in-action-second-edition-hobson-lane/dc5586a786c45232?ean=9781617299445&next=t) by Hobson Lane and Maria Dyshel is a beginner's guide to NLP for beginners and professional practioners
2. [_Speech and Language Processing_](https://web.stanford.edu/~jurafsky/slp3/) by Daniel Jurafsky & James H. Martin - for students who want to pursue NLP in college

### Downloading some natural language text

You can download the ``*.md`` text files you need from the [nlpia2 source code here](https://gitlab.com/tangibleai/nlpia2/-/tree/main/src/nlpia2/data/ngram_model/). Once you have 6 markdown files from Wikipedia, you can skip to the next section.

Advanced students will want to install the `requests` package which you can use to download pages from the web automatically. And if you install the `python-markdownify` package, you can use it to convert HTML into markdown text files, removing all the javascript and HTML styling that you don't need for a language model. You only want the natural language text for your small language model.

```bash
uv pip install requests python-markdownify
```

You can use the requests package to download any web pages you like. Here's how to download 6 Wikipedia articles about the Python programming language.
First set up the default directory to store HTML and MD text files.

```python
>>> import requests
>>> import time
>>> from mesa.constants import PUBLIC_DIR
>>> lesson_dir = PUBLIC_DIR / 'canvas' / 'ngram_model'
```

Create a "User-Agent" header so that Wikipedia doesn't block your requests. Make sure you replace the e-mail address with your Mesa College e-mail address.

```python
>>> headers = dict()
... headers['User-Agent'] = 'cisc179/1.0 (https://gitlab.com/mesa_python/feb26) student project for Intro to Python at Mesa College'
... headers['From'] = 'your_student_email_username@student.sdccd.edu'
```

Find some wikipedia page titles that you want to download.

```python
>>> titles = [
...     'Python_(programming_language)',
...     'Python_syntax_and_semantics',
...     'History_of_Python',
...     'Expression_(computer_science)',
...     'Statement_(computer_science)',
...     'Computer_science',
...     ]
>>> wikipedia = 'https://en.wikipedia.org/wiki'
```

Check your local data directory to make sure you haven't already downloaded those pages. And if you do download from wikipedia programmatically, keep it slow, with ``time.sleep()`` so you don't use up their internet connection bandwidth.

```python
>>> html_texts, md_texts = [], []
>>> for title in titles:
>>>     path = (lesson_dir / title).with_suffix('.html')
>>>     try:
>>>         with open(path) as fin:
>>>             html_texts.append(fin.read())
>>>     except Exception:
>>>         time.sleep(3)
>>>         print(f'Downloading {title}...')
>>>         html_texts.append(requests.get(
...             f'{wikipedia}/{title}',
...             headers=headers
...         ).text)
>>>         with open(path, 'wt') as fout:
>>>             fout.write(html_texts[-1])
>>>     print(title, html_texts[-1][:80])
>>>     md_texts.append(markdownify.markdownify(html_texts[-1]))
>>>     print(title, md_texts[-1][:160])
>>>     with open(path.with_suffix('.md'), 'wt') as fout:
>>>         fout.write(md_texts[-1])
```

Now that you have some HTML text files you are ready to build your character-based n-gram model!

## Build an n-gram model

Because there are millions of possible words that appear in web pages on the internet, it would be very difficult to build a simple n-gram model based on words. So for this exercise you will base your model on the _character_ n-grams from the HTML pages you downloaded.

Do you remember how to tokenize a string into characters?  Here's how to join a list of markdown strings into one big one, and then tokenize it into a list of characters. You want to check that you've got a good amount of text before trying out your n-gram model. The 6 wikipedia pages we downloaded have half a million characters, which should work great!

```python
>>> text = '\n'.join(md_texts)
>>> tokens = list(text)
>>> len(tokens)
504518
>>> len(text)
504518
```

And you can use your `collect_ngrams` function from last week's exercise to create n-grams out of any list:

```python
def collect_ngrams(tokens, n=3):
    return list(
        zip(*[
                tokens[i:(-n+i)] for i in range(n)
            ])
        )
```

The bigrams would be:

```python
>>> bigrams = collect_ngrams(tokens=tokens, n=2)
>>> bigrams[:5]
[('P', 'y'),
 ('y', 't'),
 ('t', 'h'),
 ('h', 'o'),
 ('o', 'n')]
>>> len(bigrams)
504516
```

And it's a little easier to read the bigrams if you use a list comprehension to convert each pair of strings into a string of length 2:

```python
>>> [''.join(bg) for bg in bigrams[:6]]
['Py', 'yt', 'th', 'ho', 'on', 'n ']
```

And the trigrams should be:

```python
>>> trigrams = collect_ngrams(tokens, 3)
>>> trigrams[:5]
[('P', 'y', 't'),
 ('y', 't', 'h'),
 ('t', 'h', 'o'),
 ('h', 'o', 'n'),
 ('o', 'n', ' ')]
>>> [''.join(bg) for bg in trigrams[:5]]
['Pyt', 'yth', 'tho', 'hon', 'on ']
```

## Counting n-grams

To be able to generate plausible words and text, you need to figure out how often one letter follows another, so the statistics of your generated characters matches when you found in your text files.

Python has a cool object called a `Counter` that will do just that for you:


```python
>>> from collections import Counter
>>> counts = Counter(bigrams)
>>> for bg, count in list(counts.items())[:5]:
>>>     print(bg, count)
('P', 'y') 1614
('y', 't') 1928
('t', 'h') 4675
('h', 'o') 2215
('o', 'n') 6036
```

Now you just need to divide by the total number of bigrams, to create a list of _frequencies_ or _probabilities_ that you can use to "roll the dice" when you pick a character to generate.

Use the accumulate pattern to compute the total probability for all previous words in the list of bigrams. This creates a cumulative probability distribution that will make it easier to use the `random` package to select a random bigram for generating the next character.

```python
>>> total = 0
>>> frequencies, cumulative_frequencies = [], [] 
>>> for (bg, count) in counts.items():
>>>    freq = count / len(bigrams
>>>    frequencies.append(freq))
>>>    total += freq
>>>    cumulative_frequencies.append(total)
>>> frequencies[:6]
[0.0031991056775206336,
 0.0038214843533208066,
 0.009266306717725502,
 0.004390346391392939,
 0.011963941678757462,
 0.006739132158345821]
```

Here are the first and last cumulative frequencies in our huge list of bigrams:

```python
>>> for f, bg in zip(cumulative_frequencies[:6], bigrams[:6]):
>>>     print(round(f, 8), bg)
0 
0.00319911 ('P', 'y')
0.00702059 ('y', 't')
0.0162869 ('t', 'h')
0.02067724 ('h', 'o')
0.03264118 ('o', 'n')
```

And the last few bigrams should give us a total probability for all the bigrams of 1.0:

```python
>>> for f, bg in zip(cumulative_frequencies[-6:], bigrams[-6:]):
>>>     print(round(f, 8), bg)
0.99998613 ('H', '2')
0.99998811 ('1', 'c')
0.99999207 ('c', '4')
0.99999604 ('d', '5')
0.99999802 ('5', 'b')
1.0 ('4', '>')
```

## Create a statistical model

A statistical model is a function that returns a prediction, given some statistics about what has happened in the past. Your `classify_text` function from a previous lesson is a statistical model, only you had to hard-code the statistics by hand. You had to list all of the intent labels that you wanted the function to return and the input words they were associated with. This time you are going to let Python do the hard work of computing the statistics so that it can make better predictions.

Before you can use your statistics ``dict``ionary of `counts` to predict the next character, you need to reorganize it. You would like to be able to do something like `char_choices['i']` and get back a list of the most likely characters that come after it, maybe `'s'` or '`t`' and a list of all their probabilities.

```python
char_choices = dict()
probabilities = dict()
for ngram in counts:
    prefix = ngram[:-1]
    last_char = ngram[-1]
    char_choices[prefix] = char_choices.get(prefix, [])
    char_choices[prefix].append(last_char)
    probabilities[prefix] = probabilities.get(prefix, [])
    probabilities[prefix].append(counts[ngram])
```

Now you can use random.choice to create a function that generates random words!

```python
import random

def generate_word(char_choices, probabilities, start=' '):
    word = start
    while True:
        word += random.choices(
            population=char_choices[word[-1]],
            weights=probabilities[word[-1]],
            k=1,
        )
        if word[-1] == ' ':
            break
```

