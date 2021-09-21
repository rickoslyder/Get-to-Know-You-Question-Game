# create a Get To Know You game
# 2+ players
# each person either chooses a number between 1-305, or has a question chosen for them (question bank reshuffles before each game)

# mobile app
# similar to picolo

# flow:

# user opens app - welcome menu with START NOW at top & an Add Player dialog (two text fields, a + button and list of added players)
# remember previous player names
# (eventually add themes / intensity levels / ask if you're playing with family/friend/lover / ???time limit???)

# ???solo or duo - solo = each person gets asked a new question, duo = both players take turn answering the same question - UI wise same thing anyway???

# start game with chosen theme etc
# question bank is reshuffled to ensure no overlap in question number across games - only pull a certain portion of bank to introduce more randomness?
# "PLAYER's turn - pick a number between 1 and 305, or let me choose for you?"

# question is displayed on screen - implement TTS (speaker icon)
# "NEXT TURN" button underneath, share button

# Keep going until XX questions threshold / time limit

# You asked each other: "XX" questions - play again, new theme?

# A List of Interesting Questions for People to Get to Know Their Friends, Family, Lovers, Coworkers, Nemeses, and Selves Better

import random, time

print("Welcome to the Question Game!")
time.sleep(2)

with open("Stripped.txt", "r") as file:
    questions = file.readlines()
    shuffled = random.sample(questions, len(questions))


def gather_player_names():
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    return [player1, player2]


asked_questions = []


def ask_question():
    userChoice = input("Type in either A or B: ")
    if userChoice.lower() == "a":
        questionChoice = int(input("What number? "))
        question = shuffled[questionChoice - 1]
        print(f"\n{question}")
        asked_questions.append(question)
        input("Press Enter when you've answered the question!")
        shuffled.remove(question)
    elif userChoice.lower() == "b":
        questionChoice = random.randint(0, len(shuffled))
        question = shuffled[questionChoice - 1]
        print(f"\n{question}")
        asked_questions.append(question)
        input("Press Enter when you've answered the question!")
        shuffled.remove(question)
    elif userChoice.lower() == "asked":
        print("*" * 80)
        print("Here is a list of all questions so far:\n")
        for i in asked_questions:
            print(f"    {asked_questions.index(i) + 1}. {i}")
        export = input("\nWould you like to export these to a file? (Y/N)\n")
        if export.lower() == "yes" or "y":
            filename = input(
                "Choose your filename - Note: file will be saved as a .txt\n"
            )
            for i in asked_questions:
                with open(f"{filename}.txt", "a") as file:
                    file.write(f"{asked_questions.index(i) + 1}. {i}")
        else:
            pass
    else:
        check = input("Do you want to quit? : ")
        if check.lower() == "yes" or "y":
            print(
                f"OK, thanks for playing! Just so you know - you answered {len(asked_questions)} questions altogether"
            )
            exit()
        else:
            ask_question()


def start_game():
    gameIsOn = True
    turn_counter = 0
    while gameIsOn:
        if turn_counter % 2 != 0:
            print("-" * 80)
            print(
                f"{players[0]}'s turn! Do you want to pick a number (A), or let me choose a question for you? (B)\n"
            )
            ask_question()
            turn_counter += 1
        else:
            print("-" * 80)
            print(
                f"{players[1]}'s turn! Do you want to pick a number (A), or let me choose a question for you? (B)\n"
            )
            ask_question()
            turn_counter += 1


def user_prompt():
    print("Are you ready to play? (Y/N)\n")
    choice = input()
    if choice == "Y" or "y":
        start_game()
    elif choice == "N" or "n":
        gather_player_names()
        user_prompt()
    else:
        print("Incorrect value - your answer must be either Y or N")
        user_prompt()


players = gather_player_names()
user_prompt()
