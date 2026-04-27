
#
# file = open('newfile.txt','r')
# for line in file:
#  if 'python' in line.lower():
#     print(line,end="")
# file.close()
# print('x'*20)
# with open('newfile.txt','r') as file:
#  for line in file:
#     if 'python' in line.lower():
#        print(line,end="")
# print('x'*20)
# with open('newfile.txt','r') as file:
#  line = file.readline()
#  while line:
#     print(line,end="")
#     line= file.readline()
# read
# readlines
 
# with open('newfile.txt','r') as file:
#  lines_list = file.readlines()
#
# print(lines_list)
#
# for line in lines_list[::-1]:
#  print(line, end='')
# print('x'*20)
#
# with open('newfile.txt','r') as file:
#  characters = file.read()
#  print(characters)
# for char in characters[::-1]:
#  print(char, end='')
# print('x'*20)
 
# writing files
# bucket = ['Apple','Banana','Orange']
#
# with open('newbucket.txt','w') as tem_bucket:
#  for fruit in bucket:
#     print(fruit,file=tem_bucket)
# Append files
 
# with open('newbucket.txt','a') as tem_bucket:
#    for i in range(1,10):
#       for j in range(1,10):
#          print(f'{j} times {i} is equal {j*i}',file=tem_bucket)
#       print('x'*20, file=tem_bucket)
def fac_fun()
result=1
for i in range(1,n+1):
    result=result*n
    return result
    for i in range(n)
    print(i ,fact_fun(i))
fact_fun(5)