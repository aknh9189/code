import time, math, itertools
import numpy as np
#set grid variable equal to one you want solved
grid = [
[0,6,0,1,0,4,0,5,0],
[0,0,8,3,0,5,6,0,0],
[2,0,0,0,0,0,0,0,1],
[8,0,0,4,0,7,0,0,6],
[0,0,6,0,0,0,3,0,0],
[7,0,0,9,0,1,0,0,4],
[5,0,0,0,0,0,0,0,2],
[0,0,7,2,0,6,9,0,0],
[0,4,0,5,0,8,0,7,0]
]
# grid = [
# [9,6,3,1,7,4,2,5,8],
# [1,7,8,3,2,5,6,4,9],
# [2,5,4,6,8,9,7,3,1],
# [8,2,1,4,3,7,5,9,6],
# [4,9,6,8,5,2,3,1,7],
# [7,3,5,9,6,1,8,2,4],
# [5,8,9,7,1,3,4,6,2],
# [3,1,7,2,4,6,9,8,5],
# [6,4,2,5,9,8,1,7,3]
# ]
# grid = [
# [0,0,0,0,8,0,7,0,0],
# [0,9,2,0,1,0,0,0,8],
# [0,0,8,2,0,7,4,0,0],
# [1,0,0,9,0,0,0,4,0],
# [0,3,0,4,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,1],
# [0,4,0,0,7,0,5,0,0],
# [5,0,9,0,0,3,0,7,4],
# [0,8,0,0,0,0,0,0,0],
# ]
#-------------# example layout of coordnate system
#|1,1|2,1|3,1|#
#-------------#
#|1,2|2,2|3,2|#
#-------------#
#|1,3|2,3|3,3|#
#-------------#



def printG(input): #function for printing the sudoko grid
	grid= input
	a = "-------------------------------" #example line
	print a #print top line
	for i in range(0,9):
		line = ""
		for j in range(0,9):
			if j == 0:
				line = line + "| {0} ".format(grid[i][j]) #print beggining of line
			elif j == 8:
				line = line + " {0} |".format(grid[i][j]) #print end of line
			elif j == 2 or j ==5:
				 line = line + " {0} |".format(grid[i][j]) #print end of 3x3 grid
			else:
				line = line + " {0} ".format(grid[i][j]) #print any other one
		print line
		if i == 2 or i == 5: #print horizontal grid lines
			print a
	print a #print bottom line

def findZeros(): #find number of empty spaces in grid total
	zeros = 0
	for i in range(0,9): #scan through each row and collumb
		for j in range(0,9):
			if grid[i][j] == 0: #if the space is zero
				zeros = zeros + 1 #add to variable
	return zeros

def missingSquares(x,y): #find and return the numbers that are not in each square (9 total)
	#x and y are distance from top(0,0), 1 through 3 to select grid to search through
	toAddX = (x*3)-3 #for 1=1, 2=3, 3=6
	toAddY = (y*3)-3 # "     "

	nums = [1,2,3,4,5,6,7,8,9]
	sq = []
	for i in range(0,3):
		for j in range(0,3):
			sq.append(grid[i+toAddY][j+toAddX]) #add all of the things to one set from square
	notInSquare = list(set(nums) - (set(sq)-set([0]))) #remove the ones that arent in it
	return notInSquare #return array of missing numbers

def missingLines(rc,which): #find the numbers that are missing from each row or collum
	#enter either the row or collumn number(1,9), then if it is a row or collum (1,0)
	place = rc-1#fix indexing
	nums = [1,2,3,4,5,6,7,8,9] #da numbas
	thereAlready = []
	
	for i in range(0,9): #scan each one
		if which == 0: # if it is down (column)
			thereAlready.append(grid[i][place]) #add pre-existing numbers
		elif which == 1: #if it is across (row)
			thereAlready.append(grid[place][i])
	notInLine = list(set(nums) - (set(thereAlready)-set([0]))) #subtact sets, result is the numbers that are not in the row alreay. 
	return notInLine #return list of mssing numbers

