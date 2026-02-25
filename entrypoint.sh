#!/bin/bash
rm /dev/urandom 
mkfifo /dev/urandom
python3 /app/generate_rand.py > /dev/urandom &
exec "$@"