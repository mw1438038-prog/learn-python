# from comp import list_s
 
# print(list_s)
# import random
# import datetime
# import timeit
 
# print('-'.join(str(n) for n in range(10000)))
# print(timeit.timeit("'-'.join(str(n) for n in range(100))",number=10000))
 
 
# # x = random.randint(1,10)
# # print(x)
# #
# # date = datetime.datetime.now()
# # print(date)
# #
# #
# # dob = datetime.date(1991,3,11)
# #
# # today = datetime.date.today()
# # age = today-dob
# # print(age)
from typing import Generator


# Generator

#
# import sys
# # Generators
# def my_gen(n:int):
#  start  = 0
#  while start < n:
#     print(f'My_range is returning:{start}')
#     yield start
#     start += 1
# gen_list = my_gen(10)
# print(next(gen_list))
# print(next(gen_list))
# print(next(gen_list))
# print(f'This generator takes {sys.getsizeof(gen_list)} bytes')
#
# print('x'*20)
# itr_list = []
# for val in gen_list:
#  itr_list.append(val)
#
# print(f'This Normal list takes {sys.getsizeof(itr_list)} bytes')
#
#
# print('x'*20)
# itr_list = []
# for val in gen_list:
#  itr_list.append(val)
#
# print(f'This Normal list takes {sys.getsizeof(itr_list)} bytes')
#
# print(itr_list)