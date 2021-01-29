import re
import win32api
from distutils.dir_util import copy_tree
import os
import sys

filesToCopy = "./files"
assettocorsaPath = f'content\cars'

def find_file(root_folder, rex):
    for root, dirs, files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                path = os.path.join(root, f)
                # remove AssettoCorsa.exe from the string, build correct folder structure
                carsPath = (path[:-16]) + assettocorsaPath
                print("Found assettocorsa file location: " + carsPath)
                # copy the skin
                print("Installing Skins...")
                copy_tree(filesToCopy, carsPath)
                break

def find_file_in_all_drives(file_name):
    rex = re.compile(file_name)
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        find_file(drive, rex)

print()
run = input("Install AC Skins? y/n: ")
if run == "y" or run == "Y":
    try:
        print("Finding assettocorsa directory and installing skins...")
        find_file_in_all_drives('AssettoCorsa\.exe')
        print("Skin Install Complete...")
        input("Press Enter to exit...")
    except:
        print("Could not find assettocorsa file location...")
        input("Press Enter to exit...")
else:
    sys.exit(0)

