#program exports the module from sayings import hello from another program
#takes the name of user as input and prints the message.

import sys
from sayings import hello #imported from sayings.py (another local file)
from sayings import goodbye #imported from sayings.py (another local file)

#will print hello + name from user
if len(sys.argv) == 2:
    hello(sys.argv[1])

#will print goodbye + name from user
if len(sys.argv) == 2:
    goodbye(sys.argv[1])
