"""
DateTime

3/27/15
Albert Liang

Importing the time module, print the current global and local date and time to console.
"""

import time

gnow = time.gmtime(time.time())
lnow = time.localtime(time.time())
	#What's with the weird nested time functions?

print "Global:\t", time.asctime(gnow)
print "Local:\t", time.asctime(lnow)

