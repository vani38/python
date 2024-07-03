#instance attributes
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
pet=dog("cutie",2)
print(pet.name)
print(pet.age)



#class attributes
class dog:
    species="canis familiaries"
    def __init__(self,name,age):
        self.name=name
        self.age=age
print(dog.species)
