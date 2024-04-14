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
            
        epic_story(user, computer)
    
# Witch and Elf Storyline
def epic_story(user, computer):
    from time import sleep
    st.write("The witch and the elf are neighbors who live together in the forest.")
    st.write("They collectively decide that they want to make more friends, as they feel isolated from everyone else who lives in town.")
    if user.get_health() > 0:
        sleep(3)
        task1(user, computer)
    if user.get_health() > 0:
        sleep(3)
        task2(user, computer)
    if user.get_health() > 0:
        sleep(3)
        task3(user, computer)
    if user.get_health() > 0:
        sleep(3)
        task4(user, computer)
    if user.get_health() > 0:
        sleep(3)
        task5(user, computer)

def task1(user, computer):
        st.write("𖠰↟𖠰𖠰", "The witch and the elf begin their journey in the forest.", "𖠰𖠰↟𖠰↟")
        sleep(1)
        st.write("They're walking together when all of a sudden, a girl in a red cape runs by.")
        sleep(1)
        st.write(user.get_species(), ": What was that?")
        sleep(1)
        st.write(computer.get_species(), ": Uhhh... ")
        sleep(2)
        st.write(computer.get_species(), ": I didn't see anything?")
        sleep(1)
        st.write("The girl runs by again but this time a wolf is chasing her.")
        sleep(1)
        st.write("Girl: HELP! PLEASE! HE'S TRYING TO EAT ME!!")
        sleep(1)
        help = st.text_input("Do you help? (y/n) ")
        while help not in "yn":
            help = st.text_input("Choose either y or n: ")
        if help == "y":
            st.write("Wolf: If you want to defeat me, you must answer this question.")
            if user.get_species() == "Witch":
                answer = st.text_input("What is the periodic symbol for Mercury? ")
                if answer == "Hg":
                    st.write("You bludgeon the wolf to death with your broomstick. He's not eating NOBODY.")
                    sleep(1)
                    st.write("Tiny Crimson: ...")
                    sleep(3)
                    st.write("Tiny Crimson: You killed him...")
                    sleep(1)
                    st.write("Tiny Crimson: THANK YOU!!! As a thank you, here's my cape.")
                    user.set_friends("Tiny Crimson")
                    sleep(3)
                    st.write("You made a new friend!")
                    st.write("Friends: ", user.get_friends())
                else:
                    st.write("You were mauled to death by the wolf...")
                    sleep(2)
                    st.write("GAME OVER.")
                    user.set_health(0)
            if user.get_species() == "Elf":
                answer = st.text_input("What is the derivative of cos(x)? ")
                if answer == "-sin(x)":
                    st.write("You shoot the wolf in the heart with an arrow.")
                    st.write("Tiny Crimson: ...")
                    sleep(3)
                    st.write("Tiny Crimson: You killed him...")
                    sleep(1)
                    st.write("Tiny Crimson: THANK YOU!!! As a thank you, here's my cape.")
                    user.set_friends("Tiny Crimson")
                    sleep(3)
                    st.write("You made a new friend!")
                    st.write("Friends: ", user.get_friends())
        elif help == "n":
            st.write("You were munched to death by the Wolf...")
            sleep(2)
            st.write("GAME OVER.")
            user.set_health(0)
        else:
            st.write("THE WOLF CONSUMED THE GIRL! YOU'RE NEXT!!!!!")
            user.set_health(0)
            st.write("GAME OVER")

