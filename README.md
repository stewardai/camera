# Steward Camera

The Steward Camera is an IoT device used to identify plant [phenotypes](https://en.wikipedia.org/wiki/Phenotype). 


## Features

- scripts for taking a picture from two cameras and merging them into one dataframe.
- Combine thermal camera output with images
- read sensor data
- python environment on the device to customize functionality to meet a wide variety of needs

## Hardware

- waveshare
- raspberry pi compute module 4
- arducam 64MP
- arducam 8MP NoIR
- case (/case folder)

The case design was originally done in fusion 360, but stl and gcode files are also included. If you are going to make edits, start with the .f3d file, and update the stl and gcode files when you are done.

## Software

- /scripts
-   /capture.py
-   /upload.py (example)

## Getting Started

- flash the raspberry pi
- load the /scripts folder onto the device
- setup crontab if you want to run the scripts on a schedule

## Tutorials

- plant monitoring
- plant phenotyping
- validate data on the device
- camera + firestore + appsmith dashboard
- pest management
- nutrient management
- early vigor experiment

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

## Related Research

- [A Versatile Phenotyping System and Analytics Platform Reveals Diverse Temporal Responses to Water Availability in Setaria](https://www.cell.com/molecular-plant/fulltext/S1674-2052(15)00268-3?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS1674205215002683%3Fshowall%3Dtrue)
- [PlantCV v2: Image analysis software for high-throughput plant phenotyping](https://peerj.com/articles/4088/#)
- [EasyDCP: An affordable, high-throughput tool to measure plant phenotypic traits in 3D](https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.13645)
- [An automated, high-throughput method for standardizing image color profiles to improve image-based plant phenotyping](https://peerj.com/articles/5727/)
- [Automated imaging of duckweed growth and development](https://www.biorxiv.org/content/10.1101/2021.07.21.453240v1)
- [Phenotypic analysis of a European Camelina sativa diversity panel](https://www.essoar.org/doi/10.1002/essoar.10508336.2)
- [Development and Implementation of an IoT-Enabled Optimal and Predictive Lighting Control Strategy in Greenhouses](https://www.mdpi.com/2223-7747/10/12/2652)
- [Multi-omic analysis of the Arabidopsis clock activator mutant rve 4 6 8 reveals connections to carbohydrate metabolism and proteasome regulation](https://www.biorxiv.org/content/10.1101/2021.10.25.465654v4)
- [Tiller estimation method using deep neural networks](https://www.researchsquare.com/article/rs-1552723/v1)
