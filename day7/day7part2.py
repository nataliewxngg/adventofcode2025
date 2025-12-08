# Dec 7 2025
# Day 7: Laboratories

# Import the puzzle
import os

here = os.path.dirname(__file__)

with open(os.path.join(here, 'day7TestInput.txt')) as puzzleFile:
    puzzle = []
    
    for line in puzzleFile:
        puzzle.append(line.strip('\n'))

puzzleFile.close()

prevBeamIndex = puzzle[0].find('S')

def findPathCount(prevBeamIndex, currentRow):
    splitCount = 0

    # Return 0 if the current grid item is out of bounds
    if currentRow >= len(puzzle):
        return 1
    if prevBeamIndex >= len(puzzle[0]):
        return 1
    
    # Only one path is possible
    if puzzle[currentRow][prevBeamIndex] == '.':
        splitCount += findPathCount(prevBeamIndex, currentRow+1)
    
    # Meets a splitter
    elif puzzle[currentRow][prevBeamIndex] == '^':
        splitCount += findPathCount(prevBeamIndex-1, currentRow+1)
        splitCount += findPathCount(prevBeamIndex+1, currentRow+1)

    return splitCount

print(findPathCount(prevBeamIndex, 1))

'''
# Slow solution

# Start by identifying the index of the tachyon beam
prevBeamIndexes = [puzzle[0].find('S')]

# Update beamIndex at each line by checking for splitters
pathCount = 1
for lineIndex in range(1, len(puzzle)):
    currentLine = puzzle[lineIndex]
    currentBeamIndexes = []

    for prevBeamIndex in prevBeamIndexes:

        # Beam meets a splitter
        if (currentLine[prevBeamIndex] == '^'):
            pathCount += 1
            currentBeamIndexes.append(prevBeamIndex-1)
            currentBeamIndexes.append(prevBeamIndex+1)

        # Beam does NOT meet a splitter
        else:
            currentBeamIndexes.append(prevBeamIndex)
    
    prevBeamIndexes = currentBeamIndexes
            
print(pathCount)

'''