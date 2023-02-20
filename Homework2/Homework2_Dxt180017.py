#Homework 2
#Dhruv Thoutireddy

#imports that are used for the program
import sys
import pathlib
import nltk
from random import seed
from random import randint
nltk.download('gutenberg')
from nltk.book import *
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.text import Text

#function preprocess takes in the text and processes it so that the number of nouns, tokens and words are available
def preprocess(tokens):
    #all words are lowercased if they are a word
    tokens = [t.lower() for t in tokens if t.isalpha()]
    text = Text(tokens)

    #removes words that are smaller than length 5 while also getting rid of stopwords
    new_text = [t for t in text if t.isalpha() and
               t not in stopwords.words('english') and len(t) > 5]

    #creates a set of tokens and calculates lexical diversity
    token_set = set(new_text)
    lexical_diversity = len(token_set)/len(new_text)
    print("\nLexical diversity is: ", lexical_diversity)

    #lemmatizes the words and adds them to a new list
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in new_text]
    unique_lemmas = set(lemmas)
    unique_lemmas = list(unique_lemmas)

    #finds the parts of speech on the unique lemmas and prints out the first 20
    tags_pos = nltk.pos_tag(unique_lemmas)
    print("\nfirst 20 pos tagging:")
    print(tags_pos[:20])

    noun_list = []

    #gets all the words that are nouns and adds them to a list
    for i in tags_pos:
        if i[1] == 'NN':
            noun_list.append(i[0])

    print(noun_list[:20])

    print("\nThis is the number of tokens: ", len(new_text))
    print("This is the number of nouns: ", len(noun_list))

    return new_text, noun_list

def game(word_list):
    seed(1234)
    userchoice = ''

    print("\nWelcome to the word guessing game")
    while(userchoice != '!'): #game runs as long as user does not quit out of the game
        score = 5
        game_end = False
        rand = randint(0,49)
        word = word_list[rand] #gets a random word from the word list
        word_length = len(word)
        user_answer = []
        for i in range(word_length):
            user_answer.append('_')
        print(' '.join(user_answer))
        #userchoice = '!'

        while(game_end == False): #loop that runs for the guessing portion of the game
            userchoice = input("guess a letter or input ! to exit the game: ")
            guess_right = False
            if(userchoice == '!'): #if user enters quit then the program quits
                game_end = True
                break

            #checks to see if the entered letter matches with the letter in the actual word
            for i in range(word_length):
                if user_answer[i] == '_' and userchoice == word[i]:
                    user_answer[i] = userchoice
                    game_end = False
                    guess_right = True

            #if the guess is right then score is calculated
            if(guess_right == True):
                win_count = 0
                for i in range(word_length):
                    if user_answer[i] == '_':
                        win_count = win_count + 1
                if(win_count > 0): #if word is not solved then score is added to
                    score = score + 1
                    print("correct! The score is now: ", score)
                    print(' '.join(user_answer))
                    game_end = False
                else: #if word is solved the game is over and score is displayed
                    score = score + 1
                    game_end = True
                    print("you solved the word, your score was: ", score)
                    print(' '.join(user_answer))
                    print("Guess another word")

            #if the guess was wrong then score is deducted
            if(guess_right == False):
                score = score - 1
                if(score < 0): #if score is less than 0 then game is over
                    print("The game is now over, the word was: ", word)
                    game_end = True
                    print("Guess another word")
                else: #if score is greater than zero then score is deducted and game continues
                    print("that is incorrect please guess again, the score is now: ", score)
                    print(' '.join(user_answer))
                    game_end = False
    return




if __name__ == '__main__':
    if len(sys.argv) < 2: #if arguments in control line are not the python file and csv, program will quit
        print('Please enter a file')
        quit()

    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r') as f:
        lines = f.read()

    #replaces new lines with spaces and then tokenizes the text
    text = lines.replace('\n', ' ')
    tokens = word_tokenize(text)

    Processed_tokens, nouns = preprocess(tokens)

    #stores the values in a dictionary
    noun_counts = {x:Processed_tokens.count(x) for x in nouns}

    #creates a list of the top 50 nouns in the text and adds them to a list to make a wordbank
    sorted_counts = sorted(noun_counts.items(), key=lambda x: x[1], reverse=True)
    counter = 0
    word_list = []
    print("\nThe top 50 nouns in the text")
    for i in sorted_counts:
        print(i)
        word_list.append(i[0])
        counter = counter + 1
        if counter == 50:
            break
    game(word_list)