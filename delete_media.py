#!/usr/bin/python

from InstagramAPI import InstagramAPI 
import sys,time
import random
import requests
import re

def bann():
	print ("""\n
	--------------------------------------
	[+] INSTAGRAM MEDIA MASS DELETE TOOL
	[+] AUTHOR : SECURITY007	
	--------------------------------------
	""")
bann()


def help():
	print ("\nUsage:\npython "+sys.argv[0]+" <username> <password> ")
try:
	username = sys.argv[1]
	password = sys.argv[2]
except:
	help()
	sys.exit()
ran = random.randrange(1,1000)	

ig = InstagramAPI(username, password) 
ig.login() 
try:
	while True:
		ig.getSelfUserFeed()
		MediaList = ig.LastJson 

		Media = MediaList['items'][0]
		MediaID = Media['id']
		MediaType = Media['media_type']
		isDeleted = ig.deleteMedia(MediaID, media_type=MediaType)

		if isDeleted:
    			print("\nYour Media {0} has been deleted".format(MediaID))
		else:
    			print("\nYour Media Not Deleted")
		animation = "-\|/-\|/"
		a = random.randrange(5,10)
		for i in range(a):
			time.sleep(1)
			sys.stdout.write("\r[+] Sleep For %i Seconds %i "%(a,i+1) + animation[i % len(animation)])
			sys.stdout.flush()
	
except IndexError:
	print ("\n[-] No Media Found!!")
	print ("[+] All Done!!")
except KeyboardInterrupt:
	print "\n[-] Exit!"
