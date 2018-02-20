class LinkedList():

    def __init__(self):




    def spin(self, move):
        """Example function with types documented in the docstring.

        `PEP 484`_ type annotations are supported. If attribute, parameter, and

        Args:
            param1 (int): The first parameter.

        Returns:
            bool: The return value. True for success, False otherwise.

        """
        program_index = move[1:]

        print(program_index)
        print("spin")

        return True

    def exchange(self, move):
        """Example function with types documented in the docstring.

        `PEP 484`_ type annotations are supported. If attribute, parameter, and

        Args:
            param1 (int): The first parameter.

        Returns:
            bool: The return value. True for success, False otherwise.

        """
        program_one, program_two = tuple(move[1:].split("/"))

        print(program_one, program_two)
        print("exchange")

        return True

    def partner(self, move):
        """Example function with types documented in the docstring.

        `PEP 484`_ type annotations are supported. If attribute, parameter, and

        Args:
            param1 (int): The first parameter.

        Returns:
            bool: The return value. True for success, False otherwise.

        """
        program_one, program_two = tuple(move[1:].split("/"))

        print(program_one, program_two)
        print("partner")

        return True


