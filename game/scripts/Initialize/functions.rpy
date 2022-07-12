init python:
    def BGDeclare():
        global Location
        global BGImage
        BGImage = Location.lower()
        BGImage = BGImage.replace(" " , "")
        BGImage = "images/"+BGImage +".jpg"

    def CharacterClick(Loc):
        global Dialogue
        global Chain
        global UIreturn
        global ChoiceList
        ChoiceList = []
        for q in Dialogue:
            if q.participant == UIreturn:
                if q.Location == Loc or q.Location == "":
                    ch = q.chain
                    sq = q.sequence
                    if sq == Chain [ch].sequence:
                        ChoiceList.append((q.InitText, q.lbl))

    def DialogueTriggerCheck():
        global Dialogue
        global LabelsToCall
        LabelsToCall = []

        for q in Dialogue:
            if q.check:
                LabelsToCall.append(q.lbl)
