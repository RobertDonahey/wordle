import random
guess_counter=0
RED = "\033[0;31m"
YELLOW = "\033[1;33m"
GREEN = "\033[0;32m"
LIGHT_WHITE = "\033[1;37m"
a=[]
guess1=0
guess2=0
guess3=0
guess4=0
guess5=0
guess6=0
wordlist=[ "apple", "beach", "cherry", "dream", "earth", "flute", "grape", "house", "ideal", "joker",
    "knife", "lemon", "light", "magic", "money", "night", "ocean", "peace", "plant", "plane",
    "queen", "river", "rocky", "scene", "shiny", "spend", "store", "sugar", "sweet", "table",
    "tiger", "train", "trust", "ultra", "unity", "value", "vocal", "water", "wheel", "white",
    "youth", "zebra", "zesty", "angel", "bloom", "brave", "brisk", "cloud", "crisp", "dance",
    "daisy", "deeply", "eagle", "early", "elegy", "flash", "gleam", "globe", "grasp", "gravy",
    "helic", "happy", "harsh", "heart", "honey", "index", "island", "jolly", "juice", "lunar",
    "lively", "liver", "loyal", "lucky", "magic", "mango", "marsh", "mercy", "mirth", "misty",
    "motel", "music", "peace", "plumb", "plush", "quilt", "quiet", "quick", "river", "rocky",
    "rugby", "shine", "shout", "smile", "smoke", "spark", "spend", "spicy", "stone", "store",
    "sweet", "swift", "tasty", "tiger", "today", "track", "trust", "truth", "valve", "vivid"]
secretword=random.choice(wordlist)
secretwordletters=list(secretword)
while guess_counter<7:
    guess_counter+=1
    guess=str(input())
    guess=guess.lower()
    def Guess(guess):
        wordletters=list(guess)
        for i in secretwordletters:
                if i in wordletters: 
                    a.append(i)
                    if secretwordletters[0] ==wordletters[0]:
                        print(GREEN+secretwordletters[0])
                    if secretwordletters[1]==wordletters[1]:
                        print(GREEN+secretwordletters[1])
                    if secretwordletters[2]==wordletters[2]:
                        print(GREEN+secretwordletters[2])
                    if secretwordletters[3]==wordletters[3]:
                        print(GREEN+secretwordletters[3])
                    if secretwordletters[4]==wordletters[4]:
                        print(GREEN+secretwordletters[4])
                    else:
                        print(YELLOW+i)
                    print(LIGHT_WHITE)
                    break
    (Guess(guess))
    if guess==secretword:
        print("Congrats you got it in",guess_counter,"guesses")
        break
    if guess!=secretword and guess_counter==6:
        print("YOU LOSE")
    if guess_counter==1:
        guess1=guess
    if guess_counter==2:
        guess2=guess
    if guess_counter==3:
        guess3=guess
    if guess_counter==4:
        guess4=guess
    if guess_counter==5:
        guess5=guess
    if guess_counter==6:
        guess6=guess
    
    if guess1!=0:
        print(list(guess1))
    if guess2!=0:
        print(list(guess2))
    if guess3!=0:
        print(list(guess3))
    if guess4!=0:
        print(list(guess4))
    if guess5!=0:
        print(list(guess5))
    if guess6!=0:
        print(list(guess6))