def task2(user, computer):
        st.write("After encountering the wolf, the witch and the elf enter the town.")
        sleep(3)
        st.write(user.get_species(), ": I smell pie!")
        sleep(3)
        st.write(computer.get_species(), ": There's a bakery down the street. Let's go!")
        sleep(3)
        st.write("Baker: Hey kids! Will you help us make pie?")
        help = st.text_input("Do you help them? (y/n) ")
        while help not in "yn":
            help = st.text_input("Choose either y or n: ")
        if help == "y":
            answer = st.text_input("What are the first 6 digits of pi? ")
            if answer == "3.14159":
                st.write("Baker: You're a natural! This is the most delicious pie I've ever had.")
                user.set_friends("Baker")
                user.set_friends("Baker's Wife")
                sleep(3)
                st.write("You've made 2 new friends!")
                st.write("Friends: ", user.get_friends())
            else:
                st.write("Baker: This is horrendous! I've never tasted a pie this bad in my life. Get out!")
        else:
            st.write("The Baker is offended. He grabs a pie and stuffs it in your face.")
            st.write("Baker: Get out of my sight.")
            health = user.get_health() - 30
            user.set_health(health)
            st.write("You've lost 30 health :(")

def task3(user, computer):
        st.write("The witch and the elf now make their way through town and spot a candy house.")
        sleep(2)
        st.write("You see a figure approach you....")
        sleep(3)
        st.write("Witch: Hello, I was wondering if you could come refurbish my candy house?")
        sleep(2)
        st.write(user.get_species(), ": Oh! Well, yes of course!")
        sleep(2)
        st.write("Witch: Thank you dears, just follow me.")
        sleep(2)
        st.write("The Witch leads you through the forest.")
        sleep(2)
        st.write(computer.get_species(), ": Do you see that? There's breadcrumbs all over.")
        sleep(2)
        st.write(user.get_species(), ": Yeah, thats strange...")
        sleep(2)
        st.write("Witch: Just head on in dears.")
        sleep(5)
        st.write("The exterior of the candy house appears to have bite marks on it. You walk inside the house and immediately begin to sweat. It feels 10 degrees hotter.")
        sleep(4)
        st.write("The interior of the house is covered in muddy footsteps. You notice the footsteps are small, almost as if it were a child.")
        sleep(2)
        st.write(user.get_species(), ": Lets just get to cleaning.")
        sleep(2)
        st.write(computer.get_species(), ": Alright, I'll start in the kitchen.")
        sleep(3)
        st.write("...", user.get_species(), " come here")
        sleep(2)
        st.write("You walk into the kitchen, seeing ", computer.get_species(), "staring horrified at the oven. The room is boiling.")
        sleep(2)
        answer = st.text_input("Open the oven? (y/n) ")
        sleep(2)
        while answer not in "yn":
            answer = st.text_input("Choose either y or n: ")
        if answer == "y":
            st.write("You open the oven and two small children scramble out. They're covered in burn marks.")
            sleep(2)
            st.write(user.get_species(), ": Woah... are you two okay?")
            sleep(2)
            st.write("Boy: GET AWAY FROM US!")
            sleep(2)
            st.write("The boy swats burning charcoals from the oven. It burns your skin.")
            sleep(2)
            health = user.get_health() - 20
            user.set_health(health)
            st.write(user.get_species(), ": OW!!")
            st.write(computer.get_species(), ": Wait stop! We aren't going to hurt you, I promise. Trust me!")
            sleep(2)
            st.write("Girl: You're a liar! AND you're a witch!")
            sleep(2)
            if user.get_species() == "Witch":
                st.write(user.get_species(), ": I'm a good witch, I promise. Just tell me what happened.")
            else:
                st.write(computer.get_species(), ": I'm a good witch I promise, just tell me what happened.")
            sleep(2)
            st.write("Boy: It was the other Witch! She punished us for eating some of her candy house by trying to cook us!")
            sleep(2)
            st.write("The door creaks open.")
            sleep(2)
            answer = st.text_input("Fight the Witch? y/n ")
            while answer not in "yn":
                answer = st.text_input("Choose either y or n: ")
            if answer == "y":
                answer1 = st.text_input("What kind of function is f(x)=x^4? ")
                if answer1 == "quartic" or "Quartic":
                    if user.get_species()=="Witch":
                        st.write("You break the bottom of your broomstick off and drive it into the witch's chest. She is dead.")
                        sleep(2)
                        st.write("The two children stare blankly for a moment.")
                        sleep(3)
                        st.write("Boy: Woah. Thank you! You really are a good witch.")
                    else:
                        st.write("You take an arrow out of your quiver and charge at the witch. She parries but your agility allows you to strike quickly again. You drive it into her chest and she falls. She is dead.")
                        sleep(2)
                        st.write("The two children stare blankly for a moment.")
                        sleep(2)
                        st.write("Boy: Woah. Thank you. Here, take this.")
                        st.write("The boy hands you 10 gold coins.")
                        money = user.get_money() + 10
                        user.set_money(money)
                    user.set_friends("Girl")
                    user.set_friends("Boy")
                    sleep(3)
                    st.write("You've made new friends!")
                    st.write(user.get_friends())
                else:
                    st.write(user.get_species(), ": Let's just ignore it, we've got a job to do.")
                    sleep(2)
                    st.write("You quickly sweep and mop the house, dust the shelves, and shine the peppermint furniture.")
                    sleep(2)
                    st.write("The door creaks open.")
                    sleep(2)
                    st.write("Witch: Wow. It looks lovely in here!")
                    sleep(2)
                    st.write(computer.get_species(), ": Ha ha ha ha. ha yes thank you so much.")
                    sleep(2)
                    st.write("The Witch glares suspiciously at ", computer.get_species())
                    sleep(2)
                    st.write("Witch: Well thank you for a job well done, here is your payment!")
                    sleep(3)
                    new_health = user.get_health + 100
                    user.set_health(new_health)
                    st.write("Witch: I've healed you to full health my friends.")
                    user.set_friends("Witch")
                    sleep(3)
                    st.write("The witch is now your friend!")
                    st.write("Friends: ", user.get_friends())
                
