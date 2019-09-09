#checklist to make sure your function is working
def checklist():
    check_def = raw_input("Does your function start with \'def\'?")
    check_name = raw_input("Does your function name only include characters and the _?")
    check_parenthesis = raw_input("Did you put an open parenthesis right after the name?")
    check_arg = raw_input("Are you arguements after the \( and are they seperated with a comma?")
    check_colon = raw_input("Is there a parathesis and a colon ): after the arguements?")
    check_indent = raw_input("Are all of the lines of the function indented four spaces?")
    check_end = raw_input("Does your function end by going back to writing without an indent?")

#makes sure you are calling a function correctly
def calling_checklist():
    check_name = raw_input("Did you call the function by typing its correct name?")
    check_parenthesis = raw_input("Is there a open paranthesis ( right after the name and a closing paranthesis ) after the arguements?")
    check_values = raw_input("Did you put the values you want to pass to the function inbetween the paranthesis and seperated by a comma?")
