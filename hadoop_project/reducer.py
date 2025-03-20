# I now know why Hadoop works like this
# I still don't know how I feel about it not taking input
# But flexibility wise it makes sense
# It means multiple languages can play together.
# So that's something neat.

import sys
import subprocess

def reducer():
    """This reads from stdin???
    Crazy. Makes sense, but crazy."""

    top_salaries = []

    for line in sys.stdin:
        line = line.strip()
        id, value = line.split('\t')

        company, totalyearly = value.split(',')

        totalyearly = int(totalyearly)

        top_salaries.append((company, totalyearly))

        if len(top_salaries) > 10:
            top_salaries.sort(key=lambda x: x[1], reverse=True)
            top_salaries.pop()

    for company, salary in sorted(top_salaries, key=lambda x: x[1], reverse=True):
        print(f"{company},{salary}")

if __name__ =="__main__":
    reducer()
