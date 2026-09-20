default current_room = 1
define total_rooms = 4
default overlay_visible = True
default talkedtokendra = False
default talkedtoapollo = False
default talkedtomj = False
default talkedtodeez = False
default bathroom = False
default storage = False
default janitor = False
define pants = False



screen rooms():
    
    if overlay_visible:

        add "images/bg overworld/room_[current_room].png":
            align (0.5, 0.5)

        # ROOM 1
        if current_room == 1:
            add "images/barby/standing/barby_standing_pants.png" zoom 0.5 xpos 0.2 ypos 0.24

            imagebutton:
                focus_mask True 
                xpos 0.6
                ypos 0.24
                idle "images/apollo/standing/apollo_standing.png"
                hover "images/apollo/standing/apollo_standing_hover.png"
                action Call("apollotalking")
                at transform:
                    zoom 0.7
            imagebutton:
                focus_mask True 
                idle "images/apollo/standing/apollotemp.png"
                action Call("managerroom")


            


        # ROOM 2
        elif current_room == 2:
            add "images/barby/standing/barby_standing_pants.png" zoom 0.25 xpos 0.2 ypos 0.44

            imagebutton:
                focus_mask True 
                xpos 0.5
                ypos 0.45
                idle "images/mj/standing/mj_standing.png"
                hover "images/mj/standing/mj_standing_hover.png"
                action Call("mjtalking")
                at transform:
                    zoom 0.35
            

        # ROOM 3
        elif current_room == 3:
            add "images/barby/standing/barby_standing_pants.png" zoom 0.2 xpos 0.2 ypos 0.53

            imagebutton:
                focus_mask True 
                idle "images/apollo/standing/apollotemp.png"
                action Call("storage")
            imagebutton:
                focus_mask True 
                xpos 0.3
                idle "images/apollo/standing/apollotemp.png"
                action Call("bathroom")
            imagebutton:
                focus_mask True 
                xpos 0.6
                idle "images/apollo/standing/apollotemp.png"
                action Call("janitor")
        # ROOM 4
        elif current_room == 4:
            add "images/barby/standing/barby_standing_pants.png" zoom 0.33 xpos 0.2 ypos 0.39

            imagebutton:
                focus_mask True 
                xpos 0.5
                ypos 0.3
                idle "images/deez/standing/deez_standing.png"
                hover "images/deez/standing/deez_standing_hover.png"
                action Call("deeztalking")
                at transform:
                    zoom 0.4
        
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
    scene deezcoffee with fade
    if talkedtodeez == False:
        $ talkedtodeez = True
        "ayyaayya im talkin heeeereee"
        if talkedtomj and talkedtokendra and talkedtoapollo and talkedtodeez:
            b "I think I've talked to everyone now!"
            b "I should go back to the manager's room and tell Apollo."
            jump breakroom2
    else:
        "we've already talked!"
    jump rooms



label apollotalking:
    scene apollomanagersroom with fade
    if talkedtoapollo == False:
        $ talkedtoapollo = True
        a "oh hehehe hi"
        if talkedtomj and talkedtokendra and talkedtoapollo and talkedtodeez:
            b "I think I've talked to everyone now!"
            b "I should go back to the manager's room and tell Apollo."
            jump breakroom2
    else:
        "we've already talked!"
    jump rooms


label mjtalking:
    scene mjcubicle with fade
    m "hmmmmm"
    scene room_2
    show overlay:
        blend 'multiply'
    with dissolve
    show m defaultt at center:
        subpixel True
        yoffset 500
        easein 0.6 yoffset 100
        easein 0.3 yoffset 110
        easein 0.5 yoffset 100
    if talkedtomj == False:
        $ talkedtomj = True
        
        m "hey."
        show m default
        b "Hey, MJ! How’s it going?"
        show m hmt
        m "eh...could be better..."
        show m hm
        b "oh...sorry bout that."
        show m defaultt
        m "Nah. it's g. seeya around!"
        show m default
        b "you too!"
        
        if talkedtomj and talkedtokendra and talkedtoapollo and talkedtodeez:
            b "I think I've talked to everyone now!"
            b "I should go back to the manager's room and tell Apollo."
            jump breakroom2
    else: 
        m "I'm a little busy right now..."


    
    jump rooms
    

