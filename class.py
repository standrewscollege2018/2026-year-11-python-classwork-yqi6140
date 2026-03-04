listy = [[[]]]
id = 1
class student:
    def __init__(self,gender,height,name,id):
        self.gender = gender
        self.height = height
        self.name = name
        self.id = id
        listy[self.id - 1][0].append("name")
        listy[self.id - 1][0].append(self.name)
        listy[self.id - 1][0].append("gender")
        listy[self.id - 1][0].append(self.gender)
        listy[self.id - 1][0].append("height")
        listy[self.id - 1][0].append(self.height)
    def get_height(self):
        return self.height
    def get_gender(self):
        return self.gender
listy.append(id)
listy[id] = student("female",1,"John ana",id)
listy.append(id)
listy[id] = student("male",1.5,"Yang",id)
print(listy)
