# This one should be just as easy as the last one just in reverse

from snakebite.client import Client

def deletedir(l):
    """l is a list of directories"""

    # unsure if we need to make the port, I'll confirm with Sean when I see him
    client = Client('localhost', 9000)

    # Sorting because David did and I don't yet know if it's necessary
    l.sort(reverse=True)

    respones = client.delete(l, recurse=True)

    # David and I troubleshooted this and apparantly there's something 
    # in his print statement that is necessary

    for response in respones:
        print(response)
