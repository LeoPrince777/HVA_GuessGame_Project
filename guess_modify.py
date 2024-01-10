Birds={'Crow':"I AM bLACK.I'm pet of Lord Sanieswaren ",'Parrot':"I am green. i'm pet of Goddess Meenachi"}
Reptiles={'Snake':"I have no legs,twisted tongue and toxic on my teeth and crawl on land",'Lizard':"i am living in house walls. I like to ate tiny insects"}
Insects ={'Spider': "I have eight legs", 'Mosquito': " I likes to drink the human blood and i'm living in drainage"}
Categories = { 'R': 'Reptiles', 'B' : 'Birds', 'I' : 'Insects'}
def Guess_Game():
    user = input("Please enter your name: ")
    print("-----------------------------------------------------------------------------")
    print("Hi "+ user+",  Welcome to the advanced animal guessing game. ")
    print("-----------------------------------------------------------------------------")
    print ("Choose one of the below categories by entering the first letter in capitals: Reptiles, Birds, Insects")
    for c_input in range(2):
        c_input = input()
        if c_input not in Categories.keys():
            print("Wrong input Given! Pls give the correct letter")
            continue
    if c_input in Categories.keys():
        print("Great! You have chosen the %s category.Now,I will give you some hints and you can try to guess the animal"%Categories.get(c_input))
        dic = eval(Categories.get(c_input))
        for k,v in dic.items():
            print("Hint: " +dic.get(k) + "\nWhat is your guess?")
            loop = 2 
            while loop >= 0:
                guess = input()
                if guess.capitalize() == k:
                    print("Excellent. You are right")
                    break
                else:
                    print(f"You are wrong. you have {loop} chances")
                    loop -= 1
	      
Guess_Game()
