```bash
            except urllib3.connection.VerifiedHTTPSConnection as error:
TypeError: catching classes that do not inherit from BaseException is not allowed
```

```python
try:
	requests.get(url)
# except urllib3.exceptions.NewConnectionError as error:
#     print('ERROR YES 1')
# except urllib3.connection.VerifiedHTTPSConnection as error:
#     print('ERROR YES 2')
# except urllib3.exceptions.MaxRetryError as error:
#     print('ERROR YES 3')
except requests.exceptions.ConnectionError as error:
    print('ERROR YES 4')
except Exception as error:
    traceback.print_tb(error)
    print(error)
    message += str(error)
```