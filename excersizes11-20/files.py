from sys import argv

script, filename = argv     #accepts the current file and the choosen file

txt = open(filename)        #opens the choosen file and loads it into a variable

print "Here's your file %r:" %filename      #simple print statement
print txt.read()                            #prints out the contents of the file

print "Type the filename again:"            #simple print statement
file_again = raw_input("> ")                #stores the name of a file in a variable

txt_again = open(file_again)            #loads a file into a variable

print txt_again.read()                  #prints the contents of a file