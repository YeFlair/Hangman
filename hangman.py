import random, words

chosen_word = random.choice(words.word_list) #A Word Imported From Words File - Being Chosing At Random
lives = 6 #Number of Lives Avaible 
end_of_game = False

display = [] # Empty List To Store Blank Spaces And Guessed Letter " _ _ a _ _"
for _ in range(len(chosen_word)): #Looping Through The Lenth Of The Word To Get The Number Of Needed Blank Spaces
    display += "_" #Stores A _ After Each Loop 
# print(display) #Displays Total Number OF Spaces 

while not end_of_game: #Loops Through Process Untill User Wins / Loses 
    guess = input("Enter A Letter: ").lower() #Gets User Answer And Automates The Answer To Lower Case 
    if guess in display:
        print(f"{guess} already guessed!")
    
    for position in range(len(chosen_word)): #Looks Throught The Length Of The Word To Replace _ With Correct Letter
        letter = chosen_word[position] #Indentifies The Letter's Index
        if letter == guess:
            display[position] = letter #Replaces The Blank Space With letter That Matches Proper Index
    print(f"{' '.join(display)}") #Prints Letter At Proper Index Location 
    
    if guess not in chosen_word:
        print(f"{guess} is not in word! you lose a life.")
        lives -= 1 #Reduces Lives When Guessed Letter Is Wrong 
        if lives == 0: #When Lives Are At 0 The Game Would End
            end_of_game == True
            print("You Lose.")

    if "_" not in display: #Checks If Theres No More Empty Spaces
        end_of_game = True
        print("You Win.")

