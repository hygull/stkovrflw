# Old answer 
# https://stackoverflow.com/questions/56921596/how-to-get-the-values-of-a-dictionary-using-key-path
def find_in_input_json(element, input_json):
    # Fetch element keys value
    element = element['file']["element"] # '/Users/hygull/Desktop/Python3/file1/output'

    keys = element.split('/') 
    print(keys) # ['', 'Users', 'hygull', 'Desktop', 'Python3', 'file2', 'output']

    rv = input_json

    for key in keys:
        if key in rv:     # 'file2' key is in input_json
            rv = rv[key]  # Get its value
            break         # Exit from loop, don't go further 
            
    return rv             # Return the value


if __name__ == '__main__':
    # TEST CASE 1
    key_value = {
        'file': {
            'name': 'a.py',
            'element': '/Users/hygull/Desktop/Python3/file2/output',
            'children': [
                'b.py',
                'c.py'
            ]
        }
    }

    input_json = {
        'file1': {
            'name': 'a.py',
            'element': '/Users/hygull/Desktop/Python3/file2/output',
            'children': [
                'b.py',
                'c.py'
            ]
        },
        'file2': {
            'name': 'c.py',
            'element': '/Users/hygull/Desktop/Python3/file1/output',
            'children': [
                'd.py',
                'e.py'
            ]
        },
        'file3': {
            'name': 'x.py',
            'element': '/Users/hygull/Desktop/Python3/file4/output',
            'children': [
                'y.py',
                'z.py'
            ]
        }
    }

    value = find_in_input_json(key_value, input_json)
    print(value) # {'name': 'c.py', 'element': '/Users/hygull/Desktop/Python3/file1/output', 'children': ['d.py', 'e.py']}

