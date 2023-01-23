import paho.mqtt.client as mqtt

# Set the MQTT server information
MQTT_HOST = "Test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "temperature"

# Create a new MQTT client
client = mqtt.Client()

# Connect to the MQTT server
client.connect(MQTT_HOST, MQTT_PORT)

# Subscribe to the MQTT topic
client.subscribe(MQTT_TOPIC)

# Define the callback function for incoming messages
def on_message(client, userdata, msg):
    print("Temperature: " + str(msg.payload))

# Set the callback function
client.on_message = on_message

# Continuously listen for incoming messages
client.loop_forever()
