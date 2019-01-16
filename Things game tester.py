import time
class Thing(object):
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
    def Quit(self):
        #here, if the user quits, the program waits, then ends.
        print("Goodbye!")
        time.sleep(2)
        quit
    def blow_up(self):
        #blowing up a Thing when prompted.
        #not going to blow up thing if thing cannot blow up!
        if self.can_blow_up == True:
            print("KA-BOOOM!!!\nThe program will now end because it has nothing to do.")
            #waiting for the user to read KA-BOOM...
            time.sleep(1)
            #...and making sound effects.
            print("\a")
            time.sleep(5)
            quit
        #if the Thing cannot blow up, an error message will show.
        elif self.can_blow_up == False:
            print("Sorry, your Thing cannot blow up.\nThe program will continue running as normal.")
            #Waiting for the user...
            time.sleep(4)
        #And now, if the Thing does not have a valid value assigned to it, the program will crash. 
        else:
            print("\a\a\a\a\a\a\asomething went wrong!")
            time.sleep(2)
            quit
    def describe(self):
        #tell the player about his/her Thing.
        print("The name of your Thing is:", self.name)
        time.sleep(2)
        print("All other known information about your Thing:", self.description)
        self.__pass_time
    def __pass_time(self):
        #first, check if the Thing needs food.
        if self.need_food == True:
            #then, incrase its hunger by 1.
            self.hunger += 1
        #if the Thing needs to be played with, its bordem inceases.
        if self.need_play == True:
            self.bored += 1
    def feed(self, food = 4):
        self.hungry -= food
        if hungry < 0:
            sick = True
            hungry = 4
            bored += 1
            self.rest(16)
        self.__pass_time()
    def play_with(self, fun = 4):
        self.bored -= fun
        if bored < 0:
            tired = True
            bored = 4
            self.rest()
        self.__pass_time()
    def talk(self):
        mood = self.bored + self.hungry
        if self.sick == True:
            mood += 6
        if self.tired == True:
            mood += 2
        if mood == 0:
            mood = "Great!"
        if mood < 4 and mood > 0:
            mood = "Happy!"
        if mood < 9 and mood > 4:
            mood = "Okay."
        if mood < 13 and mood < 9:
            mood = "Unhappy."
        else:
            mood = "Mad."
        print("I'm feeling", mood)
        self.__pass_time()
    def rest(self, sec = 8):
        print("Your Thing is resting...shhh.")
        time.sleep(sec)
thing1 = Thing(None, None, None, True, True, 9, 8)
thing1.talk()
thing1.play_with
