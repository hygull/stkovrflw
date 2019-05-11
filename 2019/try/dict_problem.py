import re

def get_my_target_dict(my_list):
    my_target_dict = {} # dictionary

    for string in my_list:
        # "Alex:1990:London" => ["Alex", "1990", "London"]
        # "Alex :   1990: London" => ["Alex", "1990", "London"]
        items = re.split(r"\s*:\s*", string) # `\s*` is to match spaces around `:`
        print(items)

        # Alex, Tony etc.
        key = items[0]

        if key in my_target_dict:
            my_target_dict[key].append(string)
        else:
            my_target_dict[key] = [string]

    return my_target_dict


if __name__ == "__main__":
    my_list=["Alex:1990:London", 
             "Tony:1993:NYC", 
             "Kate:2001:Beijing", 
             "Tony:2001:LA", 
             "Alex:1978:Shanghai"]

    # Call get_my_target_dict(), pass my_list & get my_target_dict
    my_target_dict = get_my_target_dict(my_list)
    print(my_target_dict)
    # {'Alex': ['Alex:1990:London', 'Alex:1978:Shanghai'], 'Tony': ['Tony:1993:NYC', 'Tony:2001:LA'], 'Kate': ['Kate:2001:Beijing']}

    # Pretty printing dictionary
    import json
    print(json.dumps(my_target_dict, indent=4))
    # {
    #     "Alex": [
    #         "Alex:1990:London",
    #         "Alex:1978:Shanghai"
    #     ],
    #     "Tony": [
    #         "Tony:1993:NYC",
    #         "Tony:2001:LA"
    #     ],
    #     "Kate": [
    #         "Kate:2001:Beijing"
    #     ]
    # }