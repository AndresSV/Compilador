# -----------------------------------------------------------------------------
# parser.py
# Este parser esta basado fuertemente en el ejemplo otorgado por la
# herramienta de PLY del archivo cparse.py asi como el material visto
# durante la clase 
# -----------------------------------------------------------------------------

import ply.yacc as yacc
import lexer
from lexer import tokens

import sys
sys.path.insert(0,"../..")

import argparse

# Precedence rules for the arithmetic operators

precedence = (
    ('left', 'AND', 'OR'),
    ('nonassoc', 'EQ', 'NE', 'GE', 'LE', 'GT', 'LT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POWER'),
)

instructions = ()

yacc.yacc()

# Main

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('filename', type=argparse.FileType('r'), help="File to Compile")
    args = parse.parse_args()

    if args.filename is not None:

        print(args.filename.name)
        f = open(args.filename.name)
        r = f.read()
        yacc.parse(r)
        # print(r)

        f.close()

    else:
        print(args.filename)

# -----------------------------------------------------------------------------
# 
# Execution
# 
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    main()