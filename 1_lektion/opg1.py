d1 = {
    "name": "Alice",
    "birth_year": 1997,
    "height": 171,
    "residence": "Vodskov",
    "uses_glasses": False,
}

d2 = {
    "name": "Bob",
    "birth_year": None,
    "height": 180,
    "residence": "Aalborg",
    "uses_glasses": True,
}

print(d1["birth_year"])
print(d2["residence"])
print(len(d1))
print("-"*20)
print(len(d2))

d2["height"] = 190

for key in d1:
    print(key, d1[key])

for key in d2:
    print(key, d2[key])

