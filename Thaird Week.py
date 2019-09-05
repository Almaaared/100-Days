Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> number = [1,2,3,4]
>>> print (number)
[1, 2, 3, 4]
>>> thislist =['apple','banana','cherry']
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> list=['Apple','Banana','Cherry']
>>> print (list[2])
Cherry
>>> my_list = ['apple','banana','cherry']
>>> my_list[0]='blackcurrant'
>>> print(my_list)
['blackcurrant', 'banana', 'cherry']
>>> my_list = ['apple','banana','cherry']
>>> del my_list[1]
>>> print(my_list)
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> my_list = ['apple','banana','cherry']
>>> del my_list[1]
>>> print (my_list)
['apple', 'cherry']
>>> my_list = ['a','b','c','d']
>>> print(my_list[1:3])
['b', 'c']
>>> lists=['apple','banana','cherry']
>>> if'apple' in lists :
	print('yes, 'apple' is in the fruite list')
	
SyntaxError: invalid syntax
>>>  lists=['apple','banana','cherry']
 
SyntaxError: unexpected indent
>>> lists=['apple','banana','cherry']
>>> if 'apple' in lists:
	print ('yes, 'apple' in the frutes list')
	
SyntaxError: invalid syntax
>>>  lists=['apple','banana','cherry']
 
SyntaxError: unexpected indent
>>> lists=['apple','banana','cherry']
>>> if 'apple' in lists:
print ('yes, "apple" in the frutes list')
SyntaxError: expected an indented block
>>> lists=['apple','banana','cherry']
>>> if 'apple' in lists:
print('yes, "apple" in the frutes list')
SyntaxError: expected an indented block
>>> lists=['apple','banana','cherry']
>>> if 'apple' in lists:
	print('yes, "apple" in the frutes list')

	
yes, "apple" in the frutes list
>>> lists1['Ahmed','Mohii','Ali']
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    lists1['Ahmed','Mohii','Ali']
NameError: name 'lists1' is not defined
>>> lists 1=['Ahmed','Mohii','Ali']
SyntaxError: invalid syntax
>>> my_lists 1 =['Ahmed','Mohii','Ali']
SyntaxError: invalid syntax
>>> My_lists1 =['Ahmed','Mohii','Ali']
>>> my_lists2 =["sara","Hind","Arwa"]
>>> my_lists3 = My_lists1 + my_lists2
>>> print(my_lists3)
['Ahmed', 'Mohii', 'Ali', 'sara', 'Hind', 'Arwa']
>>> this_list=['apple','banana','cherry']
>>> this_list.append('orange')
>>> print(this_list)
['apple', 'banana', 'cherry', 'orange']
>>> this_list=['apple','banana','cherry']
>>> this_list.insert(1,'orange')
>>> print(this_list)
['apple', 'orange', 'banana', 'cherry']
>>> my_list['apple','orange','cherry']
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    my_list['apple','orange','cherry']
TypeError: list indices must be integers or slices, not tuple
>>> my_list= ['apple','orange','cherry']
>>> my_list.remove('orange')
>>> print(my_list)
['apple', 'cherry']
>>> lists =['wlecome enytime','enyday']
>>> my_list=lists.copy()
>>> print(my_list)
['wlecome enytime', 'enyday']
>>> list_tuple =('apple','banana','cherry')
>>> for x in list_tuple:
	print(x)

	
apple
banana
cherry
>>> 
>>> my_list=('apple','orange','mango')
>>> print(len(my_list))
3
>>> listis=[3,4,5,6]
>>> my_list= tuple(listis)
>>> print(my_list)
(3, 4, 5, 6)
>>> 
