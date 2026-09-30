default current_id = ""

transform hoverup:
    on hover:
        linear 0.15 yoffset -20
    on idle:
        linear 0.15 yoffset 0

screen id_screen():
    add "images/bg overworld/overlay.png" blend 'multiply' alpha 0.9
    tag menu
    imagebutton:
        idle "deez_id.png"
        xpos 1010
        ypos 220
        action [ SetVariable("current_id", "Deez"), Jump("read_id") ]
        at hoverup
    imagebutton:
        idle "dave_id.png"
        xpos 810
        ypos 250
        action [ SetVariable("current_id", "Dave"), Jump("read_id") ]
        at hoverup
    imagebutton:
        idle "mj_id.png"
        xpos 610
        ypos 250
        action [ SetVariable("current_id", "M.J Grey"), Jump("read_id") ]
        at hoverup
    imagebutton:
        idle "kendra_id.png"
        xpos 410
        ypos 250
        action [ SetVariable("current_id", "Kendra Bell"), Jump("read_id") ]
        at hoverup
    
    imagebutton:
        idle "apollo_id.png"
        xpos 210
        ypos 250
        action [ SetVariable("current_id", "Apollo Knight"), Jump("read_id") ]
        at hoverup
    

    imagebutton:
        idle "barby_id.png"
        xpos 10
        ypos 250
        action [ SetVariable("current_id", "Fredrick Ibarra"), Jump("read_id") ]
        at hoverup

    
    
    
    
    
    

    textbutton "Done looking?":
        xalign 0.5
        yalign 0.95
        action [ SetVariable("current_id", "done"), Jump("read_id") ]
        at hoverup



