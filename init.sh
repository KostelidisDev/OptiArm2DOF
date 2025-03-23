#!/bin/sh

python3.9 -m venv .venv \
&& . ./.venv/bin/activate \
&& pip install -r requirements.txt