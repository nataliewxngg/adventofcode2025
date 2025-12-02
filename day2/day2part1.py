# Dec 2 2025
# Day 2: Gift Shop

# Import the puzzle
import os
here = os.path.dirname(__file__)

with open(os.path.join(here, 'day2Input.txt')) as puzzleFile:
    puzzle = puzzleFile.read().split(',')
print(puzzle)
puzzleFile.close()

# Find all invalid IDs
invalidIDs = []

def isInvalid(numStr, split):
    # Split numStr into separate array indexes by split length
    splitNumStr = []
    for i in range(0, len(numStr), split):
        splitNumStr.append(numStr[i:i+split])

    # Return true if all array indexes contain identical elements
    return all(x == splitNumStr[0] for x in splitNumStr)

def appendIfInvalid(num):
    numStr = str(num)

    # Split the number into 2 parts evenly,
    # but return if inputted num is a one-digit or odd-digit number
    if (len(numStr) < 2 or len(numStr)%2 != 0): 
        return
    split = int(len(numStr) / 2)

    if (isInvalid(numStr, split)): 
        invalidIDs.append(int(numStr))

# Check if each number in range is invalid
for input in puzzle: 
    lowerBound = int(input[:input.index('-')])
    higherBound = int(input[input.index('-')+1:])

    for i in range(lowerBound, higherBound + 1):
        appendIfInvalid(i)

print(invalidIDs)
print(sum(invalidIDs))
