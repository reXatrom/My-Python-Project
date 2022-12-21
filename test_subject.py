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

    #print("Welcome to my quiz game!")
    #print()

    #-----------------------------
    #playing = input("Do you want to play? ")

    #if playing.lower() != "yes":
        #quit()

    #print("Okay! Let's play :)")
    #print("---------------------------------")
    #game_mode = input("Pick the game mode you want? [easy_mode/normal_mode/hard_mode]: ")#.upper()

    #------------------------- EASY-MODE -------------------------

    #if game_mode == "easy_mode":
        #print("That's good.\n")
    #game_mode()
        new_game()
