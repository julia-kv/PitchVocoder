#!/bin/bash

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python3 stretch_wav.py $1 $2 $3
