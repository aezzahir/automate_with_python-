#!/bin/bash
python3 -m venv myvenv
source myvenv/bin/activate
pip install --upgrade pip
pip install pandas lxml requests