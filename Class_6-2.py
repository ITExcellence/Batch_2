# l = len(my_list)
# while l > 0:
#     print(my_list[l-1])
#     l -= 1


# my_list = [1, 2, 3, 4, 5, 6, 3, 9]
# for i in my_list:
#     if i == 5:
#         continue
    
#     print(i)
    
import random

answer = random.randint(1, 100)
tries = 10
t = 10
for i in range(tries):
    print(f"Tries remaining: {t}")
    num = int(input("Enter a number between 1-100: "))
    
    if num == answer:
        print("You win!")
        break
    else:
        t -= 1
        if t == 0:
            print("Sorry you are out of guesses.")
            print(f"The answer was {answer}.")
            break
        
        if num > answer:
            print("Your guess is too large. Try a smaller number")
        else:
            print("Your guess is too small. Try a larger number")
        
        