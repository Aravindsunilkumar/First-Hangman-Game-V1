#importing function
import random
from hangman_words import words
word = random.choice(words)
chosen_word = word.lower()
word_len =len(chosen_word)
#######################################
lives = 6
end = False
#######################################
#importing logo and artwork
from hangman_stage import logo
print(logo)
#######################################
#Create blanks
display=[]
for letter in chosen_word:
  display += "_"
print(display)
#######################################
while not end: 
  guess = input("Guess a letter: ").lower()
#user has entered a letter they've already guessed, print the letter and let them know.
  if guess in display:
    print (f"You.ve already guessed{guess}")
  #checked guessed letter
  for position in range(word_len):
    letter = chosen_word[position]
    if letter == guess:
      display[position]= letter
  print(f"{' '.join(display).upper()}")
  #Checking if the guessed word is wrong
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end =True
      print(f"\n its {chosen_word.upper()} you moron")
      print("\n YOU KILLED ME \n You Lose")
  from hangman_stage import stages
  print(stages[lives])
  #######################################
  #Check if user has got all letters.
  if "_" not in display:
    end = True
    print(f"\n Its {chosen_word.upper()}")
    print("You Saved me Player")
