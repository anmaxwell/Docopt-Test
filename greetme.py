"""Greeter.

Usage:
  greetme.py <greeting> <name> [--upp] [--caps] [--swap]
  greetme.py (-h | --help)

Options:
  -h --help         Show this screen.
  --upp             Will uppercase the whole output
  --caps            Willl capitalise the first letter
  --swap            Swaps upper and lower case


"""

from docopt import docopt

def greet(args):

  name = args['<name>']
  greeting = args['<greeting>']

  if args['--upp']:
      greeting = greeting.upper()
  if args['--swap']:
      greeting = greeting.swapcase()
  if args['--caps']:
      name = name.capitalize()

  output = 'It works! {} to you I say {}'.format(name, greeting)

  print(output)


if __name__ == '__main__':
    arguments = docopt(__doc__)

    greet(arguments)