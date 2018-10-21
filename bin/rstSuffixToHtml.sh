#!/bin/bash

# Convert the first argument string from using ".rst" file suffix to ".html"

if [[ $# -ge 1 ]]; then
    echo $(echo $1 | sed 's/\.rst/\.html/g');
    exit 0
else
    exit 1
fi
