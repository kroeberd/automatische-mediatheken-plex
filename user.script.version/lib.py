import sys
from plexapi.server import PlexServer

# Plex-Token import
if len(sys.argv) != 2:
    print("Usage: python lib.py <PLEX_TOKEN>")
    sys.exit(1)

# Read the Plex token from the command-line arguments
plex_token = sys.argv[1]

# Your existing Plex setup and logic
baseurl = 'http://127.0.0.1:32400'  # Replace with your Plex server URL
plex = PlexServer(baseurl, plex_token)
