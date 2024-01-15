#1. class defination is one time process
class MyClass():
    #1. Property=Variable
    name=''
    surname=''
    age=''

    #2. Constructor=SpecialFunction
    def __init__(self):
        self.name="Vishal"
        self.surname="Mahawar"
        self.age=15

    #3 Function=Method
        #3.1 function defination is one time process
    def myFunction(self):
        print(f'Hello')


#2. create class object is many time process
ceo1=MyClass()

print(ceo1.name)
print(ceo1.surname)
print(ceo1.age)

#3.2 Function calling/invoking is many time process
ceo1.myFunction()