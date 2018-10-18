# Function to determine pangram
from string import ascii_lowercase

def is_pangram(word):
    l = set(ascii_lowercase)            # made a list of all alphabets
    return l.issubset(word.lower())     #check for pangram by checking
                                        #if l is subset of sentence
    
