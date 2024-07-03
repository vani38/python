class person:
    name="Vani"
    gender="female"
    def __init__(self,qualification,age):
        self.qualification=qualification
        self.age=age
P1=person("M.com",30)
P2=person("MCA",34)
print(P1.name,P1.age,P1.qualification)
print(P2.name,P2.age,P2.qualification)
#if we change the class attribute name vani to ramesh
person.name="Ramesh"
print(P1.name,P1.age,P1.qualification)
print(P2.name,P2.age,P2.qualification)
