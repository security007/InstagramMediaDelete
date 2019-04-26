#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("login", "password")
InstagramAPI.login()                        # login
mediaId = '1469246128528859784_1520706701'    # a media_id
recipients = []                             # array of user_ids. They can be strings or ints
InstagramAPI.direct_share(mediaId, recipients, text='aquest es es darrer')
