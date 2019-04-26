#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI

"""
## Uploading a timeline album (aka carousel aka sidecar).
"""
media = [  # Albums can contain between 2 and 10 photos/videos.
    {
        'type': 'photo',
        'file': '/path/to/your/photo.jpg',  # Path to the photo file.
        'usertags': [
            {  # Optional, lets you tag one or more users in a PHOTO.
                'position': [0.5, 0.5],
                # WARNING: THE USER ID MUST BE VALID. INSTAGRAM WILL VERIFY IT
                # AND IF IT'S WRONG THEY WILL SAY "media configure error".
                'user_id': '123456789',  # Must be a numerical UserPK ID.
            },
        ]
    },
    {
        'type': 'photo',
        'file': '/path/to/your/photo.jpg',  # Path to the photo file.
    },
    # {
    #    'type'     : 'video',
    #    'file'     : '/path/to/your/video.mp4', # Path to the video file.
    #    'thumbnail': '/path/to/your/thumbnail.jpg'
    # }
]
captionText = 'caption 3'  # Caption to use for the album.
ig = InstagramAPI("login", "password")
ig.login()
ig.uploadAlbum(media, caption=captionText)
