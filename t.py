class person():
    def __init__(self,sex,age):
        self.age = age
        self.sex = sex
    def getAge(self):
        print("Age = %d"%(self.age))
    def getSex(Self):
        print("Sex = %s"%(self.sex))

class Male(person):
    self.oi = 'oi'
    def oi(self):
        print(self.oi)

lucas =  person('m',19)
lucas = Male('m')
lucas.getAge()
lucas.oi()