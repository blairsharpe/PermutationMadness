
def spin(move, programs):
    """Spin moves N amount of programs to the front keeping their order

    Args:
        move (str): The amount of programs to move
    programs (str): Programs in their current order

    Returns:
        str: Returns programs N amounts of programs spinned
    """
    program_index = int(move[1:])

    # Find N amount of programs from the right
    split_programs = programs[-program_index:] + programs[:-program_index]

    return split_programs

def exchange(move, programs):
    """Exchange causes two programs to swap depending on two numbers given

    Args:
        move (str): Contains information on which two programs to swap
    programs (str): Programs in their current order
    """
    program_one, program_two = tuple(move[1:].split("/"))
    print(program_one, program_two)
    programs = list(programs)
    programs[int(program_two)], programs[int(program_one)] = \
            programs[int(program_one)], programs[int(program_two)]

    return "".join(programs)

def partner(move, programs):
    """Example function with types documented in the docstring.
    Args:
        move (str): The amount of programs to move
    programs (str): Programs in their current order
    """
    program_one, program_two = tuple(move[1:].split("/"))

    print(program_one, program_two)
    print("partner")

    return True


if __name__ == "__main__":

    programs = "abcde"
    moves = "s1,x3/4,p4/1"

    moves = moves.split(",")

    step = 0

    for move in moves:

        step += 1
        print("\n{}. {}".format(step, move))

        if move[0] == 'p':
            partner(move, programs)

        elif move[0] == 's':
            programs = spin(move, programs)
            print(programs)

        else:
            programs = exchange(move, programs)
            print(programs)

