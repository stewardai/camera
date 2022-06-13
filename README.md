# Steward Camera

The Steward Camera is an IoT device used to identify plant [phenotypes](https://en.wikipedia.org/wiki/Phenotype). 


## Features

- scripts for taking a picture from two cameras and merging them into one dataframe. 

## Hardware

- waveshare
- raspberry pi compute module 4
- arducam 
- case (/case folder)

## Software

- /scripts

## Getting Started

- flash the raspberry pi
- load the /scripts folder onto the device
- setup crontab if you want to run the scripts on a schedule

## Development


If you need to test out interacting with the hardware, it is best to connect directly to the device:
- get a working steward camera
- enable ssh
- ssh into the device and edit the scripts with nano or vi

Because of the limited resources of the RPi compute module, I have had bad experiences using any remote development workflow through ssh. 


## Backlog

- test with rock3 compute module and pine64 SoQuartz
- test out different cameras
- add rangefinder and thermal camera support
- create a custom carrier board

