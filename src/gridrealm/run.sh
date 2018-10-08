#!/bin/bash

# Run and host the flask app with gunicorn

gunicorn -b 127.0.0.1:5000 main:APP
