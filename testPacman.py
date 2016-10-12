import argparse
from util import manhattanDistance

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
    #print_map(harta)
    print manhattanDistance((3,2),(5, 2))

if __name__ == "__main__":
    main()