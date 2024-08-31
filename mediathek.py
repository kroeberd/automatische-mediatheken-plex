from plexapi.server import PlexServer
import os
import requests
import time

#Version 0.1 08/2024 Release. By Sarcasm

##################################################
###               HIER BEARBEITEN
##################################################
# Plex-Server Informationen
PLEX_URL = 'http://IPPLEX:32400'  # Ersetze durch die IP-Adresse deines Plex-Servers
PLEX_TOKEN = 'TOKEN'         # Ersetze durch deinen Plex-Token

# UNC-Pfad zum Basisordner
base_folder = r'/media' #Hier den Pfad zum Stammverzeichnis

# Verbindung zum Plex-Server herstellen
plex = PlexServer(PLEX_URL, PLEX_TOKEN)


##################################################
##################################################


def create_library(library_name, folder_path):
    """
    Erstellt eine Plex-Mediathek mit dem gegebenen Namen und Ordnerpfad durch eine direkte API-Anfrage.
    """
    print(f'Erstelle Mediathek: {library_name} für den Pfad: {folder_path}')

    # Anfrage-URL
    url = f'{PLEX_URL}/library/sections'

    # Parameter für die Anfrage
    params = {
        'name': library_name,
        'type': 'movie',  # Typ der Mediathek (z.B. 'movie', 'show')
        'agent': 'com.plexapp.agents.stashplexagent',  # Standard Plex Movie Agent
        'scanner': 'Plex Movie Scanner',  # Standard Plex Movie Scanner
        'language': 'en',
        'location': folder_path,
        'generatePreviewThumbnails': '0',
        'enableCinemaTrailers': '0',
        'enableCreditsDetection': '0'
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
                create_library(folder_name, folder_path)
                time.sleep(5)  # 5 Sekunden warten, um zu vermeiden, dass die API überlastet wird
            else:
                print(f"Mediathek {folder_name} existiert bereits.")

if __name__ == "__main__":
    main()
