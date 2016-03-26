# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


def factorExists(list_to_check, number):
	for primeNumber in list_to_check:
		if number % primeNumber == 0:
			return True
	return False


checkNum = 3
primeNumList = [2]
while len(primeNumList) < 10002:
	if not factorExists(primeNumList, checkNum):
		primeNumList.append(checkNum)
	checkNum += 2

print primeNumList[-2]