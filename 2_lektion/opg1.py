t = range(10)
list_1 = [i+1 for i in t]
print(list_1)

list_2 = [i for i in range(20) if i % 2 == 0]
print(list_2)

list_3 = [i for i in range(20) if i % 2 != 0]
print(list_3)

list_4 = ['Bla '*i for i in t]
print(list_4)
