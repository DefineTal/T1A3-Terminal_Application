#!/usr/bin/bash

python3 -m venv .venv

source ./.venv/Scripts/activate
pip3 install -r ./requirements.txt

pip3 install pyinstaller

pyinstaller main.py

pyinstaller --onefile main.py
