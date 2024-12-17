import paho.mqtt.client as mqtt
import time

# Configuration
broker = "192.168.178.76"  # Replace with your broker IP or hostname
port = 1883           # MQTT port (default)
topic = "test/topic"  # The topic you want to publish to
message = "Hello, MQTT!"  # The message to publish
interval = 5          # Interval in seconds between each message

# Create an MQTT client instance
client = mqtt.Client()

# Connect to the broker
client.connect(broker, port, 60)

# Function to publish messages
def publish_message():
    while True:
        # Publish message to the topic
        client.publish(topic, message)
        print(f"Published: {message} to topic {topic}")
        time.sleep(interval)  # Wait for the specified interval

# Start the publishing loop
publish_message()