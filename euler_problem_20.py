'''
Factorial digit sum
Problem 20
n means n * (n - 1) * * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

digits = [0 for i in range(300)]
digits[0] = 1

def copyList(oldList, newList):
	for i in range(len(newList)):
		oldList[i] = newList[i]

def multiply(num, digits):
	i = 0
	tempDigits = [0 for j in range(300)]
	for digit in digits:
		result = num*digit
		if not result == 0:
			addToArrayNum(result, i, tempDigits)
		i += 1
	copyList(digits, tempDigits)

def addToArrayNum(num, tenToThePowerOf, tempDigits):
	i = tenToThePowerOf
	carryOverVal = 0
	while (num > 0):
		tempVal = tempDigits[i] + (num % 10) + carryOverVal
		if tempVal < 10:
			tempDigits[i] = tempVal
			carryOverVal = 0
		else:
			tempDigits[i] = (tempVal % 10)
			carryOverVal = (int)(tempVal/10)
		num  = (int)(num/10)
		i += 1

	if carryOverVal > 0:
		tempVal = tempDigits[i] + carryOverVal
		if tempVal < 10:
			tempDigits[i] = tempVal
		else:
			tempDigits[i] = (tempVal % 10)

def factorial(num):
	for i in range(1, num+1):
		multiply(i, digits)

factorial(100)
print reduce(lambda x, y: x+y, digits)



