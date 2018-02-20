
def spin():
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    """
    pass

def exchange():
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    """

    pass

def partner():
     """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    """
    pass

if __name__ == "__main__":

    programs = "abcde"
    moves = "s1,x3/4,p4/1"

    moves = moves.split(",")

    step = 0

    for move in moves:

        step += 1
        print("{}. {}".format(step, move))




