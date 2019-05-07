String_list = ['I','D','X']

CIG_list = [(65, '='), (1, 'X'), (91, '='), (3, 'D'), (60, '='), (1, 'X'), (7, '='), (2, 'S')]

for index, tup in enumerate(CIG_list): 
    ch = CIG_list[index][1]
    if ch in String_list:
        slice_l = CIG_list[: index + 1]
        total = sum([t[0] for t in slice_l])
        last_char = slice_l[-1][1]
        print(slice_l, ",", total, ",", last_char)


