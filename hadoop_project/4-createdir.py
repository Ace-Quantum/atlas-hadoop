# So now we're introduced into using "snakebite"
# Which is kinda badass? It was aparantly made by the internet archive
# Which is cool af.
# Status update no it's not? It was made by Spotify.
# That's not as cool of a story

from snakebite.client import Client

def createdir(l):
    """l is a list of directories
    l is also a character in DeathNote
    That's fairly inconsequential though"""

    # unsure if we need to make the port, I'll confirm with Sean when I see him
    client = Client('localhost', 9000)

    for directory in l:
        result = client.mkdir([directory], create_parent=True)
        print(result)

    # Wow it actually is that easy
    # Nuts