def task4(user, computer):
        st.write("↟𖠰↟𖠰 You begin another long walk within the forest. 𖠰↟𖠰𖠰")
        sleep(2)
        st.write("You stumble across a large cobblestone bridge which towers unnecessarily above a small stream, it seems almost useless to even go over it")
        sleep(2)
        st.write ("???: IT IS I...")
        sleep(3)
        st.write("R: ...Rumplestiltzkin!")
        sleep(2)
        st.write("R: Now that you've found me, you must answer my riddles 3 or you may never escape! >:D")
        st.write("R: First...")
        sleep(3)
        riddleoneanswer = st.text_input("What feels like green paint, smells like green paint, but isn't green paint? ")
        if riddleoneanswer == ("paint"):
            st.write("R: WOAH you've answered my riddle one... and got it correct, i'm honestly stunned. Just as a reward you will answer just one more riddle... MY RIDDLE ONE!")
        else:
            st.write("R: heh heh, just as i suspected you got it UNBELIEVABLY incorrect. The only way to save you now is to answer one final riddle. MY RIDDLE ONE!")
        riddletwoanswer = st.text_input("R: What is my name heh heh? ")
        if riddletwoanswer == ("rumplestiltzkin") or ("Rumplestiltzkin"):
            st.write("....")
            sleep(3)
            st.write("Rumplestiltzkin: I have absolutely no clue how you knew that...")
            sleep(2)
            st.write("Rumplestiltzkin: well a deal is a deal and I shall set you free, and with a reward I suppose. And of course access to my bridge!")
            st.write(user.get_species(), ": oh... thanks i guess.")
            money = user.get_money() + 10
            user.set_money(money)
            user.set_friends("Rumplestiltzkin")
        else:
            st.write("Rumplestiltzkin: L! haha you absolute bafoon that is just not my name. now you must pay the price of prices! 3 pieces of gold in payment for my riddles 3")
            money = user.get_money() - 3
            user.set_money(money)


