import argparse
import nodewalker.walker as walker
import sys


def args():
    parser = argparse.ArgumentParser(description='Delete node_modules.')
    parser.add_argument('directory', metavar='DIR', type=str,
                        help='root directory for the walk')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='quiet mode, default interactive')
    args = parser.parse_args()
    return args.directory, args.quiet


if __name__ == '__main__':
    #(dir, quiet) = args()
    #walker.walk_the_walk(dir, quiet)
    try:
        walker.walk_the_walk(*args())
    except walker.WalkerError as we:
        print('Error', we)
    except SystemExit:
        pass  # argparse raises this error for incorrect arguments
    except:
        print(sys.exc_info()[1])