import paho.mqtt.client as mqtt
import time

# Configuration
broker = "10.8.120.1"  # Replace with your broker IP or hostname
port = 1883           # MQTT port (default)
topic = "test/topic"  # The topic you want to publish to
message = "Hello, MQTT!"  # The message to publish
interval = 5          # Interval in seconds between each message

# Create an MQTT client instance
client = mqtt.Client()

def on_message(client, userdata, message):
  print(f"Received message with index {message.payload[0:6]} on topic {message.topic}", flush=True)


client.connect(broker, port)
client.subscribe(topic)
client.on_message = on_message

client.loop_forever()