
user_name=input("Enter ur name:")
my_file=open("data.txt","a")
my_file.write(user_name)
my_file.close()

my_file_r=open("data.txt","r")
file_content=my_file_r.read()
my_file_r.close()

print(file_content)