#!/bin/bash

# uninstall test for macOS

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
if [ -e "$test_path" ]
then
    rm -rv "$test_path"
else
    echo "no installation"
fi
