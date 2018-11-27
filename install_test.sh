#!/bin/bash

# install test for macOS

if [ `uname -s` != "Darwin" ]
then
    echo "This is only for macOS"
    exit 1
fi

addon_path="$HOME/Library/Application Support/Anki2/addons21"

if [ ! -e "$addon_path" ]
then
    echo "${addon_path} not exist"
    exit 1
fi
test_path="${addon_path}/urlplay-test"
[ -e "$test_path" ] || mkdir "$test_path"

cp -v __init__.py "$test_path/"
