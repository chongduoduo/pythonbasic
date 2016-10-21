def resetgame(myblood, monsterblood, meatroomfull, ham, bone, dogfull):  ##reset the origin values
    print "Please choose the game mode: easy, or hard? "
    
    mode = raw_input('>')
 
    if mode == "easy":
        myblood = 10
        monsterblood = 5
    elif mode == "hard":
        myblood = 5
        monsterblood = 12
    elif mode == "exit":
        exit(0)
    else:
        print "Wrong mode."
        myblood, monsterblood, meatroomfull, ham, bone, dogfull = resetgame(myblood, monsterblood, meatroomfull, ham, bone, dogfull)

    meatroomfull = True
    ham = False
    bone = False
    dogfull = False
    
    return myblood, monsterblood, meatroomfull, ham, bone, dogfull

def dead(s):  ##dead step
    print s
    exit(0)

def printhand(ham, bone):  ###print the status of player
    if ham == False and bone == False:
        print "You have nothing on your hand."
    elif ham == False and bone == True:
        print "You have a bone, as your weapon, on your hand."
    else:
        print "You have a good ham on your hand."

def startplace(myblood, monsterblood, meatroomfull, ham, bone, dogfull):  ## what should do when entering the first place.
    print "-------------------------------------------------------------------"
    print "Your blood is %d." % myblood
    printhand(ham, bone)
    print "-------------------------------------------------------------------"
    print "Enter 'Dog Room', press '1'"
    print "Enter 'Meat Room', press '2'"
    print "Enter 'Monster Room', press '3'"

    Roomchoice = raw_input('>')
    
    if Roomchoice == "1":
        myblood, monsterblood, meatroomfull, ham, bone, dogfull = dog_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
    elif Roomchoice == "2":
        myblood, monsterblood, meatroomfull, ham, bone, dogfull = meat_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
    elif Roomchoice == "3":
        myblood, monsterblood, meatroomfull, ham, bone, dogfull = monster_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
    else:
        print "Wrong input."
        startplace(myblood, monsterblood, meatroomfull, ham, bone, dogfull)

