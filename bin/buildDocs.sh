#!/bin/bash

# Run rst2html5.py on all doc files in build/docs
# Note: Must be run from the repository root.
# Note: not intended for manual use. Use "make doc" instead.

for doc in $(find build/docs -iname "*.rst"); do
    pyvenv/bin/rst2html5.py $doc $(./bin/rstSuffixToHtml.sh $doc);
done
