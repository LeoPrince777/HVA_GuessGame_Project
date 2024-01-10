Birds={'Crow':"I AM bLACK.I'm pet of Lord Sanieswaren ",'Parrot':"I am green. i'm pet of Goddess Meenachi"}
Reptiles={'Snake':"I have no legs,twisted tongue and toxic on my teeth and crawl on land",'Lizard':"i am living in house walls. I like to ate tiny insects"}
Insects ={'Spider': "I have eight legs", 'Mosquito': " I likes to drink the human blood and i'm living in drainage"}
Categories = { 'R': 'Reptiles', 'B' : 'Birds', 'I' : 'Insects'}

def Guess_Game():
	  user = input("Please enter your name: ")
	  print("-----------------------------------------------------------------------------")
	  print ("Hi "+ user+",  Welcome to the advanced animal guessing game. ")
	  print("-----------------------------------------------------------------------------")
	  print ("Choose one of the below categories by entering the first letter in capitals: Reptiles, Birds, Insects")
	  c_input = input()
	  if c_input in Categories.keys():
	    print ("Great! You have chosen the " + Categories.get(c_input) + " category.Now,I will give you some hints and you can try to guess the animal")
	    dic = eval(Categories.get(c_input))
	    print(dic)
	    	  
  #for i in Categories.keys():
    #print(Categories.keys())
    #if (c_input == i ):
        #print (Categories.get(i))
        #print ("Great! You have chosen the " + Categories.get(i) + " category.Now,I will give you some hints and you can try to guess the animals.")
        #dic = Categories.get(i)
        #print(dic)
        #dic =eval(dic)
    #else:
          #print("Given input is wrong!")

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
             else:
      	    	print("Sorry, you are Exceed the Limit")
	      
Guess_Game()
