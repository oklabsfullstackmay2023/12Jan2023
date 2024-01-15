#1 class defination is one time process
class MyClass():
       #1. Property=Variable
    name=""
    surname=""
    age=""
    address=""
    schoolname=""
    schooladdress=""

    #2. Constructor=SpecialFunction
    def __init__(self):
        self.name="Vishal"
        self.surname="Mahawar"
        self.age=15
        self.address="Neemuch"
        self.schoolname="Alpha English H.S. School"
        self.schooladdress="Near Opium Factory, Station Road,Neemuch"

        #3 Method=Function
        #3.1 function defination is one time proces
    def myFunction(self):
        print(f'hello')
        pass

#2 create class object is many time process
ceo1=MyClass()

print(ceo1.name)
print(ceo1.surname)
print(ceo1.age)
print(ceo1.address)
print(ceo1.schoolname)
print(ceo1.schooladdress)

#3.2 Function calling/invoking is many time process
ceo1.myFunction()