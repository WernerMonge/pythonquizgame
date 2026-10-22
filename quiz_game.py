print("Welcome to the quiz game! For each correct answer, you earn a point. Good luck!")

while True:
    play = input("Do you want to play? (yes/no): ").strip().lower()
    if play in ["yes", "no"]:
        break
    else:
        print("Please enter 'yes' or 'no'.")

if play == "yes":
    print("Excellent! Let's begin.")
    points = 0

#---------------------------------------Question 1------------------------------------------#
    while True:
        answer = input("Question: What is the capital of France? A) Paris B) London C) Berlin D) Rome: ").strip().lower()
        if answer in ["a", "b", "c", "d"]:
            break
        else:
            print("Please enter A, B, C, or D.")

    if answer == "a":
        points += 1
        print("Correct! You earned 1 point." + f" Total points: {points}")
    else:
        print("Incorrect. The correct answer is A) Paris." + f" Total points: {points}")

#---------------------------------------Question 2------------------------------------------#
    while True:
        answer = input("Question: In what year did Christopher Columbus arrive in America? A)1496  B) 1519 C) 1492 D) 1620: ").strip().lower()
        if answer in ["a", "b", "c", "d"]:
            break
        else:
            print("Please enter A, B, C, or D.")

    if answer == "c":
        points += 1
        print("Correct! You earned 1 point." + f" Total points: {points}")
    else:
        print("Incorrect. The correct answer is C) 1492." + f" Total points: {points}")


#-------------------------------Question 3--------------------------------------------------#
    while True:
        answer = input("Question: In what year did the first human travel into space? A) 1962 B) 1961 C) 1963 D) 1964: ").strip().lower()
        if answer in ["a", "b", "c", "d"]:
            break
        else:
            print("Please enter A, B, C, or D.")

    if answer == "b":
        points += 1
        print("Correct! You earned 1 point." + f" Total points: {points}")
    else:
        print("Incorrect. The correct answer is B) 1961." + f" Total points: {points}")


#----------------------------------Question 4-----------------------------------------------#
    while True:
        answer = input("Question: Which king sent the Spanish Armada against England and lost? A) Charles IX B) Philip III C) Charles I D) Philip II: ").strip().lower()
        if answer in ["a", "b", "c", "d"]:
            break
        else:
            print("Please enter A, B, C, or D.")

    if answer == "d":
        points += 1
        print("Correct! You earned 1 point." + f" Total points: {points}")
    else:
        print("Incorrect. The correct answer is D) Philip II." + f" Total points: {points}")

#---------------------------------------Question 5------------------------------------------#
    while True:
        answer = input("Question: In which city did Romeo and Juliet live? A) Verona B) Bologna C) Florence D) Rome: ").strip().lower()
        if answer in ["a", "b", "c", "d"]:
            break
        else:
            print("Please enter A, B, C, or D.")

    if answer == "a":
        points += 1
        print("Correct! You earned 1 point." + f" Total points: {points}")
    else:
        print("Incorrect. The correct answer is A) Verona." + f" Total points: {points}")


    print(f"Game over! You scored a total of {points} points.")
#---------------------------------------------------------------------------------#
else:
    print("Too bad you do not want to play. Bye, bye.")
    quit()
