#!/bin/bash

# build the docs into webpages
RST_BUILD=${HOME}/code/rstbuild.sh
${RST_BUILD} docs/

# Run and host the flask app with gunicorn
gunicorn -b 127.0.0.1:5000 main:APP
