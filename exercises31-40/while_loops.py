def loop(num, inc):
    i = 0
    numbers = []

    while i < num:
        print "At the top i is %d" %i
        numbers.append(i)

        i = i + inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" %i

    return numbers

numbers = loop(6, 1)

print "The numbers: "

for num in numbers:
    print num

numbers_1 = loop(18, 2)

print "The numbers: "

for num in numbers_1:
    print num

#let's do it with a for loop
def loop_2(num, inc):
    numbers = []

    for i in range(0, num, inc):
        print "At the top i is %d" %i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" %i

    return numbers


numbers_for = loop_2(29, 3)

print "The numbers from for loop: "

for num in numbers_for:
    print num        