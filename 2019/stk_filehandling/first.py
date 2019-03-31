list=["ab","cd","ef"]

for i in list:
    with open("input.txt", "a+") as input_file:
        print("{}".format(i), file = input_file)