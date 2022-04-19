""" Breadth first exploration (crawling) of a graph of web pages (Wikipedia Articles) """
import logging
import time
from collections import abc

from tqdm import tqdm
import wikipedia as wiki

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def get_page(title):
    try:
        return wiki.page(title, auto_suggest=False)
    except (wiki.DisambiguationError, wiki.PageError) as e:
        log.warning(f'auto_suggest=False: {e}')
    try:
        return wiki.page(title, auto_suggest=True)
    except (wiki.DisambiguationError, wiki.PageError) as e:
        log.warning(f'auto_suggest=True: {e}')
    return False


def walk_wikipedia(pages, depth=1, delay=0.1):
    depth_goal = depth
    depth = 0
    if isinstance(pages, str):
        pages = {t: None for t in pages.split(',')}
    elif not isinstance(pages, abc.Mapping):
        pages = {t: None for t in pages.split(',')}
    pages = pages
    next_level = {t: None for t in pages}
    while depth < depth_goal and len(next_level):
        log.info(f"depth={depth}, len(nextlevel)={len(next_level)}, nextlevel[0]={list(next_level)[0]}")
        thislevel = next_level
        next_level = {}
        for title in tqdm(thislevel):
            if pages.get(title) is None:  # if False then retrieval has been attempted and failed
                time.sleep(delay)
                page = get_page(title)
                log.debug(page)
                pages[title] = (page, depth)
                if page:  # page will sometimes be false when get_page() failed to find a valid page
                    next_level.update({t: None for t in page.links if t not in pages})
        depth += 1
    return pages
