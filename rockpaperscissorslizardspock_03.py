#8bitpro workshop#

import random,time

userScore = 0
compScore = 0

choices = ["r","p","s","l","k"]

rnd = 1

while True: #Infinite Loop
    print("Round: ", rnd)
    userChoice = input("What do you pick: (r)ock, (p)aper, (s)cissors, (l)izard or spoc(k)?")
    compChoice = random.choice(choices)
    print("Computer chose: ", compChoice)

    if len(userChoice) == 0:
        print("Invalid answer. Try again")
        time.sleep(1)
        continue

    if userChoice[0].lower() == compChoice:
        print("Draw!")
        time.sleep(1)
        continue

    elif userChoice[0].lower() == "s" and compChoice == "p":
        print("Scissors cuts Paper - User wins this round")
        time.sleep(1)
        userScore = userScore + 1
    elif userChoice[0].lower() == "p" and compChoice == "s":
        print("Scissors cuts Paper - Computer wins this round")
        time.sleep(1)
        userScore = compScore + 1
    elif userChoice[0].lower() == "p" and compChoice == "r":
        print("Paper wraps Rock - User wins this round")
        time.sleep(1)
        userScore = userScore + 1
    elif userChoice[0].lower() == "r" and compChoice == "p":
        print("Paper wraps Rock - Computer wins this round")
        time.sleep(1)
        userScore = compScore + 1
    elif userChoice[0].lower() == "r" and compChoice == "l":
        print("Rock crushes Lizard - User wins this round!")
        time.sleep(1)
        userScore = userScore + 1
    elif userChoice[0].lower() == "l" and compChoice == "r":
        print("Rock crushes Lizard - Computer wins this round!")
        time.sleep(1)
        userScore = compScore + 1
    elif userChoice[0].lower() == "l" and compChoice == "k":
        print("Lizard poisons Spock - User wins this round!")
        time.sleep(1)
        userScore = userScore + 1
    elif userChoice[0].lower() == "k" and compChoice == "l":
        print("Lizard poisons Spock - Computer wins this round!")
        time.sleep(1)
        userScore = compScore + 1
    elif userChoice[0].lower() == "k" and compChoice == "s":
        print("Spock smashes Scissors - User wins this round!")
        time.sleep(1)
        userScore = userScore + 1
    elif userChoice[0].lower() == "s" and compChoice == "k":
        print("Spock smashes Scissors - Computer wins this round!")
        time.sleep(1)
        userScore = compScore + 1
    elif userChoice[0].lower() == "s" and compChoice == "l":
        print("Scissors decapitates Lizard - User wins this round!")
        time.sleep(1)
        userScore = userScore + 1
    elif userChoice[0].lower() == "l" and compChoice == "s":
        print("Scissors decapitates Lizard - Computer wins this round!")
        time.sleep(1)
        userScore = compScore + 1
    elif userChoice[0].lower() == "l" and compChoice == "p":
        print("Lizard eats Paper - User wins this round!")
        time.sleep(1)
        userScore = userScore + 1
    elif userChoice[0].lower() == "p" and compChoice == "l":
        print("Lizard eats Paper - Computer wins this round!")
        time.sleep(1)
        userScore = compScore + 1
    elif userChoice[0].lower() == "p" and compChoice == "k":
        print("Paper disproves Spock - User wins this round!")
        time.sleep(1)
        userScore = userScore + 1
    elif userChoice[0].lower() == "k" and compChoice == "p":
        print("Paper disproves Spock - Computer wins this round!")
        time.sleep(1)
        userScore = compScore + 1
    elif userChoice[0].lower() == "k" and compChoice == "r":
        print("Spock vapourises Rock - User wins this round!")
        time.sleep(1)
        userScore = userScore + 1
    elif userChoice[0].lower() == "r" and compChoice == "k":
        print("Spock vapourises Rock - Computer wins this round!")
        time.sleep(1)
        userScore = compScore + 1
    elif userChoice[0].lower() == "r" and compChoice == "s":
        print("Rock crushes Scissors - User wins this round!")
        time.sleep(1)
        userScore = userScore + 1
    elif userChoice[0].lower() == "s" and compChoice == "r":
        print("Rock crushes Scissors - computer wins this round!")
        time.sleep(1)
        userScore = compScore + 1
    else:
        print("Invalid answer. Try again!")
        continue

    rnd = rnd + 1
    if rnd == 6:
        break

print("User Wins: ", userScore)
print("Comp Wins: ", compScore)

if userScore > compScore:
    print("The user wins the game!")
elif compScore > userScore:
    print("The computer wins the game!")
else:
    print("Draw!")
