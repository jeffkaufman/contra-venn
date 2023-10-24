#!/usr/bin/env bash

IN=~/Downloads/Contra\ Band\ Composition\ -\ Sheet1.tsv
if [ -e "$IN" ]; then
    mv "$IN" sheet.tsv
fi

./process2.py

dot -Tpng graph.dot -o contra-members-big.png

open contra-members-big.png
