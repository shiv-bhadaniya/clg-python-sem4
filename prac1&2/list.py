a = [2, 2.5, "xyz", 12]
print(a)

print(a[1])

print(a[0: 2])

print(a[1: ])

print(a[ :2])

a.append(3)

print(a)

b = [4,5, 1,2,7,3]

b.insert(2, 6)

print(b)


b.remove(3)

print(b)

b.remove(2)

print(b)

b.pop()

b.pop(0)

print(b)

l1 = [1,4,5,3]

l1.sort()

print("sort : ", l1)

l1.sort(reverse=True)

print(l1)

print(min(l1))

print(max(l1))

mysum = 0

for x in l1:
  mysum += x

print(mysum)

print(sum(l1))

l1.reverse()

print(l1)