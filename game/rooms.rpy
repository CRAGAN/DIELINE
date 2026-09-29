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
default day = 1
define breakroom_unlocked = False
transform add_door:
    blend 'add'

image room_1 = Movie(play="images/bg overworld/room_1.webm", loop=True)
image room_2 = Movie(play="images/bg overworld/room_2.webm", loop=True)
image room_3 = Movie(play="images/bg overworld/room_3.webm", loop=True)
image room_4 = Movie(play="images/bg overworld/room_4.webm", loop=True)
image kendraintro = Movie(play="images/cg/kendraintro.webm", loop=True)
image picture = Movie(play="images/cg/thepicures.webm", loop=True)
image managerroom = Movie(play="images/bg overworld/managersroom.webm", loop=True)
image bathroom = Movie(play="images/bg overworld/bathroom.webm", loop=True)
image storage = Movie(play="images/bg overworld/shelfs over world.webm", loop=True)
image janitor = Movie(play="images/bg overworld/Janitor closet.webm", loop=True)
screen rooms(): 
    
    if overlay_visible:

        add "room_[current_room]":
            align (0.5, 0.5)
        add "images/lighter.png" blend 'add' alpha 0.3

        # ROOM 1
        if current_room == 1:
            
            add "images/barby/standing/barby_standing_pants.png" zoom 0.6 xpos 0.2 ypos 0.16
            imagebutton:
                xpos 0.388
                ypos 0.07
                idle "images/door_idle.png"
                hover "images/door_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("managerroom")]
                at transform:
                    blend 'add'

            ##imagebutton:
                # focus_mask True 
                # xpos 0.6
                #  ypos 0.2
                # idle "images/apollo/standing/apollo_standing.png"
                # hover "images/apollo/standing/apollo_standing_hover.png"
                # action Call("apollotalking")
                # at transform:
                    #    zoom 0.8
            


        # ROOM 2
        elif current_room == 2:
            add "images/barby/standing/barby_standing_pants.png" zoom 0.45 xpos 0.2 ypos 0.3
            add "images/bg overworld/borders.png" blend 'multiply'
            imagebutton:
                focus_mask True 
                xpos 0.5
                ypos 0.33
                idle "images/mj/standing/mj_standing.png"
                hover "images/mj/standing/mj_standing_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("mjtalking")]
                at transform:
                    zoom 0.6
                    
            

        # ROOM 3
        elif current_room == 3:
            add "images/bg overworld/borders1.png"
            

            imagebutton:
    
                xpos 0.176
                ypos 0.409
                
                idle "images/door_idle.png"
                hover "images/door_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("storage")]
                at transform:
                    blend 'add'
                    zoom 0.29
            imagebutton:
                xpos 0.597
                ypos 0.4087
                
                idle "images/door_idle.png"
                hover "images/door_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("bathroom")]
                at transform:
                    blend 'add'
                    zoom 0.293
            imagebutton:
                xpos 0.79
                ypos 0.408
                
                idle "images/door_idle.png"
                hover "images/door_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("janitor")]
                at transform:
                    blend 'add'
                    zoom 0.297
            add "images/barby/standing/barby_standing_pants.png" zoom 0.2 xpos 0.2 ypos 0.43
        # ROOM 4
        elif current_room == 4:
            add "images/barby/standing/barby_standing_pants.png" zoom 0.43 xpos 0.2 ypos 0.3

            imagebutton:
                focus_mask True 
                xpos 0.5
                ypos 0.2
                idle "images/deez/standing/deez_standing.png"
                hover "images/deez/standing/deez_standing_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("deeztalking")]
                at transform:
                    zoom 0.5
            add "images/bg overworld/chairs.png"
       
        
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
    


# DEEZ


# APOLLO

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
# MJ


    
# KENDRA


 
label storage:
    $ storage = True
    call screen storage
label bathroom:
    call screen bathroom
label janitor:
    call screen janitor

