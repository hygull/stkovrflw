import requests
from bs4 import BeautifulSoup
import os
import json
import pandas as pd

url = "https://m.rbi.org.in/Scripts/bs_viewcontent.aspx?Id=2009"

print("Stage 1")
response = requests.get(url)
print("Stage 2")
print(response.status_code)
print("Stage 3")
print(response.text)
print("Stage 4")


soup = BeautifulSoup(response.text, "html.parser")
print(soup)
#     anchors = soup.findall("a", class_="links")
# TypeError: 'NoneType' object is not callable
anchors = soup.find_all("a", class_="links")
print(anchors)

hrefs = [anchor.get("href") for anchor in anchors]
print(hrefs)

with open('hrefs.txt', "w") as fw:
	fw.write(json.dumps(hrefs, indent=4))


print("Total links =>", len(hrefs))

hrefs = enumerate(hrefs)
index, href = hrefs.__next__()
index += 1
while True and href and index:
	try:
		print("Processing link [", href, "]", index)
		file_name = href.split("/")[-1]
		# {
		#     'TERM_PROGRAM': 'Apple_Terminal', 'SHELL': '/usr/local/bin/zsh', 
		#     'TERM': 'xterm-256color', 'TMPDIR': '/var/folders/_h/d17s0sg11q74f68sxqnvg1nm0000gn/T/', 
		#     'Apple_PubSub_Socket_Render': '/private/tmp/com.apple.launchd.BhK0SraDmZ/Render', 
		#     'TERM_PROGRAM_VERSION': '421.1.1', 'TERM_SESSION_ID': '1A5D8461-35FA-45EC-AE8C-F4BC605375B5', 
		#     'USER': 'hygull', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.4JkDlgnD7v/Listeners', 
		#     'PATH': '/Users/hygull/Desktop/try_django_tenant_schemas/venv3.6.7.26apr/bin:/Users/hygull/bin:/usr/local/bin:/Users/hygull/Library/Python/3.6/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin', 'PWD': '/Users/hygull/Desktop/try_django_tenant_schemas/src', 
		#     'XPC_FLAGS': '0x0', 'XPC_SERVICE_NAME': '0', 'SHLVL': '1', 'HOME': '/Users/hygull', 
		#     'LOGNAME': 'hygull', 'LC_CTYPE': 'UTF-8', 'SECURITYSESSIONID': '186a7', 
		#     'OLDPWD': '/Users/hygull/Desktop/try_django_tenant_schemas', 
		#     'ZSH': '/Users/hygull/.oh-my-zsh', 'PAGER': 'less', 'LESS': '-R', 
		#     'LSCOLORS': 'Gxfxcxdxbxegedabagacad', 'VIRTUAL_ENV': '/Users/hygull/Desktop/try_django_tenant_schemas/venv3.6.7.26apr', 
		#     'PS1': '(venv3.6.7.26apr) ${ret_status} %{$fg[cyan]%}%c%{$reset_color%} $(git_prompt_info)', 
		#     '_': '/Users/hygull/Desktop/try_django_tenant_schemas/venv3.6.7.26apr/bin/python', 
		#     '__CF_USER_TEXT_ENCODING': '0x1F5:0x0:0xF', 'DJANGO_SETTINGS_MODULE': 'proj.settings', 'TZ': 'UTC', 'RUN_MAIN': 'true', 
		#     'SERVER_NAME': '1.0.0.127.in-addr.arpa', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '9001', 
		#     'REMOTE_HOST': '', 'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 
		#     'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/', 'QUERY_STRING': '', 
		#     'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': 'my-domain.com:9001', 
		#     'HTTP_CONNECTION': 'keep-alive', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 
		#     'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36', 
		#     'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 
		#     'HTTP_PURPOSE': 'prefetch', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate', 
		#     'HTTP_ACCEPT_LANGUAGE': 'en-GB,en-US;q=0.9,en;q=0.8,fr;q=0.7,bn;q=0.6', 
		#     'HTTP_COOKIE': 'csrftoken=uGSspU2vSuAjKIAWJL98EpmmXIjsiHOo5KV1IJdFdVL5rfVsF82Q69esnc8yYALH; sessionid=e4hvc3195c204g5z4e2d5x40furp1ghw', 
		#     'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x103595eb8>, 
		#     'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>, 
		#     'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 
		#     'wsgi.multithread': True, 'wsgi.multiprocess': False, 
		#     'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>, 
		#     'CSRF_COOKIE': 'uGSspU2vSuAjKIAWJL98EpmmXIjsiHOo5KV1IJdFdVL5rfVsF82Q69esnc8yYALH'
		# }

		# *---* 'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
		# *---* 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
		
		# headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
		headers = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
		}

		# 1st way
		# res = requests.get(href, headers=headers)

		# 2nd way
		session = requests.Session()
		print("OLD HREF => ", href)
		href = href.replace("http://", "https://") # Otherwise 403
		print("NEW HREF => ", href)
		res = session.get(href,headers={'User-Agent': 'Mozilla/5.0'})

		if res.status_code == 200:
			print("*---*", index, "Success", "*---*")
		else:
			print("*---*", index, "Failed *---*")

		with open(os.path.join(os.path.abspath("."), "xlsx_files4", file_name), "wb") as fw:
			fw.write(res.content)

		print("DataFrame Excel Path =>" + os.path.join(os.path.abspath("."), "xlsx_files4", file_name))
		df = pd.read_excel(os.path.join(os.path.abspath("."), "xlsx_files4", file_name))

		csv_file_name = file_name.replace(".xlsx", ".csv")
		print("CSV PATH =>" + csv_file_name)
		df.to_csv(os.path.join(os.path.abspath("."), "csvs", csv_file_name))
		# else:
		# 	print(index, "Failed")
		# 	print(res.text)
		# 	print("-----")
		# 	print(res.status_code)
		# 	with open("failed.html", "w") as fw:
		# 		fw.write(res.text)
		# 	break
		index, href = hrefs.__next__()
		index += 1
	except TimeoutError as error:
		with open("timeout_new.txt", "a+") as fa:
			fa.write(str(index) + "-" + str(error) +  "-" + href)
		print("@" * 40, "\nRetrying for " + href + "@" * 40)
		continue
	except StopIteration as error:
		print("*---* Done *---*")
		break
	except Exception as error:
		print(index, error)
		print("Failed")
		import traceback
		import sys
		exc_type, exc_value, exc_traceback = sys.exc_info()
		traceback.print_tb(exc_traceback, limit=40, file=sys.stdout)

		break