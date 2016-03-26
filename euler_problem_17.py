#Number letter counts
#Problem 17
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

import string

oneToNineteen = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen"
oneToNineteenList = oneToNineteen.split()
tens = "ten twenty thirty forty fifty sixty seventy eighty ninety"
tensList = tens.split()
hundred = 7 
ands = 3
thousand = 8
oneToNineteenNum = []
tensNum = []
total = 0

for word in oneToNineteenList:
	oneToNineteenNum.append(len(word))

for word in tens.split():
	tensNum.append(len(word))

totalChars = 0
listz = [342]
for num in range(1,1001):
# for num in listz:

	numChars = 0
	numRevList = list(str(num))[::-1]
	totalLength = len(numRevList)
	modTens = num%100
	if modTens == 0:
		hundo = hundred
	else:
		hundo = hundred + ands
	i = 0

	if modTens < 20 and modTens > 0:
		numChars += oneToNineteenNum[modTens - 1]
		if totalLength > 2:
			i = 2
		else:
			totalChars += numChars
			continue

	if i == 0 and numRevList[0] == 0:
		i == 1

	while i < totalLength:
		digitChar = numRevList[i]
		digitNum = string.atoi(digitChar)
		if not digitNum == 0: 
			if i == 0 or i == 2:
				numChars += oneToNineteenNum[digitNum - 1]
				if i == 2:
					numChars += hundo
			elif i == 1:
				numChars += tensNum[digitNum - 1]
			elif i == 3:
				numChars += len("onethousand")

		i += 1

	totalChars += numChars

print totalChars
