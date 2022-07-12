screen Topbarlocation():
    imagebutton:
        xpos 25
        ypos -10
        focus_mask True
        hover "mapNav/minimap.png"
        idle "mapNav/minimap.png"
        action SetVariable("clickType","mapOpen"), Return(None)
    frame:
        xpos 890
        ypos 10
        xsize 230
        ysize 60
        hbox:
            xalign 0.5
            yalign 0.5
            text Location
