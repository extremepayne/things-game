#imoprts
import time



#Making the class Thing, the main component of the game.
class Thing(object):
    """The user's personal \"pet\""""
    def __init__(self, name, description, can_blow_up, need_food, need_play, bored = 4, hungry = 4, sick = False, tired = False):
        #preparing the object's attributes.
        self.name = name
        self.description = description
        self.can_blow_up = can_blow_up
        self.hungry = hungry
        self.bored = bored
        self.need_food = need_food
        self.need_play = need_play
        self.tired = tired
        self.sick = sick
    def blow_up(self):
        #blowing up a Thing when prompted.
        #not going to blow up thing if thing cannot blow up![although only blow-up-able Things should reach
        if self.can_blow_up == True:
            print("KA-BOOOM!!!\n")
            #waiting for the user to read KA-BOOM...
            time.sleep(0.9)
            #...and making sound effects.
            print("\a")
            time.sleep(3)
            quit(code = None)
        #if the Thing cannot blow up, an error message will show.
        else:
            print("Sorry, your Thing cannot blow up.\n")
            #Waiting for the user...
            time.sleep(4)            
    def describe(self):
        #tell the player about his/her Thing.
        print("Your thing is a", self.name)
        time.sleep(1)
        if self.can_blow_up == True:
            print("Your", self.name, "can blow up.")
        else:
            print("Your", self.name, "cannot blow up.")
        time.sleep(1)
        if self.need_food == True:
            print("Your", self.name, "will need food as time passes.")
        else:
            print("Your", self.name, "does not need food.")
        time.sleep(1)
        if self.need_play == True:
            print("Your", self.name, "will get bored if not played with.")
        else:
            print("Your", self.name, "does not need to be played with.")
        time.sleep(1)
        if self.description:
            if self.description.lower() != "nothing":
                print("All other known information about your", self.name, ":\n", self.description)
        time.sleep(2)
        self.__pass_time
    def __pass_time(self):
        #first, check if the Thing needs food.
        if self.need_food == True:
            #then, incrase its hunger by 1.
            self.hungry += 1
        #if the Thing needs to be played with, its bordem inceases.
        if self.need_play == True:
            self.bored += 1
    def feed(self):
        if self.need_food:
            print("Your", self.name, "is eating.")
            time.sleep(1)
            self.hungry -= 3
            if self.hungry < 0:
                self.sick = True
                hungry = 4
                self.bored += 1
                self.__rest(11, "Your " + self.name + " is not feeling well...")
            self.__pass_time()
        else:
            print("Sorry, I don't recognize the thing you want to do.")
    def play_with(self):
        self.bored -= 3
        print("Your ", self.name, " is going down the slide... WHEEE and swinging on the swings... WHEEE!", sep = "")
        if self.bored < 0:
            tired = True
            self.bored = 3
            self.__rest(message = "Your " + str(self.name) + " is sleeping because it played too much...shhhh...")
        self.__pass_time()
    def talk(self):
        if self.need_food or self.need_play:
            mood = self.bored + self.hungry
            if self.sick == True:
                mood += 6
            if self.tired == True:
                mood += 2
            if mood == int(2):
                mood = "great!"
            elif mood < int(5) and mood > int(2):
                mood = "happy!"
            elif mood < int(11) and mood > int(5):
                mood = "okay."
            elif mood < int(14) and mood < int(11):
                mood = "unhappy."
            else:
                mood = "mad."
            print("I'm feeling", mood)
            self.__pass_time()
            time.sleep(1)
        else:
            print("Sorry, I don't recognize the thing you want to do.")
    def __rest(self, sec = 8, message = ""):
        print(message)
        time.sleep(sec)
        #now, if the Thing is tired or sick, it recovers.
        if self.sick == True:
            self.sick = False
        if self.tired == True:
            self.tired = False
#code consolidation implemeted 
def ask_yes_no(question):
    """Ask for a yes or no response."""
    response = input(question)
    response = response.lower()
    while response not in ("y", "n"):
        #Extra feedback to user
        print("That was not either y or n.")
        response = input(question)
    if response == "y":
        response = True
    else:
        response = False
    return response

#introduces the user.
print("Welcome to the Thing game, where you can manipulate a Thing of your own!")
#waiting for the statement to be read and registered by the mind.
time.sleep(3)
#Now for the user's Thing
name_thing = input("What is your Thing called? (Please do not include the word \"a\") ")
blowUp = ask_yes_no("Can your " + str(name_thing) + " blow up? Answer y for yes, n for no. ")
play_1 = ask_yes_no("Does your " + str(name_thing) + " need to be played with? Answer y for yes, n for no. ")
food_1 = ask_yes_no("Does your " + str(name_thing) + " need to be fed? Answer y for yes, n for no. ")

print("What else is worth knowing about your", name_thing, end = "")
describe_thing = input("? ")
user_thing = Thing(name_thing, describe_thing, blowUp, food_1, play_1)
quit = None
while quit != True:
    menu = "\n"
    menu += "q - Quit\n"
    menu += "l - Look at info about your " + user_thing.name +  ".\n"
    if user_thing.can_blow_up:
        menu += "b - Blow your " + user_thing.name +   " up.\n"
    if user_thing.need_play:
        menu += "p - Play with your " + user_thing.name +  ".\n"
    if user_thing.need_food:
        menu += "f - Feed your " + user_thing.name +  ".\n"
    if user_thing.need_food or user_thing.need_play:
        menu += "t - Have your " + user_thing.name + " talk about its feelings.\n"
    print(menu)
    do = input("Please make a selection from the list above. ")
    do = do.lower()
    if do == "b":
        if "b - Blow your " in menu:
            user_thing.blow_up()
            break
    elif do == "q":
        quit = True
    elif do == "l":
        user_thing.describe()
    elif do == "p":
        user_thing.play_with()
    elif do == "f":
        user_thing.feed()
    elif do == "t":
        user_thing.talk()
    else:
        print("Sorry, I don't recognize the thing you want to do.")

print("Goodbye!")
input("Press enter to exit.")