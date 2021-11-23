# -----------------------------------------------------------------------------
# parser.py
# Este parser esta basado fuertemente en el ejemplo otorgado por la
# herramienta de PLY del archivo cparse.py asi como el material visto
# durante la clase 
# -----------------------------------------------------------------------------

import lexer
import yacc as yacc


import sys
sys.path.insert(0,"../..")

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=argparse.FileType('r'), help="File to Compile")
args = parser.parse_args()

if args.filename is None:
    print(args.filename.name)
    f = open(args.filename.name, 'r')
    content = f.read()
    print(content)
else:
    print(args.filename)