def task5(user, computer):
        st.write("The witch and the elf have reached the end of the forest.")
        sleep(3)
        st.write("Ahead of them lies the Queen's castle. But the gates are wide open.")
        sleep(3)
        st.write(user.get_species(), ": If the gates are open I guess we can go inside.")
        sleep(3)
        st.write("You enter the castle and find a tall spiral staircase. Someone is snoring really loud at the top.")
        sleep(4)
        st.write(computer.get_species(), ": Who could that be?")
        sleep(2)
        st.write("The two of you start climbing the stairs and discover a beautiful woman asleep in bed.")
        sleep(4)
        st.write(computer.get_species(), ": According to this note only a true love's kiss will wake her up.")
        sleep(4)
        help = st.text_input("Do you kiss her? (y/n) ")
        while help not in "yn":
            help = st.text_input("Choose either y or n" )
        if help == "y":
            st.write("The princess's eyes flutter open.")
            if user.get_species() == "Witch":
                sleep(2)
                st.write("She lays eyes on you and screams. She grabs the teapot beside her bed and smashes it on your head.")
                sleep(4)
                st.write("Princess: EWWW! Witch!")
                health = user.get_health() - 30
                user.set_health(health)
                st.write("You fall to the floor in shock. You lost 30 health.")
                sleep(3)
                st.write(user.get_species(), ": I'm a good witch! Why does everyone think I'm bad? :(")
                sleep(3)
                st.write("Princess: I'm sorry. I jumped to conclusions. Let's get married!")
            else:
                st.write("Princess: Oh! You saved me!")
                sleep(2)
                st.write("She kisses you.")
                sleep(2)
                st.write("Princess: Will you marry me?")
                sleep(2)
                st.write(user.get_species(), ": Yes!")
            money = user.get_money() + 1000000
            user.set_money(money)
            st.write("You now have", user.get_money(), " moneys.")
            sleep(2)
            st.write("And they lived happily ever after. The end.")
        else:
            st.write("As you're standing beside the bed, two guards barge in unannounced.")
            sleep(3)
            st.write("Guard 1: Are you the one's who poisoned the princess?")
            sleep(3)
            st.write("Guard 2: Get them!!")
            sleep(2)
            st.write("Without giving them a chance to deny, the two guards barge forward and put you in handcuffs.")
            sleep(4)
            st.write("You're dragged off to the town prison where you're sentenced to a lifetime behind bars.")
            sleep(4)
            st.write("And they lived not so happily ever after.")


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
                st.write("the farmer says, 'Thank you for fixing my fence! I will forever be grateful for your help.' \n You have gained morality points")
                user.set_morality(1)

        elif ahh=="no":
            user.set_morality(-1)
            st.write("The farmer starts crying as you deny her request and yells after you, 'You two are evil and I hope you never experience joy again!'\nYou have lost morality points")

        st.write(user)
            

        # 1 fix a broken fence so cows don't escape
        #Good: they fix it, Bad: they don't and the cows escape
def task_2(user, comp):    
        from time import sleep
    # update_stats(user, comp)  
    # 2 Mythicical sheep eating beast or feral pig
        st.write("You and the ", comp.get_species(), "are talking over the results of the last task when... ")
        sleep(.5)
        st.write("you hear a scream coming from the town hall!")
        go = st.text_input("Go investigate? (y/n): ")
        if go == "n":
            go = st.text_input("are you SURE? (y/n): ")
            if go == "n":
                user.set_morality(-2)
                st.write("Wow... you lose morality points for not caring about your town!")
                st.write("A farmer runs up to you as you stand pointlessly in the middle of the town")
            else:
                user.set_morality(1)
                st.write("Good choice. You enter the town hall and encounter a frazzled farmer.")
        else:
            user.set_morality(2)
            st.write("You encounter a frazzled farmer and ask what the matter is.")
        st.write("He says 'Please help me! A evil beast is eating my sheep and I don't know what to do.'\n You and your companion head to the edge of the woods and encounter a wild beast!\n The beast has sharp teeth but strangly compassionate eyes. It roars at you.")
        attack = st.text_input("Begin your attack? (y/n): ")
        if attack =="y":
            st.write("The monster wails and takes damage from your ", user.get_weapon())
            user.set_morality(2)
            st.write("The monster finally collapses! \n You saved the town! If you had spared the monster, all the sheep would have been eaten. Good job!")
        else:
            user.set_morality(1)
            st.write("You spared the monster, at the expense of the village! All the farmers sheep will be eaten. \n Your compassion was admirable but ill-fated.")

