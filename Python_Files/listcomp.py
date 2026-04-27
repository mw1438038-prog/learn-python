# # # List Comprehension
# #
# # num = [1,2,3,4,5,6,7,8,9]
# # sqr_num1 = []
# # for x in num:
# #  sqr_num1.append(x**2)
# # print(sqr_num1)
# #
# # print('x'*20)
# #
# #
# # sqr_num2 = [x**2 for x in num]
# #
# #
# #
# # print(sqr_num2)
 
 
# # name = []
# # for letter in 'Mohsin':
# #  name.append(letter)
# # print(name)
 
# # name = [letter for letter in 'Mohsin']
# #
# # print(name)
 
# # Conditional In list Compreehension
 
 
# # even = []
# #
# # for x in range(10):
# #  if x%2==0:
# #     even.append(x)
# #
# # print(even)
 
# # List COmp with conditional
 
# # even = [x**2 for x in range(10) if x%2==0]
# #
# #
# #
# # print(even)

# # Nested For in List Comprehension
# #
# # my_list = []
# #
# # for x in[2, 4, 6]:
# #  for y in [1, 3, 5]:
# #     my_list.append(x*y)
# #
# # print(my_list)
# #
# #
# #
# #
# # my_list = [x*y for x in[2, 4, 6] for y in [1, 3, 5] if x*y !=10 if x*y !=20 ]
# # print(my_list)
# list_ = [['A','B','C'],['D','E','F'],['G','H','I']]
 
# list_s = []
 
# for letter in list_:
#    if 'G' not in letter:
#       list_s.append(letter)
#    else:
#       list_s.append('Letter was skipped')
 
# print(list_s)
# print('X'*20)
 
# list_sc = [letter for letter in list_ if 'G' not in letter ]
# print(list_sc)
 
 
# print('X'*20)
 
# list_scx = [letter if 'G' not in letter else 'Letter was skipped' for letter in list_ ]
# print(list_scx)


