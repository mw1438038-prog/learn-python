# # n=int(input('enter your number :'))
# # i=1
# # for i in range(1,11):
# #     if i % 2 == 1:
        
# #           continue
# #     print(f'{n}*{i}={n*i}')
# # i+=1


# # # for i in range(1,11):
# # #     for j in range(1,11):
# # #         print(f'{i} {j} ,{i*j}={i*j}')

# # ==============================
# # 1. Simple Function
# # ==============================

# def add2(x):
#     y = x + 2
#     print("Result:", y)

# add2(2)


# # ==============================
# # 2. *args (Multiple Arguments)
# # ==============================

# def greet(*args):
#     print("All names:", args)
    
#     for name in args:
#         print("Hello", name)

# greet('Samy', 'Mohsin', 'John', 'Bally')


# # ==============================
# # 3. Sum Function using *args
# # ==============================

# def sum_fun(*args):
#     result = 0
#     for x in args:
#         result += x
#     print("Sum:", result)

# sum_fun(1, 2, 3, 4, 5)


# # ==============================
# # 4. Mixed Parameters
# # ==============================

# def greet_mix(name, *args, named_value, **kwargs):
#     print(f'Hello {name}')
    
#     print("Args:", args)
#     for i in args:
#         print(f'Hello {i}')
    
#     print("Named Value:", named_value)
    
#     print("Kwargs:", kwargs)

# greet_mix('Mohsin', 'Ali', 'Ahmed', named_value='Special Name', age=20, city="Lahore")


# =========.=====================
# 5. **kwargs (Dictionary Arguments)
# ==============================

def myfun(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

a = {
    "fname": 'Mohsin',
    "mname": 'John',
    "lname": 'Kally'
}

myfun(**a)


==============================
