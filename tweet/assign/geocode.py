import json
import sys
import string

def createDict(afinnfile_url):
	afinnfile = open(afinnfile_url)
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.

	return scores


def hw(sent_file,tweet_file):
    global word_dict 
    word_dict = createDict(sent_file)
    '''
    jsonstr = json.loads(open(tweet_file).read())
    if jsonstr.has_key("statuses"):
    	for line in jsonstr["statuses"]:
    		print line[u'text']
    		if jsonstr.has_key("text"):
    			compute_sent(jsonstr["text"])
    '''
    
    '''
    for line in data.statuses:
		jsonstr=json.loads(line)
		if jsonstr.has_key("text"):
			compute_sent(jsonstr["text"])
    '''
    for line in tweet_file:
    	if(len(line)>=3):
	    	jsonstr=json.loads(line)
	    	if 'telangana' in line.lower():
		    	compute_sent(jsonstr["text"])
		    	if (jsonstr["geo"] is not None):
		    		print jsonstr["geo"][u'coordinates']
		    	
		    	
	
		
    #print dict

			
def compute_tweet(line):
	jsonline=json.loads(line).encode('utf-8')
	return 

def compute_sent(tweet):
#	print tweet.strip()
	tweet_words="".join((char if (char.isalpha()) else " ") for char in tweet).split()
	sum=0
	for word in tweet_words:
		word=word.lower()
		if word_dict.has_key(word):
			sum=sum+int(word_dict[word])
	print(sum)

def lines(fp): #returns no of lines in file
    return len(fp.readlines())

def main():
    tweet_file = open(sys.argv[2])
    hw(sys.argv[1],tweet_file)

if __name__ == '__main__':
    main()			


