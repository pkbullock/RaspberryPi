#!/usr/bin/env python3

import configparser
import logging
import time
from azure.iot.device import IoTHubDeviceClient, Message

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

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(IOTHUBConnectionString)
    return client

# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE, universal_newlines=True)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])

try:

    # Create a connection outside of the loop
    client = iothub_client_init()

    while True:
        logging.info("""monitor.py - Displays readings from all of Enviro' sensors and record on Azure IOT Hub - Press Ctrl+C to exit!""")
        

        # Test
        pressure = 10
        temperature = 23.5
        humidity = 56
        light = 52
        
        # Format message to send to Azure IOT Hub
        msg_txt_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity, pressure=pressure, light=light)
        message = Message(msg_txt_formatted)
        
        #   Send the message to Azure
        logging.info( "Sending message: {}".format(message) )
        client.send_message(message)
        logging.info( "Message successfully sent" )
        time.sleep(1)

# Exit cleanly
except KeyboardInterrupt:
    #st7735.set_backlight(0)
    sys.exit(0)