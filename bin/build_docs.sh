#!/bin/bash

RST2HTML=rst2html.py
STYLE="src/gridrealm/client/css/style.css"

echo "Building Grid Realm Docs..."
for fname in $(find src/gridrealm/docs/ -iname "*rst"); do
  echo "$fname";
  out=$(echo $fname|cut -d "." -f "1");
  $RST2HTML --link-stylesheet --stylesheet $STYLE $fname ${out}.html;
done
echo "Docs built."
