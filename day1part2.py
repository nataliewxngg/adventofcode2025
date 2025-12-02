# Dec 1 2025
# Day 1: Secret Entrance

# Import the puzzle
with open('day1Input.txt') as puzzleFile:
    puzzle = puzzleFile.read().splitlines()
print(puzzle)
puzzleFile.close()

# Start at 50
dial = 50
password = 0

# Iterate through each rotation and update dial
for rotation in puzzle:
    print(rotation)

    if rotation[0] == 'L': # L - subtract
        if (dial == 0):
            dial = 100
        dial -= int(rotation[1:])
    else: # R - add
        dial += int(rotation[1:])
    
    # Adjust the dial number if out of range
    while (dial < 0):
        dial += 100
        password += 1 
        print('added from pass')
    while (dial > 99):
        dial -= 100
        if (dial != 0): # For part 2 only
            password += 1 
            print('added from pass')

    # Update password (dial at 0 count)
    if (dial == 0):
        password += 1
        print('added from land')

print('Dial: ' + str(dial))
print('The password is ' + str(password))
