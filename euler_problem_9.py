# Special Pythagorean triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math
import sys

def checkIdentity(a, b):
	return a + b + math.sqrt(a*a + b*b)

startVal = 10

while (1):
	i = 1
	if checkIdentity(startVal, startVal + i) > 1000:
		print checkIdentity(startVal, startVal + i)
		print "Failed to find values"
		sys.exit(-1)
	while checkIdentity(startVal, startVal + i) < 1000:
		i += 1
	if checkIdentity(startVal, startVal + i) == 1000:
		print startVal, startVal+i
		print startVal*(startVal+i)*math.sqrt(startVal*startVal + (startVal+i)*(startVal+i))
		sys.exit(0)
	else:
		startVal += 1


