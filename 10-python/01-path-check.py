#!/usr/bin/env python3

import os

path_to_check = "/tmp/temp.txt"  # Replace with your path

if os.path.isfile(path_to_check):
    print(f"'{path_to_check}' is a file.")
elif os.path.isdir(path_to_check):
    print(f"'{path_to_check}' is a directory.")
else:
    print(f"'{path_to_check}' does not exist or is of an unknown type.")
