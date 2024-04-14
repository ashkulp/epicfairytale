import time
import streamlit as st
class Person:

    def __init__(self, weapon = None, money = None, agility = None, health = None, species = None, morality = None, height = None):
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
    st.set_page_config("instructions")
    instructions()
    user_char = st.text_input("What character would you like to be? Select 1 for princess, 2 for hobbit, 3 for witch, 4 for elf: ")
    while user_char != "1" and user_char != "2" and user_char != "3" and user_char != "4":
        user_char = input("Please choose a number between 1 and 4: ")

    if user_char=="1" or user_char=="2":
        
        if user_char== "1":
            user=Person("fancy dagger",1000000,3,100,"Princess",0,64)
            computer=Person("club",4,7,60,"Hobbit",0,42)
                
        if user_char == "2":
            computer=Person("fancy dagger",1000000,3,100,"Princess",0,64)
            user=Person("club",4,7,60,"Hobbit",0,42)

        town_story(user, computer)
        
    if user_char == "3" or user_char == "4":
    
        if user_char == "3":
            user = Person("broomstick", 5, 4, 100, "Witch", None, 63)
            computer = Person("longbow", 0, 8, 100, "Elf", None, 69)
            
        if user_char == "4":
            user = Person("longbow", 0, 8, 100, "Elf", None, 69)
            computer = Person("broomstick", 5, 4, 100, "Witch", None, 63)
            
        epic_story(user)
    
