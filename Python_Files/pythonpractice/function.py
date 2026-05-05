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
# class ATM:
#     def __init__(self, balance):
#         self.balance = balance

#     def withdraw(self, amount):
#         if amount > self.balance:
#             return "Insufficient funds"
#         else:
#             self.balance -= amount
#             return f"Withdrawal successful. Remaining balance: {self.balance}"
# atm = ATM(100000000000000)
# print(atm.withdraw(200))
# class result:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def grade(self):
#         if self.marks >= 90:
#             return "A"
#         elif self.marks >= 80:
#             return "B"
#         elif self.marks >= 70:
#             return "C"
#         elif self.marks >= 60:
#             return "D"
# #         else:
# #             return "F"
# # # student1 = result("Alice", 10)
# # # print(f"{student1.name} got grade {student1.grade()}")
# # class rectangle:
# #     def __init__(self, length, width):
# #         self.length = length
# #         self.width = width

# #     def area(self):
# #         return self.length * self.width

# #     def perimeter(self):
# #         return 2 * (self.length + self.width)

# # rect = rectangle(10, 200)
# # print(f"Area: {rect.area()}")pi
# # print(f"Perimeter: {rect.perimeter()}")
# # class mobile:
# #     def __init__(self, brand, model):
# #         self.brand = brand
# #         self.model = model

# #     def info(self):
# #         return f"Brand: {self.brand}, Model: {self.model}"

# # phone = mobile("Apple", "iPhone 12")
# # print(phone.info())
# class Bank:
#     def __init__(se
#         self.__balance = 1000  # private

#     def show_balance(self):
#         print(self.__balance)

# b = Bank()
# b.show_balance()