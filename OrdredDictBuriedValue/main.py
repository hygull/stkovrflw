# OrderedDict([('totalSize', 1),
#          ('done', True),
#          ('records',
#           [OrderedDict([('attributes',
#                          OrderedDict([('type', 'Case'),
#                                       ('url',
#                                        '/services/data/v38.0/sobjects/Case/5003700000ReKcJAAV')])),
#                         ('Id', '5003700000ReKcJAAV')])])])


from collections import OrderedDict
import json

l = [('totalSize', 1),
         ('done', True),
         ('records',
          [OrderedDict([('attributes',
                         OrderedDict([('type', 'Case'),
                                      ('url',
                                       '/services/data/v38.0/sobjects/Case/5003700000ReKcJAAV')])),
                        ('Id', '5003700000ReKcJAAV')])])]
ordDict = OrderedDict(l)

print json.dumps(ordDict, indent=4)
"""
{
    "totalSize": 1,
    "done": true,
    "records": [
        {
            "attributes": {
                "type": "Case",
                "url": "/services/data/v38.0/sobjects/Case/5003700000ReKcJAAV"
            },
            "Id": "5003700000ReKcJAAV"
        }
    ]
}
"""

print ordDict['records'][0]['Id'] # 5003700000ReKcJAAV