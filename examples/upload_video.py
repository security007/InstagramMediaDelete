#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import urllib

video_url = 'https://instagram.fmad3-2.fna.fbcdn.net/t50.2886-16/17157217_1660580944235536_866261046376005632_n.mp4'  # a valid instagram video
video_local_path = video_url.split("/")[-1]
thumbnail_url = "https://instagram.fmad3-2.fna.fbcdn.net/t51.2885-15/e15/17075853_1759410394387536_3927726791665385472_n.jpg"
thumbnail_local_path = thumbnail_url.split("/")[-1]

urllib.urlretrieve(video_url, video_local_path)
urllib.urlretrieve(thumbnail_url, thumbnail_local_path)

InstagramAPI = InstagramAPI("login", "password")
InstagramAPI.login()  # login
InstagramAPI.uploadVideo(video_local_path, thumbnail_local_path, caption="Tortuguero")
