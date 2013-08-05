unicode_string = u'aaa'
encoded_string = unicode_string.encode('utf-8')
print encoded_string

'''import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
print json.load(response)'''

'''afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

print scores.items() # Print every (term, score) pair in the dictionary'''

'''import sys
tweet_file = open(sys.argv[1])
for i in range(0,len(tweet_file.readlines())):
    tweet=tweet_file.readline()
    print tweet'''
'''
import sys
import json
tweet_file=open(sys.argv[1])
#jsonstr= json.load(tweet_file)
data = []
for line in tweet_file:
    jsonstr=json.loads(line)
    if jsonstr.has_key("text"):
    	print jsonstr["text"]
'''
#print data[0]['delete'].encode('utf-8')
#jsonstr = json.load(tweet_file_str)