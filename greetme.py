"""Greeter.

Usage:
  basic.py hello <name> [--caps] [--greeting=<str>]
  basic.py goodbye <name> [--caps] [--greeting=<str>]
  basic.py (-h | --help)

Options:
  -h --help         Show this screen.
  --caps            Uppercase the output.
  --greeting=<str>  Greeting to use [default: Hello].

Commands:
   hello       Say hello
   goodbye     Say goodbye

"""

from docopt import docopt

HELLO = """usage: basic.py hello [options] [<name>]

  -h --help         Show this screen.
  --caps            Uppercase the output.
  --greeting=<str>  Greeting to use [default: Hello].
"""

GOODBYE = """usage: basic.py goodbye [options] [<name>]

  -h --help         Show this screen.
  --caps            Uppercase the output.
  --greeting=<str>  Greeting to use [default: Goodbye].
"""