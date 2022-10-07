# Display the title of the story as 'Kings and Dragons of UMBC'
print("~ Kings and Dragons of UMBC ~")
print("    (A Developer's Tale)")
print()
# Display details to the user about what the story 'Kings and Dragons' is about
print("You are a knight in the year 650 CE, and you're trying to become")
print("the most famous knight of them all.")
print()
print("You decide to go on your quest at Castle UMBC to slay the dragon and")
print("marry the princess to earn your glory!")
print()
# Tell the user they have 3 different people as options they can talk to outside the castle grounds
print("You are outside the castle grounds, and see three people asking for help.")
print("The 3 you can talk to are:")
# Display a list of people called 'blacksmith, magician, and princess Nadia' that the user can talk to using options 'a, b, or c'
print("  A. The local blacksmith, who needs a rare sword")
print("  B. The magician, who has a question")
print("  C. Princess Nadia, who's looking for a brave warrior")
# Ask the user to pick one of the 3 options and store in a variable called 'strangers'
strangers = input("Who will you talk to? Please select A through C: ")
print()
# If the user picks answer 'A', tell the user details about the Blacksmith story
if(strangers == "a"):
  print("You meet with the town's blacksmith looking for a legendary sword.")
  print("He tells you that the legend is that the sword is buried and hidden")
  print("somewhere underground in UMBC's Kingdom waiting to be found.")
  # Display a message telling the user they choose to search for the sword
  print("You choose to search for it:")
  # Display a list of areas called 'The Cave', 'The Dungeon', and 'The Atlantic Ocean' labeded a, b, and c
  print("  A. In the Dungeon")
  print("  B. In the Cave")
  print("  C. In the Atlantic Ocean")
  # Ask the user to pick one of the 3 options and store in a variable called 'hiddenSword'
  hiddenSword = input("Please select option A through C: ")
  print()
  # If the user picks 'A', display a message detailing the users victory
  if(hiddenSword == "b"):
    print("After looking long and hard through the cave, you've found it.")
    print("The Developers Sword! The blacksmith is thrilled and rewards you")
    print("with a suit of armor worthy of a hero!")

  
# If the user picks answer 'B', tell the user details about the Magician story
elif(strangers == "b"):
  print("You met with a wandering magician, who is asking you a question.")
  print("'I have be honest with you,' the magician says. 'I'm not really that good at magic.  I will give all my magic powers if you can answer this question.")
  print("They gesture to a math problem that reads as follows:")
  print()
  print("R = (2 * 6) + 4")
  print()
  # Calculate the math problem and store the correct answer as a variable called 'mathProblem'
  mathProblem = ((2 * 6) + 4)
  # Tell the user to enter a solution to the math problem and store as a variable called 'mathSolution'
  mathSolution = input("Please enter a solution to the math problem: ")
  # Convert the math solution into an integer
  mathSolution = int(mathSolution)
  
# If the user picks answer 'C', tell the user details about princess Nadia
elif(strangers == "c"):
  print("You bump into princess Nadia.  She tells you that she's looking for a")
  print("brave warrior that can slay the evil dragon and prove his worth to be")
  print("her husband.")
  print()
  print("You head east and find the dragon. You ready yourself for battle.")
  print("But in a twist, the dragon ask you to solve a riddle in exchange for")
  print("the right to marry the princess and be the future King of UMBC.")
  print()
  print("'How many letters are in princess Nadia's name?'")
  print()
  print("You ponder for a moment. Attempting to spell princess Nadia's name")
  print("in your head and count the letters.")
  print("After pondering for a moment you give the dragon an answer. . .")
  print()
  # Ask the user to enter a number and store as a variable called 'namelength'
  namelength = input("Enter the number of letters: ")
  #Convert namelength into an integer
  namelength = int(namelength)
  
# 

