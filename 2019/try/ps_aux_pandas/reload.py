import subprocess
import os

def get_process(command, param):
	try:
		print('---' * 30)
		print('GETTING PROCESS ID')
		command = f"{command} {param}"
		print('Executing ' + command)
		output = subprocess.check_output(command, shell=True)
		print(output)
		lines = output.strip().split('\n')
		pid = lines[0].split()[1]
		print(pid)
		return pid, 0
	except Exception as error:
		print(error)
		return None, 1

def kill_process(command, param):
	param = param.format(pid=pid)
	try:
		print(f"Executing {command} {param}")
		ret = subprocess.call(f"{command} {param}")
	except Exception as error:
		print(error)
		ret = 1

	return ret

def run(commands):
	pid = None

	for key, value in commands.items():
		print('---' * 30)
		if key == 'ps':
			pid, ret = get_process_id(key, value)
			if ret:
				break
		elif key == 'kill':
			ret = kill_process(key, value)
			if ret:
				break
		elif key == "git":
			for i, sub_command in enumerate(value):
				command = f"{key} {sub_command}"
				print(f'{i} Executing {command}')
				# output = subprocess.check_output(command, shell=True)
				ret = subprocess.call(command, shell=True)
				if not ret:
					break
		elif key == "cd":
			ret = subprocess.call(f"{key} '{value}'", shell=True)
			if not ret:
				break
	else:
		ret = 0
		print('---' * 30)

	return ret

def deploy(*args, project_path="/home/centos/pandora", branch='jwt-auth-2', filter_str='uwsgi', port=8002, **kwargs):
	from collections import OrderedDict
	commands = OrderedDict()

	commands["cd"] = project_path
	commands["git"] = [
			"status"
			"log"
			"stash"
			f"pull origin {branch}"
		]

	commands["ps"] = f"aux | grep '{filter_str}'" # uwsgi
	commands["kill"] = '-9 {pid}' # 16913
	commands["uwsgi"] = f'server.ini --http :{port}' # 8002
	
	return run(commands)

if __name__ == "__main__":
	project_path = "/Users/hygull/Projects/Python3/CorporateFdRoot/pandora_old"
	ret = deploy(project_path= project_path)

	if ret:
		print('OPERATION FAILED')
	else:
		print('OPERATION SUCCESSFUL')