def func1():
    user_name = input("What's your name? ")

    if any(char.isdigit() for char in user_name):
        print("You can't put a number in your name.")
        sys.exit()
    else:
        pass

    return user_name

first_name_information = func1

def func2():
    user_name = first_name_information()
    last_name = input("What's your last name {}? ".format(user_name))

    if any(char.isdigit() for char in last_name):
        print("You can't put a number in your last name.")
        sys.exit()
    else:
        print("So, you are {0} {1}".format(user_name, last_name))
        pass

func2()