#program will print in the command line a cow with a message

import cowsay
import sys

if len(sys.argv) == 2:\
    cowsay.cow("Hello, " + sys.argv[1])
