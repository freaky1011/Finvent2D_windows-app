init python:
    class place(object):
        """docstring for ."""

        def __init__(self,x,y,name,unLocked):
            self.x = x
            self.y = y
            self.name = name
            self.unLocked = unLocked

    class person(object):
        """docstring for ."""

        def __init__(self, name,weight,cash):

            self.name = name
            self.weight = weight
            self.cash = cash


    MC = person("Fin", 75, 0)

    Rooms = []
    Rooms.append(place(200,410,"house",True))
    Rooms.append(place(750,1000,"company",True))
    Rooms.append(place(1250,620,"bank",True))
    Rooms.append(place(950,610,"company",True))
    Rooms.append(place(1150,320,"firedept",True))
    Rooms.append(place(770,180,"burgerstore",True))
    Rooms.append(place(1550,600,"government",True))
    Rooms.append(place(200,150,"park",True))
    Rooms.append(place(470,140,"pizzastore",True))
    Rooms.append(place(1550,160,"hospital",True))
    Rooms.append(place(1150,150,"police",True))
    Rooms.append(place(640,70,"school",True))
    Rooms.append(place(200,600,"tuanhouse",True))
    Rooms.append(place(410,380,"mall",True))

    Location = Rooms[0].name


    class NPerson(object):
        def __init__(self, forename, surname, Location, love):
            self.forename = forename
            self.surname = surname
            self.Location = Location
            self.love = love

        @property
        def name(self):
            return "{} {}".format(self.forename, self.surname)

        @property
        def avatar(self):
            mood = "_Neutral.png"
            if -10 < self.love < 10:
                mood = "_Neutral.png"
            elif self.love <= -10:
                mood = "_Sad.png"
            elif self.love >= 10:
                mood = "_Happy.png"
            return "images/char/"+ self.forename +"/"+ self.forename + mood
    Npc = []
    Npc.append(NPerson("Fin","Dela Cruz", "house", 0))
    #Npc.append(NPerson("Franco","Nircota", "burgerstore", 0))
    Npc.append(NPerson("Tuan","Jimenez", "tuanhouse", 0))
    #Npc.append(NPerson("Francis","Nircota", "pizzastore", 0))
    #Npc.append(NPerson("Jorge","Oneil", "school", 0))
    Npc.append(NPerson("Ariana","Concepcion", "bank", 0))
    #Npc.append(NPerson("Daisy","Mann", "government", 0))
    #Npc.append(NPerson("Jerome","Dixon", "company", 0))
    #Npc.append(NPerson("Karter","Pineda", "firedept", 0))
    #Npc.append(NPerson("Leonardo","Ruiz", "police", 0))
    #Npc.append(NPerson("Nylah","Padilla", "hospital", 0))


    class DIALOGUE(object):
        def __init__(self, Location, participant, chain, sequence,lbl,InitText):
            self.participant = participant
            self.Location = Location
            self.chain = chain
            self.sequence = sequence
            self.lbl = lbl
            self.InitText = InitText
        @property
        def check(self):
            global Location
            #global Npc
            #for q in Npc:
            #    if q.name == self.forename or self.name == "":
                #    if q.Location == self.Location == Location:
                #        return True
            if self.participant == "":
                if self.InitText == "":
                    if self.Location == Location or self.Location == "":
                        if self.sequence == Chain [self.chain].sequence or self.chain == -1:
                            return True
            return False

    Dialogue = []

    Dialogue.append(DIALOGUE("house", "",0,0,"chain_1_0", ""))
    Dialogue.append(DIALOGUE("mall", "",0,1,"chain_1_1", ""))
    Dialogue.append(DIALOGUE("house", "",0,2,"chain_1_2", ""))
    Dialogue.append(DIALOGUE("bank", "",0,3,"chain_1_3", ""))

    class CHAIN(object):
        def __init__(self, evnt, sequence, IsActive):
            self.evnt = evnt
            self.sequence = sequence
            self.IsActive = IsActive
        def next(self):
            self.sequence+=1

    Chain = []
    for t in range (0,9):
        Chain.append(CHAIN([],0,False))

    for i,q in enumerate(Dialogue):
        tempInt = q.chain
        Chain[tempInt].evnt.append(i)
    class CLICKY(object):
        def __init__(self,x,y,Location,isActive,icon,func):
            self.Location = Location
            self.isActive = isActive
            self.icon = icon
            self.func = func
            self.x = x
            self.y = y
    objects = []


    objects.append(CLICKY(1500,600,"mall",True,"images/Click/Lottery.png","gotoLottery"))
    objects.append(CLICKY(150,478,"mall",True,"images/Click/Houseller.png","gotoHouseller"))
    objects.append(CLICKY(50,548,"mall",True,"images/Click/Deviceseller.png","gotoDeviceseller"))
    objects.append(CLICKY(1100,490,"mall",True,"images/Click/Clothesseller.png","gotoClothesseller"))
    objects.append(CLICKY(980,450,"mall",True,"images/Click/Burgervendor.png","gotoBurgervendor"))

    objects.append(CLICKY(200,280,"pizzastore",True,"images/char/Francis/Francis_Neutral.png","gotopizzastore"))
    objects.append(CLICKY(200,280,"burgerstore",True,"images/char/Franco/Franco_Neutral.png","gotoburgerstore"))
    objects.append(CLICKY(200,280,"school",True,"images/char/Jorge/Jorge_Neutral.png","gotoschool"))
    #objects.append(CLICKY(200,280,"bank",True,"images/char/Ariana/Ariana_Neutral.png","gotobank"))
    objects.append(CLICKY(200,280,"government",True,"images/char/Daisy/Daisy_Neutral.png","gotogovernment"))
    objects.append(CLICKY(200,280,"company",True,"images/char/Jerome/Jerome_Neutral.png","gotocompany"))
    objects.append(CLICKY(200,280,"firedept",True,"images/char/Karter/Karter_Neutral.png","gotofiredept"))
    objects.append(CLICKY(200,280,"police",True,"images/char/Leonardo/Leonardo_Neutral.png","gotopolice"))
    objects.append(CLICKY(200,280,"hospital",True,"images/char/Nylah/Nylah_Neutral.png","gotohospital"))
