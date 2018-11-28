import sys
import numpy as np


def errorprint(string):
    """
    Print a message to stderr, prefixed with 'Error:'
    """
    print("Error: %s" % string, file=sys.stderr)


def get_input():
    """
    Get input from user, interpret as integer.
    
    Returns:
    int: Input from user. Defaults to 0 if the input could not be read 
    properly
    """
    try:
        return int(input())

    except ValueError:
        errorprint("Cannot convert input to int")
        return 0


def output(num):
    """
    Output a sign to stdout. Input number is interpreted as character.
    
    Args:
    num (int):   Ascii value of sign to output
    """
    print(str(chr(num)), end="")


def _num_of_symbols(num):
    """
    Calculate the number of symbols necessary to print the given number
    
    Args:
    num (int):   Input number
    
    Returns:
    int: Number of signs necessary to write 'num'
    """
    if (num == 0):
        return 1
    elif (num > 0):
        return int(np.ceil(np.log10(num + 0.1)))
    else:
        return int(np.ceil(np.log10(-num + 0.1))) + 1


def showtape(tape, position):
    """
    Print the current status for the tape to the terminal. Current position is
    highlighted in bold. 
    
    Args:
    tape (np.ndarray):  Current tape
    position (int):     Position of tape pointer
    """
    nonzero = np.flatnonzero(tape)

    if (nonzero.size == 0):
        last = position + 3

    else:
        last = min(tape.size, max(nonzero[-1], position) + 3)

    widths = [None] * last

    for i in range(last):
        widths[i] = max(_num_of_symbols(i), _num_of_symbols(tape[i])) + 1
        if (i == position):
            print("\033[1m", end="")

        print(("%%%dd" % widths[i]) % i, end="")
        if (i == position):
            print("\033[0m", end="")

    print()
    for i in range(last):
        if (i == position):
            print("\033[1m", end="")

        print(("%%%dd" % widths[i]) % tape[i], end="")
        if (i == position):
            print("\033[0m", end="")

    print()