
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print(counter)
print(miles)
print(name)

a = b = c = 1

print(a)
print(b)
print(c)

a,b,c = 1,2,"john"

print(a)
print(b)
print(c)


var_a = 1
var_b = 10


# del var
del var_a, var_b




# print(var)
# print(var_a)
# print(var_b)





print('\n');
str = 'Hello World!'

print(str         ) # Prints complete string
print(str[0]      ) # Prints first character of the string
print(str[2:5]    ) # Prints characters starting from 3rd to 5th
print(str[2:]     ) # Prints string starting from 3rd character
print(str * 2     ) # Prints string two times
print(str + "TEST") # Prints concatenated string




print('\n');
print('list');



list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(list           ) # Prints complete list
print(list[0]        ) # Prints first element of the list
print(list[1:3]      ) # Prints elements starting from 2nd till 3rd 
print(list[2:]       ) # Prints elements starting from 3rd element
print(tinylist * 2   ) # Prints list two times
print(list + tinylist) # Prints concatenated lists



print('\n');
print('tuple');


tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print(tuple            ) # Prints the complete tuple
print(tuple[0]         ) # Prints first element of the tuple
print(tuple[1:3]       ) # Prints elements of the tuple starting from 2nd till 3rd 
print(tuple[2:]        ) # Prints elements of the tuple starting from 3rd element
print(tinytuple * 2    ) # Prints the contents of the tuple twice
print(tuple + tinytuple) # Prints concatenated tuples









tuple = ( 'x', 786 , 2.23, 'john', 70.2  )
list = [ 'y', 786 , 2.23, 'john', 70.2  ]
# tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list

print(tuple);







print('\n');
print('dict');


dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print(dict['one']    ) # Prints value for 'one' key
print(dict[2]        ) # Prints value for 2 key
print(tinydict       ) # Prints complete dictionary
print(tinydict.keys()) # Prints all the keys











