import sys
import os
import paho.mqtt.client as mqtt 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.mongodb_handler import insert_into_mongodb
from database.mysql_handler import insert_into_mysql
from database.neo4j_handler import insert_temperature, insert_humidity, insert_light_intensity, insert_motion  # Import Neo4j insert functions

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()

    if topic == "home/sensors/temperature":
        temperature = float(payload)
        print(f"Received temperature: {temperature}")
        insert_into_mysql("temperature", {"temperature": temperature})
        insert_into_mongodb("temperature", {"temperature": temperature})
        insert_temperature(temperature)

    elif topic == "home/sensors/humidity":
        humidity = int(payload)
        print(f"Received humidity: {humidity}")
        insert_into_mongodb("humidity", {"humidity": humidity})
        insert_into_mysql("humidity", {"humidity": humidity})
        insert_humidity(humidity)

    elif topic == "home/sensors/light_intensity":
        light_intensity = int(payload)
        print(f"Received light intensity: {light_intensity}")
        insert_into_mongodb("light_intensity", {"light_intensity": light_intensity})
        insert_into_mysql("light_intensity", {"light_intensity": light_intensity})
        insert_light_intensity(light_intensity) 

    elif topic == "home/sensors/motion":
        motion = payload
        print(f"Received motion: {motion}")
        insert_into_mysql("motion", {"motion": motion})
        insert_into_mongodb("motion", {"motion": motion})
        insert_motion(motion) 

client = mqtt.Client("data_subscriber")
client.on_message = on_message
client.connect("localhost", 1883, 60)

client.subscribe("home/sensors/temperature")
client.subscribe("home/sensors/humidity")
client.subscribe("home/sensors/light_intensity")
client.subscribe("home/sensors/motion")

client.loop_forever()
