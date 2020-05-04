#!/bin/bash
pip install -r requirements.txt
pip install psycopg2-binary
python database.py
gunicorn -w 4 app:app
