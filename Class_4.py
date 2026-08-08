#  a b c
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# a, b, c = map(int, input("Enter ").split())

# print(f"{a}  {b}  {c}")

# B

# a, b, k = map(int, input("Enter the numbers: ").split())


# if (a % k == 0) and (b % k == 0):
#     print("Both")
# elif (a % k == 0) and (b % k != 0):
#     print("Memo")
# elif (b % k == 0) and (a % k != 0):
#     print("Momo")
# else:
#     print("None")


# a, b, c, d = map(int, input("Enter: ").split())

# if (a + b - c == d) or (a - b + c == d) or (a + b * c == d) or (a * b + c == d) or (a * b - c == d) or (a - b * c == d):
#     print("YES")
# else:
#     print("NO")


# x, p = map(int, input("Enter: ").split())

# g = p / (1 - (x/100))

# print(round(g, 2))
# print(g)



# from math import sqrt

# a, b, c = map(int, input("Enter: ").split())

# D = b**2 - 4*a*c

# if D < 0:
#     print("No real values")
# else:
#     D = sqrt(D)
#     x1 = (-b + D)/(2*a)
#     x2 = (-b - D)/(2*a)
    
#     # print("x1  = ", x1, " and x2 = ", x2)
#     print(f"x1 = {x1} and x2 = {x2}")