from screen import *

from PIL import Image
import numpy as np

import time

def initialize():
    rect = get_window_rect()
    time.sleep(0.1)
    pixels = get_window_pixels(rect)

    img = Image.fromarray(pixels, "RGB")
    img.show()