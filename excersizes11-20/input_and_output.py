print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall, and %r heavy." %(
    age, height, weight
)

#this should display height correctly
print "So, you're %s old, %s tall, and %s heavy." %(
    age, height, weight
)

#more ways to use raw_input()
eye_color = raw_input("What color are your eyes? ")
print "You have %r eyes" %eye_color