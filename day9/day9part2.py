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
print(puzzle)

# Collect the vertices for the outline green tiles
edges = []
for indexOfPt in range(len(puzzle)):
    curr = puzzle[indexOfPt]
    next = puzzle[(indexOfPt + 1) % len(puzzle)]

    edges.append((curr[0], curr[1], next[0], next[1]))

print(edges)

# Determines the area given two points (of red tiles)
def getArea(pt1, pt2):
    return (pt1[0]-pt2[0]+1) * (pt1[1]-pt2[1]+1)

# Returns a and b such that a is always less than b
def sort(a, b):
    return (a, b) if a < b else (b,a)

# Calculate the manhatten distance between 2 points
def manhattan(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

# Return true if the rectangle crosses the boundary
def rectangleIntersectsEdge(minx, miny, maxx, maxy, edges):
    for edge in edges:
        x1, y1, x2, y2 = edge

        edgeMinX, edgeMaxX = sort(x1, x2)
        edgeMinY, edgeMaxY = sort(y1, y2)

        if (minx < edgeMaxX and maxx > edgeMinX and miny < edgeMaxY and maxy > edgeMinY):
            return True
    return False


# Calculate the greatest area
greatestArea = 0

for indexOfPt1 in range(len(puzzle)):
    for indexOfPt2 in range(indexOfPt1, len(puzzle)):

        pt1 = puzzle[indexOfPt1]
        pt2 = puzzle[indexOfPt2]

        minx, maxx = sort(pt1[0], pt2[0])
        miny, maxy = sort(pt1[1], pt2[1])

        # Optimize solution by skipping small rectangles
        manhattanD = manhattan(pt1, pt2)
        if manhattanD**2 <= greatestArea:
            continue
        
        # Reject if rectangle crosses the boundary
        if rectangleIntersectsEdge(minx, miny, maxx, maxy, edges):
            continue

        area = getArea(pt1, pt2)
        if area > greatestArea:
            greatestArea = area

print(greatestArea)