# # Large sum
# # Problem 13
# # Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

f = open('data_13', 'r')
fullArray = []
for line in f:
	cols = []
	for char in line:
		try:
			cols.append(int(char))
		except ValueError:
			pass
	cols.reverse()
	fullArray.append(cols)

carryOnValue = 0
totalValue = []
for j in range(len(fullArray[0])):
	sumOfColumn = carryOnValue
	for i in range(len(fullArray)):
		sumOfColumn += fullArray[i][j]
	lastDigit = str(sumOfColumn)[-1]
	totalValue.append(lastDigit)
	list_sumOfColumn = list(str(sumOfColumn))
	del list_sumOfColumn[-1]
	str_sumOfColumn = ''.join(list_sumOfColumn)
	carryOnValue = int(str(str_sumOfColumn))

totalValue.reverse()
answerString = str(carryOnValue)
lastEightDigits = ''.join(totalValue[0:8])
answerString += lastEightDigits

print answerString