
myList1 = [3,1,77,69,30,40,3,8,24,37,112,46]  # Create list
print("List : ", myList1)

myList1.append(55)  # apply append method
print("After appending : ", myList1)

myList2 = [10,20,1,3,4]
myList1.extend(myList2)  # apply extend
print("After extend : ", myList1)

myList1.remove(112)  # remove one value from list
print("After remove 112 from list : ", myList1)

myList1.reverse()  # reverse a list
print("After reverse list : ", myList1)