def dog_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull):  ### what should do in dog room
    if dogfull == True:
        print "There is just a lovely big dog wagging his tail. Go back to the start place."
        startplace(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
    else:
        print "In the room there is a big, black dog! And It's staring at you with drooling!"
        print "And no other doors in the room."
        print "What would you do?"
        print "-------------------------------------------------------------------"
        myblood, monsterblood, meatroomfull, ham, bone, dogfull = handledog(myblood, monsterblood, meatroomfull, ham, bone, dogfull)

    return myblood, monsterblood, meatroomfull, ham, bone, dogfull

def handledog(myblood, monsterblood, meatroomfull, ham, bone, dogfull): ###what should do when meet the dog
    if ham == False:
        print "'Flee from the room', press '1'."
        print "'Hit the dog', press '2'."
        
        dog_choice = raw_input('>')
        
        if dog_choice == "1":
            startplace(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
        elif dog_choice == "2":
            dead("The dog is too strong, you are dead.")	
        else:
            print "Wrong input."
            dog_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
    else:
        printhand(ham, bone)
        print "'Flee from the room', press '1'."
        print "'Hit the dog', press '2'."
        print "'Feed the dog', press'3'."
    
        dog_choice = raw_input('>')

        if dog_choice == "1":
            startplace(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
        elif dog_choice == "2":
            dead("The dog is too strong, you are dead.")
        elif dog_choice == "3":
            dogfull, ham, bone = feeddog()
            print "The dog becomes friendly. Go back to the start place."
            startplace(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
        else:
            print "Wrong input." 
            dog_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull)

    return myblood, monsterblood, meatroomfull, ham, bone, dogfull

def feeddog():  ## feed the dog
    dogfull = True
    ham = False
    bone = True

    return dogfull, ham, bone

def meat_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull): ###what should do in a meat room
    if meatroomfull == True:
        myblood, monsterblood, meatroomfull, ham, bone, dogfull = takeham(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
    else:
        print "The room is empty. Go back to the start place."
        print "-------------------------------------------------------------------"
        myblood, monsterblood, meatroomfull, ham, bone, dogfull = startplace(myblood, monsterblood, meatroomfull, ham, bone, dogfull)

    return myblood, monsterblood, meatroomfull, ham, bone, dogfull

def takeham(myblood, monsterblood, meatroomfull, ham, bone, dogfull):  ## what should do when seeing a ham
    print "There is a delicious ham in this room. But no more doors."
    print "Do you want to take it? Y/N"

    hamtake = raw_input(">")
    
    if hamtake == "Y" or hamtake == "y":
        ham = True
        meatroomfull = False
    elif hamtake == "N" or hamtake == "n":
        ham = False
        meatroomfull = True
    else:
        Print ("Wrong input.")
        myblood, monsterblood, meatroomfull, ham, bone, dogfull = meat_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
    
    if ham == True:
        myblood, monsterblood, meatroomfull, ham, bone, dogfull = eatham(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
    else:
        print "Ok. Go back to the start place."
        startplace(myblood, monsterblood, meatroomfull, ham, bone, dogfull)

    return myblood, monsterblood, meatroomfull, ham, bone, dogfull

def eatham(myblood, monsterblood, meatroomfull, ham, bone, dogfull):     ### if eat the ham or not
    print "Now you have a ham. Do you want to eat it? Y/N"
    
    hameat = raw_input(">")

    if hameat == "Y" or hameat == "y":
        myblood += 2
        ham = False
        bone = False
        print "Ops! The bone of the ham has been broken. You have nothing on your hand. "
        myblood, monsterblood, meatroomfull, ham, bone, dogfull = meat_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
    elif hameat == "N" or hameat == "n":
        print "Ok. The room is empty. Go back to the start place."
        startplace(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
    else:
        print "Wrong input"
        myblood, monsterblood, meatroomfull, ham, bone, dogfull = eatham(myblood, monsterblood, meatroomfull, ham, bone, dogfull)

    return myblood, monsterblood, meatroomfull, ham, bone, dogfull

def monster_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull):  ## what should do when entering the monster room
    print "A scary monster in this room!! He is staring at you !!"
    print "But there is a door behind him. You are sure that it is a exit. What do you want to do?"
    print "-------------------------------------------------------------------"
    printhand(ham, bone)
    print "You have %d blood." %myblood
    print "The monster has %d blood" %monsterblood
    print "-------------------------------------------------------------------"
	
    if ham == True:
        print "'Flee from the room', press '1'."
        print "'Feed the monster_room', press '2'. "
        print "'Eat the ham by yourself', press '3'."
        print "'Fight with the monster', press '4'."

        domoster = raw_input('>')

        if domoster == "1":
            dead( "The monster catches you and eat you. You are dead.")
        elif domoster == "2":
            monsterblood += 2
            ham = False
            print "The monster becomes stronger! His blood has %d." % monsterblood
            myblood, monsterblood, meatroomfull, ham, bone, dogfull = monster_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
        elif domoster == "3":
            myblood +=2
            ham = False
            print "Ops! The bone of the ham has been broken. You have nothing on your hand."
            myblood, monsterblood, meatroomfull, ham, bone, dogfull = monster_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
        elif domoster == "4":
            myblood, monsterblood, meatroomfull, ham, bone, dogfull = fight(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
        else:
            print "Wrong input."
            myblood, monsterblood, meatroomfull, ham, bone, dogfull = monster_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull)

    elif ham == False and bone == False:
        print "'Flee from the room', press '1'."
        print "'Fight with the monster', press '2'."

        domoster = raw_input(">")

        if domoster == "1":
            dead( "The monster catches you and eats you. You are dead.")
        elif domoster == "2":
            myblood, monsterblood, meatroomfull, ham, bone, dogfull = fight(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
        else:
            print "Wrong input."
            myblood, monsterblood, meatroomfull, ham, bone, dogfull = monster_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull)

    else:
        print "'Flee from the room', press '1'."
        print "'Fight with the monster', press '2'."

        domoster = raw_input(">")

        if domoster == "1":
            dead( "The monster catches you and eat you. You are dead.")
        elif domoster == "2":
            myblood, monsterblood, meatroomfull, ham, bone, dogfull = fight(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
            myblood, monsterblood, meatroomfull, ham, bone, dogfull = monster_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
        else:
            print "Wrong input."
            myblood, monsterblood, meatroomfull, ham, bone, dogfull = monster_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull)

    return myblood, monsterblood, meatroomfull, ham, bone, dogfull

def fight(myblood, monsterblood, meatroomfull, ham, bone, dogfull):  ##fight with the monster
    if bone == True:
        myblood -= 1
        monsterblood -= 3
    else:
        myblood -= 1
        monsterblood -= 1

    if myblood <= 0:
        print "Your blood: %d." % myblood
        print "Monster's blood: %d." % monsterblood
        dead("You have no blood. You are dead.")
    elif myblood > 0 and monsterblood <= 0:
        print "Your blood: %d." % myblood
        print "Monster's blood: %d." % monsterblood
        print "Congratulations! You defeat the monster and escape successfully!"
        exit(0) 
    else:
        myblood, monsterblood, meatroomfull, ham, bone, dogfull = monster_room(myblood, monsterblood, meatroomfull, ham, bone, dogfull)

    return myblood, monsterblood, meatroomfull, ham, bone, dogfull

#######the start of the game#######
print "You've been transferred into a weird place."  
print "There are only 3 doors in the room. You have to get away from here!"

#####global variables#####
meatroomfull = True
ham = False
bone = False
dogfull = False
myblood = 0
monsterblood = 0
##########################

myblood, monsterblood, meatroomfull, ham, bone, dogfull = resetgame(myblood, monsterblood, meatroomfull, ham, bone, dogfull)

startplace(myblood, monsterblood, meatroomfull, ham, bone, dogfull)
