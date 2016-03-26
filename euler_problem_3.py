# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# what is a prime number
# no other number except for one is divisible by it except for 1
# what is a prime factor of a number x?
# a number that divides through x with no remainders and which is also a prime number
# the number we're looking for has three properties:
# prime number
# factor
# largest number from that list

import math

def multipleInList(list_of_prime_factors, num):
	for prime_num in list_of_prime_factors:
		if num % prime_num == 0:
			return True
	return False

num = 600851475143
x = 2
list_of_prime_factors = [2]
largestPrimeFactor = -1

while (x < math.sqrt(num)):
	if (num % x == 0):
		if not multipleInList(list_of_prime_factors, x):
			list_of_prime_factors.append(x)
	x += 1

print list_of_prime_factors[-1]

