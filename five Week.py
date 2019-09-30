#a = 33

#b = 200

#if b > a:
   # print("b is greater than a")

"""a = 33
b = 33

if b>a:
    print("bis greatre than a")
elif a==b:
    print("a and b are equal")"""
"""
a = 2
b = 330

print("A") if a>b  else print("B")
"""
"""
a = 200
b =33
c = 500
if a>b and c>a:
    print("Both conditions are True")
"""
"""
a = 200
b =33
c = 500
if a>b or a>c:
    print("At least one of the conditions is True")
    """
"""
x = 41
if x > 10:
    print("Above ten")
    if x > 20:
        print("Above 20")
    else:
        print("but not above 20")
        """
"""
i = 1
while i < 6:
    print(i)
    i+= 1
"""
""""
i = 1
while i < 6:
    print(i)
    if i ==3:
        break
    i+= 1
"""
"""
i = 0
while i < 6:

    i +=1
    if i ==3:
        continue
    print(i)
"""
"""
i = 1
while i < 10:
    print(i)
    i += 1
else:
    print('i is no longer less than 10')
"""
"""
fruits = ['apple','banana','cherry']
for x in fruits:
    print(x)
"""
'''
fruoits =['apple','banana','cherry']
for x in fruoits:
    print(x)
    if x == "apple":
        break'''

"""
fruoits =['apple','banana','cherry']
for x in fruoits:
    if x == "banana":
        continue
    print(x)
"""
"""
i = 1
while i < 6:
    print(i)
    i += 1
else :
    print("i is no longer less than 6")
    """
"""
for x in range(2,6):
    print(x)
    """
"""
for x in range (6):
    print(x)
else:
    print('Finally')
"""
'''
adj = ["red","big","tasty"]
fruits =['apple','banana','cherry']
for x in adj:
    for y in fruits:
        print(x,y)
   '''
"""
def My_function():

    print('Hello from a function')
My_function()
"""
"""
def my_function(fname):
    print(fname + ' Refsnes')

my_function("Email")

my_function("Tobias")

my_function('Linus')
"""
"""
def my_function(country = "KSA"):
    print("iam from " +country)
my_function("Bhrain")
my_function("UAE")
my_function()
"""
"""
for A in range(3,17) :
    for B in range(2,16):
        print(A,B)
"""
''' week 6th '''
'''
def my_function (food):
    for x in food:
        print(x)

fruits =['apple','banana','cherry']
my_function(fruits)
'''
"""
def my_function(x):
    return 5 * x

print(my_function(5))
print(my_function(3))
"""
"""
def my_function(*kids):
    print('The yougest child is ' + kids[2])
my_function('Emil','Tobias','Mishary')
"""
def tri_recursion(k):
    if (k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print('\n\n Recursion Example Results')
tri_recursion(6)
