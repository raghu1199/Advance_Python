import json

csv_file = open("csv_file.txt", "r")
lines = csv_file.readlines()
csv_file.close()
lines = [line.strip() for line in lines]
print(lines)
data_list = list()

for line in lines:
    club,city,country = line.split(",")
    line_dict={
        'club':club,
        'city':city,
        'country':country
    }
    print(line_dict)
    data_list.append(line_dict)

csv_file.close()
print(data_list)

json_file=open("josn_file.txt","w")
json.dump(data_list,json_file)
json_file.close()
