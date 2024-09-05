# automatische-mediatheken-plex

English version: https://github.com/kroeberd/automatische-mediatheken-plex/blob/main/README_EN.md

Hallo zusammen,
wer viele einzelne Mediatheken auf Basis von Unterordnern benötigt, kann dieses Script gebrauchen.

**Die Nutzung des Scripts und dieser Anleitung geschieht auf eigene Verantwortung.**

## Einfacher Weg:
Shell öffnen und Befehl ausführen in Unraid:
```git clone https://github.com/kroeberd/automatische-mediatheken-plex.git /tmp/automatische-mediatheken-plex && mkdir -p /boot/config/plugins/user.scripts/scripts/automaticplexlibs/ && cp -r /tmp/automatische-mediatheken-plex/bash/* /boot/config/plugins/user.scripts/scripts/automaticplexlibs/ && rm -rf /tmp/automatische-mediatheken-plex```

**Voraussetzungen:**
- User-Scripts, siehe dazu Apps unter unraid.
- Das Hauptverzeichniss **muss** im Docker **/media** sein.

Einrichtung:
- DOCKER_NAME mit dem Namen des Plex-Dockers ersetzen (EXAKT)
- YOUR_PLEX_TOKEN mit dem Token des Servers austauschen -> https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/
- PLEX_AGENT, PLEX_SCANNER, OVERWRITE_OFFLINE_FILE und PLEX_URL nur bei Bedarf anpassen!
- Danach speichern und einfach Starten.

## Manueller weg:

unRAID mit dem Plex Docker-Container:

1. ```docker exec -it NAME_DES_DOCKERS /bin/bash``` (dabei NAME_DES_DOCKERS mit dem tatsächlichen Namen ersetzen)
2. ```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```
3. ```python3 get-pip.py --break-system-packages```
4. ```pip install plexapi --break-system-packages```
5. ```nano /root/mediathek.py```
6. ```Einfügen des Scriptinhaltes.```
7. ```Strg + X und mit Y bestätigen```
8. ```python3 /root/mediathek.py```

Damit sollte das Script die Arbeit tun.

**Anmerkung:** Entsprechend den Agent im Script anpassen. Dieser ist Standartgemäß auf Stash eingestellt.
Stash-Agent -> https://github.com/Darklyter/StashPlexAgent.bundle
Plex Token -> https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/

## Funktion

Das Script prüft ebenfalls auf vorhandene Mediatheken, entsprechend der Unterordner.

Beispiel:

```/media``` ist das Hauptverzeichnis, in welchem sich weitere Verzeichnisse befinden: ```/media/abc/098``` und ```/media/123/def```:

Wenn ```/media``` als das Hauptverzeichnis gesetzt ist, werden dabei die Mediatheken ```abc``` und ```123``` erstellt.

## Bugs
- Viele Bibliotheken führen zum Ruckeln der Plex-App auf Konsolen

**Viel Spaß!**
