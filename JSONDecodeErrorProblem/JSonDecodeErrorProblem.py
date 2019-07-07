import json 

with open('result4.json', 'r') as f:
    distros_dict = json.load(f)

for distro in distros_dict:
    print(distro['host'], "," , distro['tlsVersions'], '\n')