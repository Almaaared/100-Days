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
class person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("Hello my name is "+abc.name)
p1 = person("Jone", 36)
p1.myfunc()


