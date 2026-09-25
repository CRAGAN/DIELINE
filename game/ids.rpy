default current_id = ""

transform hoverup:
    on hover:
        linear 0.15 yoffset -20
    on idle:
        linear 0.15 yoffset 0

screen id_screen():
    add "images/bg overworld/overlay.png" blend 'multiply' alpha 0.4
    tag menu
   
    imagebutton:
        idle "barby_id.png"
        xpos 100
        ypos 300
        action [ SetVariable("current_id", "Fredrick Ibarra"), Jump("read_id") ]
        at hoverup

    imagebutton:
        idle "apollo_id.png"
        xpos 300
        ypos 300
        action [ SetVariable("current_id", "Apollo Knight"), Jump("read_id") ]
        at hoverup
    
    imagebutton:
        idle "kendra_id.png"
        xpos 500
        ypos 300
        action [ SetVariable("current_id", "Kendra Bell"), Jump("read_id") ]
        at hoverup
    
    imagebutton:
        idle "mj_id.png"
        xpos 700
        ypos 300
        action [ SetVariable("current_id", "M.J Grey"), Jump("read_id") ]
        at hoverup
    
    imagebutton:
        idle "dave_id.png"
        xpos 900
        ypos 300
        action [ SetVariable("current_id", "Dave"), Jump("read_id") ]
        at hoverup
    
    imagebutton:
        idle "deez_id.png"
        xpos 1100
        ypos 300
        action [ SetVariable("current_id", "Deez"), Jump("read_id") ]
        at hoverup

    textbutton "Done looking?":
        xalign 0.5
        yalign 0.95
        action [ SetVariable("current_id", "done"), Jump("read_id") ]
        at hoverup



label read_id(item_name=None):
    hide screen id_screen
    window auto hide
    # call screen ids

    if current_id == "Fredrick Ibarra":
        show barby_id at zoomin
        $ renpy.pause(1.5, hard=True)
        "NAME: Fredrick “Barby” Ibarra\n
        ID: #NS0N-0309\n
        POSITION: Managerial Secretary Assistant Manager"
        b "Barby It’s me!"
        hide barby_id
    elif current_id == "Apollo Knight":
        show apollo_id at zoomin
        $ renpy.pause(1.5, hard=True)
        "NAME: Apollo Knight\n
        ID: #C4-0407\n
        POSITION: Assistant Manager"
        b "Oh, this is your ID! You have such an {i}original character do not steal{/i} name."  
        a "What does that mean?" 
        b "Uh. Nothing, boss, here!"
        a "I told you not to call me that Barbs!"
        b "Sorry!!!"
        hide apollo_id
    elif current_id == "Kendra Bell":
        show kendra_id at zoomin
        $ renpy.pause(1.5, hard=True)
        "NAME: Kendra Bell\n
        ID: #ABC-0115\n
        POSITION: Storage Compliance Operations Technician"
        a "If you think her name rings a bell, this is the person who went around the office in roller skates!"
        b "Oh! Her! Yeah, you told me about that."
        a "You were there, though…?"
        b "Well, yeah, but…"
        b "She looks so different with her new hair…" 
        a "Right? I’m really excited she’s on our team! She was such a big help last project, I can’t wait to work with her again!"

        a "I just… hope she feels the same way about me."
        b "Really? When?"
        a "...When you worked with her?"
        b "Yeah! Right…"
        hide kendra_id
    elif current_id == "M.J Grey":
        show mj_id at zoomin
        $ renpy.pause(1.5, hard=True)
        "NAME: M.J Grey\n
        ID: #C4-0420\n
        POSITION: (scrubbed out) Team Member"
        a "You remember MJ, right?"
        b "Right… What’s their job, again?"
        a "... I don’t. Know."
        a "Well, as long as they’re doing their part in the team, it should be fine!"
        b "I wonder what MJ stands for."
        a "Maybe we can ask them… I wanna know, too."
        a "Huh. Their surname’s familiar. Maybe I heard it from my family once…?"
        b "That’s a pretty common last name, though."
        a "Ah. That’s true."
        b "There’s at least 50 shades of it."
        hide mj_id
    elif current_id == "Dave":
        show dave_id at zoomin
        $ renpy.pause(1.5, hard=True)
        "NAME: Romeo Anastasia Malk\n
        ID: #C4-0515\n
        POSITION: Information Storage Project Lead"
        a "Ah, Dave."
        b "I miss Dave."
        a "Me too… it’s been so long since his employee of the month streak."
        b "He didn’t come in to take a photo?"
        a "Mm… he hasn’t come back to the office since the divorce."
        b "Well, you and I haven’t been here for at least 6 weeks, so maybe things have changed?"
        a "I’m not sure. He hasn’t logged in or anything."
        a "Maybe check around and ship his ID if he isn’t here?"
        b "Sure! I’ll look around and get on my computer to get it shipped later."
        hide dave_id
    elif current_id == "Deez":
        show deez_id at zoomin
        $ renpy.pause(1.5, hard=True)
        "NAME: Daniel Emil Elezar Zeimermalng\n
        ID: #C4-1112\n
        POSITION: Facilitator of Team Needs and General Maintenance"
        b "Who!?"
        a "Our new intern!"
        b "Ah. I see it now."
        b "Why… is his ID uhm, different and laminated?"
        a "Ah, weeelll… interns don’t really get IDs so I made one for him! So he won’t feel left out!"
        b "Aww, that’s pretty thoughtful."
        b "Maybe I can help him, tour him around better."
        hide deez_id
    elif current_id == "done":
        a "Okay, I need to go to the meeting now. You’ve got this, don’t you, Barby?"
        b "Like you said, it’ll be easy peasy."
        b "Well, I wanted to ask… I know we’ve got the deadline already, but what about our project? Do you know what it is?"
        a "I… don’t know, but I’ll probably find out in the meeting. If I can get into the meeting, haha!"
        b "Are you sure you don’t want me to help you figure it out?"
        a "I’m sure! Now go on, Barby, those IDs aren’t going to distribute themselves."
        b "If you say so. Well, good luck with the meeting!"
        a "Thank you!"
        scene black with fade
        jump rooms
    
    call screen id_screen