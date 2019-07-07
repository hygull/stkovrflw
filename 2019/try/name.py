class Name(object):
    def __init__(self):
        self.names = []

    def make_names(self):
        while True:
            names = {} # Dictionary to store `first_name` & `last_name`

            first_name = input("Enter the first name of someone you know, press q to exit: ")
            if first_name == "q":
                break
            else:
                names["first_name"] = first_name

            last_name = input("Enter the last name of someone you know, press q to exit : ")
            if last_name == "q":
                # If no `last_name`, remove `first_name` (you can write your own logic as you want) 
                del names['first_name']
                break
            else:
                names["last_name"] = last_name
                self.names.append(names)

    def get_all_names(self):
        return self.names

    def get_name(self, n):
        # `n` will be 1 if you want to get the first entered names in the list & so on
        try:
            name = self.names[n-1]
        except Exception as err:
            name = None
            print(err) # list index out of range

        return name

if __name__ == "__main__":
    name = Name()
    name.make_names()

    name_list = name.get_all_names()

    import json
    print(json.dumps(name_list, indent=4)) # PRETTY PRINT 
    # [
    #     {
    #         "first_name": "Rishikesh",
    #         "last_name": "Agrawani"
    #     },
    #     {
    #         "first_name": "Hemkesh",
    #         "last_name": "Agrawani"
    #     }
    # ]

    name1 = name.get_name(1)
    print(name1)
    # {'first_name': 'Rishikesh', 'last_name': 'Agrawani'}

    name2 = name.get_name(2)
    print(name2)
    # {'first_name': 'Hemkesh', 'last_name': 'Agrawani'}

    name3 = name.get_name(3) # None (only 2 names are there in this case)
    print(name3)
    # None

