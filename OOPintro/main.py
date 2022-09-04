class Person:
    species = "human"#Class variable, these are attributes that are shared by all the objects..
    def __init__(self, name, age):
        #Instance Variables, these are unique for every instance(object) created from the class..
        self.name = name
        self.age = age
    def greet(self):#Method, this is also shared by all the objects...
        print("Hello, " + self.name + ".")

    def getSex(self, sex): #Ordinary method, to instantiate instance variables..
        self.sex = sex
    
    def putSex(self, )

if __name__ == '__main__':
    p1 = Person("Uday", 20)
    print(p1.name + "\t" + str(p1.age) + "\t" + p1.species)
    p1.greet()

    p2 = Person("Ramya", 21)
    print(p2.name + "\t" + str(p2.age) + "\t" + p2.species)
    p2.greet()
