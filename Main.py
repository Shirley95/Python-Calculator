import re
'''making sure using eval more safely by removing letters otherwise can damage laptop '''

print("Our Magical Calculator")

previous = 0 # holds data value of the previous calculation
run = True


def performMath():
    global previous #without 'Global' scope these variables declared outside of function cannot be accessed in function
    global run
    equation = ""  #initialising

    if previous == 0:
        equation = input("Enter an equation:")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Goodbye, human.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,()" "]', "", equation)  # keeping eval function safe
        if previous == 0:
            previous = eval(equation)  # eval fails at second loop
        else:
            previous = eval(str(previous) + equation)  # therefore need to evaluate second time like this


while run:
    performMath()
