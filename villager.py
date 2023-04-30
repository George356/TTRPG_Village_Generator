
class villager:
    def __init__(self,id,name,gender,age,spouse,children,profession,money,house):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.spouse = spouse
        self.children = children
        self.profession = profession
        self.money = money
        self.house = house

    def __init__(self):
        self.name = None
        self.age = 0
        self.spouse = 0
        self.children = None
        self.profession = None

class proffession:
    def __init__(self,name,wealth):
        pass   