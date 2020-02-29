
file=open("csv_data.txt","r")
lines=file.readlines()
file.close()

lines=[line.strip() for line in lines[2:]]

for line in lines:
    person_data=line.split(",")
    name=person_data[0].title()
    age=person_data[1]
    university=person_data[2].title()
    degree=person_data[3].capitalize()

    print(f"{name} is {age} old studying {degree} at {university}")

sample_csv=",".join(['Rahul','22','MIT','VLSI'])
file_csv=open("csv_data.txt","a")
file_csv.write(f"\n{sample_csv}")
file_csv.close()