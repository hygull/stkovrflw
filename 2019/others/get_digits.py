def get_digits(n):
    while str(n):
        yield n % 10

        n = n // 10
        if not n:
            break

digit = get_digits(1729)

print(next(digit)) # 9
print(next(digit)) # 2
print(next(digit)) # 7
print(next(digit)) # 1



for digit in get_digits(74831965):
	print(digit)

# 5
# 6
# 9
# 1
# 3
# 8
# 4
# 7

# >>> def letter(name):
# ...     for ch in name:
# ...         yield ch
# ... 
# >>> 
# >>> char = letter("RISHIKESH")
# >>> 
# >>> next(char)
# 'R'
# >>> 
# >>> "Second letter is my name is: " + next(char)
# 'Second letter is my name is: I'
# >>> 
# >>> "3rd one: " + next(char)
# '3rd one: S'
# >>> 
# >>> next(char)
# 'H'
# >>> 