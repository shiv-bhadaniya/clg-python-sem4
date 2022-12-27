list = [1,42,2,8,33,5]

list2 = list[0:]
list3 = list[slice(len(list))]

print(list3)