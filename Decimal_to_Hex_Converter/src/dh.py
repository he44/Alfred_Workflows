# This file is contains the python script that turns a decimal integer
# into its hexdecimal correspondence and outputs that string

import sys

query = int("{query}")

query = str(hex(query))

sys.stdout.write(query)
