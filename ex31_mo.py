print "Welcome to the world of blood. You have to answer some questions and the system tell you your blood type. It's interesting, isn't?"
raw_input("Press Enter to start >")

print "Are you ready?"
print "Yes: Press '1'."
print "Not yet: Press '2'."
print "I don't want to play such idiot game: Press '3'."

answer1 = raw_input ('>')

if answer1 == "3":
    print "Aha!You AB boy!"

elif answer1 == "1":
    print "Open your purse, and look at the cash you have. Are they neatly placed?"
    print "Yes: Press '1'."
    print "Absolutely no: Press '2'."
    print "I want quit: Press '3'."
    
    answer2 = raw_input('>')
    if answer2 == "3":
        print "It's ok. See you next time.(I bet you are AB type, aren't you?)"
    elif answer2 == "2":
        print "Are you always late?"
        print "Always...: Press '1'."
        print "No: Press '2'."
        print "Err...I don't remember: Press '3'."
        
        answer3 = raw_input('>')
        if answer3 == "1":
            print "You're absolutely B type."
        elif answer3 == "2":
            print "You look like a O type guy."
        elif answer3 == "3":
            print "You're totally O type."
        else:
            print "Hey! Why didn't you follow the rules? I suppose you are B type!"
    elif answer1 == "1":
        print "I know you, cute A type."
    else:
        print "Hey! Why didn't you follow the rules? I suppose you are B type!"
elif answer1 == "2":
    print "It's ok. See you next time."
else:
    print "Hey! Why didn't you follow the rules? I suppose you are B type!"

