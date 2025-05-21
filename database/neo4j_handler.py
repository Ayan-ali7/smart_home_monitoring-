from py2neo import Graph, Node, Relationship
import datetime

graph = Graph("bolt://localhost:7687", auth=("neo4j", "alhanali123"))

def insert_sensor_data(sensor_type, value):
    timestamp = datetime.datetime.now()
    event = Node("Event", type=sensor_type, value=value, timestamp=timestamp)
    graph.merge(event, "Event", "timestamp") 

    sensor = Node("Sensor", type=sensor_type)
    graph.merge(sensor, "Sensor", "type")

    detected_by = Relationship(event, "DETECTED_BY", sensor)
    graph.merge(detected_by)

def insert_temperature(value):
    insert_sensor_data("Temperature", value)

def insert_humidity(value):
    insert_sensor_data("Humidity", value)

def insert_light_intensity(value):
    insert_sensor_data("LightIntensity", value)

def insert_motion(value):
    insert_sensor_data("Motion", value)
