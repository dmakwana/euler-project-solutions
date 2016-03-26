'''
Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a)  b and d(b)  a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
# import math

def find_sum_of_divisors(n):
	sumFactors = 0
	lim = n/2
	i = 1
	while i <= lim:
		if n % i == 0:
			sumFactors += i
		i += 1
	return sumFactors

def populate_sum_divisor_table(table):
	for i in range(len(table)):
		table[i] = find_sum_of_divisors(i)

sumDivisorTable = [0 for j in range(10001)]

populate_sum_divisor_table(sumDivisorTable)
sumAmicable = 0

for i in range(len(sumDivisorTable)):
	val = sumDivisorTable[i]
	if val > 0 and val <= 10000:
		if sumDivisorTable[val] == i:
			if not val == i:
				sumAmicable += val
				sumAmicable += i
			sumDivisorTable[val] = 0

print sumAmicable



