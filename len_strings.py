# Author: Martin Luther Bironga
# Date: 27/1/2021

# problem statement
"""
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.

friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
"""

def friend(x):
    #Code
    friends=[]
    for i in range(len(x)):
        if len(x[i])==4:
            friends.append(x[i])
    return friends

# variations
def friend(x):
    return [i for i in x if len(i) == 4]

def friend(x):
    return filter(lambda name: len(name) == 4, x)