label apollo_manager_reply:
    scene managerroom
    
    show apollosit:
        xpos 0.56
        ypos 0.335
        zoom 0.53
    show barby_standing_pants:
        zoom 0.33 xpos 0.25 ypos 0.32
    show managersroom
    show lighter:
        blend 'add' alpha 0.3
    $ quick_menu = True
    if day == 1:
        a "Now go on, Barby, those IDs aren’t going to distribute themselves."
        jump rooms
    if day == 2:
        $ talkedtoapollo = True
        b "Good morning, Apollo!"
        a "Good morning, Barby!"
        a "Ready to give it our all today?"
        b "You betcha!"
        jump rooms2
    

label managerroom:
    call screen managerroom


screen storage():
    
    add "storage":
            align (0.5, 0.5)
    add "images/barby/standing/barby_standing_pants.png" zoom 0.5 xpos 0.2 ypos 0.26
    if day == 1:
        imagebutton:
            xpos 0.5
            ypos 0.23
            focus_mask True
            idle "images/kendra/standing/kendra_standing.png"
            hover "images/kendra/standing/kendra_standing_hover.png"
            action [With(Fade(0.4, 0.0, 0.4)), Call("kendratalking")]
            at transform:
                zoom 0.7
    imagebutton:
        idle "images/apollo/standing/apollotemp.png"
        action Call("rooms")
screen bathroom():
    add "bathroom":
            align (0.5, 0.5)
    add "images/lighter.png" blend 'add' alpha 0.3
    add "images/barby/standing/barby_standing_pants.png" zoom 0.4 xpos 0.2 ypos 0.38
    imagebutton:
        idle "images/apollo/standing/apollotemp.png"
        action Call("rooms")
screen janitor():
    add "janitor":
            align (0.5, 0.5)
    add "images/lighter.png" blend 'add' alpha 0.3

    imagebutton:
        focus_mask True
        xpos 0.45
        ypos 0.8
        idle "images/arrowd_idle.png"
        hover "images/arrowd_hover.png"
        action Call("rooms")
screen managerroom():
    add "managerroom":
            align (0.5, 0.5)
    
    add "images/barby/standing/barby_standing_pants.png" zoom 0.33 xpos 0.25 ypos 0.32
    imagebutton:
        xpos 0.56
        ypos 0.335
        
        idle "images/apollo/standing/apollosit.png" 
        hover "images/apollo/standing/apollosit_hover.png"
        action Call("apollo_manager_reply")
        at transform:
            zoom 0.53
    add "images/bg overworld/managersroom.png"
    add "images/lighter.png" blend 'add' alpha 0.3
# ROOMS BREAKROOM TIME


screen hallwaysdeez():
    default time_passed = False
    timer 10.0 action SetScreenVariable("time_passed", True)

    add "deezscene1" zoom 1.2 xoffset -50
    if not time_passed:
        imagebutton: 
            ypos 0.12
            xpos 0.3
            idle "images/deez/deezle2.png" 
            hover "images/deez/deezle2hover.png"
            action Jump("youdied")
            at deezwalk
    else:
        imagebutton:
                xpos 0.5
                idle "arrow_idle.png"
                hover "arrow_hover.png"
                action Call("breakroom4")
    add "images/barby/standing/shock.png" zoom 0.55 xoffset 300 ypos 0.296
    add "images/blue.png" blend 'multiply' alpha 0.3
label youdied:
    scene room_3 
    show overlay:
        blend 'multiply' alpha 0.3
    show blue:
        blend 'multiply' alpha 0.3
        easein 1 alpha 0.7
    show borders1 at center:
        zoom 1.2
        easein 0.8 zoom 1.0
    show deez back at up, center:
        zoom 0.6
    
    b_sub "Deez, wait. Stop. You have something on your—"
    hide deez back
    show de monstert at shaking, center:
        easein 0.5 zoom 3 yoffset 600 xoffset -100
    show noises:
        alpha 0.1
        blend 'add'
    with vpunch
    pause 0.9
    scene black
    centered " "

    jump encounter4

transform deezwalk:
    zoom 0.4
    xoffset 280 
    easein 0.2 xoffset 300
    linear 0.3 xoffset 290
    pause 2
    xoffset 580
    easein 0.2 xoffset 600
    linear 0.3 xoffset 590
    pause 2.0
    xoffset 880
    easein 0.2 xoffset 900
    linear 0.3 xoffset 890
    pause 2.0
    xoffset 1180
    easein 0.2 xoffset 1200
    linear 0.3 xoffset 1190
    pause 2.0
    alpha 0.0
    pause 2.0


