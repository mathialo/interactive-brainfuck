import sys
import numpy as np

from tokenizer import *
from inputoutput import *


def interpret(tokens, tape, tape_pointer=0):
    """
    Run the BF code described by the given tokens.
    
    Args:
    tokens (list):      List of tokens to execute
    tape (np.ndarray)   Tape to act on (data cells)
    tape_pointer (int): Optional. Initial state of data pointer.
    
    Returns:
    int: Final state of tape (data) pointer.
    """
    token_index = 0

    tokens.append(None)

    while (tokens[token_index] != None):
        token = tokens[token_index]

        if (token.op == "tapedec"):
            tape_pointer -= 1

        elif (token.op == "tapeinc"):
            tape_pointer += 1

        elif (token.op == "valdec"):
            tape[tape_pointer] -= 1

        elif (token.op == "valinc"):
            tape[tape_pointer] += 1

        elif (token.op == "getchar"):
            tape[tape_pointer] = get_input()

        elif (token.op == "putchar"):
            output(tape[tape_pointer])

        elif (token.op == "loop"):
            if (token.type == "start"):
                if (tape[tape_pointer] == 0):
                    token_index = token.pair.index + 1
                    continue

            else:
                token_index = token.pair.index
                continue

        token_index += 1

    return tape_pointer


def run_interpreter():
    """
    Run an interactive interpreter session.
    """
    command = None
    tape_pointer = 0
    tape = np.zeros(30000, dtype=np.uint8)

    while (command != "quit"):
        try:
            command = input("> ")

            if (command == "tape"):
                showtape(tape, tape_pointer)

            elif (command.split(" ")[0] == "run"):
                try:
                    # Read into string
                    with open(command.split(" ")[1], "r") as infile:
                        input_str = infile.read()

                    tape_pointer = interpret(
                        tokenize(input_str), tape, tape_pointer)

                except FileNotFoundError:
                    errorprint("Cannot find file '%s'" % command.split(" ")[1])
                except IndexError:
                    errorprint("Provide a file name!")

            else:
                tape_pointer = interpret(tokenize(command), tape, tape_pointer)

        except KeyboardInterrupt:
            print("\nInterrupted!")

        except EOFError:
            print("\nEOF detected")
            return

        except BFSyntaxError as e:
            errorprint(str(e))
