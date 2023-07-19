import random

words_bank = ["tree","book","blue","train","fish","woman","life","freedom","iran","sky"]
user_mistakes = 0
good_char = []
bad_char = []
users_mistakes =0

x = random.randint(0 , len(words_bank)-1)
word = words_bank[x]

while user_mistakes<6:
  
    for i in range(len(word)):
        if word[i] in good_char:
           print(word[i] , end=" ")
           if word != "- ":
               print("you won")
        else: 
           print("- " , end="")
 

        if len(word) == len(good_chars):
            print("You win")
            break

    user_char = input("please write your guess  ")
    if len(user_char) == 1:
        if user_char in word:
            good_char.append(user_char)
            print("yes")
        else:
            bad_char.append(user_char)
            user_mistakes += 1
            print("no")
    else:
        print(" mese adam vared kon")
        
if users_mistakes == 6:
    print("Game Over 💀")