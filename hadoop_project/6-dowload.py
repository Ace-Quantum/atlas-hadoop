# It occurs to me that I probably should be including a shebang
# Proper documentation wouldn't hurt either.
# Oh, also, here's some reference material
# https://www.geeksforgeeks.org/retrieving-file-data-from-hdfs-using-python-snakebite/

from snakebite.client import Client

def download(l):
    """Downloads files listed in l and stores them in the /tmp folder"""

    client = Client('localhost', 9000)

    client.copyToLocal([l], '/tmp')

    # I think that's it but I'm not sure
    # Because the tutorial I'm following has this in a loop printing the l
    # So I'm unsure if this also needs to be in a loop?
    # Actually I'm just going to type another guess here in the comments

    # for file in l:
    #   client.copyToLocal([file], '/tmp')

    # It feels like that would be better
