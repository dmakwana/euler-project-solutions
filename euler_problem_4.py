# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


# need some way to check if the number is a palindrome
#
# make sure the given number is 6 digits before passing it through
import sys

def isPalindrome(num):
	chars = list(str(num))
	if chars[0] == chars[5]:
		if chars[1] == chars[4]:
			if chars[2] == chars[3]:
				return True
	return False

num = 998001
largestNumber = 0

while num > 99999:
	if isPalindrome(num):
		val1 = 999
		while (val1 > 99):
			val2 = num/val1
			if (num % val1 == 0 and val2 < 1000 and val2 > 99 ):
				print num
				print val2
				print val1
				sys.exit()
			val1 -= 1

	num -= 1

# print largestNumber