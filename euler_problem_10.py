# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from math import sqrt
from math import floor

listPrimeNumbers = [2, 3, 5, 7]

# make sure value is greater than 8
def isPrime(value):
	if value % 3 == 0:
		return False
	if value % 5 == 0:
		return False
	if value % 7 == 0:
		return False
	else:
		limit = floor(sqrt(value))
		f = 6
		while f-1 <= limit:
			if value % (f-1) == 0:
				return False
			if value % (f+1) == 0:
				return False
			f += 6
	return True

value = 9
while value < 2000000:
	value += 2
	if isPrime(value):
		listPrimeNumbers.append(value)

# print listPrimeNumbers
print reduce(lambda x,y: x+y, listPrimeNumbers)