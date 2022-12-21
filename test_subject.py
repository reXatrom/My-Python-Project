print()
print("---------------------------------------------------")
print("Welcome to my RIDDLE QUIZ GAME!")
print()
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
print("---------------------------------")

#def game_mode():
mode = input("Pick the game mode you want? [easy_mode/normal_mode/hard_mode]: ")
if mode == "easy_mode":
        print("That's good.\n")

#elif mode == "normal_mode":
        #print("Not bad.\n")

#elif mode == "hard_mode":
        #print("That more like it.\n")
#---------------------
        def new_game():

            guesses = []
            correct_guesses = 0
            question_num = 1

            for key in easy_mode:
                print("---------------------")
                print(key)
                for i in easy_mode_options[question_num - 1]:
                    print(i)
                guess = input("Enter (A, B, C or D): ").upper()
                guesses.append(guess)

                correct_guesses += check_answer(easy_mode.get(key),guess)
                question_num += 1

            display_score(correct_guesses, guesses)

                #---------------------
        def check_answer(answer, guess):

            if answer == guess:
                print("CORRECT!")
                return 1
            else:
                print("INCORRECT!")
                return 0
            #---------------------
        def display_score(correct_guesses, guesses):
            print("-------------------")
            print("RESULTS")
            print("-------------------")

            print("Answers: ", end=" ")
            for i in easy_mode:
                print(easy_mode.get(i), end=" ")
            print()

            print("Guesses: ", end=" ")
            for i in guesses:
                print(i, end=" ")
            print()

            score = int((correct_guesses / len(easy_mode)) * 100)
            print(f"Your score is: {score}%")

                #---------------------
        def play_again():
                pass

        easy_mode = {
        "1. What as to be broken before you can use it?: ": "Egg A",
        "2. I'm tall when i'm young, and i'm short when am old. What am i?: ": "B",
        "3. What month of the year as 28 days?: ": "C",
        "4. What is full of holes but still hold water?: ": "A",
        "5. What question can you never answer yes to?: ": "D",
        "6. What is always infront of you but can never be seen?: ": "A",
        "7. There is a one-story house in which everything inside is yellow. Yellow walls, yellow doors, yellow furniture. What colour are the stairs?: ": "D",
        "8. What can you break, even if you never pick it or touch it?: ": "C",
        "9. What goes up but never comes down?: ": "A",
        "10. A man was outside in the rain without an umbrella or hat didn't get a single hair on his head wet. Why?: ": "B",
        }

        easy_mode_options = [["A. Egg", "B. Trust", "C. Bricks", "D. Coconut"],
            ["A. Tongue", "B. Candle", "C. Tree", "D. Spoon"],
            ["A. February", "B. September", "C. All months", "D. Feburuary"],
            ["A. Sponge","B. Foam", "C. Towels", "D. Bucket"],
            ["A. There is no question i can't answer yes to", "B. Can you sing?", "C. Do you love you job?", "D. Are you asleep already?"],
            ["A. The future", "B. Los vegas", "C. Ghost", "D. Smell"],
            ["A. Yellow", "B. Mangeta", "C. Colourless", "D. There aren't any--it's a one story house"],
            ["A. A friendship","B. An egg", "C. A promise", "D. A Bucket"],
            ["A. Your age", "B. A tree", "C. A space X rocket", "D. Eagle"],
            ["A. He is under a shade", "B. He was bald", "C. He as super powers", "D. It's impossible"]]

        new_game()

elif mode == "normal_mode":
        print("Keep on challenging yourself.\n")

        def new_game2():

            guesses = []
            correct_guesses = 0
            question_num = 1

            for key in normal_mode:
                print("---------------------")
                print(key)
                for i in normal_mode_options[question_num - 1]:
                    print(i)
                guess = input("Enter (A, B or C): ").upper()
                guesses.append(guess)

                correct_guesses += check_answer(normal_mode.get(key),guess)
                question_num += 1

            display_score(correct_guesses, guesses)

                #---------------------
        def check_answer(answer, guess):

            if answer == guess:
                print("CORRECT!")
                return 1
            else:
                print("INCORRECT!")
                return 0
            #---------------------
        def display_score(correct_guesses, guesses):
            print("-------------------")
            print("RESULTS")
            print("-------------------")

            print("Answers: ", end=" ")
            for i in normal_mode:
                print(normal_mode.get(i), end=" ")
            print()

            print("Guesses: ", end=" ")
            for i in guesses:
                print(i, end=" ")
            print()

            score = int((correct_guesses / len(normal_mode)) * 100)
            print(f"Your score is: {score}%")

        def display_answer():
            print(f"""
        |---------------------------------------------------------------------------------------------|
        |The Correct Answers and Explanations.                                                        |
        |---------------------------------------------------------------------------------------------|
        |1. Three apples.                                                                             |
        |2. The score is always 0-0 before the game.                                                  |
        |3. Two – the inside and the outside.                                                         |
        |4. 9.                                                                                        |
        |5. None, because the barn is already built.                                                  |
        |6. 6,457 because the last number is moved to the front to make the next number in the series.|
        |7. 9.                                                                                        |
        |8. 20 times (8, 18, 28, 38, 48, 58, 68, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 98).     |
        |9. Zero.                                                                                     |
        |10. None, because roosters do not lay eggs.                                                  |
        |---------------------------------------------------------------------------------------------|
        """)
        def play_again():
                pass

        normal_mode = {
	    "1. If there are 4 apples and you take away 3, how many do you have?: ": "B",
	    "2. How did the soccer fan know before the game that the score would be 0-0?: ": "C",
	    "3. How many sides does a circle have?: ": "A",
	    "4. If two’s company and three’s a crowd, what are four and five?: ": "A",
	    "5. If it took 6 people 9 hours to build a barn, how long would it take 12 people to build the same barn?: ": "B",
	    "6. What is the next number in the series? 7,645 5,764 4,576: ": "C",
	    "7. A farmer has 17 sheep and all but 9 die. How many are left?: ": "A",
	    "8. Tom was asked to paint the apartment number on plates for 100 apartments which means he will have to paint numbers 1 through 100. How many times will he paint the number 8?: ": "A",
	    "9. If you multiply this number by any other number, the answer will always be the same. What number is this?: ": "B",
	    "10. If you buy a rooster for the purpose of laying eggs and you expect to get three eggs each day for breakfast, how many eggs will you have after three weeks?: ": "C",
	    }

        normal_mode_options = [["A. 4 apples", "B. 3 appples", "C. 1 apple"],
        ["A. The scure is always 0-0 before the game", "B. They predicted the score", "C. The score is always 0-0 before the game"],
        ["A. Two sides", "B. No sides", "C. One side"],
        ["A. 9", "B. Audience", "C. Family"],
        ["A. 18 hours", "B. None", "C. 4 hours 30min"],
        ["A. 6,547", "B. 6,574", "C. 6,457"],
        ["A. Nine", "B. Eight", "C. None"],
        ["A. 20 times", "B. 10 times", "C. 25 times"],
        ["A. One", "B. Zero", "C. Two"],
        ["A. 63 eggs", "B. 21 eggs", "C. None"]]

        new_game2()
        print()
        display_answer()