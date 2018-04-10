# Resources

https://github.com/jacksonliam/mjpg-streamer


https://www.raspberrypi.org/forums/viewtopic.php?f=43&t=45178

## VLC Player

http://www.raspberry-projects.com/pi/pi-hardware/raspberry-pi-camera/streaming-video-using-vlc-player

sudo apt-get install vlc


This is slow

raspivid -o - -t 0 -n | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264

Better

raspivid -o - -t 0 -n -w 600 -h 400 -fps 12 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264


raspivid -o - -t 0 -n -w 400 -h 300 -fps 12 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264