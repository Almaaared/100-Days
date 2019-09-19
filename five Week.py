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
fruoits =['apple','banana','cherry']
for x in fruoits:
    if x == "banana":
        continue
    print(x)