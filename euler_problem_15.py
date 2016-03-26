# Starting in the top left corner of a 22 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 2020 grid?

lengthRow = 21
rows = []
for i in range(lengthRow-1):
	cols = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
	rows.append(cols)

rows.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

maxLength = 20

for i in reversed(range (maxLength)):
	for j in reversed(range (maxLength)):
		rows[i][j] = rows[i][j+1] + rows[i+1][j]

print rows[0][0]
