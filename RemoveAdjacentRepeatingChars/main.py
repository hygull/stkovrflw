def remove_adjacent_duplicates(answer):
    new_answer = ""    # output string
    ch_last = ""       # current character of last iteration
    start, end = 0, 0  # start and end indices of adjacent characters sequence

    for index, ch in enumerate(answer):
        if index: # for index 1 and onwards
            if ch == ch_last:
                end = index 
            else: # if new character encountered after repetition of any particular character
                if start == end: # if there is a repetition
                    new_answer = new_answer + ch_last
                start, end = index, index
        else:   # index == 0 (only 1st time)
            start, end = index, index

        ch_last = ch # save the current character to use it in next iteration

    if start == end: # if the last encountered character is not of repeating nature
        new_answer = new_answer + ch_last

    return new_answer

# START
if __name__ == "__main__":
    # INPUT 1
    answer = input("Enter a string: ")         # abbabd
    print(remove_adjacent_duplicates(answer))  # aabd

    # INPUT 2
    answer = input("Enter a string: ")         # abcddddeefffghii
    print(remove_adjacent_duplicates(answer))  # abcgh
    
    # INPUT 3
    answer = input("Enter a string: ")         # abcddddeefffghi
    print(remove_adjacent_duplicates(answer))  # abcghi    

    # INPUT 4
    answer = input("Enter a string: ")         # aa**mmmxxnnnnRaaI++SH((IKES))H
    print(remove_adjacent_duplicates(answer))  # RISHIKESH