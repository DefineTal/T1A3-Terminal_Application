#!/usr/bin/bash

python3 -m venv .venv

source ./.venv/Scripts/activate

pip3 install -r ./requirements.txt

python3 main.py



