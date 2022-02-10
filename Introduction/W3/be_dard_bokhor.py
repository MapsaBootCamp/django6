from functools import reduce


LOG_LEVEL_NAME = ("ERROR", "WARNING", "INFO", "DEBUG", "A")
LOG_LEVEL_CODE = (40, 30, 20, 10)


### ZIP
for elm in zip(LOG_LEVEL_NAME, LOG_LEVEL_CODE):
    print(elm)


### MAP
def maskhare(item1):
    return 2 * item1

# map_object = map(maskhare, [2, 3, 4, 5])
map_object = map(lambda x : 2 * x, [2, 3, 4, 5])
list_cast_map_object = list(map_object)
print(list_cast_map_object)



# FILTER
print(tuple(filter(lambda x :  x % 2, [2, 3, 4, 5, 6, 7])))

# b = (lambda x, y: x + y)("salam", " ashkan")
# print(b)


# REDUCE
print("##################################################### Reducer")
def maskhareSholagh(item1 , item2):
    print("item1: ", item1)
    print("item2: ", item2)
    return item1 + item2

print(reduce(maskhareSholagh, {1, 2, 3, 4, 5, 6}))

factorial_number = 10

# print(reduce(lambda x, y: x*y, range(1, factorial_number+1)))
# print(reduce(lambda x, y: x*y, [1, 2, 3, 4]))


print("##################################################### Reducer")


# difference between is and ==
a = ["a", 2]
b = ["a", 2]

# a = 2
# b = 2

if a is b:
    print("a va b yejaye hafezan")
elif a == b : 
    print("a va b maghadir yeksan darand ama jahashun fargh dare")
else:
    print("a va b kolan fargh darand")


### unpack
a = ("abcf", 21,"mamad" , 22)
def f(arg1, arg2, arg3):
    print("arg1", arg1)
    print("arg2", arg2)
    print("arg3", arg3)


# f(a[0], a[1], a[2])
# f(*a)
d, *b , c = a

print(b)
print(c)

def g(name="a", age=23):
    print(name, age)

my_dict = {"name": "ashkan", "age": 18}

g(**my_dict)