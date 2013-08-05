import urllib2

proxy = urllib2.ProxyHandler({'http': 'http://rajlaxmisahu:ilovegoogle%3AD@netmon.iitb.ac.in:80/','https': 'https://rajlaxmisahu:ilovegoogle%3AD@netmon.iitb.ac.in:80/'})

opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

#html = urllib2.urlopen("http://search.twitter.com/search.json?q=microsoft").read()
html = urllib2.urlopen("http://www.flipkart.com/").read()
print html