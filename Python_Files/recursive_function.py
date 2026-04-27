# def fact_fun(n):
#     result = 1
#     for n in range(2,n+1):
#         result*= n
#         return result

# # #     print(fact_fun(5))
   
# # def factorial(n):
# #     result = 1
    
# #     for i in range(1, n+1):
# #         result = result * i
        
# #     return result


# # num = 12
# # print("Factorial:", factorial(num))
# Calculate Factorial: Recursive
# print('x'*20)
# def recursivefun(n):
#    if n <= 1:
#       return 1
#    else:
#       a = n*recursivefun(n-1)
#       return a
 
# for i in range(1,10):
#    print(i,recursivefun(i)
n=int(input('enter your number :'))
for i in range(n,0,-1):
    print('*'* i)