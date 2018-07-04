# https://stackoverflow.com/questions/51165779/combine-2-lists-of-pairs#51165779

def get_combined_users(list1, list2):
	usernames = set()
	combined = []

	for user in sorted(list2 + list1, key=lambda user: user[0]): # Do not use => list1 + list2
		if not user[0] in usernames:
			usernames.add(user[0])
			combined.append(user)

	return combined

if __name__ == "__main__":
	dyndns = [('user1', 'dyndns1'), ('user2', 'dyddns2'), ('user3', 'dyndns3'), ('user4', 'dyddns4')]
	ip = [('user1', '1.1.1.1'), ('user2', '1.1.1.2'), ('user4', '1.1.1.4')]

	combined = get_combined_users(dyndns, ip)
	print(combined)

# >> options.colBy = 5;
# >> options.rowBy = 3;
# >> obj = LatexTableFromMCode('magic(20)', options)
# ...
# ...
# ...
# >> obj.compileLatex();
# ...
# ...
# ...
# >> obj.options

# ans = 

#   struct with fields:

#     latexFileName: 'Latex-Table-03-Jul-2018-19-23-23.tex'
#             rowBy: 3
#             colBy: 5
#         alignment: 'c'
#          tablePos: 'htbp'
#          colNames: ''
#     fillBlankWith: ''
#      colFontStyle: ''

# >> 