# Witch and Elf Storyline
def epic_story(user):
    print("The witch and the elf are neighbors who live together in the forest.")
    print("They collectively decide that they want to make more friends, as they feel isolated from everyone else who lives in town.")
    while user.get_health() <= 0:
        task1()
    while user.get_health() <= 0:
        task2()
    while user.get_health() <= 0:
        task3()
    while user.get_health() <= 0:
        task4()
    while user.get_health() <= 0:
        task5()

    def task1(user, computer):
        print("𖠰↟𖠰𖠰", "The witch and the elf begin their journey in the forest.", "𖠰𖠰↟𖠰↟")
        print("They're walking together when all of a sudden, a girl in a red cape runs by.")
        print(user.get_species() + ": What was that?")
        print(computer.get_species() + ": Uhhh... " + time(2), "I didn't see anything?")
        print("The girl runs by again but this time a wolf is chasing her.")
        print("Tiny Crimson Commuting Cowl: HELP! PLEASE! HE'S TRYING TO EAT ME!!")
        help = input("Do you help? (y/n) ")
        while help not in "yn":
            help = input("Choose either y or n: ")
        if help == "y":
            print("Wolf: If you want to defeat me, you must answer this question.")
            if user.get_species() == "Witch":
                answer = input("What is the periodic symbol for Mercury?" )
                if answer == "Hg":
                    print("You bludgeon the wolf to death with your broomstick. He's not eating NOBODY.")
                else:
                    print("You were mauled to death by the wolf...", time(2), "GAME OVER.")
                    user.set_health(0)
            if user.get_species() == "Elf":
                answer = input("What is the derivative of cos(x)?")
                if answer == "-sin(x)":
                    print("You shoot the wolf in the heart with an arrow.")
            print("Tiny Crimson Commuting Cowl: ...", time(3), "You killed him...", time(1), "THANK YOU!!! As a thank you, here's my cape.")
            user.set_friends("Tiny Crimson Commuting Cowl")
            print("You made a new friend!")
            print("Friends: " + user.get_friends())
        elif help == "n":
            print("You were munched to death by the Wolf...", time(2), "GAME OVER.")
            user.set_health(0)
        else:
            print("THE WOLF CONSUMED THE GIRL! YOU'RE NEXT!!!!!")
            user.set_health(0)
            print("GAME OVER")

    def task2(user, computer):
        print("After encountering the wolf, the witch and the elf enter the town.")
        print(user.get_species() + ": I smell pie!")
        print(computer.get_species() + ": There's a bakery down the street. Let's go!")
        print("Baker: Hey kids! Will you help us make pie?")
        help = input("Do you help them? (y/n) ")
        while help not in "yn":
            help = input("Choose either y or n: ")
        if help == "y":
            answer = input("What are the first 6 digits of pi? ")
            if answer == "3.14159":
                print("Baker: You're a natural! This is the most delicious pie I've ever had.")
                user.set_friends("Baker")
                user.set_friends("Baker's Wife")
                print("You've made 2 new friends!")
                print("Friends: " +  user.get_friends())
            else:
                print("Baker: This is horrendous! I've never tasted a pie this bad in my life. Get out!")
        else:
            print("The Baker is offended. He grabs a pie and stuffs it in your face.")
            print("Baker: Get out of my sight.")
            health = user.get_health() - 30
            user.set_health(health)
            print("You've lost 30 health :(")

    def task3(user, computer):
        print("You see a figure approach you....", time(3))
        print("Witch: Hello, I was wondering if you could come refurbish my candy house?")
        print(user.get_species() + ": Oh! Well, yes of course!")
        print("Witch: Thank you dears, just follow me.")
        print("The Witch leads you through the forest.")
        print(computer.get_species(), ": Do you see that? There's breadcrumbs all over.")
        print(user.get_species(), ": Yeah, thats strange...")
        print("Witch: Just head on in dears.")
        print("The exterior of the candy house appears to have bite marks on it. You walk inside the house and immediately begin to sweat. It feels 10 degrees hotter.")
        print("The interior of the house is covered in muddy footsteps. You notice the footsteps are small, almost as if it were a child.")
        print(user.get_species(), ": Lets just get to cleaning.")
        print(computer.get_species(), ": Alright, I'll start in the kitchen.", time(5), "... ", user.get_species(), " come here")
        print("You walk into the kitchen, seeing ", computer.get_species(), "staring horrified at the oven. The room is boiling.")
        answer = input("Open the oven? y/n ")
        while answer not in "yn":
            if answer == "y":
                print("You open the oven and two small children scramble out. They're covered in burn marks.")
                print(user.get_species(), ": Woah... are you two okay?")
                print("Boy: GET AWAY FROM US!")
                print("The boy swats burning charcoals from the oven. It burns your skin.")
                health = user.get_health() - 20
                user.set_health(health)
                print(user.get_species(), ": OW!!")
                print(computer.get_species(), ": Wait stop! We aren't going to hurt you I promise, trust me!")
                print("Girl: You're a liar! AND you're a witch!")
                if user.get_species() == "Witch":
                    print(user.get_species(), ": I'm a good witch I promise, just tell me what happened.")
                else:
                    print(computer.get_species(), ": I'm a good witch I promise, just tell me what happened.")
                print("Boy: It was the other Witch! She punished us for eating some of her candy house by trying to cook us!")
                print("The door creaks open.")
                answer = input("Fight the Witch? y/n")
                while answer not in "yn":
                    if answer == "y":
                        answer1 = input("What kind of function is f(x)=x^4 ?")
                        if answer1 == "quartic" or "Quartic":
                            if user.get_species()=="Witch":
                                print("You break the bottom of your broomstick off and drive it into the witches chest. She is dead.")
                                print("The two children stare blankly for a moment", time(1))
                                print("Boy: Woah. Thank you, you really are a good witch.")
                                user.set_friends("Girl")
                                user.set_friends("Boy")
                            else:
                                print("You take an arrow out of your quiver and charge at the witch, she parries, but your agility allows you to strike quickly again. You drive it into her chest and she falls. She is dead.")
                                print("The two children stare blankly for a moment", time(1))
                                print("Boy: Woah. Thank you. Here take this.")
                                print("The boy hands you 10 gold coins.")
                                money = user.set_money() + 10
                                user.set_money(money)
                                user.set_friends("Girl")
                                user.set_friends("Boy")
                    else:
                        print("Woah buddy. That answer isn't valid. It has to be either y or n. Tsk. Tsk.")
            else:
                if answer == "n":
                    print(user.get_species(), ": Let's just ignore it, we've got a job to do.")
                    print("You quickly sweep and mop the house, dust the shelves, and shine the peppermint furniture.")
                    print("The door creaks open.")
                    print("Witch: Wow. It looks lovely in here!")
                    print(computer.get_species(), ": Ha ha ha ha. ha yes thank you so much.")
                    print("The Witch glares suspiciously at ", computer.get_species())
                    
                else:
                    print("Woah buddy. That answer isn't valid. It has to be either y or n. Tsk. Tsk.")
                
    def task4(user, computer):
        print ("IT IS I...")
        time.sleep(3)
        print("...Rumplestiltzkin!")
        print("Now that you've found me, you must answer my riddles 3 or you may never escape! >:D")
        print("First...")
        time.sleep(3)
        riddleoneanswer = input("What feels like green paint, smells like green paint, but isn't green paint? ")
        if riddleoneanswer == ("paint"):
            print("WOAH you've answered my riddle one... and got it correct, i'm honestly stunned. Just as a reward you will answer just one more riddle... MY RIDDLE ONE!")
        else:
            print("heh heh, just as i suspected you got it UNBELIEVABLY incorrect. The only way to save you now is to answer one final riddle. MY RIDDLE ONE!")
        riddletwoanswer = input("What is my name heh heh? ")
        if riddletwoanswer == ("rumplestiltzkin") or ("Rumplestiltzkin"):
            print("....")
            time.sleep(3)
            print("I have absolutely no clue how you knew that...")
            print("well a deal is a deal and I shall set you free, and with a reward I suppose")
            treasure= treasure + random.randint(1,11)
        else:
            print("haha you absolute bafoon that is just not my name. now you must pay the price of prices! 3 pieces of gold in payment for my riddles 3")
            treasure = treasure - 3

    def task5(user, computer):
        print("The witch and the elf have reached the end of town.")
        print("Ahead of them lies the Queen's castle. But the gates are wide open.")
        print(user.get_species() + ": If the gates are open I guess we can go inside.")
        print("You enter the castle and find a tall spiral staircase. Someone is snoring really loud at the top.")
        print(computer.get_species() + ": Who could that be?")
        print("The two of you start climbing the stairs and discover a beautiful woman asleep in bed.")
        print(user.get_species() + ": Who is this unconscious baddie?")
        print(computer.get_species() + ": According to this note only a true love's kiss will wake her up.")
        help = input("Do you kiss her? (y/n) ")
        while help not in "yn":
            help = input("Choose either y or n" )
        if help == "y":
            print("The princess's eyes flutter open.")
            if user.get_species() == "Witch":
                print("She lays eyes on you and screams. She grabs the teapot beside her bed and smashes it on your head.")
                print("Princess: EWWW! Witch!")
                health = user.get_health() - 30
                user.set_health(health)
                print("You fall to the floor in shock. You lost 30 health.")
                print(user.get_species() + ": I'm a good witch! Why does everyone think I'm bad? :(")
                print("Princess: I'm sorry. I jumped to conclusions. Let's get married!")
            else:
                print("Princess: Oh! You saved me!")
                print("She kisses you.")
                print("Princess: Will you marry me?")
                print(user.get_species() + ": Yes!")
            money = user.get_money() + 1000000
            user.set_money(money)
            print("You now have " + user.get_money() + " moneys.")
            print("And they lived happily ever after. The end.")
        else:
            print("As you're standing beside the bed, two guards barge in unannounced.")
            print("Guard 1: Are you the one's who poisoned the princess?")
            print("Guard 2: Get them!!")
            print("Without giving them a chance to deny, the two guards barge forward and put you in handcuffs.")
            print("You're dragged off to the town prison where you're sentenced to a lifetime behind bars.")
            print("And they lived not so happily ever after.")


