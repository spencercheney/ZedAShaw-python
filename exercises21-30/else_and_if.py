people = 30
cars = 40
buses = 15

#are there more cars than people
if cars > people:
    print "We should take the cars."
#if not, are there less cars than people
elif cars < people:
    print "We should not take the cars."

#are there more buses than cars
if buses > cars:
    print "That's too many buses."
#if not, are there less busses than cars
elif buses < cars:
    print "Maybe we could take the buses."
#if the others aren't true do this
else:
    print "We still can't decide."

#more people than buses
if people > buses:
    print "Alright, let's just take the buses."
#if that's not true do this
else:
    print "Fine, let's stay home then."

#are there more people than cars, less buses than cars, and more people than buses
if people > cars & buses < cars & people > buses:
    print "We need to take the buses."