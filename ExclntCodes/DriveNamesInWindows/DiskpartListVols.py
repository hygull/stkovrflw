"""
	Coded on: 08 July 2018, Sunday
	Aim     : To print all the drive names in Windows System (Username also if 'USER' environment variable is SET)
	Coded by: Rishikesh Agrawani
"""

import os

file_name = 'log.txt'

os.system('diskpart /s diskpart_commands.txt > ' + file_name)
drives = []

with open(file_name) as f:
	lines = f.readlines()

	while lines:
		if '----------' in lines[0]:
			lines.remove(lines[0])
			while lines:
				drive = lines[0].split(' ')[8]

				if drive:
					drives.append(drive)
				lines.remove(lines[0])
		else:
			lines.remove(lines[0])

user = os.environ['USER'].split('\\')[2]
if not user:
	user = 'USER'
else:
	user = user

print 'Dear ' + user + ','
print 'You have the following drives in your system.'
print '\n'.join([str(t[0] + 1) + ". " + t[1] for t in enumerate(drives)])

"""
['', '', 'Volume', '0', '', '', '', '', 'D', '', '', 'System', 'Rese', '', 'NTFS', '', '', 'Partition', '', '', '', '100', 'MB', '', 'Healthy', '', '', '', '', '', '', '', '', '', '', '', '\n']
['', '', 'Volume', '1', '', '', '', '', 'C', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'NTFS', '', '', 'Partition', '', '', '', '243', 'GB', '', 'Healthy', '', '', '', 'Boot', '', '', '', '\n']
['', '', 'Volume', '2', '', '', '', '', 'F', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'NTFS', '', '', 'Partition', '', '', '', '221', 'GB', '', 'Healthy', '', '', '', '', '', '', '', '', '', '', '', '\n']
['', '', 'Volume', '3', '', '', '', '', '', '', '', '', 'System', 'Rese', '', 'NTFS', '', '', 'Partition', '', '', '', '100', 'MB', '', 'Healthy', '', '', '', 'System', '', '\n']
['', '', 'Volume', '4', '', '', '', '', 'G', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'NTFS', '', '', 'Partition', '', '', '', '244', 'GB', '', 'Healthy', '', '', '', '', '', '', '', '', '', '', '', '\n']
['', '', 'Volume', '5', '', '', '', '', 'H', '', '', 'New', 'Volume', '', '', 'NTFS', '', '', 'Partition', '', '', '', '221', 'GB', '', 'Healthy', '', '', '', '', '', '', '', '', '', '', '', '\n']
"""

