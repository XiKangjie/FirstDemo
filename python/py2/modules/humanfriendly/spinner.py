import itertools
import random
import time
from humanfriendly import Spinner, Timer

with Spinner(label="Downloading", total=100) as spinner:
    progress = 0
    while progress < 100:
        # Do something useful here.
        time.sleep(0.1)
        # Advance the spinner.
        spinner.step(progress)
        # Determine the new progress value.
        progress += random.random() * 5
