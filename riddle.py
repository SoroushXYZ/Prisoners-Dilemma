import random

numberOfPrisoners = 100
numberOfRounds = 100000 # Number of the test runs

results = [0, 0] # 0 for the losses and 1 for the wins

for i in range(numberOfRounds):
    # Generate an array with numbers 0 to 99
    numbers = list(range(numberOfPrisoners))
    # Randomize the number inside the boxes
    random.shuffle(numbers)

    # Looping through the prisoners
    for prisoner in range(numberOfPrisoners):
        # Their first box choice will be their own number
        lastChoice = prisoner
        # They can search boxes as many as their polulation divided by 2
        for attemps in range(int(numberOfPrisoners / 2)):
            # If he find his number we break the loop
            if(prisoner == numbers[lastChoice]):
                break
            # Choosing the next box based on the number inside the current box
            lastChoice = numbers[lastChoice] # His next choice will be the number in the box
        
        # If not all of them made it else if none of them made it
        if(prisoner != numbers[lastChoice]):
            results[1] += 1 # Counts a loss
            break
        elif(prisoner == numbers[lastChoice] and prisoner == numberOfPrisoners - 1):
            results[0] += 1 # Counts a win
            
    print("Success Chance: " + str(results[0] / (sum(results)) * 100) + "%")