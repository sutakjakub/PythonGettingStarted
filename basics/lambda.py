from os import name


people = [
    {"name": "harry", "house": "gryffindor"},
    {"name": "cho", "house": "ravenclaw"},
    {"name": "draco", "house": "slytherin"}
]

#def f(person):
#    return person["name"]

people.sort(key=lambda person: person["name"])

print(people)
