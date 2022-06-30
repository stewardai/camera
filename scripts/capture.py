from picamera import PiCamera
from time import sleep
import numpy as np

# camera_number = 0

with PiCamera(1, led_pin=2) as camera:
  camera.resolution = (100, 100)
  camera.framerate = 24
  sleep(2)
  output = np.empty((112 * 128 * 3,), dtype=np.uint8)
  camera.capture(output, 'rgb')
  output = output.reshape((112, 128, 3))
  output = output[:100, :100, :]