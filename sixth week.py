'''def my_function (child3,child2,child1):
    print('The youngest child is '+ child3)
my_function(child1='Emil',child2='Tobise',child3='Linus')
'''
'''def tri_recursion (k):
    if (k>0):
        result = k+ tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print('/n/nRecursion Example Results')
tri_recursion(6)
'''
'''x = lambda a : a + 10
print(x(5))
x = lambda a,b : a*b
print(x(5,6))
'''
'''def myfunc(n):
    return lambda a : a*n
mydoubler = myfunc(2)
print(mydoubler(11))
'''
'''cars = ['Ford','Volvo','BMW']
x = cars [1]
print(x)
cars = ['Ford','Volvo','BMW']
cars [1] = 'Toyota'
print(cars)
cars = ['Ford','Volvo','BMW']
x = len (cars)
print(x)
cars = ['Ford','Volvo','BMW']
for x in cars:
    print(x)
cars = ['Ford','Volvo','BMW']
cars.append('Honda')
print(cars)
cars= ['Ford','Volvo','BMW']
cars.remove('Ford')
print(cars)'''
'''def az_recursion(k):
    if (k=5):
    result = k+az_recursion(k^3)
    print(result)
    
az_recursion(5)'''
'''x = lambda 88,9,7,3,2,-1,-5,-6,-4: x>0
print(x)'''