
# my_list = [1, 2, 9, 4, 0, 5]

# my_list.sort()

# print(my_list)

# # my_list[1] = 9
# # my_tuple[1] = 9

# # del my_list[1]
# # del my_tuple[1]
# # print(len(my_list))
# # print(my_list)
# my_tuple = (1, 9, 3, 4, 3, 5, 6, 0)

# # print(len(my_tuple))

# print(sorted(my_tuple, reverse=True))
# print(my_tuple)

# # my_tuple

# # print(my_tuple.count(9))
# # print(my_tuple.index(3, 3, 6))



# for i in range(10, 0, -1):
#     print(i, end=" ")


# n = int(input("Enter : "))

# for i in range(1, 13):
#     print(f"{n} x {i} = {n*i}")


# size = int(input("N: "))
# nums = list(map(int, input("Enter: ").split()))

# odd = 0
# even = 0
# pos = 0
# neg = 0

# odd, even, pos, neg = 0, 0, 0, 0
# #  nums = [1, 2, 3, 4, 5]
# for i in range(len(nums)):
#     if nums[i] % 2:
#        odd += 1
#     else:
#         even += 1 
    
#     if nums[i] > 0:
#         pos += 1
#     elif nums[i] < 0:
#         neg += 1
        

# print(f"Even: {even}")
# print(f"Odd: {odd}")
# print(f"Positive: {pos}")
# print(f"Negative: {neg}")


# print(nums)


# Dictionary

info = {
    "name": "Ahmed",
    "age": 24,
    "height": 175.5
}

info["address"] = "Chittagong"

print(info.keys())
print(info.values())
print(info.items())

info.clear()
info.pop("gpa", None)
info.popitem()

info.update({"name": "Ahil", "age": 20})

# print(info)

for key in info.keys():
    print(key)

for value in info.values():
    print(value)

for key, value in info.items():
    print(f"{key}: {value}")

# my_list = [2, 5, 2, 6, 0, 7]

# # print(list(enumerate(my_list)))

# for index, value in enumerate(my_list):
#     print(f"{index} : {value}")


n = int(input("Enter: "))
fact = 1
print(f"{fact} x", end=" ")
for i in range(2, n+1):
    fact *= i
    print(f"{i} x", end=" ")

print("\n")
print(fact)


