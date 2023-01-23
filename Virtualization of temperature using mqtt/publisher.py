import paho.mqtt.client as mqtt
import random
import time 

# Set the MQTT server information
MQTT_HOST = "Test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "temperature"

# Create a new MQTT client
client = mqtt.Client()

# Connect to the MQTT server
client.connect(MQTT_HOST, MQTT_PORT)

# Continuously publish simulated temperature data
while True:
    temperature = random.uniform(20, 25)
    client.publish(MQTT_TOPIC, temperature)
    time.sleep(5)

