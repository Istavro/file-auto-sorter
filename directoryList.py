# Define home directory so you dont have to type it all out.
from pathlib import Path
home = str(Path.home())

# Use the same syntax as the example for directory shortcuts.
# shortcut-name = "path/to/directory"

downloads = home + "/Downloads"