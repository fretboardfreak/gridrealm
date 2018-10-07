#!/bin/bash

# Copyright 2018 - Curtis Sand, Dennison Gaetz

# Run NGINX in a docker container to host the client and assets of Grid Realm


# TODO: write better script logic to determine these variables
GR_REPO="${HOME}/gridrealm/"
RSTBUILD="${HOME}/code/rstbuild.sh"

DKR_HTML_DIR="/usr/share/nginx/html"
CLIENT="$GR_REPO/src/gridrealm/client"
ASSET_SRV="$GR_REPO/src/gridrealm/assetserver"
DOCS="$GR_REPO/src/docs/"

# build docs into html pages
$RSTBUILD $DOCS

sudo docker run --rm -p 80:80 -v $CLIENT:$DKR_HTML_DIR/client:Z \
    -v $DOCS:$DKR_HTML_DIR/docs:Z \
    -v $ASSET_SRV/nginx_index.html:$DKR_HTML_DIR/index.html:Z nginx
