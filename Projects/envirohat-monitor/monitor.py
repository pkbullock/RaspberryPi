#!/usr/bin/env python3

import configparser
import logging
import time
import os
import sys
import ST7735
try:
    # Transitional fix for breaking change in LTR559
    from ltr559 import LTR559
    ltr559 = LTR559()
except ImportError:
    import ltr559

from azure.iot.device import IoTHubDeviceClient, Message
from bme280 import BME280
from subprocess import PIPE, Popen


# Read configuration
config = configparser.ConfigParser()
config.read_file(open(r'azure.conn'))

IOTHUBConnectionString = config.get('Connection', 'IOTHub')
MSG_TXT = '{{"temperature": {temperature},"humidity": {humidity}, "pressure": {pressure},"light": {light}}}'



# Logging Setup
logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

# BME280 temperature/pressure/humidity sensor
bme280 = BME280()


def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(IOTHUBConnectionString)
    return client


# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE, universal_newlines=True)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])

# Enviro Hat Sensors
def get_sensor_temperature():

    # Tuning factor for compensation. Decrease this number to adjust the
    # temperature down, and increase to adjust up
    factor = 2.25
    cpu_temps = [get_cpu_temperature()] * 5

    # variable = "temperature" unit = "C"
    cpu_temp = get_cpu_temperature()
    # Smooth out with some averaging to decrease jitter
    cpu_temps = cpu_temps[1:] + [cpu_temp]
    avg_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))
    raw_temp = bme280.get_temperature()
    return raw_temp - ((avg_cpu_temp - raw_temp) / factor)

def get_sensor_pressure():
    # variable = "pressure" unit = "hPa"
    return bme280.get_pressure()

def get_sensor_humidity():
    # variable = "humidity" unit = "%"
    return bme280.get_humidity()

def get_sensor_light():
    # variable = "light" unit = "Lux"
    return ltr559.get_lux()


try:

    # Create a connection outside of the loop
    client = iothub_client_init()

    while True:
        logging.info("""monitor.py - Displays readings from all of Enviro' sensors and record on Azure IOT Hub - Press Ctrl+C to exit!""")
        
        # Test
        pressure = get_sensor_pressure()
        temperature = get_sensor_temperature()
        humidity = get_sensor_humidity()
        light = get_sensor_light()
        
        # Format message to send to Azure IOT Hub
        msg_txt_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity, pressure=pressure, light=light)
        message = Message(msg_txt_formatted)
        
        #   Send the message to Azure
        logging.info( "Sending message: {}".format(message) )
        client.send_message(message)
        logging.info( "Message successfully sent" )
        time.sleep(60) #secs

# Exit cleanly
except KeyboardInterrupt:
    sys.exit(0)