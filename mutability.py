immutable_obj = ['a', 'b', 'c', 'd'] #list

immutable_obj[2] = 'x'

#print(immutable_obj)

#dictionary
immutable_dict= {"first": "ananth", 'second': "radha", "1":"chaitra", 'fourth':"sukruth"}

#print(immutable_dict["fourth"])

a= ["first", "second", "third"]

#print(a)

#frozenset
a= frozenset(a)

#a[1] = "fourth"

#print(a)

# string is immutable


b = "how are you?"



#b[1] = 'm'

#print(b[1])


# aliases creation for mutable and immutable

lst = ['1','2', '3']

x = lst

x.append('4')

print(lst)

# string doesn't create aliases

strng = "period"

x = strng

x = x + 's'

print('x: ', x, 'while strng: ',strng)

# copy list using [:]

x =[1,2,3,4]

z = x

y = x[:]

y.append(5)

#print(x, y)


# is operator allows you to compare locations in memory

print(x is z, "id of x, y, z", id(x), id(y), id(z))