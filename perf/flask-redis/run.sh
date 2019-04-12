#!/bin/bash

#python /flask-redis/main.py

pushd /flask-redis/
    gunicorn main:redis --workers=5 --timeout=10 --bind=:8080
popd
