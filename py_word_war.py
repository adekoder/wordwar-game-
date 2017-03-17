import random
score_board = {"user_point" : 0 , "computer_point": 0}
def main():
	print("""
Welcome this is a word war game where you 
play against the computer , you and the computer fight with words
****************************************************************
Instructions:
you enter a word into the game and the computer also generate a word
then common letters in both is cancelled out the higher number of letters
your left with determine your point 
""")
	print("-" * 50)
	print("1 : Start Game")
	print("2 : exit Game\n")
	user_option = input("enter your option >>> ")
	if user_option == "1":
		user_name = input("Please enter your name >>> ")
		global score_board
		while True:
			gamePlay()
			print("Score Board".center(50, "-"))
			print(user_name.ljust(15 , ".") + str(score_board["user_point"]).rjust(10))
			print("computer".ljust(15, ".") + str(score_board["computer_point"]).rjust(10))

	else:
		exit()


def gamePlay():
	
	user_word = input("enter you word >>> ")
	user_word = user_word.lower()
	computer_word = list(wordGenerator(len(user_word)).lower())
	print("computer word : %s" %("".join(computer_word)))
	user_word_list  = list(user_word)
	for letter in user_word:
		if letter in computer_word:
			user_word_list.remove(letter)
			computer_word.remove(letter)
		else:
			continue
		litleAI(user_word)
	#print("user number of letters left =  %d"%(len(user_word_list)))
	#print("computer number of letters left =  %d"%(len(computer_word)))
	if len(user_word_list) > len(computer_word):
		score_board["user_point"] += 1
		print("user won")
		return score_board
	elif  len(computer_word) > len(user_word_list):
		score_board["computer_point"] += 1 
		print("computer won")
		return score_board
	else:
		print("draw")
		return score_board


def wordGenerator(user_word_length):
	word_list = gameData()
	random_number = random.choice(range(len(word_list))) 
		# if the gameData has a word that is of the same length with the user word 
		# create a new list of the word and select at random 
	new_list = [word for  word in word_list if len(word.rstrip())  == user_word_length]	
	if len(new_list) != 0:
		computer_word =  new_list[random.choice(range(len(new_list)))]
		return computer_word.rstrip()
	computer_word =  word_list[random_number] # selecting word form the list using random index
	return computer_word.rstrip()

def gameData():
	file = open("gameData.txt")
	word_list = file.readlines()
	file.close()
	return word_list

def litleAI(user_word):
	""" this provide a way for the computer to learn new word"""
	word_list = gameData()
	if user_word+"\n" not in word_list: # i added + "\n " to the user_word because .... 
		file = open("gameData.txt", "a") #  the words in the word list have new line character
		file.write(user_word+"\n")
		file.close()

main()
