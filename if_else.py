# # ==============================
# # 1. Simple IF-ELSE
# # ==============================
# x = int(input('Enter a number: '))

# if x > 2:
#     print('Number is greater than 2')
# else:
#     print('Number is 2 or less')


# # ==============================
# # 2. IF-ELIF-ELSE
# # ==============================
# sound = input('Enter sound (meo/wuf): ')

# if sound == 'meo':
#     print('You love cats')
# elif sound == 'wuf':
#     print('You love dogs')
# else:
#     print('Unknown sound')


# # ==============================
# # 3. Nested IF
# # ==============================
# x_dir = input('Enter direction (Right/Left): ')
# y_dir = input('Enter direction (Up/Down): ')

# if x_dir == 'Right':
#     if y_dir == 'Up':
#         print('You are going Right and Up')
#     else:
#         print('You are going Right but not Up')
# else:
#     print('You are going somewhere else')


# # ==============================
# # 4. Logical Operators
# # ==============================
# num = int(input('Enter a number: '))

# if num > 5 or num < 10:
#     print('Number is in range')


# # ==============================
# # 5. Membership Operator
# # ==============================
# sentence = 'A quick brown fox jumps over the lazy dog'
# word = input('Enter word to search: ')

# if word in sentence:
#     print('Word exists in sentence')
# else:
#     print('Word not found')


# # ==============================
# # 6. FOR LOOP + CONTINUE + BREAK
# # ==============================
# print("Loop Example:")

# for i in range(10):
#     if i == 3:
#         continue   # skip 3
#     if i == 7:
#         break      # stop at 7
# #     print(i)


# # # ==============================
# # # 7. STRING LOOP
# # # ==============================
# # for ch in "string":
# #     if ch == 'i':
# #         break
# #     print(ch)


# # # ==============================
# # # 8. LIST LOOP
# # # ==============================
# # grocery_list = ['milk','pasta','eggs','cheez','bread']

# # for item in grocery_list:
# #     if item == 'cheez':
# #         print('I dont buy ' + item)
# #         continue
# #     print('I buy ' + item)


# # # ==============================
# # # 9. PRIME NUMBER CHECK
# # # ==============================
# # num = int(input('Enter number to check prime: '))

# # if num > 1:
# #     for i in range(2, num):
# #         if num % i == 0:
# #             print('Not Prime')
# #             break
# #     else:
# #         print('Prime Number')
# # else:
# #     print('Not Prime')


# # # ==============================
# # # 10. WORD COUNTER
# # # ==============================
# # article = "Python is easy and powerful"

# # count = 1
# # for char in article:
# #     if char == ' ':
# # #         count += 1

# # # print('Total words:', count)


# # # # ==============================
# # # # 11. DATA CLEANING
# # # # ==============================
# # # ip = "23112,32154,564,897"

# # # clean_num = ''

# # # for ch in ip:
# # #     if ch in '0123456789':
# # #         clean_num += 
# # # #     print('Empty list is False')

# # def fib(n):
# #     if n<2:
# #         return n
# #     else:
# #         return fib(n-1)+fib(n-2)

# # for i in range(10):
# #         print(i , fib(i))
        
        
# # # import os
# # # list_=os.walk('lear-python')
        

# # # from datetime import datetime
# # # print(datetime.now())

# # # import os
# # # print(os.listdir())

# # # import os
# # # print(os.getcwd())

# # # import os
# # # list_os=os.walk("D:\\Coding\python\\learn-python")

# # # for root,direct,files in list_os:
# # #     print(root)
    
# # #     for i in direct:
# # #         print(i)
        
# # #     for j in files:
        
# # #             print(j)
            
                
# # import os
# # import shutil

# # # folder path
# # path = 

# # # files list
# # files = os.listdir(path)

# # # extension dictionary
# # file_types = {
# #     ".txt": "Text_Files",
# #     ".jpg": "Images",
# #     ".png": "Images",
# #     ".py": "Python_Files"
# # }

# # for file in files:
# #     file_path = os.path.join(path, file)

# #     # skip folders
# #     if os.path.isdir(file_path):
# #         continue

# #     # extension nikalna
# #     ext = os.path.splitext(file)[1]

# #     # folder decide karna
# #     folder_name = file_types.get(ext, "Others")

# #     folder_path = os.path.join(path, folder_name)

# #     # folder create karna agar na ho
# #     if not os.path.exists(folder_path):
# #         os.mkdir(folder_path)

# #     # file move karna
# #     shutil.move(file_path, os.path.join(folder_path, file))

# # print("Files Organized Successfully 👍")
# import os
# import shutil

# # folder path
# path = "D:\\Coding\python\\learn-python"

# # files list
# files = os.listdir(path)

# # extension dictionary
# file_types = {
#     ".txt": "Text_Files",
#     ".jpg": "Images",
#     ".png": "Images",
#     ".py": "Python_Files"
# }

# for file in files:
#     file_path = os.path.join(path, file)

#     # skip folders
#     if os.path.isdir(file_path):
#         continue

#     # extension nikalna
#     ext = os.path.splitext(file)[1]

#     # folder decide karna
#     folder_name = file_types.get(ext, "Others")

#     folder_path = os.path.join(path, folder_name)

#     # folder create karna agar na ho
#     if not os.path.exists(folder_path):
#         os.mkdir(folder_path)

#     # file move karna
#     shutil.move(file_path, os.path.join(folder_path, file))

# print("Files Organized Successfully 👍")