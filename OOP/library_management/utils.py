from typing import Counter, Iterator


def hello_yield():
    count = 0

    while count < 10:
        count += 1
        yield count
    yield "bye"





a = hello_yield()

for elm in a:
    print(elm)
    if elm == 4:
        break

print("salam")

try:
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
except StopIteration:
    print('payan')