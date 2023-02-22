#!/usr/bin/env bash
# release.sh
# set -e
PKG_NAME=qary
USAGE="./release.sh [VERSION | [MESSAGE]]"
DEPENDENCIES=(twine wheel setuptools pip keyring rfc3986)
ENV_PATHS=(.env $PKG_NAME.env $PKG_NAME/.env ~/.ssh/.env ~/.ssh/.env/twine.env "~/.ssh/$PKG_NAME.env")


## now loop through the above array
for p in "${ENV_PATHS[@]}"
do
    echo "Checking for .env files containing environment variables in: $p"
    if [ -f $p ]; then
        echo "Found: $p"
        source $p
        if [ -n "$TWINE_PASSWORD" ]; then
            echo "Found TWINE_PASSWORD env variable."
        fi
    fi
done

if [ -z "$1" ] || [ -z "$2" ] ; then
    echo "USAGE: ./scripts/release.sh VERSION MESSAGE"
    echo ""
    echo "EXAMPLE: ./scripts/release.sh 1.2.3 'add new qary skill'"
    exit 1
else
    VERSION=$1
    MESSAGE=$2
    echo "Recent versions: "
    git tag | sort | tail -n 10
    echo ""
    echo "Tagging the git repository with git tag -a '$VERSION' -m '$MESSAGE'..."
    echo "Do you want to proceed [N]/y?"
fi

read answer

if [ "$answer" != "y" ] ; then
    exit 0
fi


echo "Building and publishing qary version '$VERSION' with message: '$MESSAGE'..."

# set -e
# pip install -U twine wheel setuptools
git commit -am "$VERSION: $MESSAGE"
git push
git tag -l | cat

rm -rf build
rm -rf dist

echo "Large data files..."
find src/qary/data -type f -size +20M -exec ls -hal {} \;
echo ""
echo "Would you like to remove these files?"
read answer
if [ "$answer" == "y" ] ; then
    find src/qary/data -type f -size +20M -exec rm -f {} \;
fi

# python setup.py sdist
# python setup.py bdist_wheel

# if [ -z "$(which twine)" ] ; then
#     echo 'Unable to find `twine` so installing it with pip.'
#     pip install --upgrade pip setuptools twine poetry
# fi

function bump_version_poetry {
    CONFIG_PATH=scripts/pyproject.toml
    sed -i 's/^version\s*=\s*"[0-9]*\.[0-9]*\.[0-9]*"/version = "'$1'"/g' CONFIG_PATH
    VERSION_ASSIGNMENT_LINE=$(grep '^version' $CONFIG_PATH)
    echo "Bumped version in $CONFIG_PATH :"
    echo "version assignment config line: $VERSION_ASSIGNMENT_LINE"
    git commit -am "$VERSION: $MESSAGE"
}


function bump_version_twine {
    CONFIG_PATH=setup.cfg
    sed -i 's/^version\s*=\s*"[0-9]*\.[0-9]*\.[0-9]*"/version = "'$1'"/g' CONFIG_PATH
    grep '^version' $CONFIG_PATH
    git commit -am "$VERSION: $MESSAGE"
}

function upload_with_twine {

    CMD=$'try:\n  import twine\n  print("1")\nexcept ImportError:\n  print("")\n\n\n'
    TWINE_INSTALLED=$(python -c "$CMD")
    if [ -n "$TWINE_INSTALLED" ] ; then
       echo "twine is already installed"
    else
       echo "Installing dependencies: ${DEPENDENCIES[*]}"
       conda install -c conda-forge -c defaults -y ${DEPENDENCIES[*]}
       # pip install --upgrade twine wheel setuptools
    fi

    rm -rf build
    rm -rf dist
    # find nessvec-data -type f -size +10M -exec rm -f {} \;

    python setup.py sdist bdist_wheel

    if [ -z "$(which twine)" ] ; then
        echo 'Unable to find `twine` so installing twine with conda.'
        conda install -c conda-forge -c defaults -y twine
    fi

    twine check dist/*
    twine upload dist/"$PKG_NAME-$VERSION"*"-py"* --verbose
    twine upload dist/"$PKG_NAME-$VERSION"*".tar"* --verbose
    git push --tag
}


function upload_with_poetry {
    sed -i 's/^version\s*=\s*"[0-9]*\.[0-9]*\.[0-9]*"/version = "'$1'"/g' scripts/pyproject.toml
    grep '^version' scripts/pyproject.toml
    git commit -am "$VERSION: $MESSAGE"

    cp scripts/pyproject.toml .
    poetry build
    poetry publish
    # poetry public --username=__token__ --password=pypi-...

    mv pyproject.toml scripts/

    git commit -am "pyproject file version updated for release $VERSION: $MESSAGE"
    git push
    git tag -a "$VERSION" -m "$MESSAGE"
    git push --tag
}


upload_with_poetry