def invert(input): #invert the list ex a = [1,4,5,7] inverted = [2,3,6,8,9]
	input = set(input)
	nums = set([1,2,3,4,5,6,7,8,9]) #simple function to be used later (I think?)
	return list(nums - input)

def totalMissing(): #find all the missing numbers
	missing = []
	for i in range(0,9):
		curLine = missingLines(i,0) #find all the missing numbers for each row
		for j in range(0,len(curLine)):
			missing.append(curLine[j]) #append them all to one array
	return missing #return it

def valid(input): #check if a grid is valid by cross referencing the numbers in lines vs the numbers in grid cells (3x3)
	grid = input #grab input
	#check lines
	for i in range(0,9): #rows
		line = []
		for j in range(0,9): #collums
			unit = grid[i][j]
			if unit != 0:
				line.append(unit) #append every number in array as long as it is not an empty space (zero)
		if len(line) != len(list(set(line))): #sees if there are any doubles in lines
			return i #returns the row(across) that is not valid
	for i in range(0,9):
		line = []
		for j in range(0,9):
			unit = grid[j][i]
			if unit != 0:
				line.append(unit)
		if len(line) != len(list(set(line))): #sees if there are any doubles in lines
			return i #returns the row(across) that is not valid
	#check squares
	
	for y in range(1,4):
		for x in range(1,4):
			toAddX = (x*3)-3 #for 1=1, 2=3, 3=6 #checks eaach 3x3 grid
			toAddY = (y*3)-3 # "     "
			sq = []
			for i in range(0,3): #rows in grid
				for j in range(0,3): #cols in grid
					if grid[i+toAddY][j+toAddX] != 0:
						sq.append(grid[i+toAddY][j+toAddX]) #add all of the things to one set from square
			if len(sq) != len(list(set(sq))): #verifies that the 9 grids are alright
				return (x,y) #returns 


def zeroPos(line): #enter a line (1-9) and returns a list of the zero positions
	zeroLoc = []
	linePos = line-1
	for i in range(0,9):
		if 0 == grid[linePos][i]:
			zeroLoc.append(i)
	return zeroLoc
