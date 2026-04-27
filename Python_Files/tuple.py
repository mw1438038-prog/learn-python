
# # Immutable
# # tuple_b = 1,2,3,'g','f'
# tuple_c = (2,6,9,'A')
# tuple_d = (4,9,2,'B')
# tuple_f = (8,0,1,'C')
# # tuple_c[0] = 'b'
# print(tuple_c)
# tuple_c = tuple_c[0],tuple_c[2],'S',tuple_f[2]
# print(tuple_c)
 
# ele_a,ele_b,ele_c,ele_d = tuple_c
 
# print(ele_a)
# print(ele_b)
# print(ele_c)
# print(ele_c)
#                                               dic unpaicking
D = {
   'key1': 'This is values for key1',
   'key2': 'This is values for key2',
   'key3': 'This is values for key3',
   'key4': 'This is values for key4',
   'key5': 'This is values for key5',
   'key6': 'This is values for key6',
   'key7': 'This is values for key7',
}

# Keys
for key in D.keys():
    print(key)

# Values
for value in D.values():
    print(value)

# Key + Value
D.clear()
print(D)