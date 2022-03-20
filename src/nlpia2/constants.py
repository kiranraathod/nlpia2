from pathlib import Path

import logging

log = logging.getLogger(__name__)


PACKAGE_DIR = Path(__file__).absolute().resolve().parent
SRC_DIR = PACKAGE_DIR.parent
REPO_DIR = SRC_DIR.parent
__version__ = next(iter(
    line for line in (REPO_DIR / 'setup.py').open() if line.startswith('__version__ = ')))
__version__ = __version__[len('__version__ = '):].strip('"').strip("'")


HOME_DIR = Path.home()
DATA_DIR_NAME = '.nlpia2-data'
DATA_DIR = PACKAGE_DIR / DATA_DIR_NAME
if not DATA_DIR.is_dir():
    DATA_DIR = REPO_DIR / DATA_DIR_NAME
if not DATA_DIR.is_dir():
    DATA_DIR = HOME_DIR / DATA_DIR_NAME
    # try/except this and use tempfiles python module as backup
    DATA_DIR.mkdir(parents=True, exist_ok=True)

# canonical data directory to share data between nlpia2 installations
HOME_DATA_DIR = HOME_DIR / DATA_DIR_NAME
if not HOME_DATA_DIR.is_dir():
    HOME_DATA_DIR.mkdir(parents=True, exist_ok=True)
# TODO: create data.py file
# TODO: add download_if_necessary to data.py
# TODO: all required data files
# TODO: add list of all required data files to data.py
# TODO: ensure all files are in HOME_DATA_DIR (DATA_DIR is just a subset)
# TODO: move DATA_DIR constant to data.py
# DATA_FILENAMES = dict(
#     DATA_DIR
# )
