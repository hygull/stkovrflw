def reverse_words(message):
    # Reverse entire message
    reverse_message(0, len(message) - 1, message)

    # Reverse each word. Space indicates when word is completed
    start_index = 0

    for i in range(len(message)): # OLD => for i in range(0, len(message) - 1):
        if(message[i] == ' '):
            reverse_message(start_index, i - 1, message)
            start_index = i + 1

        #At the end of the message
        if(i == len(message) - 1):
            reverse_message(start_index, len(message) - 1, message)

    return message

def reverse_message(start_index, end_index, message):
    while(start_index < end_index):
        message[start_index],message[end_index] = message[end_index],message[start_index]
        start_index += 1
        end_index -= 1


# Test 1
message = ['C','a','k','e',' ','T','h','i','e','f']    
new_message = reverse_words(message)
print(new_message)

message2 = ['R', 'i', 's', 'h', 'i', 'k', 'e', 's', 'h', ' ', 'o', 'f', ' ', 'I', 'n', 'd', 'i', 'a']  
new_message2 = reverse_words(message2)
print(new_message2)


