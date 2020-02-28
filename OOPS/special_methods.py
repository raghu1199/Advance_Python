class Club:
    def __init__(self,name):
        self.name=name
        self.players=[]

    def __len__(self):
        return len(self.players)

    def __getitem__(self,item):
        return self.players[item]

    def __repr__(self):
        return f"Club {self.name}: {self.players}"

    def __str__(self):
        return f"Club {self.name} with {len(self)} players"

c = Club("Karnavati")
c.players.append("RAhul")
c.players.append("Raghu")
c.players.append("Milan")
print(c)
print(repr(c))
print(c[1])
for i in c:
    print(i)