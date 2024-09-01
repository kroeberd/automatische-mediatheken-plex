# automatische-mediatheken-plex

If you want to have many individual media libaries based on subfolders in Plex, this is the script you need.  

**The use of the script and these instructions is at your own risk.**

## How-to:
unRAID with the Plex Docker-Container:

1. ```docker exec -it DOCKER_NAME /bin/bash``` (change DOCKER_NAME with the name of your Plex-Docker)
2. ```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```
3. ```python3 get-pip.py --break-system-packages```
4. ```pip install plexapi --break-system-packages```
5. ```nano /root/mediathek.py```
6. ```insert the script```
7. ```save the script with Ctrl + O and exit nano with Ctrl + X```
8. ```python3 /root/mediathek.py```

**Note:** If you want to, change the agent in the script. By default, it's the Stash-Agent.
Stash-Agent -> https://github.com/Darklyter/StashPlexAgent.bundle

## How the script works:
The script checks for existing libaries in the subfolders.

Example:
```/media``` is the main folder, in which you can find some subfolders: ```/media/abc/098``` and ```/media/123/def```:

If ```/media``` is set as the main folder, the libaries ```abc``` and ```123``` will be created.

**Have fun with the script!**