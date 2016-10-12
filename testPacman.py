import argparse
def read_from_file(config_file):
    f = open(config_file, 'r')
    for eachLine in f:
        print eachLine,
    f.close()


def main():
    parser = argparse.ArgumentParser(description='Help')
    parser.add_argument(
        'matrix_file',
        help='the matrix file'
    )
    args = parser.parse_args()
    m = args.matrix_file
    read_from_file(m)


if __name__ == "__main__":
    main()