class person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    
def myfunc(self):
    print("Hello my name is"+self.name)
p1=person("kanchan",20)
print(p1.myfunc())  