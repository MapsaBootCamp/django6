import math
import numpy as np


# data structure
my_string = "Ashkan" #immutable
my_string_2 = "Ashkan"
my_string_3 = my_string_2 + "a"

my_list = ["a", 434] # mutable, indexable
print(id(my_list))
my_list.append(12)
print(id(my_list))
my_list_2 = ["a", 434]


my_array = np.array(["ashkan", 23])


my_tuple = ("a", 434) # immutable, indexable
my_tuple_2 = ("a", 434)
my_tuple_3 = my_tuple

# list_falsafi = ["a"]
# tuple_falsafi = (1, list_falsafi)
# print(tuple_falsafi)
# print(id(tuple_falsafi))
# list_falsafi.append(12)
# print(tuple_falsafi)
# print(id(tuple_falsafi))

# my_list.extend(my_tuple)


# print(id(my_string))
# print(id(my_string_2))
# print(id(my_string_3))


# print(id(my_list))
# print(id(my_list_2))

# print(id(my_tuple))
# print(id(my_tuple_2))
# print(id(my_tuple_3))
# print(id(my_list[-1]))


my_set = {"a", "a", ("a",), ("a",)} # unidexable, unordered, mutable


set_is_unordered = {"a", 2, 3, 4, "a"}


# print(set_is_unordered)
# print(len(my_set))


list_ununique_data = ["a", 12, "a"]

# print(list(set(list_ununique_data)))



my_dictionary = {"name": "ashkan", "age": 12}
dictionary_messed_up = {"a": 12, "hashable": "value harchi"}



print(my_dictionary["name"])
print(my_dictionary.get("nama", "ghasemGholi"))


for elm in ["a", "b", 12]:
    print(elm)
    if elm == "b":
        # break
        continue
    print("salama")
    
count = 0
while count < 5:
    print(count)
    count += 1
#     break
# else:
#     print("salam ali")


extra_prirority = []

for elm in ["tahsilat", "rang mored alaghe"]:
    temp = input(f"{elm}: ")
    extra_prirority.append(temp)

print(extra_prirority)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
shoghlesh = input("Enter your shoghlesh: ")
ghad = input("Ghaded chandeh: ")
PERSONALITY = ["D", "I", "S", "C"]
personality_type = input("Enter your type: (D, I, S, C)")



if personality_type not in PERSONALITY:
    print("baghali tavajoh kon, shab bekheir")
    exit()




if shoghlesh == "programmer":
    daramad = 10
elif shoghlesh == "pezeshk":
    daramad = 100
elif shoghlesh == "aghazadeh":
    daramad = float("inf")
else:
    daramad = 5

# camelCase   shartEzdevaj
# PascalCase  ShartEzdevaj


shart_ezdevaj = 2 * age ** 2 + age + age ** 0.5 - 12

if shart_ezdevaj < 3000 and personality_type != "D":
    adad_disc = input("adad disc ro begu: (4 ragham!!)")
    if len(adad_disc) != 4:
        print("boro dars bekhun, shab bekheir")
        exit()
    if int(adad_disc[1]) >= 5:
        if int(adad_disc[3]) < 5:
            print("boro khosh begfzarun ma be dard ham nemikhorim, shab belheir")
            exit()
    if 3 * 2 ** 3 ** math.sqrt(ghad) > 8 * 195 :
        print("yes!")
    elif daramad > 15:
        print("ghadet nemirese, vali pulet mireseh")
    else:
        print("hichit nemireseh(sen mohem ni), shab bekheir")
else:
    print("baraye man pir shodi, shab bekheir!!")


print(type(name))

print(f"hello {name} {age} sale")
# print("hello", name)
# print("hello " + name)






#TODO: chegune int mifahme string numericable hast???