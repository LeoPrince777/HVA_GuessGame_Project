Birds={'Crow':"I AM bLACK.I'm pet of Lord Sanieswaren ",'Parrot':"I am green. i'm pet of Goddess Meenachi"}
print (type(Birds)) # checking line
Reptiles={'Snake':"I have no legs,twisted tongue and toxic on my teeth and crawl on land",'Lizard':"i am living in house walls. I like to ate tiny insects"}
Insects ={'Spider': "I have eight legs", 'Mosquito': " I likes to drink the human blood and i'm living in drainage"}
Categories = { 'R': 'Reptiles', 'B' : 'Birds', 'I' : 'Insects'} 
user = input("Please enter your name: ")
print("-----------------------------------------------------------------------------")
print ("Hi "+ user+",  Welcome to the advanced animal guessing game. ")
print("-----------------------------------------------------------------------------")
print ("Choose one of the below categories by entering the first letter in capitals: Reptiles, Birds, Insects")
c_input = input()
for i in Categories.keys():
	if (c_input == i ):
		#print (Categories.get(i)) # checking line
		
		#print ("Great! You have chosen the"+ Categories.keys() +"category.Now,I will give you some hints and you can try to guess the animals.")    # it given Type Error
		print ("Great! You have chosen the " + Categories.get(i) + " category.Now,I will give you some hints and you can try to guess the animals.")
		dic = Categories.get(i)
		#print("m1: "+ dic) # Birds
		#dic1 = repr(Categories.get(i))  #checking line
		#print("m2: "+ dic1) #checking line
		#print(Birds) # {'Crow': 'i AM bLACK', 'Parrot': 'I am green'} #checking line
#print(dic)
dic =eval(dic)
for k in dic:
	print("Hint: " +dic.get(k) + "\nWhat is your guess?")
	while True:
		guess = input()
		if (guess == k):
			print("Excellent. You are right")
			break
		else:
			print("Sorry, you are wrong. you have another one Attempt")
			continue
		
		
#for j in Birds:
		#print("Hints: " + j)
	#print("Hint: " +Birds[j]+ "\nWhat is your guess?")
	#guess = input()
	#if (guess == j):
		#print("Excelent. You are right")
	#else:
		#print("Sorry, you are wrong")
	
	

	
	
