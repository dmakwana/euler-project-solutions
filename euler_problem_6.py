# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

numbers = range(1,101)
sumNums = reduce(lambda x,y: x+y, numbers)
print sumNums
retVal = sumNums * sumNums
for value in numbers:
	retVal -= value*value

print retVal