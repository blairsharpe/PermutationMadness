import LinkedList


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

