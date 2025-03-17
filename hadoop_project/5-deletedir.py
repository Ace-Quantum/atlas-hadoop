# This one should be just as easy as the last one just in reverse

from snakebite.client import Client

def createdir(l):
    """l is a list of directories"""

    # unsure if we need to make the port, I'll confirm with Sean when I see him
    client = Client('localhost', 9000)

    for directory in l:
        client.delete([directory], create_parent=True)