def add(a, b):
    print "ADDING %d + %d" %(a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" %(a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" %(a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" %(a , b)
    return a / b

print "Let's do some math with just funcitons!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))      #age + (height - (weight * (iq / 2))) = 35 + (74 - (180 * (50 / 2)))

print "That becomes: ", what, "Can you do it by hand?"

what2 = add(weight, subtract(weight, multiply(weight, divide(weight, age))))      #weight + (weight - (weight * (weight / age))) = 180 + (180 - (180 * (180 / 35)))

print "That becomes: ", what2, "Can you do it by hand?"

def bmi_calculator(height, weight):             #uses inches and lbs
    return multiply(703, divide(weight, multiply(height, height)))

def bmi_calculator_metric(height, weight):      #uses meters and kg
    return divide(weight, multiply(height, height))

my_height_inches = 66.0
my_weight_lbs = 170.0

my_height_meters = 1.6764
my_weight_kg = 77.1107

print "Did it work? %f = %f" %(bmi_calculator(my_height_inches, my_weight_lbs), bmi_calculator_metric(my_height_meters, my_weight_kg))

print "YESSS!!!!"