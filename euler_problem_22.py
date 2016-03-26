'''
Names scores
Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value 
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3  15  12  9  14 = 53, 
is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
'''
'''How do you do string comparison in Python?...directly'''

import random
f = open('data_22', 'r')
listNames = []
for line in f:
	names = line.split('","')
	for name in names:
		try:
			listNames.append(name)
		except ValueError:
			pass

listNames[0] = "MARY"
listNames[len(listNames)-1] = "ALONSO"


def quicksort(listNames, startIdx, endIdx):
	pivotIdx = (int)((startIdx+endIdx)/2)
	i = startIdx
	j = endIdx

	while i != pivotIdx or j != pivotIdx:
		while listNames[i] <= listNames[pivotIdx] and i < pivotIdx:
			i += 1
		while listNames[j] >= listNames[pivotIdx] and j > pivotIdx:
			j -= 1
		pivotIdx = swap(listNames, j, i, pivotIdx)
	if startIdx != pivotIdx:
		quicksort(listNames, startIdx, pivotIdx - 1)
	if endIdx != pivotIdx:
		quicksort(listNames, pivotIdx + 1, endIdx)


def swap(listNames, fromIdx, toIdx, pivotIdx):
	temp = listNames[fromIdx]
	listNames[fromIdx] = listNames[toIdx]
	listNames[toIdx] = temp
	if pivotIdx == fromIdx:
		return toIdx
	elif pivotIdx == toIdx:
		return fromIdx
	else:
		return pivotIdx

quicksort(listNames, 0, len(listNames) - 1)

for i in range(len(listNames)):
	sumz = 0
	for char in listNames[i]:
		sumz += (ord(char) - 64)
	listNames[i] = sumz*(i+1)

print reduce(lambda x, y: x+y, listNames)
	# move less than pivot values to the left of the pivot
	# move more than pivot values to the right of the pivot

