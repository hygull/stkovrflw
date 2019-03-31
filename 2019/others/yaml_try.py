import yaml
list1 = [{'Test01': '01', 'Test02': '02'}, {'Test03': '03', 'Test04': '04'}]

# list1

some_data = {"data": list1} 
yaml_data = {
  'version': '1.0'
}
yaml_data.update(some_data)
# yaml_data = [yaml_data]

print(yaml.dump(yaml_data, default_flow_style=False))