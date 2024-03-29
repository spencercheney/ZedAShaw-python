from sys import argv

script, input_file = argv

def print_all(f):           #prints the entire contents of a file
    print f.read()

def rewind(f):              #moves to the begining of a file
    f.seek(0)

def print_a_line(line_count, f):            #prints the line number and a line in a file
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)