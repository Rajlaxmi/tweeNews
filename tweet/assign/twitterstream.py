import oauth2 as oauth
import urllib2 as urllib
import json

# See Assignment 1 instructions or README for how to get these credentials
access_token_key = "1417182607-TOaH3qLQbeD8KgI5jZpnKZT5MReuAz75VW6GNV4"
access_token_secret = "p0k1b4VchtTfF9A0HGOITOAkIYZmeWH5lBnPN8oKjN8"

consumer_key = "3dqaszQiz9RJxw5788Sg"
consumer_secret = "h0YKRNbHi4BrbBx1IvbuCIqbR9gC7vekcx14Mk"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"

http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  #url = "https://search.twitter.com/1.1/statuses/filter.json?locations=68,8,97,37"
  #url = "https://api.twitter.com/1.1/search/tweets.json?geocode=19.74,75.71,200mi"
  #url = 'https://api.twitter.com/1.1/search/tweets.json?q=lang%3A&geocode=19.74,75.71,200mi'
  #url='https://api.twitter.com/1.1/followers/ids.json?cursor=-1&screen_name=CNN&count=100'
  url='https://stream.twitter.com/1.1/search/tweets.json?q=telangana lang%3Aen'
  parameters = []
  response = twitterreq(url, "GET", parameters)
  #print response
  for line in response:
    print line.strip()
  '''
  for line in response:
    #print line.strip()
    jsonstr=json.loads(line)
    ids=jsonstr[u'ids']
    for i in ids:
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?include_entities=true&include_rts=false&user_id='+str(i)
        parameters=[]
        resp = twitterreq(url, "GET", parameters)
        for ln in resp:
          print ln.strip()
  '''

        

if __name__ == '__main__':
  fetchsamples()