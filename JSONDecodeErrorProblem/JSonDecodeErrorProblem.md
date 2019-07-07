**@user9371654**, there are 2 main problems associated with your `JSON file` and `Python code`.

* The contents of `result2.json` is not properly formatted.

* The parameters of `print()` function should be separated with `,` in place of `+` ( If you still prefer `,` then uou will need to convert your list to string using `str()` to support concatenation).

### result2.json &raquo;

> Copy your JSON content of `result2.json` and format it at https://jsonformatter.curiousconcept.com.

> **Note:** Update your JSON file `result2.json` with the following content.

	[  
	   {  
	      "host":"host1.com",
	      "ip":"x.x.x.x",
	      "port":443,
	      "tlsVersions":[  
	         "TLSv1_2"
	      ],
	      "cipherSuite":{  
	         "supported":[  
	            "ECDHE-RSA-AES256-GCM-SHA384"
	         ]
	      },
	      "x509ChainDepth":2,
	      "verifyCertResult":true,
	      "verifyHostResult":true,
	      "ocspStapled":true,
	      "verifyOcspResult":true,
	      "certificateChain":[  
	         {  
	            "version":3
	         },
	         {  
	            "version":3
	         }
	      ]
	   },
	   {  
	      "host":"host2.com",
	      "ip":"y.y.y.y",
	      "port":443,
	      "tlsVersions":[  
	         "TLSv1_2"
	      ],
	      "cipherSuite":{  
	         "supported":[  
	            "ECDHE-RSA-AES256-GCM-SHA384"
	         ]
	      },
	      "x509ChainDepth":2,
	      "verifyCertResult":true,
	      "verifyHostResult":true,
	      "ocspStapled":true,
	      "verifyOcspResult":true,
	      "certificateChain":[  
	         {  
	            "version":3
	         },
	         {  
	            "version":3
	         }
	      ]
	   }
	]

### Python Code &raquo;

Finally try the below code:

	import json 

	with open('result2.json', 'r') as f:
	    distros_dict = json.load(f)

	for distro in distros_dict:
	    print(distro['host'], "," , distro['tlsVersions'], '\n')

### Output &raquo;

	host1.com , ['TLSv1_2']

	host2.com , ['TLSv1_2']