#Hobbit and Princess storyline
def town_story(user, computer):
    print()
    task_1(user, computer)
    
    task_2(user, computer)
    
    task_3(user, computer)
    
    task_4(user, computer)
    
    task_5(user, computer)
    ending(user, computer)
    #tasks:
def task_1(user, comp):    
        st.write("You and the ", comp.get_species()," come across a troubled famer, her fence is broken. \n When she sees you she says,'Please help me! My fence needs fixing, but my arm is broken so I can't fix it myself. If I leave it broken all my cows will get out!")
        ahh=st.text_input("Will you help fix the fence or not (yes/no): ")
        if ahh=="yes":
            st.write ("In order to fix the fence you must hammer in all of the posts \n You will have to hammer in 6 nails, if you spell hammer wrong you will have failed to complete your task and lose morality points")
            write=st.text_input("Type out hammer: ")
            if write=="hammer":
                nail="correct"
            else:
                nail="not"
                st.write("you have failed the famer, she is crying in distress as all of her cows escape \n you have lost morality points")
                user.set_morality(-1)
            if nail=="correct":
                st.write("the farmer says, 'Thank you for fixing my fence! I will forever be grateful for your help.' \n You have gained moarality points")
                user.set_morality(1)

        elif ahh=="no":
            user.set_morality(-1)
            st.write("The farmer starts crying as you deny her request and yells after you, 'You two are evil and I hope you never experience joy again!'\nYou have lost morality points")
        else:
            st.write("error, your input is invalid try again")
            task_1(user,comp)
        st.write(user)
            

        # 1 fix a broken fence so cows don't escape
        #Good: they fix it, Bad: they don't and the cows escape
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

