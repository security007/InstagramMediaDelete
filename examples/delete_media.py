#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
# 
# example delete_media
# this example for how to delete self media feed
# have 2 parameter on method deleteMedia( MediaID, MediaType)

from InstagramAPI import InstagramAPI 

# change this username & password
username = 'your_username_here'
password = 'your_password_here'

ig = InstagramAPI(username, password) 

# login 
ig.login() 

# get Self user feed 
ig.getSelfUserFeed()

# get response json and assignment value to MediaList Variable
# dict type data 
MediaList = ig.LastJson 

# get first media for example delete media
Media = MediaList['items'][0]

# get media ID 

MediaID = Media['id']
MediaType = Media['media_type']

# call deleteMedia Method
# deleteMedia return BOOL {true|false} 
isDeleted = ig.deleteMedia(MediaID, media_type=MediaType)

if isDeleted:
    print("Your Media {0} has been deleted".format(
        MediaID
    ))
else:
    print("Your Media Not Deleted")
