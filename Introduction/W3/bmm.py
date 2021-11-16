import datetime

def intersection_list(a, b):
    result = []
    for elm in a:
        if elm in b and elm not in result:
            result.append(elm)
    return result

a = [2, 4, 5, 6, 3, 4, 6, 7, 8, 9]
b = [2, 4, 3, 2, 3, 4, 6, 12]

print(intersection_list(a, b))

def bmm_maskhare(a , b):
    a_devisor = set()
    b_devisor = set()
    for i in range(1, a+1):
        if not a % i:
            a_devisor.add(i)
    

    for i in range(1, b+1):
        if not b % i:
            b_devisor.add(i)
    
    return max(a_devisor.intersection(b_devisor))


def bmm_Saman(a, b):
    temp = min(a, b)
    result = 1

    for i in range(1, temp+1):
        if not a % i and not b % i:
            result = i

    return result

def bmm_fisaghoresi_ham(a, b):
    if a < b: 
        a, b = b, a

    while b:
        a, b = b, a%b
    
    return a

print(bmm_fisaghoresi_ham(12, 34))