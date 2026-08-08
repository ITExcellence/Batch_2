# Set

# first_set = {1, 2, 3, 4, 5, 6}
# second_set = {3, 6, 9}

# - | ^ &

# print(first_set | second_set)  # union
# print(first_set & second_set) # intersection
# print(first_set - second_set) # difference
# print(first_set ^ second_set) # symmetric difference


# my_set.add(7)
# my_set.remove(9)
# my_set.discard(9)
# # my_set.clear()
# print(second_set.issuperset(first_set))
# print(first_set.issuperset(second_set))

# tries = 5
# actual_pass = 1999
# while True:
#     # print(1)
    
#     password = int(input("Enter: "))
    
#     if password == actual_pass:
#         print("Correct")
#         break
#     else:
#         print("Wrong")
#         # tries -= 1
    

# li = [1, 3, -1, 5, 90, 87, 101, 7, 43]
# print(max(li))
# max_val = li[0]

# for i in range(len(li)):    
#     if li[i] > max_val:
#         max_val = li[i]
    
#     print(f"{i} | {max_val}")
    
# print(max_val)



# def fact(n):
    
#     if n == 0 or n == 1:
#         return 1
    
#     return n*fact(n-1)

# ans = fact(5)

# print(ans)


n = int(input("Enter: "))
print(n, end=" ")
while n != 1:
    
    if n % 2:
        n = (n*3) + 1
    else:
        n //= 2
    print(n, end=" ")



