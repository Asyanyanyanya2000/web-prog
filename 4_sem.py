# import random

# def view_arr(arr2):
#     for i in arr2:
#         print(end="\n")
#         for j in range(len(i)):
#             if j==len(i)-1:
#                 print(i[j], end=";")
#             else:
#                 print(i[j], end=",")
#     print(end="\n")

# # arr2 = [[1,2,3,4], [5,6,7,8]]

# # print (arr2)

# def get_random_array(size, crit):
#     arr = random.choices(range(crit), k=size)
#     return arr

# def create_multi_arr(row,col,crit):
#     arr2 = []
#     for i in range(row):
#         arr2.append(get_random_array(col, crit))
#     return arr2

# view_arr(create_multi_arr(3,3,10))