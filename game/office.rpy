default employee_id = ""

transform down:
    ypos 100
screen officewalk():
    tag menu

    imagebutton:
        idle "mj_standing.png"
        hover "mj_standing_hover.png"
        xpos 0.5
        ypos 0.5
        action [SetVariable("employee_id", "M.J Grey"), Jump("officemeet")]


label officemeet(item_name=None):
    hide screen officewalk
    window auto hideO

    if employee_id == "M.J Grey":
        show mj default at down
        b "Hiya! MJ Grey, was it?"
        m "That I am! MJ Grey, here at your service. How can I help you, Barby?"
        b "Oh, um, I’m actually here to help you!"
        m "Oh, no, no, no, please, allow me to help you out. It’s no problem."

        b "I appreciate it! Thank you! But it {i}is{/i} my job to assist, as the assistant manager."
        m "Yes, but your wellbeing is my wellbeing! If you let me help you out, then you’re also helping me out in a way. It’s a win-win, isn’t it?"
        b "...Sure..!"
        b "Uhh, Here's your ID!"
        hide mj default
        pause 0.2

        show mj_id with zoomin
        $ renpy.pause(1.5, hard=True)
        #sfx_id2
        m "Neat, thanks. Hey, I don’t look bad."
        b "Yeah… you and I worked together before, right?"
        m "Yes? What about it?"
        b "That’s what I thought! Just jogging my memory."
        m "Huh? It wasn’t that long ago though."
        b "Yeah… time flies!"
        hide mj_id
        show mj default
        menu chatting:
            set picked
            "What does it stand for?":
                b "Can I ask what MJ stands for?"
                m "Oh, it’s nothing special. Just plain old MJ, haha!"
                b "They didn’t answer the question. Aww…" 
                m "I’m surprised it isn’t written on my ID, actually. Not that it’s an issue. I like being MJ more anyway."
                b "Oh! If that’s the case, then you can just be MJ."
                b "Follow your heart."
                m "Hm! Apollo says that sometimes."
                b "Yeah."
                jump chatting
            "What department are you from?":
                b "Just to make sure— with the whole name being faded and everything— what exactly {i}is{/i} your job title?"
                m "Hmm? What do you mean?"
                m "I am a part of the team, if that’s what you were wondering."
                b "Oh yes, of course."
                jump chatting
            "How's work?":
                b "So, how's work been so far?"
                m "Well, we don't know what our job actually is yet, but we're making good progress!"
                b "That's true—I just got here, but it looks like a lot’s already being done?"
                m "Yep! Everyone here is so hardworking."
                m "You know, the intern offered me coffee even though I didn’t ask for it. How kind." 
                b "I’m glad you’ve been experiencing a positive work environment. It looks like the intern got the memo!"
                b "We’ve… always tried to make things as nice as possible for each other. We’re all in the same boat, after all."
                jump chatting
            "How's life?":
                b "Outside all of that, how are you?"
                m "It’s all been fine and dandy on my end!"
                m "Though the recent uptick in work has left me with less time to practice my music, which is a bummer."
                b "Aw, I’m sorry to hear that. Hopefully you can play some more… after this project? I mean- I’d love to hear you play!"
                m "Aww, thank you. Maybe one day. Though I’m probably rusty by now."
                m "How about you?" 
                b "Me? Like… if I do any music?"
                m "I meant how’s your life."
                b "My life… oh god… the life insurance…"
                b "Sorry ‘bout that! Talkin’ to myself again, haha! Classic. Haha! Hah!"
                b "... MJ. Why am I like this?"
                m "What? No, it's fine you’re not cringe or anything. It’s okay, I’ve been tuning out when you talk to yourself, so no worries about me hearing anything I’m not supposed to!"
                b "Oh, phew."
                b "... wait…! Have you been doing that this whole conversation?!"
                m "xD"
                return()



