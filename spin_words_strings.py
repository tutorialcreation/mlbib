# Author: Martin Bironga
# Date: 29/1/2021

# Problem
"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or 
more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. 
Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
"""

# Solution
def spin_words(sentence):
    words=[i for i in sentence.split(" ")]
    reverse_=[i.join(i.split(" "))[::-1] if len(i)>=5 else i for i in words]
    new_sentence=" ".join(reverse_)   
    return new_sentence


# variations
def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

def spin_words(sentence):
    return ' '.join(word if len(word)<5 else word[::-1] for word in sentence.split())

import re
def spin_words(sentence):
    return re.sub(r"\w{5,}", lambda w: w.group(0)[::-1], sentence)

spin_words = lambda s: ' '.join([len(w) > 4 and w[::-1] or w for w in s.split()])

spin_words = lambda a:" ".join(list(map(lambda s:s[::-1] if len(s) >= 5 else s, a.split(' '))))
