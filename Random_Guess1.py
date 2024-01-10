import random
class Game():
    user_name = ''
    animals   = ''
    
    def __init__(self,user_name):
        print (" Welcome ", user_name, "! Lets begin the game.")
        self.user_name = user_name
        #self.initialize_dict()
        #self.selection()
    def selection(self):
        self.Categories = { 'R': 'reptiles', 'B' : 'birds', 'I' : 'insects'}
        c_input =input("Enter you categories:")
        if c_input in self.Categories.keys():
            print("Great! You have chosen the %s category.Now,I will give you some hints and you can try to guess the animal"%self.Categories.get(c_input))
            select = self.Categories.get(c_input)
            print(select)
            
class Game_child(Game):
    def category_dic(self):
        self.birds    = {'parrot': "I am a bird; I am green in color and have reddish beak",
                         'peacock': "I am a bird. I am colorful and known as the national bird of India",
                         'hen': "I am a domestic bird and give you eggs for omelete"}
        self.reptiles = {'crocodile': "I am a reptile; I am brownish green in colour, big in size and live in water.",
                         'snake': "I am a reptile. I make a hiss sound and can move without any legs",
                         'lizard': "I am a reptile; I live in most houses and I can easily crawl on the walls"}
        self.insects  = {'bee': "I am an insect and I help with pollination and collect honey",
                         'mosquito': "I am an insect and I drink blood and spread disease",
                         'butterfly': "I am an insect and I have beautiful wings and I love nectar"}
        self.Categories = { 'R': 'reptiles', 'B' : 'birds', 'I' : 'insects'}
        self.category = dict(**self.birds,**self.reptiles,**self.insects)
        

    def play(self):
        print("Guess who I am From the below hints")    
        for i in self.category:
            randomanimal = random.choice(list(self.category.keys())) 
            hints = self.category.get(randomanimal) 
            print(hints)
            chance = int(input("How many Chances you want: "))
            while chance > 0:
                print("your guess : ")
                guess = input().lower().strip() 
                if guess == randomanimal:
                    print("You are right!")
                    break
                else:
                    print("Given input Wrong")
                    chance -= 1
            if chance == 0:
                    print("Chances are ended")
                    print("if you want to reload the game, Yes/No")
                    ans = input()
                    if ans.lower() == "yes":
                        print("cool")
                        if __name__ == "__main__":
                            user_name = ''
                            print(" Welcome to animal guessing game. Please enter your name: ")
                            guess = input()
                            game  = Game_child(guess)
                            game.category_dic()
                            game.play()
                    else:
                        print("Thank you and The Game End")
                        break            
                    
if __name__ == "__main__":
    user_name = ''
    print(" Welcome to animal guessing game. Please enter your name: ")
    guess = input()
    game  = Game_child(guess)
    #game.selection()
    game.category_dic()
    game.play()
     
     
               
