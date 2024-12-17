docker build -t mqtt-broker .
docker run -d \
  --name mqtt-broker \
  -p 1883:1883 \
  -p 9001:9001 \
  mqtt-broker