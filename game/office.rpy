# default employee_id = ""

# transform down:
#     ypos 100
# screen officewalk():
#     tag menu

#     imagebutton:
#         idle "mj_standing.png"
#         hover "mj_standing_hover.png"
#         xpos 0.5
#         ypos 0.5
#         action [SetVariable("employee_id", "M.J Grey"), Jump("officemeet")]

label officemeetday1(item_name=None):
    hide screen officewalk
    window auto hide

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
        # hide mj default
        # pause 0.2

        # show mj_id with zoomin
        # $ renpy.pause(1.5, hard=True)
        #sfx_id2
        m "Neat, thanks. Hey, I don’t look bad."
        b "Yeah… you and I worked together before, right?"
        m "Yes? What about it?"
        b "That’s what I thought! Just jogging my memory."
        m "Huh? It wasn’t that long ago though."
        b "Yeah… time flies!"
        # hide mj_id
        # show mj default
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
        b "Alright, gotta go check on some things!"
        m "Okay! Let me know if you need help!"
        b "Let me know if—! Aww man."
        m "I win, heh." 

        if employee_id == "Kendra":
            b "Oh! Hiya, Kendra! Do you— do you need help with that?"
            k "AH! BARBY! UHH, ahem! Thanks but—it’s ahh… it’s all good, yeah. I'm almost done here."
            k "A-Anyways haha, I never got to properly thank you for the hairclip!"
            k "So! Thanks! Yes!"
            b "Right! All of them look so good on you!"
            k "Huh? But… you—you only gave me this one…"
            b "Oh! How about the other ones in your hair?"
            k "I… do you not remember? Is uhm, everything okay?"
            b "Ah, well, after the accident, my memory’s a little spotty, haha! Oops."
            b "Concussion, coma… both went away, so the amnesia should, too! Hopefully I don’t, uh, fumble anything before then."
            k "You… you really forgot everything? Oh, I see… I’m— I’m really sorry…"
            k "About the accident…"
            b "It’ll come back to me!!! I’ll try my hardest!"
            k "Okay… if you say so."
            b "..."
            k "..."
            #sfx_id2
            # ID pops out
            b "Here’s your ID, by the way!"
            k "Oh! Uhm, thank you." 
            #ID goes away, UI comes out
            menu chatting2:
                set picked
                "Compliment.":
                    b "You’ve got a really cool surname. It’s got a nice ring to it."
                    k "Oh, uh, thanks! It isn’t my birth name but…"
                    k "Everyone at my work- well, the theater one, called me ‘Bell’. ‘Cause I looked like one, and they said I was really noisy whenever I reacted to anything."
                    b "Ah! Well… I thought it suited you for other reasons; I’ve only talked to you for a bit, and you don’t sound super noisy."
                    b "Not that you’re quiet! Just that you’re, like. Yeah."
                    b "So you basically picked it?"
                    k "Aha, ha? Yeah… I don’t remember if I had a family or anything before I started working— and… basically living— at the soup kitchen."
                    k "I just kept working, and it became my life!" 
                    k "So that’s how I learned to do most of the things I do…!"
                    b "Ohh! Yeah, we’re like… forgetting twinsies."
                    k "Oh. Aha. Yeah…"
                    b "...Yeah. Just for now! Until I remember again."
                    jump chatting2
                "Roller skating?":
                    b "I heard you do roller skating? I think that’s really neat! I’ve always wanted to learn how to do that."
                    k "Hah, yeah, I do quite a lot of, ahh—things…!"
                    k "I don’t know if you, erm, remember this but, like… we planned on going roller skating together!"
                    k "It’s—it’s not important anymore though, o-of course! Especially since ahh—"
                    k "Your… leg. I was... yeah, I was wondering if your leg was, uhm, okay?"
                    b "Ah… my leg?"
                    #VA: Kendra is visibly shaken recalling the accident, says “accident” in a low voice/whisper 
                    k "Well… it looked pretty bad in the a-accident, and you’ve been a little wobbly while we talk."
                    #VA: Whispers “accident” 
                    b "Oh, you saw the… {i}accident{/i}?"
                    k "I was, uh, the one who called the emergency hotline…"
                    b "Oh…"
                    b "Um, I’ve healed a lot! So maybe… maybe we can still roller skate? I mean. If you still want to-! Even if I don’t remember…"
                    k "It’s…it’s whatever— I-I mean— don’t, uhm… don’t worry too hard about it! Maybe next time, when you’re…"
                    k "...Feeling better." 
                    b "Okay…"
                    jump chatting2
                "How's work?":
                    b "How’s work been for ya?"
                    k "Which one?"
                    b "Oh… this one?"
                    k "Ahh, it’s like— you know, the usual. So much of this and that, it’s a little crazy compared to my other jobs!"
                    k "Honestly, how can you guys manage this much work {i}all{/i} the time?"
                    b "Ough… sorry you have to deal with all that…"
                    k "But it’s okay! I-I’ve almost finished with everything before our team meet, so… it’s fineee."
                    b "Oh! Wow! That’s really… Wow! Congrats and, uh, good job? Color me surprised!"
                    k "Ahaha, it’s—it’s nothing! I’m just trying my best, like everyone else!"
                    jump chatting2
                "How's life?":
                    b "How’s life?"
                    k "Uh… good."
                    k "Yeah— ahh, yes. Just alright! Nothing too bad, I suppose."
                    k "How about… you?"
                    b "Me!?"
                    #VA: Dont shout too loud for the words in caps but shift the tone!
                    b "I’m not really thinking ‘bout it too much. I’m mostly thinking about you, WAIT. LIKE. HOW YOU’RE DOING??? Yeahh… like an assistant manager thinks about employees and— wellbeing…"
                    k "ME?! AHAHA OH! Oh like— like normal amounts of thinking about me! Your— your uhm, underling?"
                    b "UNDERLING!?"
                    k "S-SORRY! I mean, teammate! Like I said I’m…"
                    k "Good." 
                    b "Me. Me, too."
                    jump chatting2
                    return()
            b "Well, I hope you the best, uh, finishing up what you gotta do before the meet!"
            k "Ah! You’re going? Thank… thank you!"
        if employee_id == "Deez":
            #no nametag yet
            b "Hiya, there! Do you need help with that coffee machine?"
            #VA Deez: say this in a slightly cocky way more than nervous. Like “pssh! Haha Im such a capable person.” 
            d "No, I can fix—IT WAS BROKEN WHEN I FOUND IT—I SWEAR."
            b "That’s okay! It happens. We call it the {i}breakroom{/i} for a reason, haha!"
            d "..."
            
            #VA: in a low tone, a little awkward and sad that they didnt get the joke  
            b "...Cause things always break."
            #(or edited in voiceline) sfx_badjoke
            b "AHEM— I don't think we’ve met before. I’m Fredrick Ibarra! But people just call me Barby."
            b "What’s your name?"
            d "Right…introductions. I am a fresh catch, as they say in um. Finance."
            d "Daniel Emil Elazar Zémiermalng."
            d "My name is too long so you can call me {i}Deez{/i} for short."
            # change name in textbox to real nametag
            b "That I knew! Here’s your ID."
            #sfx_id2
            # ID pops out
            d "...Oh."
            d "It looks low budget. I-I don’t like it."
            b "Oh! Yes! The. Interns don’t actually get IDs… So our manager, Ms. Apollo Knight, made this for you herself!"
            #VA Deez: Flustered tone to feigning interest 
            d "OH! Uh—wow! It’s sooo-sooo good for a hand-made card! Explenditure!"
            d "She got my…pupils, my orbs right."
            d "I love it."
            # deadpan
            b "I’ll be sure to tell her!"
            #id foes away, UI comes out
            menu chatting3:
                set picked
                "Welcome!":
                    b "Welcome to the team! I also started out as an unpaid intern, so I understand the boat you’re in."
                    b "Please let me know if you need anything!"
                    d "Thank you for the warm regards."
                    d "But I disagree. I’m not on the boat, I’m paid."
                    b "... Paid {i}money{/i}?"
                    d "What else would I be paid in?"
                    b "A sense of fulfilment."
                    b "Resume fodder?" 
                    d "Oh. That, too, but economic currency is also there on the list."
                    b "Well, it’s good to know that the system’s changing for the better! I gotta tell the boss- DAMN IT- Apollo about this!" 
                    d "Until further notice, I will not be paid yet. But I will when they do compensate me. Which is soon. It will happen. Percentagely."
                    b "Oh."
                    b "Cool."
                    d "Likewise."
                    jump chatting2
                "Where did you learn to fic the coffee machine?":
                    # pan to coffee machine
                    b "Haha. So. Um. Where'd ya learn how to fix coffee machines?"
                    d "Di- Du- I’m a neutral born learner. I’m very complement in the ways of engineering machinery."
                    b "Oh! Alright?!"
                    b "You do engineering! That’s awesome! I took mechanics courses in an early college program during senior high- not the same thing, but you get me?"
                    b "Never went to college past that, though."
                    b "More convenient to pursue a job instead, am I right?" 
                    #VA Deez: say the words in italics as a whisper, or a mumble to himself 
                    d "{i}Oh no{/i}—uh! I mean. Yeah! I relate to that experience, we are quart similar, like, like. Uh. I’m in college, and I’m doing a job!"
                    b "Wow! That’s commendable, really! Don’t go into debt though, haha!"
                    d "Impossible for me to do that. It’s very easy not to."
                    b " {i}Right.{/i}"
                    jump chatting2
                "How's work?":
                    b "How’s work been for you?"
                    d "It’s an experience of ease."
                    b "That’s words. In a sentence." 
                    d "Paragraph."
                    jump chatting2
                "How's life?":
                    b "So… how’s the life? Outside of work, y’know." 
                    d "I’m not deceased yet. So it’s going as it should."
                    b "Congratulations, then! What’ve you been up to? Hobbies, other responsibilities?"
                    d "I do a lot of things. Like. Uhhhhhhh…."
                    d "..."
                    d "An abundant amount. It’s a lot I can’t think of because there are so surplus."
                    #VA: Barby feels sad for Deez
                    b "...Sounds like you’re drowning in abundance."
                    d "You look like you have hobbies."
                    b "Depends who you ask!"
                    d "I’m asking you."
                    b "Well. Well- what do you consider a hobby?"
                    b "Haha, why are we talking about me." 
                    d "You keep talking at me so I’m talking at you."
                    b "That’s. So. Cool."
                    b "Since you asked so nicely, my favorite hobbies are making the work environment a friendly place for you and your work family."
                    d "That’s one hobby. You said it like it was plural."
                    #VA Barby: coughs
                    b " "
                    d "Why."
                    jump chatting2
                    return()
            b "It was nice chatting with you, but I gotta get back to work."
            b "Thanks, Deez! I’ll be sure to hold onto that. Your name. Trying to be better at remembering things."
            d "Clockwise."

label donetalking:
    b "I think that’s everyone! I haven't seen Dave around… he's probably working from home again."
    b "He doesn't live too far from here, so if I ship his ID now, he should receive it soon!"
    b "Just gotta get on my computer."
#sfx_computer

label officewalk5:
    