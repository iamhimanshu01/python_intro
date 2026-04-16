# t1 = ("python","himanshu",16,10.5,True,[1,2,3,5],(0,1,2))
# print(len(t1))
# print(t1)
# #accesing the items of tuple -index
# print(t1[1])
# print(t1[0:2:3])# 2 represent to stop
# print(type(t1))

#to change the list to tuple

# l1 = [1,2,4,89]
# print(l1,type(l1))
# t1 = tuple(l1)
# print(t1)

#tuple to list

# fruits = ('apple',"orange","mango","grapes")
# print(fruits,type(fruits))
# fruits = list(fruits)
# print(fruits, type(fruits))

#concatenation
# student_details1 =(1001,"himanshu")
# student_details2 =(1002,"kumar")
# student_details = student_details1 + student_details2
# print(student_details)

#repeat
# t1 = ('class',100,2000)
# print(t1*4)

#memership operator in / not in
# t1= (12,23,34,56,'himanshu')
# print('himanshu' not in t1)
# print('himanshu'in t1)

t1 = (10,4,6,8,4,9,6,9)
print(min(t1))
print(f"the smallest numbers in t1:{min(t1)}")
print(f"the biggest number is t1:{max(t1)}")