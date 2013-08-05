import oauth2 as oauth
import urllib2 as urllib
import urllib as ul
import json
import sys
import string
import time
import logging

_debug = 0
http_handler2  = urllib.HTTPHandler(debuglevel=_debug)
https_handler2 = urllib.HTTPSHandler(debuglevel=_debug)
opener2 = urllib.OpenerDirector()
opener2.add_handler(http_handler2)
opener2.add_handler(https_handler2)

fname='/home/rajlaxmi/Desktop/2.txt'
i=0
while(1):
	with open(fname) as f:
			j=0
			for line in f:
				j=j+1
				if(j>i):
					if line is not None:
						line = line.split(":")
						line = line[2].split(",")
						line[2]=line[2][:-1]
						print line
						url2 = 'http://localhost/tweet/addtodb_action.php?x='+str(line[0])+'&y='+str(line[1])+'&z='+str(line[2])
						opener2.open(url2)
						i=i+1
			f.close()
			#url2 = 'http://localhost/tweet/addtodb_action.php?x='+str(x)+'&y='+str(y)+'&z='+str(score)
			#opener2.open(url2)
		
		


