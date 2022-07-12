# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define audio.bgm = "audio/2.ogg"
image company = im.Scale("company.jpg",1980,1080)
image fronthouse = im.Scale("house.jpg",1980,1080)
image tuanhouse = "tuanhouse.jpg"
image park = im.Scale("park.jpg",1980,1080)
image Electronic_Store = "images/Electronic_Store.jpg"
image Burger_Store = "images/Burger_Interior.jpg"
image Clothes_Store = "images/Clothes_Store.jpg"
image Sleeping = "images/Sleeping.jpg"
define Seller = Character ("Lottery Seller")
define seller = "images/Click/Lottery.png"
define mother = Character ("Ignacia", color = "00FFFF")
define Tuan = Character ("Tuan", color = "FFA500")
define Fin = Character ("Fin")
define Salesman = Character ("Salesman")
define melissa = Character ("Melissa")
define Clerk = Character ("Clerk")
define Waiter = Character("Waiter")
define Financer = Character("Mr.Literet")
define Caller = Character ("Caller")
define Francis = Character ("francis",color = "C04000")
define Franco = Character ("Franco")
define Jorge = Character ("Jorge")
define Ariana = Character ("Ariana")
define Daisy = Character ("Daisy")
define Jerome = Character ("Jerome")
define Karter = Character ("Karter")
define Leonardo = Character ("Leonardo")
define Nylah = Character ("Nylah")
image malleating = "images/malleating.jpg"
image pizzaeating = "images/pizzaeating.jpg"
image burgereating = "images/burgereating.jpg"
define mall = "mall.jpg"
image finhappy = "images/char/Fin/Fin_Happy.png"
image finsad = "images/char/Fin/Fin_Sad.png"
image finneutral = "images/char/Fin/Fin_Neutral.png"
image fincalling = "images/char/Fin/Fin_Calling.png"
image finthinking = "images/char/Fin/Fin_Thinking.png"
image tuanhappy = "images/char/Tuan/Tuan_Happy.png"
image tuansad = "images/char/Tuan/Tuan_Sad.png"
image tuanneutral = "images/char/Tuan/Tuan_Neutral.png"
image lotterygirl = "images/Lottery_Girl1.png"
#change this to char
image salesman = "images/Device_Seller.png"
image clerk = "images/Clothes_Vendor.png"
image waiter = "images/Burger_vendor.png"
image pizzastore = "images/pizzastore.jpg"

image bank = "images/bank.jpg"
image burgerstore = "images/burgerstore.jpg"
image company = "images/company.jpg"
image firedept = "images/firedept.jpg"
image government = "images/government.jpg"
image hospital = "images/hospital.jpg"
image police = "images/police.jpg"
image school = "images/school.jpg"
image francis = "images/char/Francis/Francis_Neutral.png"
image franco = "images/char/Franco/Franco_Neutral.png"
image jorge = "images/char/Jorge/Jorge_Neutral.png"
image ariana = "images/char/Ariana/Ariana_Neutral.png"
image daisy = "images/char/Daisy/Daisy_Neutral.png"
image jerome = "images/char/Jerome/Jerome_Neutral.png"
image karter = "images/char/Karter/Karter_Neutral.png"
image leonardo = "images/char/Leonardo/leonardo_Neutral.png"
image nylah = "images/char/Nylah/Nylah_Neutral.png"
image conclusion = "images/conclusion.jpg"
image conclusion2 = "images/conclusion2.jpg"
image Clothes_2 = "images/Clothes_2.png"
image Clothes_3 = "images/Clothes_3.png"









# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene fronthouse
    play music bgm
    "There's a lot of people living in this world,"
    "some of them having a hard time saving money"
    "since they are lack of financial literacy."
    "one of them is “Fin”."
    "Fin lives in a medium class of "
    "A family, since his father died since he was born."
    "He only lives in his mother right now. "
    scene mall
    "One day Fin walks into the mall to check something out."
    "walking around the mall is a habit for Fin, "
    "Suddenly he saw a new stall around the corner of the mall"
    "But he knew it's not right to go in but"
    "He feels something strange so he decided to check it out."
    "After checking it out he tries to buy a ticket."
    show lotterygirl at right
    melissa "Hi sir! want to try our raffle?"
    melissa"You just have to buy a ticket then you will get a chance to win a 10,000 Pesos."
    show finhappy at left with moveinleft
    Fin "Wow, is it real? It's very interesting."
    Fin "Can I buy 3? how much is that?"
    melissa "It's only 100 Pesos each"
    Fin "When will be the draw?"
    melissa "Tomorrow sir!"
    Fin"Really? Fine I'll be there!"
    melissa "Thank you sir, wish you luck"
    "After buying a ticket Fin exited the stall while"
    "Talking to his self."
    Fin "Maybe this is my lucky chance to win a draw."
    Fin "WHO KNOWS?"
    "AFTER THAT"
    "Fin decided to home since it's getting late"
    hide lottery girl at right
    hide finhappy at left
    scene fronthouse
    scene Sleeping
    "Fin arrives at his house then gets some sleep"
    scene fronthouse
    "It's a bright new day for Fin since it's the day"
    "for the raffle and he wants to see the result of the draw"
    "Fin rushes to eat his breakfast then take a bath."
    "After that Fin Walks to the mall"
    scene mall
    show finhappy at left
    "Fin was shookt because he saw his name on the lottery bulletin board"
    "He was so happy"
    $ MC.cash+=10000
    Fin "Wow, is this true?"
    Fin"My name is at the list of winners I have to tell this to my friend Tuan"
    "After that Fin Rushes To Go Back Home To Call Tuan"



    # These display lines of dialogue.






    $ Playing = True
    while Playing:
        $ DialogueTriggerCheck()
        while len(LabelsToCall) > 0:
            if renpy.has_label(LabelsToCall[0]):
                call expression LabelsToCall.pop(0) from _call_expression





        $ clickType = ""
        $ UIreturn  = renpy.call_screen("mainUI")#_layer="screens"

        if clickType == "move":
            $Location = UIreturn
        if clickType == "mapOpen":
            call mapNav from _call_mapNav
        if clickType == "CharacterClick":
            $ CharacterClick(Location)
            if ChoiceList <> []:
                $ LabelToCall = renpy.display_menu(ChoiceList, Interact = True, screen="choice")
                call expression LabelToCall from _call_expression_1
        if clickType == "Clicky":
            call expression UIreturn from _call_expression_2
        #menu:
            #"add cash":
                #$ MC.cash += 100



    # This ends the game.

    return

label   LocationMover:
    python:
        TempMenu= []
        for q in Rooms:
            if q.unLocked:
                TempMenu.append((q.name,q.name))
        TempMenu.append(("cancel", 1))
    $ renpy.say(None,"Where would you like to go?", interact=False)
    $ Location = renpy.display_menu(TempMenu)
    if not mover == -1:
        $Location = mover

    return
