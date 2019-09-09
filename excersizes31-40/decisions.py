print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Eat the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear is friendly and shares the cake. You made a friend. Good job!"
    elif bear == "2":
        print "The bear doesn't like you getting angry and you are forced to wrestle the bear. You somehow beat him. Good job!"
    else:
        print "Well, doing %s is might better. Bear runs away" %bear

elif door == "2":
    print "You find a mountain of gold with a small oil lamp at the top."
    print "1. Take the lamp and forget the gold."
    print "2. You need the money and you take the gold."
    print "3. Search for a magic carpet."

    alladin = raw_input("> ")

    if alladin == "2" or alladin == "3":
        print "You do realize that the lamp has a genie inside, right?"
    else:
        print "You rub the lamp and the genie comes out and sings you a song. Good job!"

else:
    print "You don't listen, did you?"