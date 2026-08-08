
# class Person():
    
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
        
#     def getInfo(self):
#         return f"Name: {self.name} \n Age: {self.age}"
    
        
    

# person_1 = Person("Albert", 20)
# person_2 = Person("Ahmed", 23)        

# print(person_1.getInfo())

class BankAccount():
    
    def __init__(self, account_holder, password: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.password = password
        self.initial_balance = initial_balance
        
    def authenticate(self):
        t = 3
        while t > -1: 
            p = input("Enter your password: ")
            if p != self.password:
                print("Invalid password.")
            else:
                return True
            t -= 1
            
            if t == 0:
                return False
    
    def deposit(self, amount: float):
        
        if self.authenticate() == False:
            return "Login failed"
        
        if amount < 0:
            return "Please input a positive number."
        else:
            self.initial_balance += amount
            return f"{amount} deposited successfully."
    
    def withdraw(self, amount: float):
        
        if self.authenticate() == False:
            return "Login failed"
        else:
            self.initial_balance -= amount
            return f"{amount} withdrawn successfully."

    def getInfo(self):
        
        if self.authenticate() == False:
            return "Login failed"
        else:
            return f"Acount Holder: {self.account_holder}\nBalance: {self.initial_balance}"
    
obj_1 = BankAccount("Tamzid", "python321", 2000)
print("-------------💸 My Bank 💸 -------------")
print("Options: ")
print("1: Deposit")
print("2: Withdraw")
print("3: Check balance")
print("4: Exit")

while True:
    
    op = int(input("Press: "))
    
    if op == 1:
        amount = float(input("Enter deposit amount: "))
        print(obj_1.deposit(amount))
    elif op == 2:
        amount = float(input("Enter withdraw amount: "))
        print(obj_1.withdraw(amount))
    elif op == 3:
        print(obj_1.getInfo())
    elif op == 4:
        print("Thnak you for choosing us. Bye bye.")
        break
    else:
        print("Enter a valid option.")