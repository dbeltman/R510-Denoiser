import json
import os
import paho.mqtt.publish as mqtt_publish
from templates import fan_config, temperature_config, power_config, energy_config, chassispower_config

mqtt_host = os.getenv('MQTTHOST', 'MQTT-Server')
mqtt_port = os.getenv('MQTTPORT', 1883)
mqtt_username = os.getenv('MQTTUSERNAME', 'iot')
mqtt_password = os.getenv('MQTTPASSWORD', 'changeme')
mqtt_client_name = os.getenv('MQTTCLIENTNAME', 'r510-denoiser')

device_name = os.getenv('DEVICENAME', 'Poweredge-R510')
fan_config_topic = os.getenv('DISCOTOPIC', 'homeassistant/fan/' + fan_config.fan_name + '/config')
temp_config_topic = os.getenv('DISCOTOPIC', 'homeassistant/sensor/' + temperature_config.temp_sensor_name + '/config')
power_config_topic = os.getenv('DISCOTOPIC', 'homeassistant/sensor/' + power_config.power_sensor_name + '/config')
energy_config_topic = os.getenv('DISCOTOPIC', 'homeassistant/sensor/' + energy_config.energy_sensor_name + '/config')        
chassispower_config_topic = os.getenv('DISCOTOPIC', 'homeassistant/button/' + chassispower_config.button_name + '/config')

mqtt_energy_topic = energy_config.mqtt_energy_topic
mqtt_ambient_temp_topic = temperature_config.mqtt_ambient_temp_topic
mqtt_control_topic  = fan_config.mqtt_control_topic
mqtt_fanspeed_topic = fan_config.mqtt_fanspeed_topic
mqtt_power_topic = power_config.mqtt_power_topic
mqtt_chassispower_topic = chassispower_config.mqtt_button_topic
mqtt_chassispower_avt_topic = chassispower_config.mqtt_button_availability_topic
def publish(topic, payload):
    print("Publishing " +str(payload) + " @" + str(topic))
    try:
        mqtt_publish.single(topic, payload,
                        hostname=mqtt_host,
                        client_id=mqtt_client_name,
                        port=mqtt_port,
                        retain=True,
                        auth={'username':mqtt_username, 'password':mqtt_password})
    except:
        print("ERROR: Something went wrong publishing '" + str(payload) + "' to topic '" + str(topic) + "'!")

try:       
    publish(fan_config_topic, json.dumps(fan_config.fan_config_template))
    publish(power_config_topic, json.dumps(power_config.power_config_template))
    publish(energy_config_topic, json.dumps(energy_config.energy_config_template))
    publish(temp_config_topic, json.dumps(temperature_config.temp_config_template))
    publish(chassispower_config_topic, json.dumps(chassispower_config.chassispower_config_template))
    publish(mqtt_chassispower_avt_topic, "online")
except:
    print("Something went wrong publishing configs to discovery topic!")