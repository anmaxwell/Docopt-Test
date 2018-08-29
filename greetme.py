"""Greeter.

Usage:
  greetme.py [--caps] <greeting> <name> 
  greetme.py (-h | --help)

Options:
  -h --help         Show this screen.
  --caps            Will uppercase the output


"""

from docopt import docopt

def greet(args):
    output = 'It works! {} to you I say {}'.format(args['<name>'], args['<greeting>'])
    if args['--caps']:
        output = output.upper()
        print('caps works')
    print(output)


if __name__ == '__main__':
    arguments = docopt(__doc__, options_first=True)
    print(arguments)
    greet(arguments)