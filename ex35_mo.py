from sys import exit

def gold_room():  ##the last room 
    print "This room is full of gold. How much do you take?"

    choice = raw_input(">")
    if choice.isdigit():  ## it's improved: judge the choice is a number or not. 
        how_much = int(choice)  ## make the string from raw_input function become an integer. the argument must be a number, not words.
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
	    dead("You gready bastard!")  


def bear_room(): ##the second room 
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:   ###there is a loop that if you can't exit or dead, you have to input something here.
        choice = raw_input(">")

        if choice == "take honey":
            dead ("The bear looks at you then slaps your face off.")  ##a dead way
        elif choice == "taunt bear" and not bear_moved:  ###the first step you can exit and the bear's moved.
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved: ## if you've taunt bear again, you will be dead.
            dead("The bear gets pissed off and chews your leg off.")
        elif choice =="open door" and bear_moved:  ## the second step to go outside. and go to next room: gold room
            gold_room()
        else:  ## if your first input is not "take honey", or "taunt bear", the sentence will repeat. The second input should be "take honey","taunt bear" and "open door"
            print "I got no idea what that means."


def cthulhu_room(): ##the third room
    print "Here you see the great evil Cthulhu"
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input(">")

    if "flee" in choice:  ## if you flee, you have to go back the first room: start room.
        start()
    elif "head" in choice: ## a dead way
        dead("Well that was tasty!")
    else:  ## if you enter words are not "flee" or "head", you have to in the room to input sth again and again.
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():  ##the first room 
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input(">")

    if choice == "left":
        bear_room()
    elif choice =="right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()  ## the start of the game, call start function