def task_3(user, comp):    
        print("The owner of the horse stables needs help \n He says, 'One of my farm hand got pneumonia and died, the other got the bubonic plauge and died! I need someone to help muck my horse stable!'\n If you help you will get covered in horse manure, the princess is very vain and will be upset if she gets dirty, \n and the hobbit will lose health because he is so short that he will accidentally ingest some of the manure as he is mucking the stable")
        ahh = input ("Will you help muck the stables? (yes/no): ")
        if ahh=="yes":
            if user.get_species()=="Hobbit":
                user.set_health(50)
            print("You need to figure out how many shovel fulls of manure you need to move \nEach shovel full will clear 1 square foot of space, the stable is 36ft by 60ft")
            temp=input( "How many shovel fulls will you have to do to clear the entire stable: " )
            if temp== "2160":
                print("You need to know how many days it will take you to clear the stable. \n Each shovel will take 1 minute, but it is winter and the days are short so you can only work 6 hours each day. Remember that there are two of you so it will take half the time")
                tem=input("How many days will it take you to clear the stable: ")
                if tem=="3":
                    print("Good job! The stable owner is so appreciative of your help that he will allow you to take a shower in his home before seeing you off.\nYou have gained morality points!")
                    user.set_morality(1)
                else:
                    print("You have failed the stable owner, in response to your stupidity he says,'You are dirty and unhelpful! You better wish I never see you again or you will face the wrath of my meanist unicorn'\nYou have lost morality points :(")
                    user.set_morality(-1)
            else:
                print("You have failed the stable owner, in response to your stupidity he says,'You are dirty and unhelpful! You better wish I never see you again or you will face the wrath of my meanist unicorn'\nYou have lost morality points :(")
                user.set_morality(-1)
        elif ahh=="no":
            print("The stable owner is upset that you won't help him and says, 'You are fair too proud and vain. I will be celebrating the day you die, I will dance on your grave and graffiti your headstones'\nYou have lost morality points")
            user.set_morality(-1)
        else:
            print("your input is invalid, try again")
            task_3(user,comp)
        print(user)
            
        # 3 Mucking the horse stables
        #Good: They do it (and are smelly) Bad: They refuse because they are proud/lazy and lose respect 
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
                user.set_morality(-2)
                print("Wow. That is cold. You lose some morality.")
            # 4 Helping a lost child (5 yrs and kinda snotty)
            # Good: help find their family Bad: leave child on the ground
#def task_5(user, comp):    
        # 5 Do you help Pamela (shes a bitch), she is going to lose her house and needs all your money, 
        # good: yes bad: no
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
        print(user, comp)
        
def instructions():
    st.write("Welcome to the epic fairytale adventure program! \n In this program, you will be a character of your choice that gets placed in an adventure, along with your trusty sidekick. \n You will advance through the game.")

main()
