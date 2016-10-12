import argparse
from util import manhattanDistance
from Pacman import Pacman

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
    for i in xrange(len(harta)):
        for j in xrange(len(harta[i])):
            if agent == int(harta[i][j]):
                if agent == 4:
                    print "PACMAN pos: (" + str(i) + ", " + str(j) + ")"
                    return i, j
                elif agent == 3:
                    print "GHOST pos: (" + str(i) + ", " + str(j) + ")"


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
    print_map(harta)
    (pacman.dx, pacman.dy) = position(4, harta)
    position(3, harta)

    print pacman.getScore()

    find_closest_food(pacman.dx, pacman.dy)
    move(pacman.dx, pacman.dy, harta)
    print_map(harta)
    position(4, harta)

if __name__ == "__main__":
    main()