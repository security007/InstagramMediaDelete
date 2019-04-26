#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

import subprocess

from InstagramAPI import InstagramAPI

USERNAME = ''
PASSWORD = ''
FILE_PATH = '/path/to/video/file'
PUBLISH_TO_LIVE_FEED = False
SEND_NOTIFICATIONS = False

api = InstagramAPI(USERNAME, PASSWORD, debug=False)
assert api.login()

# first you have to create a broadcast - you will receive a broadcast id and an upload url here
assert api.createBroadcast()
broadcast_id = api.LastJson['broadcast_id']
upload_url = api.LastJson['upload_url']

# we now start a boradcast - it will now appear in the live-feed of users
assert api.startBroadcast(broadcast_id, sendNotification=SEND_NOTIFICATIONS)

ffmpeg_cmd = "ffmpeg -rtbufsize 256M -re -i '{file}' -acodec libmp3lame -ar 44100 -b:a 128k -pix_fmt yuv420p -profile:v baseline -s 720x1280 -bufsize 6000k -vb 400k -maxrate 1500k -deinterlace -vcodec libx264 -preset veryfast -g 30 -r 30 -f flv '{stream_url}'".format(
    file=FILE_PATH,
    stream_url=upload_url.replace(':443', ':80', ).replace('rtmps://', 'rtmp://'),
)

print("Hit Ctrl+C to stop broadcast")
try:
    subprocess.call(ffmpeg_cmd, shell=True)
except KeyboardInterrupt:
    print('Stop Broadcasting')

assert api.stopBroadcast(broadcast_id)

print('Finished Broadcast')

if PUBLISH_TO_LIVE_FEED:
    api.addBroadcastToLive(broadcast_id)
    print('Added Broadcast to LiveFeed')
