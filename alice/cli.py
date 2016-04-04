''' Bob & Alice command line

Usage:
    alice hello [--name <name>]
    alice json

Options:
    alice -h | --help

'''

import docopt

from . import bob


def main():
    '''
        Main part of alice command line
    '''
    arguments = docopt.docopt(__doc__, version='Naval Fate 2.0')

    if arguments['hello']:
        if arguments['--name']:
            name = arguments['<name>']
            hello_string = bob.say_hello(name)
        else:
            hello_string = bob.say_hello()

        print hello_string

    if arguments['json']:
        print bob.get_json()


if __name__ == '__main__':
    main()
