# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

digits = []
digits.append(1)
for i in range(999):
	digits.append(0)

for i in range(1000):
	carryOnValue = 0
	for j in range(1000):
		timesTwo = digits[j]*2 + carryOnValue

		if timesTwo >= 10:
			carryOnValue = 1
		else:
			carryOnValue = 0
		digits[j] = (timesTwo % 10)

sumDigits = reduce(lambda x, y: x+y, digits)
print sumDigits