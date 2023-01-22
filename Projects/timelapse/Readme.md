 # Cron Job

Good Cron Planning Tool: [https://crontab.guru/#0_*/3_*_*_*](https://crontab.guru/#0_*/3_*_*_*)

```bash

sudo crontab -e
crontab -e

0 */3 * * * /home/pi/Pictures/timelapse.sh 2>&1

```

# Useful Resources

[https://www.raspberrypi.org/documentation/usage/camera/raspicam/timelapse.md](https://www.raspberrypi.org/documentation/usage/camera/raspicam/timelapse.md)

[https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md)

[https://pimylifeup.com/raspberry-pi-time-lapse/](https://pimylifeup.com/raspberry-pi-time-lapse/)

## Using the updated library

https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf

https://www.raspberrypi.com/documentation/computers/camera_software.html#getting-started

https://github.com/raspberrypi/libcamera-apps

https://datasheets.raspberrypi.com/camera/raspberry-pi-camera-guide.pdf

https://www.raspberrypi.com/documentation/computers/camera_software.html#common-command-line-options

# Setup

> Note: this is installed on raspberrypi images so this would only update it

sudo apt install -y python3-picamera2

Examples:
https://github.com/raspberrypi/picamera2/tree/main/examples