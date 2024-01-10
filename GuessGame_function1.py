Birds={'Crow':"I AM BLACK.I'm pet of Lord Sanieswaren ",'Parrot':"I am green. i'm pet of Goddess Meenachi"}
Reptiles={'Snake':"I have no legs,twisted tongue and toxic on my teeth and crawl on land",'Lizard':"I'm living in house walls. I like to ate tiny insects"}
Insects ={'Spider': "I don't have hand.But,i have eight legs.", 'Bee': " I'm collecting Honey from flowers"}
Categories = { 'R': 'Reptiles', 'B' : 'Birds', 'I' : 'Insects'}
def Guess_Game(user,c_input):
  #user = input("Please enter your name: ")
  print("-----------------------------------------------------------------------------")
  print(f"Hi {user},Welcome to the advanced animal guessing game.")
  print("-----------------------------------------------------------------------------")
  print("Choose one of the below categories by entering the first letter in capitals: Reptiles, Birds, Insects")
  #c_input = input()
  for i in Categories.keys():
    if (c_input == i ):
      #print (f"Great! You have chosen the  {Categories.get(i)} category.Now,I will give you some hints and you can try to guess the animals.")
      print("Great! You have chosen the %s category.Now,I will give you some hints and you can try to guess the animals." % Categories.get(i))
      Tool_box = eval(Categories.get(i))
  for key,value in Tool_box.items():
    #print(f"Hint: {dic.get(k)} \nWhat is your guess?")
    #print("Hint: %s \nWhat is your guess?" % dic.get(k))
    print("Hint: %s \nWhat is your guess?" % value)
    loop = 2 
    while loop >= 0: 
      guess = input()
      if guess.capitalize() == key:
        print("Excellent. You are right")
        break
      else:
        print(f"You are wrong. you have {loop} chances")
        loop -= 1
    else:
      print("Sorry, you are Exceed the Limit")
user ="Genesis" 
c_input ='I'
Guess_Game(user,c_input)