label read_id(item_name=None):
    hide screen id_screen
    window hide
    # call screen ids

    if current_id == "Fredrick Ibarra":
        show barby_id at zoomin
        $ renpy.pause(1.5, hard=True)
        voice "audio/Barby/Day 1 ID/barby_line020.mp3"
      
        b_id "Barby It’s me!"
        hide barby_id
    elif current_id == "Apollo Knight":
        show apollo_id at zoomin
        $ renpy.pause(1.5, hard=True)
        
        
        
        
        voice "audio/Barby/Day 1 ID/barby_line021.mp3"
        b_id "Oh, this is your ID! You have such an {i}original character do not steal{/i} name." 
        voice "audio/Apollo/Day 1 ID/apollo_line019.mp3"
        a_id "What does that mean?" 
        voice "audio/Barby/Day 1 ID/barby_line022.mp3"
        b_id "Uh. Nothing, boss, here!"
        voice "audio/Apollo/Day 1 ID/apollo_line020.mp3"
        a_id "I told you not to call me that Barbs!"
        voice "audio/Barby/Day 1 ID/barby_line023.mp3"

        b_id "Sorry!!!"
        hide apollo_id
    elif current_id == "Kendra Bell":
        show kendra_id at zoomin
        $ renpy.pause(1.5, hard=True)
        voice "audio/Apollo/Day 1 ID/apollo_line021.mp3"
        a_id "If you think her name rings a bell, this is the person who went around the office in roller skates!"
        voice "audio/Barby/Day 1 ID/barby_line024.mp3"
        b_id "Oh! Her! Yeah, you told me about that."
        voice "audio/Apollo/Day 1 ID/apollo_line022.mp3"
        a_id "You were there, though...?"
        voice "audio/Barby/Day 1 ID/barby_line025.mp3"
        b_id "Well, yeah, but..."
        voice "audio/Barby/Day 1 ID/barby_line026.mp3"
        b_id "She looks so different with her new hair..." 
        voice "audio/Apollo/Day 1 ID/apollo_line023.mp3"
        a_id "Right? I’m really excited she’s on our team! She was such a big help last project, I can’t wait to work with her again!"
        voice "audio/Apollo/Day 1 ID/apollo_line024.mp3"
        a_id "I just... hope she feels the same way about me."
        voice "audio/Barby/Day 1 ID/barby_line027.mp3"
        b_id "Really? When?"
        voice "audio/Apollo/Day 1 ID/apollo_line025.mp3"
        
        a_id "...When you worked with her?"
        voice "audio/Barby/Day 1 ID/barby_line028.mp3"
        b_id "Yeah! Right..."

        hide kendra_id
    elif current_id == "M.J Grey":
        show mj_id at zoomin
        $ renpy.pause(1.5, hard=True)
        voice "audio/Apollo/Day 1 ID/apollo_line026.mp3"
        a_id "You remember MJ, right?"
        voice "audio/Barby/Day 1 ID/barby_line029.mp3"
        b_id "Right... What’s their job, again?"
        voice "audio/Apollo/Day 1 ID/apollo_line027.mp3"
        a_id "... I don’t. Know."
        voice "audio/Apollo/Day 1 ID/apollo_line029.mp3"
        a_id "Well, as long as they’re doing their part in the team, it should be fine!"
        voice "audio/Barby/Day 1 ID/barby_line030.mp3"
        b_id "I wonder what MJ stands for."
        voice "audio/Apollo/Day 1 ID/apollo_line029.mp3"
        a_id "Maybe we can ask them... I wanna know, too."
        voice "audio/Apollo/Day 1 ID/apollo_line030.mp3"
        a_id "Huh. Their surname’s familiar. Maybe I heard it from my family once...?"
        voice "audio/Barby/Day 1 ID/barby_line031.mp3"
        b_id "That’s a pretty common last name, though."
        voice "audio/Apollo/Day 1 ID/apollo_line031.mp3"
        a_id "Ah. That’s true."
        voice "audio/Barby/Day 1 ID/barby_line032.mp3"
        b_id "There’s at least 50 shades of it."

        hide mj_id
    elif current_id == "Dave":
        show dave_id at zoomin
        $ renpy.pause(1.5, hard=True)
        voice "audio/Apollo/Day 1 ID/apollo_line032.mp3"
        a_id "Ah, Dave."
        voice "audio/Barby/Day 1 ID/barby_line033.mp3"
        b_id "I miss Dave."
        voice "audio/Apollo/Day 1 ID/apollo_line033.mp3"

        a_id "Me too... it’s been so long since his employee of the month streak."
        voice "audio/Barby/Day 1 ID/barby_line034.mp3"
        b_id "He didn’t come in to take a photo?"
        voice "audio/Apollo/Day 1 ID/apollo_line034.mp3"
        a_id "Mm... he hasn’t come back to the office since the divorce."
        voice "audio/Barby/Day 1 ID/barby_line035.mp3"
        b_id "Well, you and I haven’t been here for at least 6 weeks, so maybe things have changed?"
        voice "audio/Apollo/Day 1 ID/apollo_line035.mp3"
        a_id "I’m not sure. He hasn’t logged in or anything."
        voice "audio/Apollo/Day 1 ID/apollo_line036.mp3"
        a_id "Maybe check around and ship his ID if he isn’t here?"
        voice "audio/Barby/Day 1 ID/barby_line036.mp3"
        b_id "Sure! I’ll look around and get on my computer to get it shipped later."
        hide dave_id
    elif current_id == "Deez":
        show deez_id at zoomin
        $ renpy.pause(1.5, hard=True)
        voice "audio/Barby/Day 1 ID/barby_line037.mp3"
        b_id "Who!?"
        voice "audio/Apollo/Day 1 ID/apollo_line037.mp3"
        a_id "Our new intern!"
        voice "audio/Barby/Day 1 ID/barby_line038.mp3"
        b_id "Ah. I see it now."
        voice "audio/Barby/Day 1 ID/barby_line039.mp3"
        b_id "Why... is his ID uhm, different and laminated?"
        voice "audio/Apollo/Day 1 ID/apollo_line038.mp3"
        a_id "Ah, weeelll... interns don’t really get IDs so I made one for him! So he won’t feel left out!"
        voice "audio/Barby/Day 1 ID/barby_line040.mp3"
        b_id "Aww, that’s pretty thoughtful."
        voice "audio/Barby/Day 1 ID/barby_line041.mp3"
        b_id "Maybe I can help him, tour him around better."
        hide deez_id
    elif current_id == "done":
        show apo defaultt with dissolve
        $ quick_menu = True
        voice "audio/Apollo/Day 1 ID/apollo_line039.mp3"
        a "Okay, I need to go to the meeting now. You’ve got this, don’t you, Barby?"
        show apo default
        voice "audio/Barby/Day 1 ID/barby_line042.mp3"
        b "Like you said, it’ll be easy peasy."
        voice "audio/Barby/Day 1 ID/barby_line043.mp3"
        b "Well, I wanted to ask... I know we’ve got the deadline already, but what about our project? Do you know what it is?"
        show apo defaultt
        voice "audio/Apollo/Day 1 ID/apollo_line040.mp3"
        a "I... don’t know, but I’ll probably find out in the meeting. If I can get into the meeting, haha!"
        show apo default
        voice "audio/Barby/Day 1 ID/barby_line044.mp3"
        b "Are you sure you don’t want me to help you figure it out?"
        show apo defaultt
        voice "audio/Apollo/Day 1 ID/apollo_line041.mp3"
        a "I’m sure! Now go on, Barby, those IDs aren’t going to distribute themselves."
        show apo default
        voice "audio/Barby/Day 1 ID/barby_line045.mp3"
        b "If you say so. Well, good luck with the meeting!"
        show apo defaultt
        voice "audio/Apollo/Day 1 ID/apollo_line042.mp3"
        a "Thanks Barb, I'll see you later!"
        
        $ quick_menu = False
        scene black with fade
        
        $ quick_menu = True
        
        voice "audio/Barby/Day 1 OW/barby_line046.mp3"
        b default "Just gotta meet people, old and new, with the new little position of assistant manager."
        voice "audio/Barby/Day 1 OW/barby_line047.mp3"
        b default "Easy peasy…!"
        $ quick_menu = False
        play sound "audio/SFX/Day 1 /sfx_door.mp3"
        jump rooms
    
    call screen id_screen