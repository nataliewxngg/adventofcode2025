# Dec 4 2025
# Day 4: Printing Department

# Import the puzzle
import os
here = os.path.dirname(__file__)

with open(os.path.join(here, 'day4Input.txt')) as puzzleFile:
    puzzle = puzzleFile.read().splitlines()

puzzleFile.close()

# Checks for and returns the number of rolls surrounding a roll
def checkForRollsSurrounding(currentRowIndex, currentCharIndex):
    rollsSurrounding = 0
    rowLength = len(puzzle[0])
    prevRow = nextRow = '*' * rowLength

    # Set the previous row and next row, 
    # but add a placeholder if the current row is the first or last 
    if (currentRowIndex == 0): 
        nextRow = puzzle[currentRowIndex+1]
    elif (currentRowIndex == len(puzzle)-1):
        prevRow = puzzle[currentRowIndex-1]
    else:
        prevRow = puzzle[currentRowIndex-1]
        nextRow = puzzle[currentRowIndex+1]
    
    # Check left side
    if (currentCharIndex != 0):
        rollsSurrounding += (int(prevRow[currentCharIndex-1] == '@') + 
                             int(puzzle[currentRowIndex][currentCharIndex-1] == '@') + 
                             int(nextRow[currentCharIndex-1] == '@'))
    
    # Check above and below
    rollsSurrounding += (int(prevRow[currentCharIndex] == '@') + 
                         int(nextRow[currentCharIndex] == '@'))

    # Check right side
    if (currentCharIndex != rowLength-1):
        rollsSurrounding += (int(prevRow[currentCharIndex+1] == '@') + 
                             int(puzzle[currentRowIndex][currentCharIndex+1] == '@') + 
                             int(nextRow[currentCharIndex+1] == '@'))

    return rollsSurrounding

totalRemovedRolls = 0

while True:
    removedRolls = 0
    newPuzzle = list(puzzle)

    for rowIndex in range(len(puzzle)):
        for charIndex in range(len(puzzle[rowIndex])):
            if (puzzle[rowIndex][charIndex] == '@' and checkForRollsSurrounding(rowIndex, charIndex) < 4):
                removedRolls += 1
                newPuzzle[rowIndex] = newPuzzle[rowIndex][:charIndex] + '.' + newPuzzle[rowIndex][charIndex+1:]

    if removedRolls == 0:
        break
    totalRemovedRolls += removedRolls
    puzzle = list(newPuzzle)
        
print(totalRemovedRolls)