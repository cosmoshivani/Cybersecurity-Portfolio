import re

user_input = input("please type your password: ")

# one lowercase
# one uppercase
# one symbol
# one number
# length >= 8

regex = re.findall("[a-z]+[A-Z]+[0-9]+[/_/$/@/!/+/*/#]+", user_input)

if len(user_input) >= 8 and regex:
    print("valid password")
else:
    print("Not valid")