#_______________
screen breaktime1(): 
    
    if overlay_visible:

        add "room_[current_room]":
            align (0.5, 0.5)
        add "images/lighter.png" blend 'add' alpha 0.3

        # ROOM 1
        if current_room == 1:
            
            add "images/barby/standing/barby_standing_pants.png" zoom 0.6 xpos 0.2 ypos 0.16
            

            imagebutton:
                focus_mask True 
                xpos 0.5
                ypos 0.2
                idle "images/apollo/standing/apollo_standing.png"
                hover "images/apollo/standing/apollo_standing_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("deezandapollo")]
                at transform:
                        zoom 0.8
            imagebutton:
                focus_mask True 
                
                xpos 0.35
                ypos 0.1
                idle "images/deez/standing/deez_standing.png"
                hover "images/deez/standing/deez_standing_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("deezandapollo")]
                at transform:
                    zoom 0.65 xzoom -1

            

            


        # ROOM 2
        elif current_room == 2:
            add "images/barby/standing/barby_standing_pants.png" zoom 0.45 xpos 0.2 ypos 0.3
            add "images/bg overworld/borders.png" blend 'multiply'
            
            

        # ROOM 3
        elif current_room == 3:
            add "images/bg overworld/borders1.png"
            add "images/barby/standing/barby_standing_pants.png" zoom 0.2 xpos 0.2 ypos 0.48
            imagebutton:
                focus_mask True 
                xpos 0.5
                ypos 0.45
                idle "images/mj/standing/mj_standing.png"
                hover "images/mj/standing/mj_standing_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("mjandkendra")]
                at transform:
                    zoom 0.3
            imagebutton:
                focus_mask True 
                xpos 0.4
                ypos 0.45
                idle "images/kendra/standing/kendra_standing.png"
                hover "images/kendra/standing/kendra_standing_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("mjandkendra")]
                at transform:
                    zoom 0.3
            
                    
        # ROOM 4
        elif current_room == 4:
            add "images/barby/standing/barby_standing_pants.png" zoom 0.43 xpos 0.2 ypos 0.3
            add "images/bg overworld/chairs.png"
       
        
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

