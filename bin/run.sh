#!/bin/bash


# Run and host the flask app with gunicorn
pushd src/gridrealm/ && \
    sudo python main.py && \
    popd
