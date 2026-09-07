default current_room = 2
define total_rooms = 3
default overlay_visible = True
default talkedtokendra = False


screen rooms():

    modal True

    if overlay_visible:

        add "room_[current_room].png":
            align (0.5, 0.5)

        # ROOM 1
        if current_room == 1:

            imagebutton:
                xpos 0.8
                idle "images/apollo/standing/apollotemp.png"
                action Call("deeztalking")

            imagebutton:
                idle "images/mj.png"
                action Call("mjtalking")


        # ROOM 2
        elif current_room == 2:

            imagebutton:
                idle "images/barby.png"
                action Call("barbytalking")


        # ROOM 3
        elif current_room == 3:

            imagebutton:
                idle "images/kendra.png"
                action Call("kendratalking")
        
        # LEFT ARROW
        if current_room not in [1]:
            imagebutton:
                idle "arrowl_idle.png"
                hover "arrowl_hover.png"

                action [
                    SetVariable(
                        "current_room",
                        (current_room - 1) if current_room > 1 else total_rooms
                    ),
                    With(Fade(0.3, 0.2, 0.3))
                ]

                xpos 0.09
                ypos 0.5
                focus_mask True


        # RIGHT ARROW
        if current_room not in [3]: #brain fog
            imagebutton:
                idle "arrow_idle.png"
                hover "arrow_hover.png"

                action [
                    SetVariable(
                        "current_room",
                        (current_room + 1) if current_room < total_rooms else 1
                    ),
                    With(Fade(0.3, 0.2, 0.3))
                ]

                xpos 0.8
                ypos 0.5
                
                    
                focus_mask True



label deeztalking:

    "ayyaayya im talkin heeeereee"

    return


label barbytalking:

    "oh hehehe hi"

    return


label mjtalking:

    "weed"

    return


label kendratalking:
    if talkedtokendra == False:
        "hey there!"
        $ talkedtokendra = True
    else:
        "we've already talked!"
    
    return