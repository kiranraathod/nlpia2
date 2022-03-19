# import re
from pathlib import Path
from setuptools import find_packages, setup

__version__ = '0.0.8'

# TODO: default requirements here and try/except with loud failure
with Path('requirements.txt').open() as fin:
    install_requires = [req.strip() for req in fin.readlines()]
    # r = install_requires[0]
    # if re.match(r'^#\s*\d{1,2}[.]\d{1,4}.\d{1,4}[rd]?\s*$', r):
    #     __version__ = req.strip().strip('#').strip()
    install_requires = [
        req.strip() for req in install_requires
        if req.strip() and not req.lstrip().startswith('#')]



setup(
    url='https://gitlab.com/prosocialai/nlpia2',
    author_email='hobson@tangibleai.com',
    name='nlpia2',
    packages=find_packages(where='src'),
    install_requires=install_requires,
    version=__version__,
    description='Software for the Manning book Natural Language Processing in Action, 2nd Edition',
    author='Hobson Lane (TangibleAI.com)',
    license='Hippocratic License (MIT + Do No Harm)',
)