def task_3(user, comp):    
        st.write("The owner of the horse stables needs help \n He says, 'One of my farm hand got pneumonia and died, the other got the bubonic plauge and died! I need someone to help muck my horse stable!'\n If you help you will get covered in horse manure, the princess is very vain and will be upset if she gets dirty, \n and the hobbit will lose health because he is so short that he will accidentally ingest some of the manure as he is mucking the stable")
        ahh = st.text_input ("Will you help muck the stables? (yes/no): ")
        if ahh=="yes":
            if user.get_species()=="Hobbit":
                user.set_health(50)
            st.write("You need to figure out how many shovel fulls of manure you need to move \nEach shovel full will clear 1 square foot of space, the stable is 36ft by 60ft")
            temp=st.text_input( "How many shovel fulls will you have to do to clear the entire stable: " )
            if temp== "2160":
                st.write("You need to know how many days it will take you to clear the stable. \n Each shovel will take 1 minute, but it is winter and the days are short so you can only work 6 hours each day. Remember that there are two of you so it will take half the time")
                tem=st.text_input("How many days will it take you to clear the stable: ")
                if tem=="3":
                    st.write("Good job! The stable owner is so appreciative of your help that he will allow you to take a shower in his home before seeing you off.\nYou have gained morality points!")
                    user.set_morality(1)
                else:
                    st.write("You have failed the stable owner, in response to your stupidity he says,'You are dirty and unhelpful! You better wish I never see you again or you will face the wrath of my meanist unicorn'\nYou have lost morality points :(")
                    user.set_morality(-1)
            else:
                st.write("You have failed the stable owner, in response to your stupidity he says,'You are dirty and unhelpful! You better wish I never see you again or you will face the wrath of my meanist unicorn'\nYou have lost morality points :(")
                user.set_morality(-1)
        elif ahh=="no":
            st.write("The stable owner is upset that you won't help him and says, 'You are fair too proud and vain. I will be celebrating the day you die, I will dance on your grave and graffiti your headstones'\nYou have lost morality points")
            user.set_morality(-1)
        st.write(user)
            
        # 3 Mucking the horse stables
        #Good: They do it (and are smelly) Bad: They refuse because they are proud/lazy and lose respect 
def task_4(user, comp):    
        st.write("You and the ", comp.get_species(), "are wandering around the town when you encounter a child crying on the sidewalk. She looks a little odd, with a unsettling green tint to her skin." )
        help = st.text_input("Would you like to ask the child what is wrong? (y/n): ")
        if help == "n":
            user.set_morality(-2)
            st.write("You leave the child crying in the streets. Not a good look. You're going to lose some morality for that.")
        else:
            st.write("The child wipes her runny nose and then tells you that she got lost and needs help to find her way back home....")
            help= st.text_input("Do you help her find her way back home? (y/n): ")
            if help == "y":
                user.set_morality(3)
                st.write("How kind of you! You gain morality points and become a better person!")
            else:
                user.set_morality(-2)
                st.write("Wow. That is cold. You lose some morality.")
            # 4 Helping a lost child (5 yrs and kinda snotty)
            # Good: help find their family Bad: leave child on the ground
