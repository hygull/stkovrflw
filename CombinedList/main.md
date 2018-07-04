The following code can be used to achieve the output. It used Python's **sorted()** function based on its **key** keyword argument.

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

### Output

	[('user1', '1.1.1.1'), ('user2', '1.1.1.2'), ('user3', 'dyndns3'), ('user4', '1.1.1.4')]
