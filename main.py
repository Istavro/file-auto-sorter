# Importing some stuff.
import os
import time
from pathlib import Path
from directoryList import *

# Get the path for the Downloads directory.
downloads = str(Path.home()) + "/Downloads"

# Check for changes in Downloads directory.
while True:
    NumberOfFiles=len(os.listdir(downloads))
    time.sleep(20)
    OldNumber = NumberOfFiles
    NumberOfFiles = len(os.listdir(downloads))
    if NumberOfFiles != OldNumber:
        # Loop through the files and check if they have directories _ or # in the name to indicate a directory.
        print("success")
