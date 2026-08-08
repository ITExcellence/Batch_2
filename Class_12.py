from wonderwords import RandomWord

answer = RandomWord()
answer = answer.word(include_parts_of_speech=["verb"], word_min_length=5, word_max_length=8)
n = len(answer)

lst = []
for i in range(n):
    lst.append('_')
    
# print(lst)

lives = 6
count = 0

while True:
    check = False
    print(lst)
    print(f"Lives left: {lives}")
    
    guess = input("Enter your guess: ")
    
    for i in range(n):
        if guess == answer[i]:
            lst[i] = guess
            check = True
            count += 1
          
      
    if check == False:
        print(f"Sorry wrong guess.")
        lives -= 1
        
    if count == n:
        print(f"Congrats! You won. The word was {answer}.")
        break
        
    if lives == 0:
        print(f"Sorry, you are out of lives. The word was {answer}.")
        break
    
    
    
                
    
    
    
    
    
    