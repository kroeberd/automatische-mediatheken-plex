# automatische-mediatheken-plex

Hallo zusammen,
wer viele einzelne Mediatheken auf Basis von Unterordnern benötigt kann dieses Script gebrauchen.

How-to:

Unraid Docker:

1. docker exec -it NAME_DES_DOCKERS /bin/bash
2. curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
3. python3 get-pip.py --break-system-packages
    **ACHTUNG: Auf eigenes Risiko!**

6. pip install plexapi
5. nano /root/mediathek.py
6. Einfügen des Scriptinhaltes.
7. Strg + X und mit Y bestätigen
8. python3 /root/mediathek.py

Laufen lassen.