# DAY 2
screen rooms2():

    if overlay_visible:

        add "room_[current_room]":
            align (0.5, 0.5)
        add "images/lighter.png" blend 'add' alpha 0.3

        # ROOM 1
        if current_room == 1:
            
            add "images/barby/standing/barby_standing_shorts.png" zoom 0.6 xpos 0.2 ypos 0.16
            imagebutton:
                xpos 0.388
                ypos 0.07
                idle "images/door_idle.png"
                hover "images/door_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("managerroom")]
                at transform:
                    blend 'add'
        # ROOM 2
        elif current_room == 2:
            add "images/barby/standing/barby_standing_shorts.png" zoom 0.45 xpos 0.2 ypos 0.3
            add "images/bg overworld/borders.png" blend 'multiply'
            imagebutton:
                focus_mask True
                idle "images/computer.png"
                hover "images/computer_hover.png"
                if talkedtoapollo and talkedtokendra and talkedtodeez and talkedtomj:
                    action [With(Fade(0.4, 0.0, 0.4)), Call("minigametime")]
                else:
                    action [Notify("I'd better check on everybody first!")]
                    
            
            imagebutton:
                focus_mask True 
                xpos 0.6
                ypos 0.33
                idle "images/mj/standing/mj_standing.png"
                hover "images/mj/standing/mj_standing_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("mjtalking2")]
                at transform:
                    zoom 0.6
            

        # ROOM 3
        elif current_room == 3:
            add "images/bg overworld/borders1.png"
            
       
            add "images/barby/standing/barby_standing_shorts.png" zoom 0.22 xpos 0.25 ypos 0.45
            imagebutton:
                focus_mask True 
                xpos 0.5
                ypos 0.4
                idle "images/deez/standing/deez_standing.png"
                hover "images/deez/standing/deez_standing_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("deeztalking2")]
                at transform:
                    zoom 0.25
            imagebutton:
                focus_mask True 
                xpos 0.4
                ypos 0.45
                idle "images/kendra/standing/kendra_standing.png"
                hover "images/kendra/standing/kendra_standing_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("kendratalking2")]
                at transform:
                    zoom 0.3
        # ROOM 4             
        # ROOM 4
        elif current_room == 4:
            add "images/barby/standing/barby_standing_pants.png" zoom 0.43 xpos 0.2 ypos 0.3
            add "images/bg overworld/chairs.png"
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
        if current_room != 4:
            imagebutton:
                idle "arrow_idle.png"
                hover "arrow_hover.png"

                if current_room == 3 and not breakroom_unlocked:
                    action [Notify("It's not your break yet"),]
                else:
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
#BREAKTIME2
screen breaktime2():

    if overlay_visible:

        add "room_[current_room]":
            align (0.5, 0.5)
        add "images/lighter.png" blend 'add' alpha 0.3

        # ROOM 1
        if current_room == 1:
            
            add "images/barby/standing/barby_standing_shorts.png" zoom 0.6 xpos 0.2 ypos 0.16
            imagebutton:
                xpos 0.388
                ypos 0.07
                idle "images/door_idle.png"
                hover "images/door_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("managerroom2")]
                at transform:
                    blend 'add'
        # ROOM 2
        elif current_room == 2:
            add "images/barby/standing/barby_standing_shorts.png" zoom 0.45 xpos 0.2 ypos 0.3
            add "images/bg overworld/borders.png" blend 'multiply'
            imagebutton:
                focus_mask True
                idle "images/computer.png"
                hover "images/computer_hover.png"
                action [Notify("I've done my work already")]
                    
            
            imagebutton:
                focus_mask True 
                xpos 0.6
                ypos 0.33
                idle "images/apollo/standing/apollo_standing.png"
                hover "images/apollo/standing/apollo_standing_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("apollotalking22")]
                at transform:
                    zoom 0.6
            imagebutton:
                focus_mask True
                idle "images/computer.png"
                hover "images/computer_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("mjtalking22")]
                    
            

        # ROOM 3
        elif current_room == 3:
            add "images/bg overworld/borders1.png"
            

            imagebutton:
    
                xpos 0.176
                ypos 0.409
                
                idle "images/door_idle.png"
                hover "images/door_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("storage2")]
                at transform:
                    blend 'add'
                    zoom 0.29
            imagebutton:
                xpos 0.597
                ypos 0.4087
                
                idle "images/door_idle.png"
                hover "images/door_hover.png"
                action [Notify("I don't need to go in there right now")]
                at transform:
                    blend 'add'
                    zoom 0.293
            imagebutton:
                xpos 0.79
                ypos 0.408
                
                idle "images/door_idle.png"
                hover "images/door_hover.png"
                action [Notify("I don't need to go in there right now")]
                at transform:
                    blend 'add'
                    zoom 0.297
            add "images/barby/standing/barby_standing_shorts.png" zoom 0.2 xpos 0.2 ypos 0.53
        # ROOM 4             
        # ROOM 4
        elif current_room == 4:
            add "images/barby/standing/barby_standing_shorts.png" zoom 0.43 xpos 0.2 ypos 0.3
            add "images/bg overworld/chairs.png"
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
        if current_room != 4:
            imagebutton:
                idle "arrow_idle.png"
                hover "arrow_hover.png"

                if current_room == 3 and not breakroom_unlocked:
                    action [Notify("I should check on the others"),]
                elif current_room == 3 and breakroom_unlocked:
                    action [With(Fade(0.4, 0.0, 0.4)), Call("deeztalking22")]
                else:
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
label storage2:
    $ storage = True
    jump mjtalking22
label managerroom2:
    $ managerroom = True
    jump kendratalking22


