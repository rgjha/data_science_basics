#!/bin/bash 

find . -name ".DS_Store" -delete
#rm -rf `find -type d -name .ipynb_checkpoints`
rm ml_notes/*.log
rm ml_notes/*.out
rm ml_notes/*.syn*
rm ml_notes/*.aux
rm ml_notes/*.pdf
rm ml_notes/*.toc
#find . -name ".ipy*" --delete


