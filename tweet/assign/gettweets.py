import sys
import string
import json


def main():
    tweet_file = open(sys.argv[1])
    ids=""
    for line in tweet_file:
    	jsonstr=json.loads(line)
    	#print jsonstr[u'ids']
    	for i in jsonstr[u'ids']

   # print ids

if __name__ == '__main__':
    main()

