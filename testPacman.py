import argparse
from util import manhattanDistance
from Pacman import Pacman
from Ghost import Ghost


def make_map(matrix):
    height = 11
    width = 19

    harta = [[0 for c in xrange(width)] for r in xrange(height)]
    for i in xrange(height):
        harta[i] = matrix[i].split('\n')[0].split(' ')
    return harta


def read_from_file(config_file):
    data = []
    f = open(config_file, 'r')
    for eachLine in f:
        data.append(eachLine)
    f.close()
    return data


def print_map(data):
    for i in data:
        print i


def score(current_score):
    current_score += 1
    return current_score


def position(agent, harta):
    x = []
    for i in xrange(len(harta)):
        for j in xrange(len(harta[i])):
            if agent == int(harta[i][j]):
                if agent == 4:
                    return i, j
                elif agent == 3:
                    x.append(i)
                    x.append(j)
    return x


def find_closest_food(xP, yP):
     positionUp = (xP - 1, yP)
     positionDown = (xP + 1, yP)
     positionLeft = (xP, yP - 1)
     positionRight = (xP, yP + 1)
     print manhattanDistance((xP, yP), positionUp)


def move(x, y, harta):
    if harta[x-1][y] == '2':
        harta[x][y] = '1'
        harta[x-1][y] = '4'
    return harta


def display(agent, x, y):
    if agent == 4:
        print "PACMAN pos: (" + str(x) + ", " + str(y) + ")"
    elif agent == 3:
        print "GHOST pos: (" + str(x) + ", " + str(y) + ")"



def main():
    parser = argparse.ArgumentParser(description='Help')
    parser.add_argument(
        'matrix_file',
        help='the matrix file'
    )
    args = parser.parse_args()
    m = args.matrix_file
    data = read_from_file(m)
    harta = make_map(data)
    pacman = Pacman()
    ghost1 = Ghost()
    ghost2 = Ghost()
    print_map(harta)
    (pacman.dx, pacman.dy) = position(4, harta)
    ghostCoords = position(3, harta)
    #print ghostCoords
    (ghost1.dx, ghost1.dy) = ghostCoords[0:2]
    (ghost2.dx, ghost2.dy) = ghostCoords[2:4]
    display(4, pacman.dx, pacman.dy)
    display(3, ghost1.dx, ghost1.dy)
    display(3, ghost2.dx, ghost2.dy)
    ghost1.move()
    display(3, ghost1.dx, ghost1.dy)
    #print pacman.getScore()
    #find_closest_food(pacman.dx, pacman.dy)

    move(pacman.dx, pacman.dy, harta)
    print
    print_map(harta)
    (pacman.dx, pacman.dy) = position(4, harta)
    display(4, pacman.dx, pacman.dy)


if __name__ == "__main__":
    main()