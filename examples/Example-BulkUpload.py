#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

import os
import time
import random
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import InstagramAPI

PhotoPath = "~/igphoto/"  # Change Directory to Folder with Pics that you want to upload
# Change to your Photo Hashtag
IGCaption = "Your Caption Here #hashtag"

os.chdir(PhotoPath)
ListFiles = [f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))]
print("Total Photo in this folder:" + str(len(ListFiles)))

# Start Login and Uploading Photo
igapi = InstagramAPI("login", "password")
igapi.login()  # login

for i in range(len(ListFiles)):
    photo = ListFiles[i]
    print("Progress :" + str([i + 1]) + " of " + str(len(ListFiles)))
    print("Now Uploading this photo to instagram: " + photo)
    igapi.uploadPhoto(photo, caption=IGCaption, upload_id=None)
    # sleep for random between 600 - 1200s
    n = randint(600, 1200)
    print("Sleep upload for seconds: " + str(n))
    time.sleep(n)