# DAY 3
screen rooms3(): 
    
    if overlay_visible:

        add "room_[current_room]":
            align (0.5, 0.5)
        add "images/lighter.png" blend 'add' alpha 0.3

        # ROOM 1
        if current_room == 1:
            
            add "images/barby/standing/barby_standing_pants.png" zoom 0.6 xpos 0.2 ypos 0.16
            imagebutton:
                xpos 0.388
                ypos 0.07
                idle "images/door_idle.png"
                hover "images/door_hover.png"
                action [Notify("Nobody's in here."),]
                at transform:
                    blend 'add'

            ##imagebutton:
                # focus_mask True 
                # xpos 0.6
                #  ypos 0.2
                # idle "images/apollo/standing/apollo_standing.png"
                # hover "images/apollo/standing/apollo_standing_hover.png"
                # action Call("apollotalking")
                # at transform:
                    #    zoom 0.8
            


        # ROOM 2
        elif current_room == 2:
            add "images/barby/standing/barby_standing_pants.png" zoom 0.45 xpos 0.2 ypos 0.3
            add "images/bg overworld/borders.png" blend 'multiply'
            imagebutton:
                focus_mask True 
                xpos 0.5
                ypos 0.33
                idle "images/kendra/standing/kendra_monster_overworld.png"
                hover "images/kendra/standing/kendra_monster_overworldh.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("kendracubic")]
                at transform:
                    zoom 0.6
                    
            

        # ROOM 3
        elif current_room == 3:
            add "images/bg overworld/borders1.png"
            

            
            add "images/barby/standing/barby_standing_pants.png" zoom 0.2 xpos 0.2 ypos 0.43
        # ROOM 4
        
       
        
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

#DAY 5

screen rooms5(): 
    
    if overlay_visible:

        add "room_[current_room]":
            align (0.5, 0.5)
        add "images/lighter.png" blend 'add' alpha 0.3

        # ROOM 1
        if current_room == 1:
            
            add "images/barby/standing/barby_standing_pants.png" zoom 0.6 xpos 0.2 ypos 0.16
            add "black" blend 'multiply' alpha 0.3
            add "images/blue.png" blend 'multiply' alpha 0.5
            imagebutton:
                xpos 0.388
                ypos 0.07
                idle "images/door_idle.png"
                hover "images/door_hover.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("apolloweirdtime")]
                at transform:
                    blend 'add'
            imagebutton:
                focus_mask True 
                xpos 0.5
                ypos 0.28
                idle "images/kendra/standing/kendra_monster_overworld.png"
                hover "images/kendra/standing/kendra_monster_overworldh.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("kendratalking5")]
                at transform:
                    zoom 1.0
            
                    

            ##imagebutton:
                # focus_mask True 
                # xpos 0.6
                #  ypos 0.2
                # idle "images/apollo/standing/apollo_standing.png"
                # hover "images/apollo/standing/apollo_standing_hover.png"
                # action Call("apollotalking")
                # at transform:
                    #    zoom 0.8
            


        # ROOM 2
        elif current_room == 2:
            add "images/barby/standing/barby_standing_pants.png" zoom 0.45 xpos 0.2 ypos 0.3
            
            add "black" blend 'multiply' alpha 0.3
            add "images/green.png" blend 'multiply' alpha 0.5
            imagebutton:
                focus_mask True 
                xpos 0.5
                ypos 0.05
                idle "images/mj/standing/mj_monster_overworld.png"
                hover "images/mj/standing/mj_monster_overworldh.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("mjtalking5")]
                at transform:
                    zoom 1.5
            add "images/bg overworld/borders.png" blend 'multiply'
                    
            

        # ROOM 3
        elif current_room == 3:
            add "images/bg overworld/borders1.png"
            add "black" blend 'multiply' alpha 0.3
            
            imagebutton:
                focus_mask True 
                xpos 0.5
                ypos 0.3
                idle "images/deez/standing/deez_monster_overworld.png"
                hover "images/deez/standing/deez_monster_overworldh.png"
                action [With(Fade(0.4, 0.0, 0.4)), Call("deeztalking5")]
                at transform:
                    zoom 0.4

            
            add "images/barby/standing/barby_standing_pants.png" zoom 0.2 xpos 0.2 ypos 0.43
            add "images/pink.png" blend 'multiply' alpha 0.5
            add "images/blue.png" blend 'multiply' alpha 0.5
        # ROOM 4
        
        elif current_room == 4:
            add "images/barby/standing/barby_standing_shorts.png" zoom 0.43 xpos 0.2 ypos 0.3
            add "images/bg overworld/chairs.png"
        # LEFT ARROW
        
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
    