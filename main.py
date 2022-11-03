# Importing some stuff.
import os
import time
from pathlib import Path
from directoryList import *

# Check for changes in Downloads directory.
previous_count = 0
current_count = 0

while True:
    files = os.listdir(downloads)
    current_count = len(files)

    if current_count != previous_count:
        print("File count has changed")
        previous_count = current_count
        # run a loop to check if the files present in downloads have a directory to be redirected to in the name.
        for i in files:
            if "#" in i:
                dest, file_name = i.split("#")
                os.rename(downloads + "/" + i, eval(dest) + "/" + file_name)
            if "_" in i:
                dest, file_name = i.split("_")
                os.rename(downloads + "/" + i, dest + "/" + file_name)
    else:
        print("No changes detected")

    print("Waiting....")
    time.sleep(15)