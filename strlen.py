#asks user to input string and tells them how long it is

def askInput:
    print("Please input a string")
    userInput = raw_input() #raw_input() does not exist in 3.x, and has been replace by input()
    print("Your string is ", str(len(userInput)), " long.")
