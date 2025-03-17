# Ok so this and the next one are the last two
# Over all this has not been a hard project
# I've gotten most of it done in the last 3 to 4 hours actually

import sys

def mapper():
    """nothing dynamic here
    just do the thing"""

    for line in sys.stdin:
        line = line.strip()
        columns = line.split(',')

        id = columns[0]
        company = columns[1]
        totalyearly = columns[2]

        print(f"{id}\t{company},{totalyearly}")
