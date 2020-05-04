#!/bin/bash
python database.py
#flask run --host=0.0.0.0
web: gunicorn -w 4 app:app

