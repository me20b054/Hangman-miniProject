import random 
from words import word_list 

def get_word():
    word = random.choice(word_list) 
    return word 

def display_hangman(tries):
    stages = [
       ''' 0 < -- < ''', ''' 0 <--/ ''', ''' 0 <-- ''', ''' 0 /--''' , ''' 0 --''', ''' 0 -''' ,''' 0 ''' ]
    return stages[tries]


def play(word):
    word_completion = "-"*len(word)
    guessed_letters= []
    guessed_words = []
    guessed = False
    tries = 6 
    print('Let us start Hangman game')
    print(display_hangman(tries))
    while not guessed and tries>0:
        guess = input("guess your word or letter:") 
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('Already there, guess another')
            elif guess not in word:
                print("sorry, you guessed wrong,Try again")
                tries -= 1
                guessed_letters.append(guess)
            else: 
                print('Nice,you have guessed corretly')
                guessed_letters.append(guess)
                word_list = list(word_completion)
                indices = [i for i,letter in enumerate(word) if letter == guess] 
                for index in indices:
                    word_list[index] = guess
                word_completion = " ".join(word_list)     
                if "-" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Already there, guess another")
            elif guess != word :
                print("your" + guess +'is wrong') 
                guessed_words.append(guess)
                tries -= 1
            else: 
                guessed = True 
                word_completion = word
        else:
            print("Invaid guess")
    
        print(display_hangman(tries)) 
        print(word_completion)
    
    if guessed == True:
        print("Congrats, you won the game! you have guessed word correctly")
    else:
        print("sorry! you are out of tries, you didn't guess" + word + "correctly") 



def main():
    word = get_word()
    play(word) 

if __name__ == "__main__":
    main()



