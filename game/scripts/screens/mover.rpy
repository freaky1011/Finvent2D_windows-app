screen moveUI():
    frame:
        xpadding 25
        ypadding 25
        xalign 0.0
        yalign 0.5
        has vbox
        label "Location" xminimum 300
        for q in Rooms:
            if q.unLocked:
                button:
                    text  q.name
                    background "#333"
                    ypadding 3
                    xpadding 14
                    action SetVariable("clickType","move"),Return(q.name)
