print("---------------------------------")
print("Welcome to my quiz game!")
print()

#-----------------------------
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
print()

print("---------------------------------")
game_mode = input("Pick the game mode you want? [easy_mode/normal_mode/hard_mode]: ").upper()

#------------------------- EASY-MODE -------------------------

if game_mode == "easy_mode":
    print("That's good.\n")

    print("---------------------------------")
    answer = input("1. What does CPU stands for? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

#------------------------- NORMAL-MODE -------------------------

elif game_mode == "normal_mode":
    print("This would be exciting.\n")

    print("---------------------------------")
    answer = input("2. What does CPU stands for? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

#------------------------- HARD-MODE ----------------------      

elif game_mode == "hard_mode":
    print("Now that's more like it, challenge yourself to be better.\n")

    print("---------------------------------")
    answer = input("3. What does CPU stands for? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")




easy_mode = {
    "1. What as to be broken before you can use it?: ": "A",
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
          ["A. Sponge","B. Foam", "C. Towels", "D. Bucket"]
          ["A. There is no question i can't answer yes to", "B. Can you sing?", "C. Do you love you job?", "D. Are you asleep already?"],
          ["A. The future", "B. Los vegas", "C. Ghost", "D. Smell"],
          ["A. Yellow", "B. Mangeta", "C. Colourless", "D. There aren't any--it's a one story house"],
          ["A. A friendship","B. An egg", "C. A promise", "D. A Bucket"]
          ["A. Your age", "B. A tree", "C. A space X rocket", "D. Eagle"],
          ["A. He is under a shade", "B. He was bald", "C. He as super powers", "D. It's impossible"]]