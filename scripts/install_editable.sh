#!/usr/bin/env bash
set -e
echo "Making sure pyproject.toml says 'generate-setup-file = true'..."
sed s/'generate-setup-file = false'/'generate-setup-file = true'/g -i pyproject.toml
echo "Building package with 'poetry build -f sdist'..."
TARFILE=$(poetry build -f sdist | tee | grep -o -E 'nlpia2-[v0-9.]+[.]tar[.]gz')
echo "Built dist/$TARFILE"
SETUPFILE=$(tar xvzf dist/$TARFILE | grep -E 'setup[.]py')
if [[ -n "$SETUPFILE" ]]; then 
    echo "Found setup.py at dist/$SETUPFILE"
    rm -f setup.py
    cp -f dist/$SETUPFILE .
    pip install -e .
    echo "Successfully ran 'pip install -e .'..."
else
    echo "FAILED: Unable to find a setup.py file."
fi


