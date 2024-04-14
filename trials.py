class Person:

    def __init__(self, weapon=None, money=None, agility=None, health=None, species=None, morality=None,height=None):
        self._species = species
        self._weapon = weapon
        self._money = money
        self._agility = agility
        self._health = health
        self._morality = morality
        self._friends = []
        self._height = height

    # set functions
            
    def set_species(self, s):
        self._species = s
    
    def set_weapon(self, w):
        self._weapon = w

    def set_money(self, m):
        self._money = m

    def set_agility(self, a):
        self._agility = a

    def set_health(self, h):
        self._health = h

    def set_morality(self, m):
        self._morality += m
        
    def set_friends(self, f):
        self._friends.append(f)

    # get functions
        
    def get_species(self):
        return self._species
    
    def get_weapon(self):
        return self._weapon
    
    def get_money(self):
        return self._money
        
    def get_agility(self):
        return self._agility
    
    def get_health(self):
        return self._health
    
    def get_morality(self):
        return self._morality
    
    def get_friends(self):
        return self._friends

    def __str__(self):
        return str(self._species)+":\n "+ "Height: "+str(self._height)+"\n Weapon:" +str(self._weapon)+"\n Agility: "+str(self._agility)+"\n Money: "+ str(self._money)+"\n Health: "+ str(self._health)+"\n Morality: "+str(self._morality)


def main():
    #instructions()
    user_char = int(input("What character would you like to be? Select 1 for princess, 2 for hobbit, 3 for witch, 4 for elf: "))
    if user_char==1 or user_char==2:
        
        if user_char== 1:
            user=Person("fancy dagger",1000000,3,100,"Princess",0,64)
            computer=Person("club",4,7,60,"Hobbit",0,42)

        if user_char == 2:
            computer=Person("fancy dagger",1000000,3,100,"Princess",0,64)
            user=Person("club",4,7,60,"Hobbit",0,42)
        task_2(user, computer)
        user.set_morality(1)
        task_4(user, computer)
        ending(user, computer)

    if user_char == 3 or user_char == 4:
    
        if user_char == 3:
            user = Person("broomstick", 5, 4, 100, "Witch", None, 63)
            computer = Person("longbow", 0, 8, 100, "Elf", None, 69)
            
        if user_char == 4:
            user = Person("longbow", 0, 8, 100, "Elf", None, 69)
            computer = Person("broomstick", 5, 4, 100, "Witch", None, 63)

def task_2(user, comp):  
    from time import sleep
    # update_stats(user, comp)  
    # 2 Mythicical sheep eating beast or feral pig
    print("You and the ", comp.get_species(), "are talking over the results of the last task when... ")
    sleep(.5)
    print("you hear a scream coming from the town hall!")
    go = input("Go investigate? (y/n): ")
    if go == "n":
        go = input("are you SURE? (y/n): ")
        if go == "n":
            user.set_morality(-2)
            print("Wow... you lose morality points for not caring about your town!")
            print("A farmer runs up to you as you stand pointlessly in the middle of the town")
        else:
            user.set_morality(1)
            print("Good choice. You enter the town hall and encounter a frazzled farmer.")
    else:
        user.set_morality(2)
        print("You encounter a frazzled farmer and ask what the matter is.")
    print("He says 'Please help me! A evil beast is eating my sheep and I don't know what to do.'\n You and your companion head to the edge of the woods and encounter a wild beast!\n The beast has sharp teeth but strangly compassionate eyes. It roars at you.")
    attack = input("Begin your attack? (y/n): ")
    monster = 50
    while attack == "y" and monster>0:
        if user.get_species()=="Princess":
            monster -= (3*int(user.get_agility()))
        else:
            monster -= 2*int(user.get_agility())
        print("The monster wails and takes damage from your ", user.get_weapon())
        attack=input("Keep attacking or say no and take pity on the poor beast (y/n): ")
    if monster<0:
        user.set_morality(2)
        print("The monster finally collapses! \n You saved the town! If you had spared the monster, all the sheep would have been eaten. Good job!")
    else:
        user.set_morality(1)
        print("You spared the monster, at the expense of the village! All the farmers sheep will be eaten. \n Your compassion was admirable but ill-fated.")
    





    #Good: Killing beast Bad: Giving the beast a second chance (it eats the sheep)
def task_4(user, comp): 
    print("You and the ", comp.get_species(), "are wandering around the town when you encounter a child crying on the sidewalk. She looks a little odd, with a unsettling green tint to her skin." )
    help = input("Would you like to ask the child what is wrong? (y/n): ")
    if help == "n":
        user.set_morality(-2)
        print("You leave the child crying in the streets. Not a good look. You're going to lose some morality for that.")
    else:
        print("The child wipes her runny nose and then tells you that she got lost and needs help to find her way back home....")
        help= input("Do you help her find her way back home? (y/n): ")
        if help == "y":
            user.set_morality(3)
            print("How kind of you! You gain morality points and become a better person!")
        else:
            user.set_morality(-3)
            print("Wow. That is cold. You lose some morality.")
        # 4 Helping a lost child (5 yrs and kinda snotty)
        # Good: help find their family Bad: leave child on the ground



def ending(user, comp):
    from time import sleep
    print("You have reached the end of your journey, ",user.get_species(),"and it is time to discover whether you have achieved your goal of becoming a better person!" )
    print("Your final morality score is ",user.get_morality())
    if user.get_morality()> 7:
        print("Wow, you have really grown a lot. The villagers crowd around you...")
        sleep(.5)
        print("HIP")
        sleep(.5)
        print("HIP")
        sleep(.05)
        print("HURRAY")
        print("You have completed your quest to become a better ", user.get_species(), "along with your sidekick the", comp.get_species(),". Now you can look forward to your life as a better person.")
    else:
        print("Oh...")
        sleep(.5)
        print("there is an awkward silence as the villagers gather around you grumbling under their breath")
        sleep(.5)
        print("Someone breaks the silence with an angry yell, and then a farmer advances towards you brandishing a pitchfork")
        print("In your failure to be a better person, you have managed to anger the entire town. You turn to the ", comp.get_species(),"and shout RUN")
        print("You flee the town in shame, never to return. Maybe next time you'll be a better person.")
        #ending
        #either their morality is high enough that they can become a better person and the town celebrates
        #or the town hates them for destroying their community



def update_stats(user, comp):
        print(user,"\n\n", comp)



main()