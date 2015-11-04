#4chan downloader
import sys
import urllib2
import urllib
import re
import os
import time

board, thread = 'b', '643442947'

def getPath(prefName, filetype):
	path = prefName + '.' + filetype
	post = 0
	while os.path.exists(path):
		post += 1
		path = '%s (%d).%s' %(prefName, post, filetype)
	return path

reg = re.compile('<a href="(//i.4cdn.org/%s/\d+\.\w{3,4})" target="_blank">(.*?)\.(\w{3,4})</a>' %board)
page = urllib2.urlopen(r'http://boards.4chan.org/%s/thread/%s' %(board, thread)).read()
for match in reg.finditer(page):
	time.sleep(1)
	url, name, ftype = 'http:' + match.group(1), match.group(2), match.group(3)
	
	print("%s == %s.%s" % (url,name,ftype)) 
	try:
		output = open(getPath(name, ftype), 'wb')
		output.write(urllib2.urlopen(url).read())
		output.close()
	except Exception, e:
		print(str(e))
