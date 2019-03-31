output_lines = []

with open("z.txt") as f:
	lines = f.readlines()
	l =  len(lines)

	if l <= 1:
		if l == 1:
			output_lines = lines[0]
	else:
		# strip() is to remove `\n` from end of `lines[index]`
		output_lines = [lines[index].strip() + ' ' + lines[index + 1] for index in range(l-1)]

print(output_lines)
# ['alcoholic alert\n', 'alert algebra\n', 'algebra alibi\n', 'alibi blablabla']

# If you wish to save it in a file named `z_out.txt`
with open("z_out.txt", "w") as f:
	f.writelines(output_lines)


