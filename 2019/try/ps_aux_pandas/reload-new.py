import subprocess
import os

def get_process_id(command, param, ignore_error=False):
	try:
		print('---' * 30)
		print('GETTING PROCESS ID')
		command = f"{command} {param}"
		print('Executing ' + command)
		output = subprocess.check_output(command, shell=True)
		output = output.decode('utf8')
		print(output)
		lines = output.strip().split('\n') # a bytes-like object is required, not 'str' (if not decoded)
		print(lines)
		pid = lines[0].split()[1]
		print(pid)
		return pid, 0
	except Exception as error:
		print(error)
		if ignore_error:
			return None, 0
		else:
			return None, 1

def kill_process(command, param, pid, ignore_error=False):
	param = param.format(pid=pid)
	try:
		print(f"Executing {command} {param}")
		ret = subprocess.call(f"{command} {param}")
	except Exception as error:
		print(error)
		if ignore_error:
			ret = 0
		else:
			ret = 1

	return ret

def run(commands, ignore_error=False):
	pid = None

	for key, value in commands.items():
		print('---' * 30)

		if key == 'ps':
			pid, ret = get_process_id(key, value, ignore_error)
			if ret:
				if not ignore_error:
					break
		elif key == 'kill':
			ret = kill_process(key, value, pid, ignore_error)
			if ret:
				if not ignore_error:
					break
		elif key == "git":
			for i, sub_command in enumerate(value):
				command = f"{key} {sub_command}"
				print(f'{i} Executing {command}')
				# output = subprocess.check_output(command, shell=True)
				ret = subprocess.call(command, shell=True)
				if ret:
					if not ignore_error:
						break
		elif key == "cd":
			# ret = subprocess.call(f"{key} '{value}'", shell=True)
			ret = os.chdir(value)
			print(os.getcwd())

			if ret:
				if not ignore_error:
					break
		else:
			print(f"Executing -> {key} {value}")
			ret = os.system(f"{key} {value}")
			if ret:
				if not ignore_error:
					break
		# print('---' * 30)
	else:
		ret = 0
	# print('---' * 30)

	return ret

def deploy(*args, project_path="/home/centos/pandora", branch='jwt-auth-2', filter_str='uwsgi', port=8002, origin='moneybloom', ignore_error=False, allow_sudo=False, **kwargs):
	from collections import OrderedDict
	pwd = os.path.dirname(os.path.abspath(__file__))

	if allow_sudo:
		sudo = 'sudo '
	else:
		sudo = ''

	commands = OrderedDict()

	commands["cd"] = project_path
	commands["git"] = [
			"status",
			"log",
			"stash",
			f"pull {origin} {branch}"
			# 'stash apply'
		]

	commands["ps"] = f"aux | grep '{filter_str}'" # uwsgi
	commands[sudo + "kill"] = '-9 {pid}' # 16913
	commands["uwsgi"] = f'server.ini --http :{port}' # 8002

	print(commands)
	
	ret = run(commands)
	os.chdir(pwd)

if __name__ == "__main__":
	PROD = False
	allow_sudo = False

	PROD = True
	allow_sudo = True

	if PROD:
		project_path ="/home/centos/pandora"
		origin = 'origin'
	else:
		project_path = "/Users/hygull/Projects/Python3/CorporateFdRoot/pandora_old"
		origin = 'moneybloom'

	ret = deploy(project_path=project_path, origin=origin, ignore_error=True, allow_sudo=allow_sudo)

	if ret:
		print('OPERATION FAILED')
	else:
		print('OPERATION SUCCESSFUL')