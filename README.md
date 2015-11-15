# pi-electricity-monitor

Use an LDR to read pulses from an LED on an electricity meter, and use them to calculate the instantaneous power consumption. See the blog post at http://blog.arrayofbytes.co.uk/?p=144

## Getting started
- Get Raspbian up and running on your Pi.
- `apt-get install python virtualenv`
- create a `virtualenv` as desired
- install `RPi.GPIO` - using pip; you can `pip install < requirements.txt`
- follow the blog post to get the hardware set up
- `python monitor.py` to get monitoring!
