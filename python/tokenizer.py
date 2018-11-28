import re


class Token:
    """
    Class representing a token. 
    
    Args:
    index (int):    Index of token (number of instructions before this)
    op (str):       Operation to perform.
    """

    def __init__(self, index, op):
        self.index = index
        self.op = op

    def __str__(self):
        return self.op


class LoopToken(Token):
    """
    Special class for loop tokens. Automatically sets the 'op' field in the 
    Token class to 'loop'.
    
    Holds an additional field for the paired loop delimiter. 
    
    Args:
    index (int):    Index of token (number of instructions before this)
    type (str):     Either 'start' or 'end'.
    """

    def __init__(self, index, type):
        super().__init__(index, "loop")
        self.type = type
        self.pair = None

    def __str__(self):
        if (self.type == "start"):
            return "loopstart"

        else:
            return "goto " + str(self.pair.index)


class BFSyntaxError(Exception):
    """
    Exception for syntax errors in the given BF code.
    """

    def __init__(self, message):
        Exception.__init__(self, message)


def tokenize(input_str):
    """
    Tokenizes a given input string of BF code.
    
    Args:
    input_str (str):    Input code
    
    Returns:
    list: A list of tokens (as instances of the token class).
    
    Raises:
    BFSyntaxError:      If the input code contains syntax errors, ie if
    loops are not matched properly.
    """
    # Remove newlines
    input_str = input_str.replace("\n", "")

    # Remove all comments
    input_str = re.sub(r"[^<>+\-\[\],.]", "", input_str)

    tokens = [None] * len(input_str)
    active_loops = []

    for i, sign in enumerate(input_str):
        if (sign == "<"):
            tokens[i] = Token(i, "tapedec")

        elif (sign == ">"):
            tokens[i] = Token(i, "tapeinc")

        elif (sign == "-"):
            tokens[i] = Token(i, "valdec")

        elif (sign == "+"):
            tokens[i] = Token(i, "valinc")

        elif (sign == ","):
            tokens[i] = Token(i, "getchar")

        elif (sign == "."):
            tokens[i] = Token(i, "putchar")

        elif (sign == "["):
            tokens[i] = LoopToken(i, "start")
            active_loops.append(tokens[i])

        elif (sign == "]"):
            tokens[i] = LoopToken(i, "end")

            try:
                paired_token = active_loops.pop()
                paired_token.pair = tokens[i]
                tokens[i].pair = paired_token

            except IndexError:
                raise BFSyntaxError(
                    "Loop close at %d without any matching loop start" % i)

    if (len(active_loops) > 0):
        raise BFSyntaxError("Unclosed loop at %d" % active_loops.pop().index)

    return tokens
