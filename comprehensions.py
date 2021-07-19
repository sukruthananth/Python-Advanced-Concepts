nums = [1,2,3,4,5,6,7,8,9,10]


list_n = [n for n in nums if n%2 ==0]


list_n =[(letter,n) for letter in 'abcd' for n in range(4)]


place_name = ['Adoni', 'tumkur', 'chennai', 'trichi']

state_name = ['andhra', 'karnataka','tamil nadu', 'kerela']

# print(tuple(zip(place_name, state_name)))

my_dict = {}

# print(place_name, state_name)

for place_name1, state_name1 in zip(place_name, state_name):
    my_dict[place_name1] = state_name1
# print(my_dict)

# print(place_name, state_name)
my_dict = {place_name: state_name for place_name, state_name in zip(place_name, state_name) if place_name!='Adoni'}

# print(my_dict)



list_n = [1,1,1,2,2,3,4,4,5,4,6,7]

# set_n = set(list_n)

#

set_n = {n for n in list_n}

# print(set_n)


#generators

def gen_fun(num):
    for i in num:
        yield i*i

a = gen_fun([1,2,3,4,5])

# print(a)

# for i in a:
#     print(i)
# genererator comprehension
num = [1,2,3,4,5]

gen_a = (n*n for n in num)

# for i in gen_a:
#     print(i)
#
x = 5

y= 4

b =lambda x,y:x if x>y else y

# print(b(x,y))

n = [50]

# print(list(map(lambda x:x*x, n)))

n= [1,2,3,4,5,6]

from functools import reduce

# print(reduce(lambda x,y:x+y,n))


# def fun_ow(*args, **kwargs):
#     if args:
#         print(args)
#     print("ey there")
#
#     print(kwargs)
#
# fun_ow('abc','def','fgh', a = "bed", b="cot", c="not")

# fun_ow('abc','def','fgh')
#
def fun_owl(x,y):
    print(x+y)

b = {'x':'how are ','y':'you'}

a= [1,2]

fun_owl(*a) #**b