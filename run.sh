#!/bin/bash
python database.py
pip install -r requirements.txt
web: gunicorn -w 4 app:app

