screen clickies():
    for q in objects:
        if q.Location == Location and q.isActive:
            imagebutton:
                xpos q.x
                ypos q.y
                idle q.icon
                hover  q.icon
                focus_mask True
                action SetVariable("clickType", "Clicky"), Return(q.func)
