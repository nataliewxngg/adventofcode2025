# Dec 9 2025
# Day 9: Movie Theater

# Import the puzzle
import os

here = os.path.dirname(__file__)

with open(os.path.join(here, 'day9Input.txt')) as puzzleFile:
    puzzle = []
    
    for line in puzzleFile:
        puzzle.append((int(line[:line.find(',')]), int(line.strip('\n')[line.find(',')+1:])))

puzzleFile.close()

# Determines the area given two points (of red tiles)
def getArea(pt1, pt2):
    return (pt1[0]-pt2[0]+1) * (pt1[1]-pt2[1]+1)

# Collects all the outline green tiles
outlineGreenTiles = []
for indexOfPt in range(len(puzzle)):
    indexOfOtherPt = (indexOfPt + 1) % len(puzzle)

    x1, y1 = puzzle[indexOfPt]
    x2, y2 = puzzle[indexOfOtherPt]
    
    if x1 == x2:
        if (y1 > y2):
            y1, y2 = y2, y1

        for i in range(y1+1, y2):
            outlineGreenTiles.append((x1, i))
    else:
        if (x1 > x2):
            x1, x2 = x2, x1

        for i in range(x1+1, x2):
            outlineGreenTiles.append((i, y1))

# Collects and add the filling green tiles as well
validTiles = sorted(outlineGreenTiles + puzzle, key=lambda tup: (tup[1], tup[0]))
newTiles = []
for indexOfPt in range(len(validTiles)):
    indexOfOtherPt = (indexOfPt + 1) % len(validTiles)

    x1, y1 = validTiles[indexOfPt]
    x2, y2 = validTiles[indexOfOtherPt]

    # find where y changes
    if y1 == y2 and abs(x1 - x2) != 1:
            for i in range(min(x1, x2)+1, min(x1,x2) + abs(x2-x1)):
                if (i, y1) not in validTiles:
                    newTiles.append((i, y1))

validTiles = validTiles + newTiles

greatestArea = 0
for indexOfPt1 in range(len(puzzle)):
    for indexOfPt2 in range(indexOfPt1+1, len(puzzle)):

        pt3 = (puzzle[indexOfPt1][0], puzzle[indexOfPt2][1])
        pt4 = (puzzle[indexOfPt2][0], puzzle[indexOfPt1][1])

        if getArea(puzzle[indexOfPt1], puzzle[indexOfPt2]) > greatestArea and (pt3 in validTiles or pt3 in puzzle) and (pt4 in validTiles or pt4 in puzzle):
            greatestArea = getArea(puzzle[indexOfPt1], puzzle[indexOfPt2])

print(greatestArea)