# Dec 7 2025
# Day 7: Laboratories

# Import the puzzle
import os

here = os.path.dirname(__file__)

with open(os.path.join(here, 'day7Input.txt')) as puzzleFile:
    puzzle = []
    
    for line in puzzleFile:
        puzzle.append(line.strip('\n'))

puzzleFile.close()
print(puzzle)

splitCount = 0

# Start by identifying the index of the tachyon beam
prevBeamIndexes = [puzzle[0].find('S')]

# Update beamIndex at each line by checking for splitters
for lineIndex in range(1, len(puzzle)):
    currentLine = puzzle[lineIndex]
    currentBeamIndexes = []

    for prevBeamIndex in range(len(prevBeamIndexes)):

        # Beam meets a splitter
        if (currentLine[prevBeamIndexes[prevBeamIndex]] == '^'):
            splitCount += 1
            if prevBeamIndexes[prevBeamIndex]-1 not in currentBeamIndexes:
                currentBeamIndexes.append(prevBeamIndexes[prevBeamIndex]-1)
            if prevBeamIndexes[prevBeamIndex]+1 not in currentBeamIndexes:
                currentBeamIndexes.append(prevBeamIndexes[prevBeamIndex]+1)

        # Beam does NOT meet a splitter
        else:
            if prevBeamIndexes[prevBeamIndex] not in currentBeamIndexes:
                currentBeamIndexes.append(prevBeamIndexes[prevBeamIndex])
    
    prevBeamIndexes = currentBeamIndexes
    currentBeamIndexes = []
            
print(splitCount)