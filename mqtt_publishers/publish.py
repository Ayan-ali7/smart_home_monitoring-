import paho.mqtt.client as mqtt
import time
import random


broker = "localhost"
port = 1883


client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker successfully!")
    else:
        print(f"Connection failed with code {rc}")

client.on_connect = on_connect
client.connect(broker, port, 60)

def publish_temperature():
    temperature = round(random.uniform(15.0, 30.0), 1)
    client.publish("home/sensors/temperature", str(temperature))
    print(f"Published temperature: {temperature}")

def publish_humidity():
    humidity = random.randint(30, 90)
    client.publish("home/sensors/humidity", str(humidity))
    print(f"Published humidity: {humidity}")

def publish_light_intensity():
    light_intensity = random.randint(100, 1000)
    client.publish("home/sensors/light_intensity", str(light_intensity))
    print(f"Published light intensity: {light_intensity}")

def publish_motion():
    motion = random.choice(["motion_detected", "no_motion"])
    client.publish("home/sensors/motion", motion)
    print(f"Published motion: {motion}")

try:
    client.loop_start() 
    while True:
        publish_temperature()
        publish_humidity()
        publish_light_intensity()
        publish_motion()
        time.sleep(5)

except KeyboardInterrupt:
    print("Publishing stopped")

finally:
    client.disconnect()
    client.loop_stop()