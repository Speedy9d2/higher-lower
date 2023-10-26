import art
import data
import random

topLogo = art.logo
bottomLogo = art.vs
gameData = data.data


#Function for the game
def format(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

#Start of game logic
isRight = True
count = 0
nextLevel = []

while isRight:
    if count == 0:
        randomA = random.choice(gameData)
        randomB = random.choice(gameData)
        follower_Count_A = randomA["follower_count"]
        follower_Count_B = randomB["follower_count"]
        if randomA == randomB:
            randomB = random.choice(gameData)
        print(topLogo)
        print(f"Compare A: {format(randomA)}")
        print(bottomLogo)
        print(f"Against B: {format(randomB)}")
        userInput = input("Who has more followers? Type 'A' or 'B': ").lower()
        if follower_Count_A > follower_Count_B and userInput == "a":
            count += 1
            print(f"That's right A! Current score is {count}")
            nextLevel.append(randomA)
        elif follower_Count_B > follower_Count_A and userInput == "b":
            count += 1
            print(f"That's right B! Current score is {count}")
            nextLevel.append(randomB)
        else: 
            print(f"Wrong, your score is {count}")
            isRight = False
    elif count > 0:
        randomA = nextLevel[-1]
        randomB = random.choice(gameData)
        if randomA == randomB:
            randomB = random.choice(gameData)        
        print(topLogo)
        print(f"Compare A: {format(randomA)}")
        print(bottomLogo)
        print(f"Against B: {format(randomB)}")
        userInput = input("Who has more followers? Type 'A' or 'B': ").lower()
        if follower_Count_A > follower_Count_B and userInput == "a":
            count += 1
            print(f"That's right! Current score is {count}")
            nextLevel.append(randomA)
        elif follower_Count_B > follower_Count_A and userInput == "b":
            count += 1
            print(f"That's right! Current score is {count}")
            nextLevel.append(randomB)
        else: 
            print(f"Wrong, your score is {count}")
            isRight = False

