# Dec 2 2025
# Day 2: Gift Shop

# Import the puzzle
import os
here = os.path.dirname(__file__)

with open(os.path.join(here, 'day2Input.txt')) as puzzleFile:
    puzzle = puzzleFile.read().split(',')
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

    # Split the number into multiple parts evenly,
    # but return if inputted num is a one-digit
    if (len(numStr) < 2): 
        return

    # Append if all digits are the same
    if (all(char == numStr[0] for char in numStr)):
        invalidIDs.append(int(numStr))
        return
    
    split = 0
    if (len(numStr)%2 != 0):
        # Find split by common multiple
        for i in range(3, len(numStr)):
            if (len(numStr)%i == 0):
                split = i
                break
        if (split == 0):
            return
    else:
        split = 2

    while (split < len(numStr)):
        if (isInvalid(numStr, split)): 
            invalidIDs.append(int(numStr))
            return
        split += 1

# Check if each number in range is invalid
for input in puzzle: 
    lowerBound = int(input[:input.index('-')])
    higherBound = int(input[input.index('-')+1:])

    for i in range(lowerBound, higherBound + 1):
        appendIfInvalid(i)

print(sum(invalidIDs))