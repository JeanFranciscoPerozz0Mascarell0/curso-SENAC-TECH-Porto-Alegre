import random

computer = random.randint(1,5)
choice = 1

computer_points = 0
person_points = 0
print('-' * 50)
print("Welcome to the GAME: ROCK, PAPPER, SCISSORS, LIZARD, SPOCK")
print("\nIf you wanna:\n\n1) for ROCK\n2) for PAPPER \n3) for SCISSORS\n4) for LIZARD\n5) for SPOCK\n")
print('-' * 50)

while(choice == 1):
    person = int(input("Set a number for your choice: "))

    rock = 1
    papper = 2
    scissors = 3
    lizard = 4
    spock = 5

    #person wons:
    case1 = person == rock and computer == scissors
    case2 = person == rock and computer == lizard
    case3 = person == papper and computer == spock
    case4 = person == papper and computer == rock
    case5 = person == scissors and computer == papper
    case6 = person == scissors and computer == lizard
    case7 = person == lizard and computer == papper
    case8 = person == lizard and computer == spock
    case9 = person == spock and computer == scissors
    case10 = person == spock and computer == rock

    #computer wons:
    case11 = person == rock and computer == papper
    case12 = person == rock and computer == spock
    case13 = person == papper and computer == scissors
    case14 = person == papper and computer == lizard
    case15 = person == scissors and computer == spock
    case16 = person == scissors and computer == rock
    case17 = person == spock and computer == papper
    case18 = person == spock and computer == lizard
    case19 = person == lizard and computer == rock
    case20 = person == lizard and computer == scissors

    # if the person won
    if(case1 or case2  or case3 or case4 or case5 or case6 or case7 or case8 or case9 or case10):
        winner = person
        loser = computer

        person_points += 1
        
        if(winner == 1):
            answer_winner = "ROCK"
        elif(winner == 2):
            answer_winner = "PAPPER"
        elif(winner == 3):
            answer_winner = "SCISSORS"
        elif(winner == 4):
            answer_winner = "LIZARD"
        elif(winner == 5):
            answer_winner = "SPOCK"

        if(loser == 1):
            answer_loser = "ROCK"
        elif(loser == 2):
            answer_loser = "PAPPER"
        elif(loser == 3):
            answer_loser = "SCISSORS"
        elif(loser == 4):
            answer_loser = "LIZARD"
        elif(loser == 5):
            answer_loser = "SPOCK"

        print('-'*30)
        print("Your choice was:", answer_winner)
        print("And the computer chose:", answer_loser)
        print('-'*30)
        print("Congratulations, you won!")
        print('-'*30)
        print('-'*30)
        print(f"Score:\nYOU: {person_points} points.\nCOMPUTER: {computer_points} points.")
        print('-'*30)

    # if the computer won
    elif(case11 or case12 or case13 or case14 or case15 or case16 or case17 or case18 or case19 or case20):  
        winner = computer
        loser = person
        person_points += 1
        
        if(winner == 1):
            answer_winner = "ROCK."
        elif(winner == 2):
            answer_winner = "PAPPER."
        elif(winner == 3):
            answer_winner = "SCISSORS."
        elif(winner == 4):
            answer_winner = "LIZARD"
        elif(winner == 5):
            answer_winner = "SPOCK"

        if(loser == 1):
            answer_loser = "ROCK."
        elif(loser == 2):
            answer_loser = "PAPPER."
        elif(loser == 3):
            answer_loser = "SCISSORS."
        elif(loser == 4):
            answer_loser = "LIZARD"
        elif(loser == 5):
            answer_loser = "SPOCK"

        
        print('-'*30)
        print("Your choice was:", answer_loser)
        print("And the computer chose:", answer_winner)
        print('-'*30)
        print("Sorry, you lost! Computer won.")
        print('-'*30)
        print('-'*30)
        print(f"Score:\nYOU: {person_points} points.\nCOMPUTER: {computer_points} points.")
        print('-'*30)

    # if wasnt winner
    else:
        winner = person
        loser = computer
        
        if(winner == 1):
            answer_winner = "ROCK."
        elif(winner == 2):
            answer_winner = "PAPPER."
        elif(winner == 3):
            answer_winner = "SCISSORS."
        elif(winner == 4):
            answer_winner = "LIZARD"
        elif(winner == 5):
            answer_winner = "SPOCK"

        if(loser == 1):
            answer_loser = "ROCK"
        elif(loser == 2):
            answer_loser = "PAPPER"
        elif(loser == 3):
            answer_loser = "SCISSORS."
        elif(loser == 4):
            answer_loser = "LIZARD"
        elif(loser == 5):
            answer_loser = "SPOCK"

        
        print('-'*30)
        print("Your choice was:", answer_winner)
        print("And the computer chose:", answer_loser)
        print('-'*30)
        print('-'*30)
        print("There wasn\'t winners!")
        print('-'*30)

    choice = int(input("\n1 = YES 2 = NO \nDo You wanna play more? "))
print('-'*30)
print("END GAME.") 
print('-'*30)
