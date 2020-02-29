import json
from urllib.request import urlopen

with urlopen("http://dummy.restapiexample.com/api/v1/employees") as response:
    source=response.read()

content=json.loads(source)
print(type(content))
print(json.dumps(content,indent=2))
print(content['data'][1])

my_dict=dict()
fp = open("employee_data_json.txt", "w")

for item in content['data']:
    id=item['id']
    name=item['employee_name']
    salary=item['employee_salary']
    age=item['employee_age']

    my_dict['id']=id
    my_dict['name']=name
    my_dict['salary']=salary
    my_dict['age']=age

    json.dump(my_dict, fp, indent=2)

fp.close()

