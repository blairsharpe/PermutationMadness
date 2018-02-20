
def spin(move):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    """
    program_index = move[1:]

    print("spin")
    print(program_index)


def exchange(move):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    """
    program_one, program_two = tuple(move[1:].split("/"))

    print(program_one, program_two)
    print("exchange")

def partner(move):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    """
    program_one, program_two = tuple(move[1:].split("/"))

    print(program_one, program_two)
    print("partner")

if __name__ == "__main__":

    programs = "abcde"
    moves = "s1,x3/4,p4/1"

    moves = moves.split(",")

    step = 0

    for move in moves:

        step += 1
        print("\n{}. {}".format(step, move))

        if move[0] == 'p':
            partner(move)

        elif move[0] == 's':
            spin(move)

        else:
            exchange(move)
























