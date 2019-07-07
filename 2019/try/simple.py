def get_assign(user_input):
    key, value = user_input.split("gets")
    key = key.strip()
    value = int(value.strip())
    my_dict[key] = value
    print(my_dict)

def add_values(num1, num2):
    return num1 + num2


print("Welcome to the Adder REPL.")

my_dict = dict()

while True:
    user_input = input("???")

    if 'gets' in user_input:
        get_assign(user_input)

    if 'input' in user_input:
        print("Enter a value for :")
        input_assign()

    if 'adds' in user_input:

        a, b = user_input.split("adds")

    if 'print' in user_input:

        print_values()

    if 'quit' in user_input:

        print("GoodBye")

        exit()