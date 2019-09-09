the_count = [1, 2, 3, 4]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#let's display the contents of our lists
for number in the_count:
    print "This is count %d" %number

for fruit in fruits:
    print "A fruit of type: %s" %fruit

for i in change:
    print "I got %r" %i

#to create a list with a for loop you have to start with an empty list
elements = []

#then you call on the append function in the for loop
for i in range(0, 6):
    print "Adding %d to the list." %i
    elements.append(i)

#let's display the list we created
for i in elements:
    print "Element was: %d" %i