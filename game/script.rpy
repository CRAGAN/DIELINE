define b = Character("Barby")
define a = Character("Apollo", image= "i_apo", callback=name_callback,cb_name="Apollo", color = "#383d70")
define k = Character("Kendra", image= "i_ken", callback=name_callback,cb_name="Kendra", color = "#70384e")
define m = Character("MJ", image= "i_m", callback=name_callback,cb_name="MJ", color = "#3f7038")
define d = Character("Deez", image= "i_de", callback=name_callback,cb_name="Deez", color = "#523870")

default see_ids = False

transform zoomin:
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    linear 1.5 zoom 1.5

label start:

    #scene bg barbyclocksin
    #sfx clockin

    b "Shucks… I haven’t seen her since we got discharged."
    b "It should be fine. It should be normal."
    b "I can’t waste time overthinking."

    # Barby walks into manager room cg
    #sfx walking

    b "...Hiya, Apollo—I mean—boss! Good to see you again!"
    a "Oh, good morning Barby! Y—you don’t have to call me boss, I’m just your regular ol’ Apollo!" 
    b "Oh! Snap! Sorry, boss. SHOOT! AH!"
    a "Haha, every time you call me boss, I’m calling you boss, too! It’s only fair with all those emails you’ve sent with my name."
    b "Aw—hey, you know it was an accident… You have my account, too. How’d {i}you{/i} not get confused?"
    a "I triple dipple check all the time!"
    b "Wow! Please don’t say that word again." 
    a "Uhh… okay? But really, Apollo’s just fine and dandy."
    a "And hey, congratulations on {i}your{/i} promotion…! I mean look at you, ohoho, assistant manager now? You’re totally killing it!"
    b "Ahh...! Thank you. Killing it, haha, just like. The."
    b "Truck."
    a "Oh!"

    a "The truck that killed our old manager?"
    a "Yes, it was a sudden end, but that's just the cycle of life and death: a truly beautifully inevitable part of us all. I hope Mr. Sensin is resting easy now."
    b "…Wow."

    a "He’s in good hands now—I’d know! Teehee!"
    b "At least that was taken care of…" 
    # back to the scene
    b "Speaking of, have you heard back from your insurance? About the accident?" 
    a "Oh goodness, no, I haven’t! Have you? I’m worried…" 
    b "Agh, don’t be worried!"
    b "I’ll handle it for both of us :)! I don’t have too much to do yet, since it seems like a lot of my responsibilities are waiting on others." 
    a "Are you sure? I know we’re supposed to fill it out together… Sorry, but being the new manager sure has me a little frazzled. Maybe I can still help out—?" 
    b "You’ve got a whole team to handle. I'd be happy to help out!"
    b "That’s what {i}assistant manager{/i} means, after all. Let me {i}assist{/i} my manager."
    a "I—you’re right. We got this, we have to stay positive for our first day! Well, if you’re up for it… here!"
    # IDs come out
    # sfx_id1
    a "I know we just clocked in, but it’s a pretty easy task. Could you distribute the new IDs to the team?" 
    a "I’d do it myself, but I have to attend this online conference with corporate. I have yet to figure out how to log into Skycloud Meet, haha…"

    $ picked = []
    menu idchoice:
        set picked
        "Skycloudmeet?":
            b "We switched to Skycloud Meet already?"
            a "Err, yeah. It’s supposed to work better with the other Sera, Fim & Co. software we’re using, yet..."
            a "It’s kinda complicated. I’m not good at technology— but I’m positive I’ll figure it out!"
            jump idchoice
            # return to choices

        "But I don't know the team.":
            b "Ah, but I don’t even know who’s part of the team yet."
            a "It’s okay, you already know most of them by now! All their names and faces are on their IDs too, so you can figure it out easy peasy!"
            jump idchoice
            # return to choices

        "Sure! Easy!":
            jump id_see

