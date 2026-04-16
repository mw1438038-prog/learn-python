# # ================================
# # 📘 PYTHON DICTIONARY COMPLETE GUIDE
# # ================================


# # 🔹 1. Dictionary Creation
# car = {
#     "model": "suzuki",
#     "year": 2006,
#     "color": "black"
# }

# print("\n--- 1. Dictionary Creation ---")
# print(car)


# # 🔹 2. Access Values using Keys
# print("\n--- 2. Access Values ---")
# print(car["model"])
# print(car["color"])


# # 🔹 3. Nested Dictionary
# car_nested = {
#     "model": "suzuki",
#     "docs": {
#         "original": "yes",
#         "duplicate": "no"
#     }
# }

# print("\n--- 3. Nested Dictionary ---")
# print(car_nested["docs"]["original"])


# # 🔹 4. Update Dictionary
# car_update = {
#     "model": "suzuki",
#     "year": 2006
# }

# car_update["model"] = "toyota"
# car_update["tyers"] = "No"

# print("\n--- 4. Update Dictionary ---")
# print(car_update)


# # 🔹 5. keys(), values(), items()
# car_methods = {
#     "model": "suzuki",
#     "year": 2006,
#     "color": "black"
# }

# print("\n--- 5. Dictionary Methods ---")
# print("Keys:", car_methods.keys())
# print("Values:", car_methods.values())
# print("Items:", car_methods.items())


# # 🔹 6. pop() and popitem()
# car_remove = {
#     "model": "suzuki",
#     "year": 2006,
#     "color": "black"
# }

# print("\n--- 6. pop() Example ---")
# car_remove.pop("year")
# print(car_remove)

# print("\n--- popitem() Example ---")
# car_remove.popitem()
# print(car_remove)


# # 🔹 7. dict() Constructor
# new_car = dict([
#     ("model", "toyota"),
#     ("year", 2006),
#     ("color", "black")
# ])

# print("\n--- 7. dict() Constructor ---")
# print(new_car)


# # ================================
# # ✅ END OF DICTIONARY FILE
# # ================================
