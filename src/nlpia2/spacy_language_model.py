import spacy  # https://spacy.io

MODEL_NAME = 'en_core_web_md'
# dict of normalization "links" that must terminate in a cannonical name (leaf of the tree)
MODEL_NAMES = {
    # None or empty strings can be used to redirect to a default value/name 
    None: 'md',
    '': 'md',
    'default': 'md',
    # links to noncanonical names will be followed to until they are not found as keys
    'en': 'md',
    'english': 'md',
    'small': 'sm',
    'medium': 'md',
    

    'sm': 'en_core_web_sm',
    'md': 'en_core_web_md',
    
    
    'lg': 'en_core_web_md',
    'large': 'en_core_web_md'
    }


def cannonicalize_name(name=None, name_dict=MODEL_NAMES, max_redirects=5, default=None):
    """ Follow mappings to a normalized name using a dict of abbreviated_name: cannonical_name

    >>> cannonicalize_name('sm')
    'en_core_web_sm'
    >>> cannonicalize_name()
    'en_core_web_md'
    """
    for i in range(max_redirects):
        if name not in name_dict:
            if not i and default is not None:
                # first time checking for redirect abbreviation and no default specified
                return default
            # reached a leaf in the tree so name must be cannonical (a value in the kv dict) 
            return name
        name = name_dict[name]
    return name


def load(model_name=MODEL_NAME):
    """ Expand model_name abbreviations and download model weights before using spacy.load
    
    >>> nlp = load('en')
    >>> nlp.lang
    'en'
    >>> nlp.meta['name']
    'core_web_md'
    >>> load().meta['name']
    'core_web_md'
    """
    model_name = cannonicalize_name(model_name)
    try:
        nlp = spacy.load(model_name)
    except OSError:
        spacy.cli.download(model_name)
        nlp = spacy.load(model_name)
    return nlp


nlp = load()