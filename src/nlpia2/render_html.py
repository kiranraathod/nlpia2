import os
import sys
import subprocess
from pathlib import Path
import json
import logging

log = logging.getLogger(__name__)


REPO_DIR = Path(__file__).resolve().absolute().parent.parent
MANUSCRIPT_DIR = REPO_DIR / 'manuscript'
SCRIPT_WORKING_DIR = os.getcwd()


def render_adoc(doctype='book', backend='html5', destination_dir='html', embedded=False, adoc_path='adoc/*.adoc'):
    """ Render asc files in manuscript/asc to HTML or other viewable/printable format

    Input:
      backend (str): html5 xhtml5 docbook5 manpage
      doctype (str): article book manpage inline
      embedded (bool): whether to suppress enclosing document structure
    """

    # exit_code = subprocess.call(cmd, shell=True)  # exit_code == 0 if successful

    command = f'asciidoctor -d {doctype} -b {backend} -D {destination_dir} {adoc_path}'.split()
    return run(command=command, chdir=MANUSCRIPT_DIR)


def run(command, chdir=None):
    if chdir:
        log.info(f'Temporarily changing working directory to {chdir}')
        initial_cwd = os.getcwd()
        os.chdir(chdir)

    log.warning(f'Running: {" ".join(command)}')
    output = subprocess.run(command, capture_output=True)

    if chdir:
        os.chdir(initial_cwd)

    return {
        'stderr': output.stderr.decode("utf-8").splitlines(),
        'stdout': output.stderr.decode("utf-8").splitlines()
    }


def svg2png(filepath, dpi=300, width="100%", height="100%", background_color="white"):
    # exit_code = subprocess.call(cmd, shell=True)  # exit_code == 0 if successful
    filepath_noext = '.'.join(filepath.split('.')[:-1])
    # deprecated: cmd = f'inkscape --without-gui {filepath_noext}.svg -o {filepath_noext}.png'.split()
    cmd = str.split(f' inkscape {filepath_noext}.svg'
                    f' --export-filename {filepath_noext}.png'
                    f' --export-background={background_color}'
                    f' --export-dpi={dpi}'
                    # f'--export-width={width} --export-height={height}'
                    )
    return run(command=cmd, chdir=None)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        svgfilepaths = ['manuscript/images/ch02/survival-of-adequate-sentence-diagram.svg']
    else:
        svgfilepaths = sys.argv[1:]
    for filepath in svgfilepaths:
        output = svg2png(filepath=filepath)
        if output.get('stderr') or output.get('stdout'):
            print(json.dumps(output, indent=4))

    output = render_adoc(doctype='book', backend='html5', embedded=False)

    # using decode() function to convert byte string to string
    if output.get('stderr') or output.get('stdout'):
        print('output_messages:')
        print(json.dumps(output, indent=4))
