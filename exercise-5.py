# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."


first_name = input("What is your name?: ").lower()
print(first_name)
their_name = input("What is their name?: ").lower()


for x in first_name:
    t = first_name.count("t")
    r = first_name.count("r")
    u = first_name.count("u")
    e = first_name.count("e")


for x in their_name:
    l = their_name.count("l")
    o = their_name.count("o")
    v = their_name.count("v")
    e = their_name.count("e")


true = t + r + u + e
love = l + o + v + e
score = str(true) + str(love)
score = int(score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif score > 40 and score < 50:
    print(f"Your score is {score} you are alright together.")

else:
    print(f"Your score is {score}")