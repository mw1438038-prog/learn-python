# # variable &datatypes
# name="waqas"
# age=19
# price=670.44
# a=True
# print(name)
# # print(type(name)) string type
# print(age) 
# # print(type(age)) int type
# print(price)
# # print(type(price)) float type
# print(a)
# # print(type(a)) bool type

# #           oprators

#     # Arithmetic oprators
# a=20
# b=10
# print(a+b) addition
# print(a-b) subtrection
# print(a/b) division
# print(a//b) floor division
# print(a*b) multiplication
# print(a%b) modulo
# print(a**b) exponent

#     comparison oprators
# a=20
# b=10
# print(a>b) graterthen
# print(a<b) less then
# print(a<=b) less then or equal
# print(a>=b) greater then or equal
# print(a!=b) not equal
# print(a==b) equal
        #  logical oprators
        
# a=20
# b=10
# print(a>10 and b<20) and oprator
# print(a>10 or b<20) or oprator
# print(not(a>10 and b<20)) not oprator

#         assignment oprators
# a=20
# b=10
# print(a+=b) addition assignment
# print(a-=b) subtraction assignment
# print(a*=b) multiplication assignment
# print(a/=b) division assignment
# print(a//=b) floor division assignment
# print(a%=b) modulo assignment
# print(a**=b) exponent assignment
    #   membership oprators
# a=20
# b=10
# list=[1,2,3,4,5,6,7,8,9]
# print(a in list) in oprator
# print(a not in list) not in oprator

    # identity oprators
# a=20
# b=10
# print(a is b) is oprator
# print(a is not b) is not oprator

        #  list
# list=[1,2,3,4,5,6,7,8,9]
# # list.append(10)
# # list.remove(1)
# list.insert(0,1)
# # list.pop()
# # list.reverse()
# # list.sort()
# # list.clear()
# print(list)
    #   Tuple
# tuple=(1,2,2,3,4,5,6,7,8,9)
# tuple.count(2)
# print(tuple)
    #   Set
# set={1,2,3,4,5,6,7,8,9}
# set.add(10)
# set.remove(1)
# set.discard(2)
# set.pop()
# print(set)
#     #   Dictionary
# # dict={'name':'waqas','age':19,'price':670.44}
# dict.items()
# dict.keys()
# dict.values()
# print(dict)
        #  loops
        # for loop
# for i in range(1,11):
#     print(i)
        # while loop
# i=1
# while i<=10:
#     print(i)
#     i+=1
    #   function
# def add(a,b):
#     return a+b
# print(add(10,20))
#   #   lambda function
# add=lambda a,b:a+b
# print(add(10,20))
# def even_odd(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
# print(even_odd(10))
    # scoope of variable
# def func():
#     a=10      local variable
#     print(a)
# func()
#  global variable
# a=20
# def func():
#     print(a)
# func()
# global  function
# a=20
# def func():
#     global a
#     a=30
# func()
# local function
# def func():
#     a=10
# print(a)
# #              file_i_o
# file=open("file.txt","w")
# file.write("Hello, World!")
# file.close()
# with open("file.txt","r") as file:
#     content=file.read()
#     print(content)

    # oops
    # class
    # object
    # inheritance
    # polymorphism
    # encapsulation
    # abstraction
# class Person:s
#         self.name = name
#         self.age = age

#     def introduce(self):
#         return f"Hi, I'm {self.name} and I'm {self.age} years old."
# myintro = Person("mudasir", 19)
# print(myintro.introduce())