def solve():
	start = time.time()
	missingRows = []
	missingPos = []
	print "Starting at {}".format(start)
	printG(grid)
	for i in range(1,10): #finds every missing one and position
		line = i
		miss = missingLines(line,1)
		zPos = zeroPos(i)
		missingRows.append(miss)
		missingPos.append(zPos)
	
	row1 = itertools.permutations(missingRows[0],len(missingRows[0])) #generate every possible solution for the lines. 
	row2 = itertools.permutations(missingRows[1],len(missingRows[1]))
	row3 = itertools.permutations(missingRows[2],len(missingRows[2]))
	row4 = itertools.permutations(missingRows[3],len(missingRows[3]))
	row5 = itertools.permutations(missingRows[4],len(missingRows[4]))
	row6 = itertools.permutations(missingRows[5],len(missingRows[5]))
	row7 = itertools.permutations(missingRows[6],len(missingRows[6]))
	row8 = itertools.permutations(missingRows[7],len(missingRows[7]))
	row9 = itertools.permutations(missingRows[8],len(missingRows[8]))

	allCombs = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
	acceptedCombos = []
	for i in range(0,len(allCombs)): #find all the accepted possibilities for each row
		accepted = []
		positions = missingPos[i]

		for x in allCombs[i]: #(line is equal to i)

			for y in range(0,len(x)): #changes the line
				grid[i][positions[y]] = x[y]

			

			if valid(grid) == None:
				accepted.append(list(x))
		for y in range(0,len(positions)): #changes the line
				grid[i][positions[y]] = 0

		acceptedCombos.append(accepted)
	TOTAL = len(acceptedCombos[0])*len(acceptedCombos[1])*len(acceptedCombos[2])*len(acceptedCombos[3])*len(acceptedCombos[4])*len(acceptedCombos[5])*len(acceptedCombos[6])*len(acceptedCombos[7])*len(acceptedCombos[8])
	print "Longest possible solution time: {0} seconds".format(TOTAL*.2) 
	#Now try every possible solution!
	#acceptedCombos[level(0-8)][solution][objects in solution]
	#missingPosition[level]
	startLoop = time.time()
	for a in range(0, len(acceptedCombos[0])):
		for b in range(0, len(acceptedCombos[1])):
			for c in range(0, len(acceptedCombos[2])):
				for d in range(0, len(acceptedCombos[3])):
					for e in range(0, len(acceptedCombos[4])):
						for f in range(0, len(acceptedCombos[5])):
							for g in range(0, len(acceptedCombos[6])):
								for h in range(0, len(acceptedCombos[7])):
									for i in range(0, len(acceptedCombos[8])):
										for y in range(0,len(acceptedCombos[0][a])): #changes the line 1
											grid[0][missingPos[0][y]] = acceptedCombos[0][a][y]
										for y in range(0,len(acceptedCombos[1][b])): #changes the line 2
											grid[1][missingPos[1][y]] = acceptedCombos[1][b][y]
										for y in range(0,len(acceptedCombos[2][c])): #changes the line 3
											grid[2][missingPos[2][y]] = acceptedCombos[2][c][y]
										for y in range(0,len(acceptedCombos[3][d])): #changes the line 4
											grid[3][missingPos[3][y]] = acceptedCombos[3][d][y]
										for y in range(0,len(acceptedCombos[4][e])): #changes the line 5
											grid[4][missingPos[4][y]] = acceptedCombos[4][e][y]
										for y in range(0,len(acceptedCombos[5][f])): #changes the line 6
											grid[5][missingPos[5][y]] = acceptedCombos[5][f][y]
										for y in range(0,len(acceptedCombos[6][g])): #changes the line 7
											grid[6][missingPos[6][y]] = acceptedCombos[6][g][y]
										for y in range(0,len(acceptedCombos[7][h])): #changes the line 8
											grid[7][missingPos[7][y]] = acceptedCombos[7][h][y]
										for y in range(0,len(acceptedCombos[8][i])): #changes the line 9
											grid[8][missingPos[8][y]] = acceptedCombos[8][i][y]
										if valid(grid) == None:
											end = time.time()
											tExecute = end-start
											print "Finished in {0} seconds".format(tExecute)
											return grid


										else:
											for y in range(0,len(acceptedCombos[0][a])): #changes the line 1
												grid[0][missingPos[0][y]] = 0
											for y in range(0,len(acceptedCombos[1][b])): #changes the line 2
												grid[1][missingPos[1][y]] = 0
											for y in range(0,len(acceptedCombos[2][c])): #changes the line 3
												grid[2][missingPos[2][y]] = 0
											for y in range(0,len(acceptedCombos[3][d])): #changes the line 4
												grid[3][missingPos[3][y]] = 0
											for y in range(0,len(acceptedCombos[4][e])): #changes the line 5
												grid[4][missingPos[4][y]] = 0
											for y in range(0,len(acceptedCombos[5][f])): #changes the line 6
												grid[5][missingPos[5][y]] = 0
											for y in range(0,len(acceptedCombos[6][g])): #changes the line 7
												grid[6][missingPos[6][y]] = 0
											for y in range(0,len(acceptedCombos[7][h])): #changes the line 8
												grid[7][missingPos[7][y]] = 0
											for y in range(0,len(acceptedCombos[8][i])): #changes the line 9
												grid[8][missingPos[8][y]] = 0

											time2 = time.time()
											if time2-startLoop > 15:
												print "A is {0}, still working...".format(a)
												startLoop = time.time()
	print "There is no solution"




	
sol = solve() #run function
printG(sol)  #print solution



