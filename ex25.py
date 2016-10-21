def break_words(stuff):  ### stuff is a string
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words  ###words is a list
	

def sort_words(words): ### words is a list
    """Sorts the words."""
    return sorted(words) ### return a list 

def print_first_word(words): ###words is a list 
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word   ### print a list 

def print_last_word(words): ###words is a list 
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word  ## print a list 

def sort_sentence(sentence):  ###sentence is a string 
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)   ###sentence is a string
    return sort_words(words)  ##words is a list 

def print_first_and_last(sentence):  ###sentence is a string 
    """Prints the first and last words of the sentence."""
    words = break_words(sentence) ## sentence is a string 
    print_first_word(words)  ###words is a list 
    print_last_word(words)  ##words is a list 

def print_first_and_last_sorted(sentence):  ##sentence is a string 
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence) ##sentence is a string 
    print_first_word(words) ##words is a list 
    print_last_word(words) ##words is a list 