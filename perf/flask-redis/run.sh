#!/bin/bash

#python /flask-redis/main.py
gunicorn main:redis --workers=10 --timeout=10 --bind=:8080