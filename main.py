import random
import hangman_words
import hangman_art

#Printing Logo
logo=hangman_art.logo
print(logo+"\n\n")
#Choosing the word from the list
word_list=hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
#Assigning no lives
end_of_game = False
lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Creating blanks
display = []
for _ in range(word_length):
    display += "_"
  
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  
  #To check weather the user is guessing the same letter again
  if guess in display:
    print("You have already guessed this letter\n")
    continue

  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]   
    if letter == guess:
      display[position] = letter

  #Check if user is wrong.
  if guess not in chosen_word:
    lives -= 1
    print(f"'{guess}' is not in the word.You have lost 1 life Remaining lives={lives}\n")
  
  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")
    
  print(hangman_art.stages[lives])
  
  #Check if user has got all letters
  if "_" not in display:
      end_of_game = True
      print("You win.")

  #Check if user has enough lives 
  if lives == 0:
    end_of_game = True
    print("You lose.")