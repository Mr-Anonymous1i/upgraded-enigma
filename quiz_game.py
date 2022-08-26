#Quiz Game
#21/8/2022
#User gets points if they correctly answer computer promts/questions.

score = 0
print("Welcome to my computer quiz!")
playing = input("""Do you want to play?
""")

if playing.lower() != "yes":
    quit()

print("""Good choice, let's play!
""")

#The questions and answers
answer_one = input("""What does RAM stand for?
""")

if answer_one.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Unfortunatly you're wrong")

answer_two = input("""Who is the founder of Microsoft?
""")
if answer_two.lower() == "bill gates":
    print("Correct!")
    score += 1
else:
    print("Unfortunatly you're wrong")

answer_three = input("""What does GPU stand for?
""")
if answer_three.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Unfortunatly you're wrong")

answer_four = input("""What does CPU stand for?
""")
if answer_four.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Unfortunatly you're wrong")

answer_five = input("""What does PSU stand for?
""")
if answer_five.lower() == "power suply unit":
    print("Correct!")
    score += 1
else:
    print("Unfortunatly you're wrong")

if score >= 3:
    print("Congrats, you got " + str(int(score/5*100)) + "% and you have passed!")
else:
    print("Unfortunatly, you got " + str(int(score/5*100)) + "% and you have failed :(")