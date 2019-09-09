name = 'Spencer Cheney'
age = 22
height = 66 #inches
weight = 170 #lbs. I'd like it to be 155 though
eyes = 'Blue'
teeth = 'White'
hair = 'Blondish Brown, but closer to Blonde'

print "Let's talk about %s." %name
print "He's %d inches tall." %height
print "He weighs %d lbs." %weight
print "That's a little too heavy"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the soda." %teeth

print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight
)

print "%s, %d, %r, %c" %(height, height, height + age, height)

centimeters = height * 2.54
kilos = weight * 0.453592

print "%d inches is equal to %f centimeters" %(height, centimeters)
print "%d lbs is equal to %f kilograms" %(weight, kilos)