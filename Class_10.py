#  Encapsulation
# class Wallet():
    
#     def __init__(self, balance):
#         self.__balance = balance
        
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
            
#     def get_balance(self):
#         return self.__balance
    

# obj1 = Wallet(200)
# # print(obj1.balance)
# obj1.deposit(100)
# print(obj1.get_balance())


#  Inheritance

# class Parent: 
#     def __init__(self, name): 
#         self.name = name 
 
#     def sound(self): 
#         return f'{self.name}: Go to school!!' 
 
# class Child(Parent): 
#     bark = 'Let us play!!' 
 
#     # Override sound() to use bark class variable 
#     def sound(self): 
#         return f'{self.name}: {self.bark}' 
 
# jack = Child('Son') 
# parent = Parent("Dad")
# print(parent.sound())
# print(jack.sound())  # Jack barks woof! woof!! woof!!! 

#  Overloading






# O(n)
for i in range(n):
    print(i)

# O(n^2)
for i in range(n):
    for j in range(n):
        print(f"{i} -> {j}")

n = 100

a = 10

#  O(log(n))
while n > 1:
    n = n // 2
    print(n)








