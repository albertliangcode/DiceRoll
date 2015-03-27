"""
DateTime

3/27/15
Albert Liang

Importing the time module, print the current global and local date and time to console.
"""

from time import *

gnow = gmtime(time())
lnow = localtime(time())
	#What's with the weird nested time functions?

print "Global:\t", asctime(gnow)
print "Local:\t", asctime(lnow)

