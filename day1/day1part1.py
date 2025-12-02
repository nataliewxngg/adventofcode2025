# Dec 1 2025
# Day 1: Secret Entrance

# Import the puzzle
with open('day1Input.txt') as puzzleFile:
    puzzle = puzzleFile.read().splitlines()
puzzleFile.close()

# Start at 50
dial = 50
password = 0

# Iterate through each rotation and update dial
for rotation in puzzle:
    if rotation[0] == 'L': # L - subtract
        dial -= int(rotation[1:])
    else: # R - add
        dial += int(rotation[1:])
    
    # Adjust the dial number if out of range
    while (dial < 0):
        dial += 100
    while (dial > 99):
        dial -= 100

    # Update password (dial at 0 count)
    if (dial == 0):
        password += 1

print('The password is ' + str(password))
