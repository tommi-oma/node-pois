import os
import shutil
import sys


class WalkerError(Exception):
    pass


def walk_the_walk(dir, quiet):
    NODE_MODULES = 'node_modules'
    if not os.path.isdir(dir):
        raise WalkerError('"{0}" is not a directory'.format(dir))
    for root, dirs, files in os.walk(dir):
        if NODE_MODULES in dirs:
            nodedirname = os.path.join(root, NODE_MODULES)
            try:
                if quiet:
                    remove_directory(nodedirname)
                else:
                    ask_and_maybe_remove_directory(nodedirname)
            except IOError:
                print('Error deleting {0}: {1}'.format(nodedirname, sys.exc_info()[1]))
            dirs.remove(NODE_MODULES)


def ask_and_maybe_remove_directory(dirname):
    if ask_if_should_remove(dirname):
        remove_directory(dirname)
    else:
        print('Skipping "{0}"'.format(dirname))


def remove_directory(dirname):
    shutil.rmtree(dirname)
    print('Removed "{0}"'.format(dirname))


def ask_if_should_remove(dirname):
    response = input('remove {}? [Y/n]'.format(dirname))
    return response.lower() != 'n'

