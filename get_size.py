#!/usr/bin/python3

import os
import sys

def get_directory_size(path):
    try:
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        return total_size
    except (PermissionError, FileNotFoundError) as e:
        print(f"Error: {e}")
        return None

path = sys.argv[1]
if os.path.exists(path):
    if os.path.isdir(path):
        size = get_directory_size(path)
        if size is not None:
            if size >= 1024**3:
                print(f"The size of directory is: {size/(1024**3):.2f} GB")
            elif size >= 1000000:
                print(f"The size of directory is: {size/1000000:.2f} MB")
            elif size >= 1000:
                print(f"The size of directory is: {size/1000:.2f} KB")
            else:
                print(f"The size of directory is: {size} bytes")
    else:
        print("Error: Not a directory")
else:
    print("Error: File not found")
