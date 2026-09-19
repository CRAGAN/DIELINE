default current_room = 1
define total_rooms = 4
default overlay_visible = True
default talkedtokendra = False
default bathroom = False
default storage = False
default janitor = False

screen rooms():

    if overlay_visible:

        add "images/bg overworld/room_[current_room].png":
            align (0.5, 0.5)

        # ROOM 1
        if current_room == 1:

            imagebutton:
                xpos 0.0
                idle "images/apollo/standing/apollo_standing.png"
                action Call("deeztalking")
            imagebutton:
                idle "images/apollo/standing/apollotemp.png"
                action Call("managerroom")


            


        # ROOM 2
        elif current_room == 2:

            imagebutton:
                idle "images/mj/standing/mj_standing.png"
                action Call("barbytalking")
            

        # ROOM 3
        elif current_room == 3:

            imagebutton:
                idle "images/kendra/standing/kendra_standing.png"
                action Call("kendratalking")
            imagebutton:
                idle "images/apollo/standing/apollotemp.png"
                action Call("storage")
            imagebutton:
                xpos 0.3
                idle "images/apollo/standing/apollotemp.png"
                action Call("bathroom")
            imagebutton:
                xpos 0.6
                idle "images/apollo/standing/apollotemp.png"
                action Call("janitor")
        # ROOM 4
        elif current_room == 4:

            imagebutton:
                idle "images/deez/standing/deez_standing.png"
                action Call("deeztalking")
        
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
        if current_room not in [4]: #brain fog
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
    jump rooms



label barbytalking:

    "oh hehehe hi"

    jump rooms


label mjtalking:

    "weed"
    jump rooms


label kendratalking:
    if talkedtokendra == False:
        "hey there!"
        $ talkedtokendra = True
        
    else:
        "we've already talked!"
    if storage == True:
        jump storage
    else:
        jump rooms
label storage:
    $ storage = True
    call screen storage
label bathroom:
    call screen bathroom
label janitor:
    call screen janitor
label managerroom:
    call screen managerroom


screen storage():
    
    add "images/bg overworld/storage.png":
            align (0.5, 0.5)
    imagebutton:
        idle "images/kendra/standing/kendra_standing.png"
        action Call("kendratalking")
    imagebutton:
        idle "images/apollo/standing/apollotemp.png"
        action Call("rooms")
screen bathroom():
    add "images/bg overworld/bathroom.png":
            align (0.5, 0.5)
    imagebutton:
        idle "images/apollo/standing/apollotemp.png"
        action Call("rooms")
screen janitor():
    add "images/bg overworld/janitor.png":
            align (0.5, 0.5)
    imagebutton:
        idle "images/apollo/standing/apollotemp.png"
        action Call("rooms")
screen managerroom():
    add "images/bg overworld/managersroom.png":
            align (0.5, 0.5)
    imagebutton:
        idle "images/apollo/standing/apollotemp.png"
        action Call("rooms")