screen map():
    add "mapNav/mapbg.jpg"
    imagebutton:
        xpos 25
        ypos 0
        focus_mask True
        hover "mapNav/minimap.png"
        idle "mapNav/minimap.png"
        action SetVariable("clickType","mapCancel"), Return(None)

    for q in Rooms:
        if q.unLocked:
            $ TempName = "places/map_"+ q.name +".png"
            imagebutton:
                xpos q.x
                ypos q.y
                idle  TempName
                hover TempName
                focus_mask True
                action SetVariable("clickType","mapSelect"), Return(q.name)

    #frame:
        #xalign 0.0
        #yalign 0.0
        #xsize 1920
        #ysize 1080
        #background "mapNav/mapbg.jpg"
        #button:
            #xpos 1000
            #ypos 500
            #text"home"
            #action Return("Home")
