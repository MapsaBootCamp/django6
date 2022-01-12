


a = [{"name": "ashkan", "age": 18}, {"name": "as", "age": 12}]


for elm in a:
    if elm["name"] == "as":
        elm["age"] += 12

print(a)