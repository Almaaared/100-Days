'''class myclass:
    x=5
print (myclass)
'''
'''
class myclass:
    x=5
p1 = myclass()
print(p1.x)
'''
'''
class person:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    


p1 = person('Jone',36)
print(p1.name)
print(p1.age)
'''
"""
class person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("Hello my name is "+abc.name)
p1 = person("Jone", 36)
p1.myfunc()
"""
'''
myster = 'banana'
myit = iter(myster)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
'''
'''
myltuple = ('apple','banana','cherry')
for x in myltuple:
    print(x)
'''
'''
class MyNumb:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a +=1
        return x
myclass = MyNumb()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
'''
'''
class MyNumb:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a +=1
            return x
        else:
            raise stopIteration
myclass = MyNumb()
myiter = iter(myclass)
for x in myiter:
    print(x)
    '''
class Library:
    def __init__(self,book,shelf):
        self.n1 = number
        self.n2 = number
    def student(self):
        print(self.n1,self.n2)
class student (Library):
    pass
x = student(300,45)
x.

