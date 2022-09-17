import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#chosen_word = word_list[random.randint(0,2)]
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
print(chosen_word)
display = []
for _ in chosen_word:
	display += '_'

print(display)

end_of_game = False
while not end_of_game:
	guess = input("Guess a letter:  ").lower()

	#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
	i = 0

	result = []
	for char in chosen_word:
		if guess == char:
			result.append(guess)
		else:
			result.append("_")
		i += 1

	print(result)
	print("SECOND OPTION: ")
	for position in range(len(chosen_word)):
		if guess == chosen_word[position]:
			display[position] = guess
	
	print(display)
	
	if '_' not in display:
		end_of_game = True
			
print("YOU WON!")	
