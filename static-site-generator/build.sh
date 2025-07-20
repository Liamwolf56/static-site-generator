#!/bin/bash

rm -rf docs
mkdir -p docs
python3 src/main.py content/ template.html docs
cp -r static/* docs/