label kendratalking:

    if talkedtokendra == False:
        $ talkedtokendra = True
        "hey there!"
        
        if talkedtomj and talkedtokendra and talkedtoapollo and talkedtodeez:
            b "I think I've talked to everyone now!"
            b "I should go back to the manager's room and tell Apollo."
            jump breakroom2

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
    add "images/barby/standing/barby_standing_pants.png" zoom 0.5 xpos 0.2 ypos 0.26

    imagebutton:
        xpos 0.5
        ypos 0.23
        focus_mask True
        idle "images/kendra/standing/kendra_standing.png"
        hover "images/kendra/standing/kendra_standing_hover.png"
        action Call("kendratalking")
        at transform:
            zoom 0.7
    imagebutton:
        idle "images/apollo/standing/apollotemp.png"
        action Call("rooms")
screen bathroom():
    add "images/bg overworld/bathroom.png":
            align (0.5, 0.5)
    add "images/barby/standing/barby_standing_pants.png" zoom 0.4 xpos 0.2 ypos 0.38
    imagebutton:
        idle "images/apollo/standing/apollotemp.png"
        action Call("rooms")
screen janitor():
    add "images/bg overworld/janitor.png":
            align (0.5, 0.5)
    add "images/barby/standing/barby_standing_pants.png" zoom 0.5 xpos 0.2 ypos 0.24

    imagebutton:
        focus_mask True
        xpos 0.45
        ypos 0.8
        idle "images/arrowd_idle.png"
        hover "images/arrowd_hover.png"
        action Call("rooms")
screen managerroom():
    add "images/bg overworld/managersroom.png":
            align (0.5, 0.5)
    add "images/barby/standing/barby_standing_pants.png" zoom 0.33 xpos 0.25 ypos 0.32
    imagebutton:
        idle "images/apollo/standing/apollotemp.png"
        action Call("rooms")
# ROOMS BREAKROOM TIME
label breakroom2:
    $ storage = False
    $ janitor = False
    $ bathroom = False
    $ managerroom = False
    call screen alloftheminbreakroom


screen alloftheminbreakroom():
    
    if overlay_visible:

        add "images/bg overworld/room_[current_room].png":
            align (0.5, 0.5)

        # ROOM 1
        if current_room == 1:
            add "images/barby/standing/barby_standing_pants.png" zoom 0.5 xpos 0.2 ypos 0.24

            
            imagebutton:
                focus_mask True 
                idle "images/apollo/standing/apollotemp.png"
                action Call("managerroom")


            


        # ROOM 2
        elif current_room == 2:
            add "images/barby/standing/barby_standing_pants.png" zoom 0.25 xpos 0.2 ypos 0.44

            
            

        # ROOM 3
        elif current_room == 3:
            add "images/barby/standing/barby_standing_pants.png" zoom 0.2 xpos 0.2 ypos 0.53

            imagebutton:
                focus_mask True 
                idle "images/apollo/standing/apollotemp.png"
                action Call("storage")
            imagebutton:
                focus_mask True 
                xpos 0.3
                idle "images/apollo/standing/apollotemp.png"
                action Call("bathroom")
            imagebutton:
                focus_mask True 
                xpos 0.6
                idle "images/apollo/standing/apollotemp.png"
                action Call("janitor")
        # ROOM 4
        elif current_room == 4:
            add "images/barby/standing/barby_standing_pants.png" zoom 0.33 xpos 0.2 ypos 0.39

            imagebutton:
                focus_mask True 
                xpos 0.5
                ypos 0.3
                idle "images/deez/standing/deez_standing.png"
                hover "images/deez/standing/deez_standing_hover.png"
                action Call("deeztalking")
                at transform:
                    zoom 0.4
            imagebutton:
                    focus_mask True 
                    xpos 0.6
                    ypos 0.24
                    idle "images/apollo/standing/apollo_standing.png"
                    hover "images/apollo/standing/apollo_standing_hover.png"
                    action Call("apollotalking")
                    at transform:
                        zoom 0.4
            imagebutton:
                focus_mask True 
                xpos 0.5
                ypos 0.45
                idle "images/mj/standing/mj_standing.png"
                hover "images/mj/standing/mj_standing_hover.png"
                action Call("mjtalking")
                at transform:
                    zoom 0.35
            imagebutton:
                focus_mask True 
                xpos 0.5
                ypos 0.45
                idle "images/kendra/standing/kendra_standing.png"
                hover "images/kendra/standing/kendra_standing_hover.png"
                action Call("kendratalking")
                at transform:
                    zoom 0.35
            
            
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