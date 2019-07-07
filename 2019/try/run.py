import subprocess
import os

def reload(commands, server_port=8002):
	# STEP 1
	print("-> Getting process id to kill")
	print('-> Executing: {0}'.format(commands[0]))
	output = subprocess.getoutput("ps aux | grep uwsgi")
	print(output)
	port = output.split('\n')[0].split()[1]

	# STEP 2
	print('-> Killing port {0}'.format(port))
	print('-> Executing: {0}'.format(commands[1].format(port=port)))
	ret = os.system(commands[1].format(port=port))
	if ret:
		print("Failed to kill the process with id {0}".format(port))
	else:
		print("Successfully killed the process")

	# STEP 3
	print('-> Restarting server at {0}'.format(server_port))
	print('-> Executing: {0}'.format(commands[2]))
	ret = os.system(commands[2].format(server_port=server_port))
	if ret:
		print("Failed to reload server at {0}".format(server_port))
	else:
		print("Successfully restarted the server")


if __name__ == "__main__":
	commands = [
		'ps aux | grep uwsgi',
		'kill -9 {port}',
		'uwsgi server --http :{server_port}'
	]

	reload(commands)


