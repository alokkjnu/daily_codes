"""
Write a program to create progress bar using python.
"""

from alive_progress import alive_bar
import time

n = 500

with alive_bar(n) as bar:
    for i in range(n):
        time.sleep(0.05)
        bar()

from tqdm import tqdm
import time

for i in tqdm(range(100)):
    time.sleep(0.05)