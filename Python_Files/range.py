# Range: To Create Automatic Lists
#
# my_list = [1,2,3,4,5,6,7,8,9]
# odd = [1,3,5,7,9]
# even = [2,4,6,8,10]
# print(my_list)
# print(odd)
# print(even)
#
# print(list(range(1,1000)))
# even = list(range(0,1000,2))
# odd = list(range(1,1000,2))
# print(even)
# print(odd)
# print(even[334])
# print(odd[420])
#
# print(odd.index(841))
 
 
# print(list(range(1,10)))
# even = list(range(0,10,2))
# odd = list(range(1,10,2))
# print(even)
# print(odd)
 
 
 
list_seven = range(17,100000,17)
num = int(input('Please enter your number:'))
print(f'{num} does exit in list:{num in list_seven}')
 