def task_5(user, comp):
    from time import sleep
    st.write("You and the ", comp.get_species(), "here a distressed wail from the otherside of town")
    ahh=st.text_input(" Do you invistigate? (yes/no)")
    if ahh=="yes":
        st.write("As you approach you hear a belligerent woman yelling about an eviction notice\nThe ",comp.get_species()," asks, 'Are you sure we should investigate?'" )
        sleep(.5)
        st.write("You hesitate before responding 'If she needs help we should help her' \nAs you approach she becomes more erratic screaming,'I need $10,000 by tomorrow to stay in my house??? This is RIDICULOUS!!!!'")
        st.write("A villager approaches you and says, 'That's Pamela she's awful, no one likes her because she is mean to everyone.'")
        ahhh=st.text_input("Do you want to try to help Pamela?(yes/no) ")
        if ahhh=="yes":
            st.write("You go up to her and ask Pamela what's wrong\nShe screams'I'M GOING TO LOSE MY HOUSE, AN OGRE IS GOING TO EAT IT IF I DON'T GIVE HIM TEN THOUSAND DOLLARS BY TOMORROW MORNING!!!!")
            if user.get_species()=="Hobbit":
                st.write("You must convince the Princess to give all of her money to Pamela, so that the ogre doesn't eat Pamela's house")
                note=st.text_input("Write a note convincing the Princess to give all of her money away:")
                if len(note)>50:
                    st.write("You have convinced the princess to give away all of her money!\nYou have gained morality points!")
                    user.set_morality(3)
                else:
                    st.write("Your note was not convincing enough\n the Princess responds, 'This is ridiculous Pamela is an awful person and deserves any and all karma coming her way, including an ogre eating her house.")
                    sleep(.5)
                    st.write("You have lost morality points :(")
                    user.set_morality(-3)
            else:
    
                st.write("You contemplate giving your money away, if you do you'll have no more money, but Pamela needs it more than you do")
                sleep(.9)
                st.write('...right?')
                st.write("The Hobbit looks up (because he is three foot six) at you with pleading eyes\nHe says,'It's the right thing to do, to give her the money. I mean we don't really need money, and you can always fall back on your trust fund'")
                st.write("The Hobbit doesn't know that you don't have access to your trust fund for another 5 years")
    
                think=st.text_input("Do you give mean pamela ALL of your money? (yes/no) ")
                if think=="yes":
                    sleep(.5)
                    st.write("Pamela thanks you before running into the woods to find the ogre")
                elif think=="no":
                    st.write("Pamela continues wailing as she comes to terms with the fact that her house and all possessions will be eaten by an ogre in the morning\n You lose morality points :(")
                    user.set_morality(-3)
        elif ahhh=="no":
            st.write("You're a bad person and lose morality points")
            user.set_morality(-3)
    elif ahh=="no":
        st.write("You're a bad person and lose morality points")
        user.set_morality(-3)

def ending(user, comp):
        from time import sleep
        st.write("You have reached the end of your journey, ",user.get_species(),"and it is time to discover whether you have achieved your goal of becoming a better person!" )
        st.write("Your final morality score is ",user.get_morality())
        if user.get_morality()> 7:
            st.write("Wow, you have really grown a lot. The villagers crowd around you...")
            st.write(.5)
            st.write("HIP")
            sleep(.5)
            st.write("HIP")
            sleep(.05)
            st.write("HURRAY")
            st.write("You have completed your quest to become a better ", user.get_species(), "along with your sidekick the", comp.get_species(),". Now you can look forward to your life as a better person.")
        else:
            st.write("Oh...")
            sleep(.5)
            st.write("there is an awkward silence as the villagers gather around you grumbling under their breath")
            sleep(.5)
            st.write("Someone breaks the silence with an angry yell, and then a farmer advances towards you brandishing a pitchfork")
            st.write("In your failure to be a better person, you have managed to anger the entire town. You turn to the ", comp.get_species(),"and shout RUN")
            st.write("You flee the town in shame, never to return. Maybe next time you'll be a better person.")
            #ending
            #either their morality is high enough that they can become a better person and the town celebrates
            #or the town hates them for destroying their community

def update_stats(user, comp):
        print(user, comp)
        
def instructions():
    st.write("Welcome to the epic fairytale adventure program! \n In this program, you will be a character of your choice that gets placed in an adventure, along with your trusty sidekick. \n You will advance through the game.")

main()
