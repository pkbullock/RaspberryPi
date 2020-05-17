# Introduction

## setup

Setup the following scripts:

Pimoroni libraries:

[https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-plus](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-plus)

```python
git clone https://github.com/pimoroni/enviroplus-python
cd enviroplus-python
sudo ./install.sh
```

Azure IOT:

```python
pip install azure-iot-device
```

## Tutorials/References/Resources

[https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-live-data-visualization-in-power-bi](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-live-data-visualization-in-power-bi)


Using the Python Device SDK for IoT Hub:  https://github.com/Azure/azure-iot-sdk-python

[https://janakiev.com/blog/python-background/](https://janakiev.com/blog/python-background/)

## Commands

```bash

nohup python /path/to/montor.py > output.log &
nohup python -u ./montor.py > output.log &


```