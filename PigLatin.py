#Creates a "Pig Latin" translation for a user inputted word, eg. Drum becomes rumday, phone becomes honepay.

def translator():
    
    #Function asks user to input a word
    word = raw_input("Please enter a word: ")
    
    #Makes word lowercase
    word = word.lower()
    
    #Takes the first letter of the word and stores as a variable
    first = word[0]
    
    #Takes remainder of word and stores as a variable
    new_word = word[1:]
    
    #Suffix to add to pig latin word
    pig = "ay"
    
    #Combine strings to make the pig latin translation of the user's word
    pig_word = new_word + first + pig
    
    #Display translation
    print pig_word

#Keeps function running indefinitely
while True:
    translator()

