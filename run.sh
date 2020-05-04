#!/bin/bash
pip install -r requirements.txt
#python database.py

waitress-serve --call 'flaskr:oliver_bot'

