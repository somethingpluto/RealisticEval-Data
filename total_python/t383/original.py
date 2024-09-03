import time
import sys
from termcolor import colored
from colorama import init

# Initialize colorama
init()

def flashy_text(text, color1, color2, duration=5, interval=0.5):
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write('\r' + colored(text, color1))
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write('\r' + colored(text, color2))
        sys.stdout.flush()
        time.sleep(interval)
    # Clear the text at the end
    sys.stdout.write('\r' + ' ' * len(text) + '\r')
    sys.stdout.flush()