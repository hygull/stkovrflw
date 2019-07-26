```bash
(venv3.6.7) ➜  pandora git:(nseuat07062019) ✗ 
(venv3.6.7) ➜  pandora git:(nseuat07062019) ✗ python manage.py shell
Python 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 03:02:14) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from masterdata.models import IncomeMaster
>>> 
>>> ds = IncomeMaster.objects.all()
>>> ds
<QuerySet [<IncomeMaster: IncomeMaster 1, Below 1 lakh>, <IncomeMaster: IncomeMaster 2, 1 to 5 lakhs>, <IncomeMaster: IncomeMaster 3, 5 to 10 lakhs>, <IncomeMaster: IncomeMaster 4, 10 to 25 lakhs>, <IncomeMaster: IncomeMaster 5, 25 lakhs to 1 crore>, <IncomeMaster: IncomeMaster 6, Above 1 crore>]>
>>> 
>>> from masterdata.serializers import IncomeMasterSerializer
>>> 
>>> IncomeMasterSerializer(ds, many=True)
IncomeMasterSerializer(<QuerySet [<IncomeMaster: IncomeMaster 1, Below 1 lakh>, <IncomeMaster: IncomeMaster 2, 1 to 5 lakhs>, <IncomeMaster: IncomeMaster 3, 5 to 10 lakhs>, <IncomeMaster: IncomeMaster 4, 10 to 25 lakhs>, <IncomeMaster: IncomeMaster 5, 25 lakhs to 1 crore>, <IncomeMaster: IncomeMaster 6, Above 1 crore>]>, many=True):
    id = IntegerField(label='ID', read_only=True)
    name = CharField(allow_null=True, max_length=256, required=False)
    description = CharField(allow_null=True, max_length=256, required=False)
    code = CharField(allow_null=True, max_length=256, required=False)
>>> 
>>> dst = IncomeMasterSerializer(ds, many=True)
>>> 
>>> data = dst.data
>>> 
>>> data
[OrderedDict([('id', 1), ('name', 'Below 1 lakh'), ('description', 'Below 1 lakh'), ('code', '31')]), OrderedDict([('id', 2), ('name', '1 to 5 lakhs'), ('description', '1 to 5 lakhs'), ('code', '32')]), OrderedDict([('id', 3), ('name', '5 to 10 lakhs'), ('description', '5 to 10 lakhs'), ('code', '33')]), OrderedDict([('id', 4), ('name', '10 to 25 lakhs'), ('description', '10 to 25 lakhs'), ('code', '34')]), OrderedDict([('id', 5), ('name', '25 lakhs to 1 crore'), ('description', '25 lakhs to 1 crore'), ('code', '35')]), OrderedDict([('id', 6), ('name', 'Above 1 crore'), ('description', 'Above 1 crore'), ('code', '36')])]
>>> 
>>> import json
>>> 
>>> text = json.dumps(data, indent=4)
>>> print(text)
[
    {
        "id": 1,
        "name": "Below 1 lakh",
        "description": "Below 1 lakh",
        "code": "31"
    },
    {
        "id": 2,
        "name": "1 to 5 lakhs",
        "description": "1 to 5 lakhs",
        "code": "32"
    },
    {
        "id": 3,
        "name": "5 to 10 lakhs",
        "description": "5 to 10 lakhs",
        "code": "33"
    },
    {
        "id": 4,
        "name": "10 to 25 lakhs",
        "description": "10 to 25 lakhs",
        "code": "34"
    },
    {
        "id": 5,
        "name": "25 lakhs to 1 crore",
        "description": "25 lakhs to 1 crore",
        "code": "35"
    },
    {
        "id": 6,
        "name": "Above 1 crore",
        "description": "Above 1 crore",
        "code": "36"
    }
]
>>> data = [
...     {
...         "id": 1,
...         "name": "Below 1 lakh",
...         "description": "Below 1 lakh",
...         "code": "31"
...     },
...     {
...         "id": 2,
...         "name": "1 to 5 lakhs",
...         "description": "1 to 5 lakhs",
...         "code": "32"
...     },
...     {
...         "id": 3,
...         "name": "5 to 10 lakhs",
...         "description": "5 to 10 lakhs",
...         "code": "33"
...     },
...     {
...         "id": 4,
...         "name": "10 to 25 lakhs",
...         "description": "10 to 25 lakhs",
...         "code": "34"
...     },
...     {
...         "id": 5,
...         "name": "25 lakhs to 1 crore",
...         "description": "25 lakhs to 1 crore",
...         "code": "35"
...     },
...     {
...         "id": 6,
...         "name": "Above 1 crore",
...         "description": "Above 1 crore",
...         "code": "36"
...     }
... ]
>>> 
>>> queries = []
>>> 
>>> for d in data:
...     query = "INSERT INTO MASTERDATA_INCOMEMASTER(id, name, description, code) VALUES(%d, '%s', '%s', '%s')" % (d['id'], d['name'], d['description'], d['code'])
...     queries.append(query)
... 
>>> queries
["INSERT INTO MASTERDATA_INCOMEMASTER(id, name, description, code) VALUES(1, 'Below 1 lakh', 'Below 1 lakh', '31')", "INSERT INTO MASTERDATA_INCOMEMASTER(id, name, description, code) VALUES(2, '1 to 5 lakhs', '1 to 5 lakhs', '32')", "INSERT INTO MASTERDATA_INCOMEMASTER(id, name, description, code) VALUES(3, '5 to 10 lakhs', '5 to 10 lakhs', '33')", "INSERT INTO MASTERDATA_INCOMEMASTER(id, name, description, code) VALUES(4, '10 to 25 lakhs', '10 to 25 lakhs', '34')", "INSERT INTO MASTERDATA_INCOMEMASTER(id, name, description, code) VALUES(5, '25 lakhs to 1 crore', '25 lakhs to 1 crore', '35')", "INSERT INTO MASTERDATA_INCOMEMASTER(id, name, description, code) VALUES(6, 'Above 1 crore', 'Above 1 crore', '36')"]
>>> 
>>> text = json.dumps(queries, indent=4)
>>> 
>>> print(text)
[
    "INSERT INTO MASTERDATA_INCOMEMASTER(id, name, description, code) VALUES(1, 'Below 1 lakh', 'Below 1 lakh', '31')",
    "INSERT INTO MASTERDATA_INCOMEMASTER(id, name, description, code) VALUES(2, '1 to 5 lakhs', '1 to 5 lakhs', '32')",
    "INSERT INTO MASTERDATA_INCOMEMASTER(id, name, description, code) VALUES(3, '5 to 10 lakhs', '5 to 10 lakhs', '33')",
    "INSERT INTO MASTERDATA_INCOMEMASTER(id, name, description, code) VALUES(4, '10 to 25 lakhs', '10 to 25 lakhs', '34')",
    "INSERT INTO MASTERDATA_INCOMEMASTER(id, name, description, code) VALUES(5, '25 lakhs to 1 crore', '25 lakhs to 1 crore', '35')",
    "INSERT INTO MASTERDATA_INCOMEMASTER(id, name, description, code) VALUES(6, 'Above 1 crore', 'Above 1 crore', '36')"
]
>>> 
```