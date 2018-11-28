#! /usr/local/bin/bython
import sys
import argparse
import numpy as np
import readline

from tokenizer import *
from inputoutput import *
from interpreter import *


def main():
    if (len(sys.argv) == 1):
        run_interpreter()

    elif (len(sys.argv) == 2):
        try:
            # Read into string
            with open(sys.argv[1], "r") as infile:
                input_str = infile.read()

            tokens = tokenize(input_str)
            tape = np.zeros(30000, dtype=np.int32)
            interpret(tokens, tape)

        except FileNotFoundError:
            errorprint("Cannot find file '%s'" % sys.argv[1], file=sys.stderr)
            sys.exit(1)
        except BFSyntaxError as e:
            errorprint(str(e))

    else:
        errorprint("Cannot parse multiple files")
        sys.exit(1)


if (__name__ == '__main__'):
    main()
