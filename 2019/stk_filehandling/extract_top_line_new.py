# https://stackoverflow.com/questions/55410134/python-code-to-extract-the-data-from-out-file/55410727#55410727
# Solved: 29 March 2019, Fri

import re
import json

def get_dict(line):
    arr = line.split(" - ")

    d = {
        "mac_address": arr[0],
        "unit_address": arr[1],
        "execution_time": arr[2]
    }
    return d


def get_data_list(file_name):
    data_list = []

    with open(file_name) as f:
        text = f.read()
        fiter = fiter = re.finditer(r"######################################################################", text)
        
        while True:
            try:
                # --- Python2 (Uncomment these 2 lines) ---
                # e = first_hashes_ends_at = fiter.next().end()
                # s = second_hashes_starts_at = fiter.next().start()

                # --- Python 3 (If Python2 then comment the below 2 lines and uncomment above 2)---
                e = first_hashes_ends_at = fiter.__next__().end()
                s = second_hashes_starts_at = fiter.__next__().start()

                line = text[e + 1: s] # This is the final line that we want
                data_list.append(get_dict(line.strip()))
            except StopIteration as e:
                break

    return data_list


if __name__ == "__main__":
    data_list = get_data_list("data_new.txt")

    # pretty printing list of dictionaries
    print(json.dumps(data_list, indent=4))


