import sys
import numpy as np

from ibf.tokenizer import *
from ibf.inputoutput import *


class BFRuntimeError(Exception):
    """
    Exception for runtime errors in the given BF code.
    """

    def __init__(self, message):
        Exception.__init__(self, message)


def interpret(tokens,
              tape,
              tape_pointer=0,
              add_output_tag=False,
              outputformat="ascii"):
    """
    Run the BF code described by the given tokens.
    
    Args:
    tokens (list):          List of tokens to execute
    tape (np.ndarray)       Tape to act on (data cells)
    tape_pointer (int):     Optional. Initial state of data pointer
    add_tag (bool):         Whether to add a 'prompt' to the output
    outputformat (str):     Format of output
    
    Returns:
    int: Final state of tape (data) pointer.
    """
    token_index = 0

    tokens.append(None)

    while (tokens[token_index] != None):
        token = tokens[token_index]

        if (token.op == "tapedec"):
            tape_pointer -= 1

            if (tape_pointer < 0):
                tape_pointer = 0
                raise BFRuntimeError("Negative tape pointer encountered")

        elif (token.op == "tapeinc"):
            tape_pointer += 1

            if (tape_pointer >= tape.size):
                tape_pointer = tape.size - 1
                raise BFRuntimeError(
                    "Tape pointer %d is out of bounds for tape of length %d" %
                    (tape_pointer + 1, tape.size))

        elif (token.op == "valdec"):
            tape[tape_pointer] -= 1

        elif (token.op == "valinc"):
            tape[tape_pointer] += 1

        elif (token.op == "getchar"):
            tape[tape_pointer] = get_input()

        elif (token.op == "putchar"):
            output(tape[tape_pointer], add_output_tag, outputformat)
            add_output_tag = False

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


def run_repl(tape_length=30000, datatype=np.uint8, outputformat="ascii"):
    """
    Run an interactive interpreter session.
    
    Args:
    tape_length (int):           Length of tape (number of data cells)
    datatype (numpy datatype):   Datatype for tape cells
    outputformat (str):          Format of output
    """
    # Print greeting
    print("Interactive BrainFuck - ibf v0.1\n")
    print("ibf is licensed under the permissive MIT license. Full license and")
    print(
        "copyright information is available at the project's GitHub repository.\n"
    )

    command = None
    tape_pointer = 0
    tape = np.zeros(tape_length, dtype=datatype)

    while (command != "quit"):
        try:
            command = input("\033[94m[Input] \033[0m")

            if (command == "tape"):
                showtape(tape, tape_pointer)

            elif (command == "pos"):
                print("Pointer at %d" % tape_pointer)

            elif (command.split(" ")[0] == "run"):
                try:
                    # Read into string
                    with open(command.split(" ")[1], "r") as infile:
                        input_str = infile.read()

                    tape_pointer = interpret(
                        tokenize(input_str), tape, tape_pointer, False,
                        outputformat)

                except FileNotFoundError:
                    errorprint("Cannot find file '%s'" % command.split(" ")[1])
                except IndexError:
                    errorprint("Provide a file name!")

            else:
                tape_pointer = interpret(
                    tokenize(command), tape, tape_pointer, False, outputformat)

        except KeyboardInterrupt:
            print("\nInterrupted!")

        except EOFError:
            print("\nEOF detected")
            return

        except BFSyntaxError as e:
            errorprint(str(e), "Syntax error")

        except BFRuntimeError as e:
            errorprint(str(e), "Runtime error")
