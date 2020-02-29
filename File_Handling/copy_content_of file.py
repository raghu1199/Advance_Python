friends=input("Enter Friend name separated  by comma:").split(",")

people=open("people.txt","r")
people_nearby=[line.strip() for line in people.readlines()]
people.close()

friends_set=set(friends)
people_set=set(people_nearby)

friends_nearby=friends_set.intersection(people_set)

nearby_friends_file=open("nearby_friends.txt","w")

for friend in friends_nearby:
    print(f"{friend } is nearby")
    nearby_friends_file.write(f"{friend}\n")

nearby_friends_file.close()