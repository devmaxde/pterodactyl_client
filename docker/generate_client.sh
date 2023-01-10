#!/bin/bash
SCRIPTPATH=$(dirname "$SCRIPT")
SCRIPTPATH=$(cd "$SCRIPTPATH/.." && pwd -P)


docker build -t pterodactyl-python-client .

docker run -v "$SCRIPTPATH:/app/out" -it pterodactyl-python-client