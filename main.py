# Python quiz game

questions = ("How many legs does a cat have? ",
             "What is the largest animal on Earth? ",
             "What is the opposite color of white? ",
             "Which planet is the farthest from Sun? ")

options = (("A. 10", "B. 29", "C. 4", "D. 3"), 
           ("A. Cat", "B. Crocodile", "C. Elephant", "D. Whale"),
           ("A. Black", "B. Yellow", "C. Purple", "D. Green"),
           ("A. Earth", "B. Pluto", "C. Jupiter", "D. Mars"))

answers = ("C", "D", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------------------------")
    print(question)
    for option in options [question_num]:
        print(option)

    guess = input ("Enter (A, B, C, D): ").upper() # incase user put in lower case
    guesses.append (guess)
    if guess == answers[question_num]:
        score += 1
        print ("CORRECT!")
    
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("----------------------------------")
print("              RESULT              ")
print("----------------------------------")

score = int(score / len(questions) * 100)
print (f"Your score is: {score}%")
