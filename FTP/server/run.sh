#!/bin/bash

docker build -t custom-ftp-server .

docker run -d \
  --name ftp_server \
  -p 21:21 \
  -p 30000-30009:30000-30009 \
  custom-ftp-server 


#   --network host \