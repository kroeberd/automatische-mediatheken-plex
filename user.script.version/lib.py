from plexapi.server import PlexServer
import sys
import os
import requests
import time

# Plex-Token import
if len(sys.argv) != 2:
    print("Usage: python lib.py <PLEX_TOKEN>")
    sys.exit(1)

# Read the Plex token from the command-line arguments
PLEX_TOKEN = sys.argv[1]

# UNC-Path
base_folder = sys.argv[2]

# Plex Agent and Scanner
PLEX_AGENT = sys.argv[3]
PLEX_SCANNER = 'sys.argv[4]

# Your existing Plex setup and logic
PLEX_URL = 'http://127.0.0.1:32400'  # Replace with your Plex server URL
plex = PlexServer(PLEX_URL, PLEX_TOKEN)

def create_library(library_name, folder_path, agent, scanner):

    print(f'Erstelle Mediathek: {library_name} für den Pfad: {folder_path}')

    # Anfrage-URL
    url = f'{PLEX_URL}/library/sections'

    # Parameter für die Anfrage
    params = {
        'name': library_name,
        'type': 'movie',
        'agent': agent,
        'scanner': scanner,
        'language': 'en',
        'location': folder_path
    }
  
    headers = {
        'X-Plex-Token': PLEX_TOKEN
    }

    # Sende die Anfrage an den Plex-Server
    response = requests.post(url, headers=headers, params=params)

    if response.status_code == 201:
        print(f'Mediathek {library_name} erfolgreich erstellt.')
    else:
        print(f"Fehler beim Erstellen der Mediathek {library_name}: {response.status_code} {response.text}")

def main():
    sections = plex.library.sections()
    existing_libraries = {section.title for section in sections}

    # Durchlaufe alle Unterordner im Basisordner
    for folder_name in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder_name)

        if os.path.isdir(folder_path):  # Sicherstellen, dass es ein Ordner ist
            if folder_name not in existing_libraries:
                create_library(folder_name, folder_path, PLEX_AGENT, PLEX_SCANNER)
                time.sleep(5)  # 5 Sekunden warten, um zu vermeiden, dass die API überlastet wird
            else:
                print(f"Mediathek {folder_name} existiert bereits.")

if __name__ == "__main__":
    main()
