#Point counter
points = int(0)

#Putting answers and questions into a list
##Questions
questions = ["1. What are the primary colors?", "2. What are the secondary colors?",
             "3. Which two colors make green?", "4. Which two make purple?",
             "5. About how many colors can the human eye see?",
             "6. What are the color-sensitive cells in the eyes called?",
             "7. Which country was one of the most colorful flags?",
             "Bonus +3 points: 8. What is the rainbow flag color order?"  ]


##answers
answers_q1 = ["A. Red, blue and yellow", "B. Black, white and gary",
               "C. Purple and green", "D. Orange and Yellow"]
answers_q2 = ["A. Black and white", "B. Red, blue and yellow",
              "C. Orange, Purple and Green", "D. Purple and green"]
answers_q3 = ["A. Red and Blue", "B. Black and yellow",
              "C. Red and orange", "D. Yellow and Blue"]
answers_q4 = ["A. Blue and Red", "B. Orange and Purple",
              "C. Blue and Green", "D. Yellow and Green"]
answers_q5 = ["A. 10", "B. 1,000", "C. 7,000,000", "D. ????"]
answers_q6 = ["A. Rods", "B. Cones", "C. Iris","D. Pupil"]
answers_q7 = ["A. Zimbabwe", "B. China", "C. Germeny", "D. Seychelles"]
answers_q8 = ["A. Orange, purple, green, yellow, blue and indigo",
              "B. Red, orange, yellow, green, blue, indigo, violet",
              "C. Yellow, green, blue, orange, black and purple",
              "D. White, blue, green, red, yellow, blue and purple"]

#Introducting the Game           
print("\nWelcome to the colors triva game!")

start = str(input("Would you like to play?: ").lower())

if start == "yes" or "y":
    print("Thanks for playing!")
else:
    print("it's fine take your time. Rerun the Module when you're ready.")


name = input("What's you're name?: ")
print("Thanks" , name ,". Lets get started!\n" )


#Calling items from list and adding up points!
print(questions[0])
print()

###Question 1
      
for x in answers_q1:
    print(x)
print()


q1= input("Answer: ").lower()

if q1 == "a":
    points += 1
    print("\nCorrect!" +"Next question")
    print("Points: " , points)
else:
    print("Sorry! Better luck next time ", name, "!")
    points -= 1
    print("Points: " , points)

####Questions 2
print()
print(questions[1])
print()

for x in answers_q2:
    print(x)
print()


q2= input("Answer: ").lower()
if q1 == "c":
    print("Nice ", name ," Next one")
    points += 1
    print("Points: " , points)
else:
    print("Oh no!")
    points -= 1
    print("Points: " , points)

###Questions 3

print()
print(questions[2])
print()

for x in answers_q3:
    print(x)
print()


q3= input("Answer: ").lower()
if q3 == "d":
    print("Nice! " + "Next one")
    points += 1
    print("Points: " , points)
else:
    print("Oh no", name, ". Its okay.")
    points -= 1
    print("Points: " , points)

###Questions 4

print()
print(questions[3])
print()

for x in answers_q4:
    print(x)
print()


q4= input("Answer: ").lower()
if q4 == "a":
    print(name, " you got it!")
    points += 1
    print("Points: " , points)
else:
    print("Oh no!")
    points -= 1
    print("Points: " , points)

        
###Questions 5

print()
print(questions[4])
print()

for x in answers_q5:
    print(x)
print()


q5= input("Answer: ").lower()
if q5 == "c":
    print("Nice! " + "Next one")
    points += 1
    print("Points: " , points)
elif q5 == "d":
    print("I like your honesty", name)
    points += 1
    print("Points: " , points)
else:
    print("Awww :( ")
    points -= 1
    print("Points: " , points)

###Questions 6

print()
print(questions[5])
print()

for x in answers_q6:
    print(x)
print()


q6= input("Answer: ").lower()
if q6 == "b":
    print("Great!")
    points += 1
    print("Points: " , points)
else:
    print("Oh no ", name)
    points -= 1
    print("Points: " , points)
    



###Questions 7

print()
print(questions[6])
print()

for x in answers_q7:
    print(x)
print()


q7= input("Answer: ").lower()
if q7 == "a" or "d":
    print("Cool ", name, "!" )
    points += 1
    print("Points: " , points)
else:
    print("Yikes!")
    points -= 1
    print("Points: " , points)
    

###Questions 8

print()
print(questions[7])
print()

for x in answers_q8:
    print(x)
print()


q8= input("Answer: ").lower()
if q8 == "a":
    print("Whoa", name, "!!!!!")
    points += 3
    print("Points: " , points)
else:
    print("It's okay! No points are removed for this one")
    points -= 0
    print()

##End game
print("You finished the game with: ")
print(points, "points")   
    
              
    


