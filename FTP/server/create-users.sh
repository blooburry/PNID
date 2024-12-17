#!/bin/bash
# This script will add users and set their passwords

useradd -m ftpuser1 && echo "ftpuser1:password1" | chpasswd
useradd -m ftpuser2 && echo "ftpuser2:password2" | chpasswd

exec "$@"