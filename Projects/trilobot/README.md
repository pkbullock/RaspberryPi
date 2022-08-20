# Notes for development

testing the new input device: 
cd /usr/local/lib/python3.9/dist-packages/evdev
evtest.py

python3 evtest.py

example output:

time 1660985328.688783 --------- SYN_REPORT --------
time 1660985329.228764 type 3 (EV_ABS), code 0    (ABS_X), value 32768
time 1660985329.228764 --------- SYN_REPORT --------
time 1660985332.828704 type 3 (EV_ABS), code 0    (ABS_X), value 0
time 1660985332.828704 --------- SYN_REPORT --------
time 1660985333.00997 type 3 (EV_ABS), code 0    (ABS_X), value 32768
time 1660985333.00997 --------- SYN_REPORT --------
time 1660985336.368693 type 3 (EV_ABS), code 0    (ABS_X), value 65535
time 1660985336.368693 --------- SYN_REPORT --------
time 1660985336.523618 type 3 (EV_ABS), code 0    (ABS_X), value 32768
time 1660985336.523618 --------- SYN_REPORT --------


