#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

raspistill -n -o /home/pi/Pictures/Plant-$DATE.jpg