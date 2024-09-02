from plexapi.server import PlexServer
import sys
import os
import requests
import time

# by Denny Kroeber / Sarcasm / kroeberd

PLEX_TOKEN = sys.argv[1]
folder_path = sys.argv[2]
PLEX_AGENT = sys.argv[3]
PLEX_SCANNER = sys.argv[4]
PLEX_URL = sys.argv[5]
plex = PlexServer(PLEX_URL, PLEX_TOKEN)

# debug print
print(f"PLEX_URL: {PLEX_URL}")
print(f"PLEX_TOKEN: {PLEX_TOKEN}")
print(f"PLEX_AGENT: {PLEX_AGENT}")
print(f"PLEX_SCANNER: {PLEX_SCANNER}")
print(f"folder_path: {folder_path}")


def create_library(library_name, folder_path, agent, scanner):
    print(f'Erstelle Mediathek: {library_name} für den Pfad: {folder_path}')
    url = f'{PLEX_URL}/library/sections'
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

    response = requests.post(url, headers=headers, params=params)

    if response.status_code == 201:
        print(f'Mediathek {library_name} erfolgreich erstellt.')
    else:
        print(f"Fehler beim Erstellen der Mediathek {library_name}: {response.status_code} {response.text}")

def main():
    sections = plex.library.sections()
    existing_libraries = {section.title for section in sections}
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
