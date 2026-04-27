# 6. Scope of Function
# ==============================

# Global Scope
# x = 5

# def test_global():
#     print("Global x:", x)

# test_global()


# # Local Scope
# def test_local():
#     y = 10
#     print("Local y:", y)

# # test_local()

# # Global Scope
# x = 1
# def fun():
#    # Local Scope
#    # global x
#    # x = 1
#    def fun2():
#       print(x)
#    fun2()
 
 
# Global Exercise
 
 
# clothes = 'dirty_clothes'
 
# def washingmachine(cleanclothes):
#    global clothes
#    clothes = cleanclothes
#    print(clothes)
 
# print(clothes)
# washingmachine('Clean clothes')
# print(clothes)
# # fun()
 
# # Non Local Key word
# global scope
# def fun1():
#    # enclosing function/scope
#    def fun2():
#       # neseted function
#       # local scope
#       print(2)
#    fun2()
#    print(1)
# fun1()
# ************************************
# # Exercise non local
 
# #
# def fun1():
# 	def fun2():
# 		print(1)
# 	fun2()
# 	print(2)
# fun1
# print(x
# # # print(y)  # ❌ Error (outside access not allowe)