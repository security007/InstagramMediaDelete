#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import time
from datetime import datetime

user_id = ''

API = InstagramAPI("login", "password")
API.login()

API.getUsernameInfo(user_id)
API.LastJson
following = []
next_max_id = True
while next_max_id:
    print next_max_id
    # first iteration hack
    if next_max_id is True:
        next_max_id = ''
    _ = API.getUserFollowings(user_id, maxid=next_max_id)
    following.extend(API.LastJson.get('users', []))
    next_max_id = API.LastJson.get('next_max_id', '')

len(following)
unique_following = {
    f['pk']: f
    for f in following
}
len(unique_following)
