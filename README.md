# automatische-mediatheken-plex

Hallo zusammen,
wer viele einzelne Mediatheken auf Basis von Unterordnern benötigt kann dieses Script gebrauchen.

**Die Nutzung des Scripts und dieser Anleitung geschieht auf eigene Verantwortung.**

## How-to:
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

## Funktion

Das Script prüft ebenfalls auf vorhandene Mediatheken, entsprechend der Unterordner.

Beispiel:

```/media``` ist das Hauptverzeichnis, in welchem sich weitere Verzeichnisse befinden: ```/media/abc/098``` und ```/media/123/def```:

Wenn ```/media``` als das Hauptverzeichnis gesetzt ist, werden dabei die Mediatheken ```abc``` und ```123``` erstellt.

**Viel Spaß!**
