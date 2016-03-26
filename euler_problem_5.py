# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#i.e 420, 8, return 4
# after, divide small by the return value to get the number by which you should multiply by
# big should be the current_lowest_multiple
def reduceValues(big, small):
	i = 2
	if big % small == 0:
		return (big/small, small/small)
	while i < small:
		if big % i == 0 and small % i == 0:
			return reduceValues(big/i, small/i)
		i += 1
	return [big, small]

def multiplyBy(big, small):
	retVal = reduceValues(big,small)
	return retVal[1]

nums = range(2,21)
current_lowest_multiple = 2
for number in nums:
	current_lowest_multiple *= multiplyBy(current_lowest_multiple, number)


print current_lowest_multiple

