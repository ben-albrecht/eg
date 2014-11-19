#!/usr/bin/env python

import random
import string
"""
Hangman game for Kivy
"""

def loadwords():
    with open("wordslist.txt", 'r') as handle:
        lines = handle.readlines()
        words = []
        for line in lines:
            words.append(line.strip())
    return words


def pickword(words):
    return random.choice(words)


def iswordguessed(secretword, lettersguessed):
    # Check if lettersguessed is empty
    if not lettersguessed:
        return False
    for secretletter in secretword:
        if secretletter not in lettersguessed:
            return False
    return True


def getguessword(secretword, lettersguessed):
    guessword = []
    for secretletter in secretword:
        if secretletter not in lettersguessed:
            guessword.append('_')
        else:
            guessword.append(secretletter)
    return ''.join(guessword)


def remainingletters(lettersguessed):
    remaining = []
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        if letter not in lettersguessed:
            remaining.append(letter)
    return ''.join(remaining)


def checkguess(remainingletters, guess):
    if guess not in remainingletters:
        return False
    else:
        return True



def isgoodguess(guess, secretword):
    if guess in secretword:
        return True
    else:
        return False



if __name__ == '__main__':

    # Load all the words from file into words
    words = loadwords()

    # Pick our secret word
    secretword = pickword(words)

    # Initialized list of letters that have already been guessed
    lettersguessed = []

    # Number of tries depends on length of secret word
    num_tries = int(len(secretword)/2.0) + 3

    # Main Loop - Will continue to loop until word is completely guessed
    while not iswordguessed(secretword, lettersguessed) and num_tries > 0:

        # Give the user some information
        print "You have", num_tries, " tries remaining"
        print getguessword(secretword, lettersguessed)
        print remainingletters(lettersguessed)

        # Request guess from user
        guess = raw_input("Please enter a guess letter from the above list:")
        print "You guessed", guess

        # Check if guess is valid
        if checkguess(remainingletters(lettersguessed), guess):
            lettersguessed.append(guess)
            if isgoodguess(guess, secretword):
                print "Good guess!"
            else:
                print "Bad guess!"
                num_tries += -1
        else:
            print "\"", guess, " \"is an invalid guess"


    # Win or Lose
    print "The word was ", secretword
    if num_tries <= 0:
        print "You Lose!"
    else:
        print "You Win!"
