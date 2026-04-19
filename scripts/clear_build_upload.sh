#!/usr/bin/bash

python -u ./scripts/clear_dist.py
python -m build .
twine upload ./dist/*