label id_see:
    b "Alright, no problem, then! I can do that."
    a "Sweet! Here you go!"

    call screen id_screen

    #point and click on the IDs but ill make a choice list for now.
    # menu idlist:
    #     set picked
    #     "Fredrick Ibarra":
    #         "NAME: Fredrick “Barby” Ibarra\n
    #         ID: #NS0N-0309\n
    #         POSITION: Managerial Secretary Assistant Manager"
    #         b "Barby It’s me!"
    #         jump idlist

    #     "Apollo Knight":
    #         "NAME: Apollo Knight\n
    #         ID: #C4-0407\n
    #         POSITION: Assistant Manager"
    #         b "Oh, this is your ID! You have such an {i}original character do not steal{/i} name."  
    #         a "What does that mean?" 
    #         b "Uh. Nothing, boss, here!"
    #         a "I told you not to call me that Barbs!"
    #         b "Sorry!!!"
    #         jump idlist

    #     "Kendra Bell":
    #         "NAME: Kendra Bell\n
    #         ID: #ABC-0115\n
    #         POSITION: Storage Compliance Operations Technician"
    #         a "If you think her name rings a bell, this is the person who went around the office in roller skates!"
    #         b "Oh! Her! Yeah, you told me about that."
    #         a "You were there, though…?"
    #         b "Well, yeah, but…"
    #         b "She looks so different with her new hair…" 
    #         a "Right? I’m really excited she’s on our team! She was such a big help last project, I can’t wait to work with her again!"

    #         a "I just… hope she feels the same way about me."
    #         b "Really? When?"
    #         a "...When you worked with her?"
    #         b "Yeah! Right…"
    #         jump idlist

    #     "M.J Grey":
    #         "NAME: M.J Grey\n
    #         ID: #C4-0420\n
    #         POSITION: (scrubbed out) Team Member"
    #         a "You remember MJ, right?"
    #         b "Right… What’s their job, again?"
    #         a "... I don’t. Know."
    #         a "Well, as long as they’re doing their part in the team, it should be fine!"
    #         b "I wonder what MJ stands for."
    #         a "Maybe we can ask them… I wanna know, too."
    #         a "Huh. Their surname’s familiar. Maybe I heard it from my family once…?"
    #         b "That’s a pretty common last name, though."
    #         a "Ah. That’s true."
    #         b "There’s at least 50 shades of it."
    #         jump idlist
        
    #     "Dave":
    #         "NAME: Romeo Anastasia Malk\n
    #         ID: #C4-0515\n
    #         POSITION: Information Storage Project Lead
    #         (dave doesnt have a pfp)"
    #         a "Ah, Dave."
    #         b "I miss Dave."
    #         a "Me too… it’s been so long since his employee of the month streak."
    #         b "He didn’t come in to take a photo?"
    #         a "Mm… he hasn’t come back to the office since the divorce."
    #         b "Well, you and I haven’t been here for at least 6 weeks, so maybe things have changed?"
    #         a "I’m not sure. He hasn’t logged in or anything."
    #         a "Maybe check around and ship his ID if he isn’t here?"
    #         b "Sure! I’ll look around and get on my computer to get it shipped later."
    #         jump idlist

    #     "Daniel Emil Elezar Zeimermalng - Deez":
    #         "NAME: Daniel Emil Elezar Zeimermalng\n
    #         ID: #C4-1112\n
    #         POSITION: Facilitator of Team Needs and General Maintenance"
    #         b "Who!?"
    #         a "Our new intern!"
    #         b "Ah. I see it now."
    #         b "Why… is his ID uhm, different and laminated?"
    #         a "Ah, weeelll… interns don’t really get IDs so I made one for him! So he won’t feel left out!"
    #         b "Aww, that’s pretty thoughtful."
    #         b "Maybe I can help him, tour him around better."
    #         jump idlist
    #         # When all IDs have been clicked OR make a button appear that’s like “Done looking”
        
    #     "Done looking?":
    #         a "Okay, I need to go to the meeting now. You’ve got this, don’t you, Barby?"
    #         b "Like you said, it’ll be easy peasy."
    #         b "Well, I wanted to ask… I know we’ve got the deadline already, but what about our project? Do you know what it is?"
    #         a "I… don’t know, but I’ll probably find out in the meeting. If I can get into the meeting, haha!"
    #         b "Are you sure you don’t want me to help you figure it out?"
    #         a "I’m sure! Now go on, Barby, those IDs aren’t going to distribute themselves."
    #         b "If you say so. Well, good luck with the meeting!"
    #         a "Thank you!"
    #         jump officewalk

label officewalk:
    #sfx_door
    b "Just gotta meet people, old and new, with the new little position of assistant manager."
    b "Easy peasy…!"
    # point and click section

    call screen officewalk
    if current_id == "M.J Grey":
        b "Alright, gotta go check on some things!"
        m "Okay! Let me know if you need help!"
        b "Let me know if—! Aww man."
        m "I win, heh." 
        call screen officewalk
label meeting:
    ""

label day2:
