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

label officewalk2:
    #Click MJ
    b "Good morning, MJ!"
    m "Good morning! How are you?"
    b "Good! How are you?"
    m "Good!"

    #Click Deez
    b "Good morning, Deez!"
    d "Good morning."
    b "Do you need any help with anything?"
    d "Never." 
    b "Cool!"
    
    #Click Apollo
    b "Good morning, Apollo!"
    a "Good morning, Barby!"
    a "Ready to give it our all today?"
    b "You betcha!"

    #Click Kendra
    b "Good morning, Kendra!"
    k "Oh! Hi! Good morning!" 
    b "Hiya!"
    k "Hi!" 

    # click computer and didnt talk to everyone
    b "I’d better check on everybody first!"

    # click the breakroom
    b "That’s the breakroom... It’s not break time yet! I should get back to work…"

    # click computer and talked to everyone
    b "...Huh. Dave's still working remotely. He hasn't replied to any emails…"
    b "Odd."
    b "Well, I better get back to work!"
    jump breaktime2

label breaktime2:
    #     Kendra
    b "Hiya, Kendra! That’s a lot of work you seem to be handling during break time."
    k "Huh! O-oh! It’s break time?"
    K "Sorry! I-I got so swept up in all this work, haha!"
    k "I’ll just finish these last few things!"
    b "Need any help with it?"
    k "Um. I mean- it’s…"
    b "Let me help you sort these files while we chat."
    k "A-ah. Uh. Sure! I mean, I don’t mind — I DO mind, but in a good way — like, it’s helpful."
    k "Thank… you!" 
    b "Of course!"
    menu yapp:
        set picked
        "Manager":
            b "You were transferred in, right? What’s it like, working with Apollo as a new manager?"
            k "It’s- it’s been fine! Apollo is so kind and understanding and– and…"
            k "N-No problems with her at all."
            b "Are you sure? You sound… kind of not."
            k "No, there’s no issue at all, haha! Even if — even if it feels like she doesn’t like me, haha…"
            b "What?! What gave you that impression?" 
            k "Ahh don’t tell her I said that, okay?! I-I don’t want to get on her bad side any more than I already have…"
            b "I think you’d have to commit something more {i}grave{/i}  than murder to get on Apollo’s bad side."
            # sfx laugh track 
            b "{i}That wasn't even good?{/i}"
            b "B-but do go on!" 
            k "Well… there was this one time where, uhm, we got into a small disagreement."
            k "I-I wanted to, like, get everything done, all in one go! S-sure, it was a little… impractical, but we just HAD to finish it, a-and I know I deliver well even if I push myself a {i}little{/i} too hard sometimes but—"
            k "But she kept— kept insisting there wasn’t enough time to get everything done a-and to be practical and not to burn out and I…" 
            k "Gosh… I mean, she says really nice things but sometimes she looks at me… especially after the accident, I…"
            k "Ugh... I-I don't know. She's... cool. I just don't know what she thinks of me."
            b "Kendra... I... I wanna say just not to worry about it, but..." 
            b "I know it isn't that simple. Especially for people whose opinion matters to you." 
            b "I'm just sorry you feel that way; she's not like that. I'm sure she doesn't hate you. Or. Blame you for anything." 
            b "No one does." 
            k "Sigh. Like, I-I know I shouldn't let what others think get to me, either! But... it just does." 
            b 	"Aw... It's okay to feel that way..." 
            k "I know you two know each other well and she seems like a great, uh, coworker!"
            b "Yeah! Honestly we’re like… friends at this point."
            k "R-really?, like actual friends? From coworkers?"
            b "Yeah? Why?"
            k "Oh, I was just wondering. It’s just… some people think that it’s unprofessional to do that. Being friends with people from work."
            k "B-but I guess it’s nice to see that you’re, um, willing to get close with people even if they start out as workmates."
            k "Maybe I shouldn’t be surprised. I should’ve known you were, like, chill like that." 
            k "... ever since I got to know you more, you’ve been nothing but nice to me."
            k "Y-You and Apollo, really. You both seem like really kind people."
            k "Even if things are hectic right now, I-I think you guys are trying your best to make things work and manage everyone to their strengths."
            b "Oh! That’s- that’s really nice of you to say. Thank you."
            k "I-It’s nothing."
            k "..."
            k "Um, d-do you mind if I tell you something personal?"
            b "Of course. Whatever you’re, uh, comfy with!"
            k "Most of my life, I never thought about getting close to people. I was always, like, too busy anyway to get close to anyone, so I didn’t see the point…" 
            k "But things have been changing recently." 
            k "It's been nice getting to know people, even if it's hard, and even painful sometimes. It's, um, been pretty nice, actually..." 
            b "Aw… Well, I’d love to help you two become friends!" 
            k "Oh? Aw， really? Thank you so much…" 
            b "Yeah! How about… uh， remember that roller skating idea you mentioned yesterday? What if we all went together?" 
            k "{i}Oh.{/i}" 
            k "Um — well， if you’re more comfortable with that， then yeah! Haha! Of course!" 
            k "Cause… like. Person you know- better, more comfortable coming with them- yeah- haha! Of course!"
            k "All three of us."
            b "Alright! I’ll let her know!"
            b "Actually… hold on. It might be better for you to tell her. See how she feels about it first hand,"
            b "Maybe it’ll help ease your nerves, you know?"
            k "Ough… ooh… okay…! Yeah, sure! Yeah, yeah, you’re right. After all of this is over, yeah I’ll… ask her!"
            k "Thanks... really." 
            b "Yeah! Please, um, feel free to let me know if you need anything. Even if it’s not necessarily for work..."
            jump yapp
# return
        "So many tasks…":
            b “About yesterday’s team meeting… that was a lot of jobs you were assigned.”
            b "Now that I think about it, it feels a little unfair to unload so much on you… you sure you can handle it?"
            b "Especially when we don’t even know what the product we’re doing all this for is…"
            k "Oof… y-yeah, but I get it, Don’t worry! I can handle it no problem; it’s my job, after all! Even with the… circumstances."
            k "It’s just a shame Dave isn’t here anymore. He used to help with a lot of this." 
            b "Yeah. Wonder how he’s doing… the divorce must’ve been that bad if he still hasn’t shown up in person." 
            k "Yeah… I wonder. I hope he’s doing alright."
            b "...Hey, I know you're like the best fit for the jobs, but I still wanna help out."
            k "O-Oh? Um, sure?"
            b "Are there any other responsibilities I can help you with that aren’t too… {i}you know{/i}, hard on the leg?"
            k "Um, i-if you’re offering…! I have a really hard time with emails. Do you, um, think you could do those? If you'd be willing, I can give you my work account- if, if that's okay!"
            b "That’s my specialty! And sure, as long as you're comfortable!"
            k "Y-yeah, it's not like I have anything crazy there… but, gosh, thank you…"
            b "Ooh, how about… what kind of food do you like?"
            k "Oh, you don’t have to worry about that! I always forget to eat anyway, haha."
            b "What?! Kendra…"
            b "Alright, I’m getting you food, too."
            k "Aah, you– you really don’t have to! Do any of these things." 
            b "Kendra，please，take the help; it’s only fair. You’re already helping us so much!"  (Note the change from comma to semicolon for better flow) 
            b "And besides it’s not too much effort for me to do any of these things. It’s okay- I gotta make breakfast for myself and my roommate，anyway."  (Note the change from comma to semicolon for better flow) 
            k "Barby… thank you so much."
            b "Anytime!"
        
        "Why all the jobs?":
            b "Actually, if it’s alright, I’ve been curious since last meeting… it sounded like you have had lots of experience in doing all sorts of jobs!"
            b "It’s really impressive! I just wanted to know how you have so much?" 
            k "Ahh, oh jeez, it’s nothing… I’ve just been working for a {i}looong{/i} time, haha!"
            b "Really…? Wow, maybe she’s older than she looks…" 
            k "I-I’m not {i}old{/i} old!! I swear! I’ve just uhh, been through so many jobs, like, since I was a kid." 
            b "Ah— no no sorry! I was just muttering to myself but—ah, since you were a kid? L-like part timing as a teen?" 
            k "Uhh, nooo… since I was like, 5 or sooo… I don’t really remember." 
            b "W-what?! That’s so young! My condolences—wait, I mean—"
            k "Hahaha, no, it’s alright! I kinda had to since I was just by myself for a long time… b-but you don’t need to worry anymore! I think… I think I’m pretty happy now." 
            k "Uhh yeaah,我 am maybe… more than a little stressed out over the tasks given to me，butI really am doing alright!"  (Note the change from comma to semicolon for better flow) 
            k "I-I don’t think you really remember，butI’ve adopted a kid，andI co-parent with a friend，not to mention this lovely job and great coworkers! It’s all l could ever ask for…"  (Note the change from comma to semicolon for better flow) 
            b "That’s… wonderful Kendra，really! IIm happy for you…"  (Note the change from comma to semicolon for better flow) 
            b "And happy to, uh, be a part of it and see you happy."
            b "Maybe we can just be more than great coworkers in the future!" 
            k "H-huh?! More— aha… more than great coworkers?!"
            b "Of course! Maybe… great friends, soon?" 
            k "... pfft—! Hahaha, I uhh, think we’re already on track, Barby."
            b "Haha, I’m glad! I think so too."
            jump yapp 
#return

    b "Ah snap, I should leave you to it! Gotta wrap everything up so you can take your break, right?"
    k "Ohh uhh— yeah! Right, I’ve got lots to do so…"
    k "Still though, thank you for this talk. I-I feel a lot better. Bye Barby, I-I’ll see you in the break room?"
    b "You betcha! See you Kendra!" 

    #Apollo 

    b "Hiya, Apollo! It’s break time."
    a "Oh hi Barbs! Aaahhh it is? Oh cracker jackers, I lost track of time!"
    b "Ah! Haha! You really need to stop saying things like that!"
    a "I’ll just finish up over here, first! Moving my things from the cubicle to the new office is taking a bit, but I need to catch a breath, anyway. How ‘bout a chat?"
    menu yappy:
        "Kendra":
            b "I’m a little concerned… that was a lot of roles we pushed on Kendra, wasn’t it?"
            a "Yeah… I’m a big bunch worried, too."
            a "But I don’t know who else we could’ve given it to. She’s, like, the best and only pick for all those tasks, after all."
            b "That’s true, but still… isn’t that a lot for one person?"
            b "Maybe we should, like… do something about it?"
            a "I agree! I’ve been trying to think of something, honestly, but…"
            a "Who else could do those things, honestly? :(" 
            a "I know MJ is already helping her out a bit! And she’s teaching Deez, so when he figures things out, he can help more! Especially since he said he already knows most of the stuff, anyway."
            b "I just, you know, it feels bad…" 
            b "But we also have a lot to do on our ends…" 
            a "Yeah… man… I. I should apologize to her." 
            a "I’m the manager; I’m the one managing this whole thing… she shouldn’t have to get overworked." 
            a "Ogh... and to think I did it all in a team meeting in front of everyone... ogh... ough..." 
            a "I’m such a dummy! I’m sorry, Kendra…" 
            b "... Hey." 
            b "You... maybe you should talk to her... you know?" 
            a "... I dunno... would she even want to talk to me? She must—she must hate me after everything I’ve done!" 
            b "Hey，it's worth a shot，right?" 
            b "And don’t worry, I’m sure she doesn’t hate you or is upset with you about it…" 
            b "If anything, she looks… just nervous about getting it done right. So, honestly, she might need the encouragement."
            b "And if there’s anyone I know who’s great at giving that… well…"
            a "?"
            a "Aw, shucks, Barby!"
            a "You’re right. It’s worth a shot. I’ll talk with her."
            a "Thanks a lot… I think I needed that big ol’ push, haha."
            b "Of course! Anything for my buddy boss!"
            a "Heeey... hahaha! That’s why you’re my favorite assistant manager!"
            jump yappy
        "Am I acting weird?":
            b "Hey, Apollo… have I been acting weird since the accident?"
            a "Oh nooo! No, no, no, Barby!"
            a "... Well. Actually… yes…"
            a "You just seem to respond to things like you don’t really remember them? Or not as much? It kinda catches me off guard sometimes ‘cause you’re not usually this forgetful."
            b "Oh… Well, yeah… well."
            b "It’s just some sort of thing… But it’ll get better!"
            b "I remember more and more at a time, so it’s probably just some... post- accident stuff."
            a "Yeah… MJ said that sometimes people get post- traumatic amnesia or something… but that it doesn’t usually last this long."
            b "Really? I-I mean it’s not really amnesia, it's just a bit of forgetting! Nothing too serious!"
            a "Barby…"
            a "You can always open up to me about things, you know? Not only as your manager, but as your friend too…"
            b "Mngh— it’s really okay Apollo! Don’t worry about me, I’m aye-okay! I’m doing better everyday!" 
            a "Okay… well, if you’re sure it’ll be okay, then I’m sure it’ll be okay…"
            a "But — listen, Barbs. You’re still alrighty and tighty, no matter how frazzled and shaken the accident might've left you."
            b "Yeah… thanks! I just… I don’t wanna drag anything down, haha!"
            a "You never do! Honestly, I’m worried I might be…"
            b "Really??? Why?"
            a "Well- my… thingy. It’s been hard to type and write, which is, like, most of my job!"
            a "And, to be honest, I’m still kinda stressing. I feel like I’m really not good at… or maybe not even cut out for this kinda thing… I know it’s really, really not good to admit!"
            b "Apollo, you’re trying your best. You’re literally just learning how to do all of this, and, well, I think you’ve been getting better!"
            a "Ough, aw, thank you!"
            a "Hey, if you think I’m doing okay, then, you’re doing okayer!! Hehe! So, don’t worry about ‘acting weird’ or anything after the accident."
            a "...Except."
            a "Oh shucks. Insurance."
            b "Don’t worry! I’ve been handling it!"
            a "Oh! Okie! Thank you!" 
            a "I keep getting calls from emails and lawyers, actually." 
            b "Me, too. It’s like- I think it’s a call from work- something important- cause they don’t even say they’re calling about the crash until later."
            a "Right?? So you end up answering and listening to them all and aghh!!!"
            jump yappy
        "Dungeons & Dragons":
            b "We talked about playing a tabletop sometime, right?"
            a "Oh death, yes yes!! I would love to play with everyone! Maybe… maybe we can play with our whole team after this project!" 
            a "Haha, I should use my new boss—err, managerial powers to make everyone attend a required job mandated roleplay thing!" 
            a "OH! That sounds bad uhh— I’m kidding, haha! If they don’t want to play, I don’t want to force them!"
            a "Only if they want to; it’s not everyone’s cup of coco after all…"
            b "Oh, well I’m sure there’s at least one person here who’d love to play with us, and we’ll make it easy for new players!"
            b "Nothing too intense, I could be the dungeon master for our first campaign! Just something short and sweet— I can see it now, a fantasy amusement park adventure full of twist and turns!"
            a "Ohh that sounds like a lot of fun! Hehe, surely it’ll be a rollercoaster of a ride!" 
            b "I was just wondering– what classes would our team be? Just in theory."
            a "In D&D? OMD, like classic fantasy, player handbook style?"
            b "Yeah, yeah. Like… I think you’d play a pretty good cleric."
            a "A cleric? What do they do?"
            b "Ohh you know, if you’re our manager, you can totally be our cult leader cleric? Haha, joking, I mean you’d be a great healer—"
            a "WHAT? HUH? CULT? ME IN A CULT? WHAAAT? HAAHAAHAAHAAA—"
            b "Hahahaha…?"
            a "You’re so silly! Let’s talk about something else!"

        b "Oh, do you need help moving your things, actually?"
        a "Aww thanks Barbs, but I’m good! Go take your well deserved break!"
        b "Well, if you say so! See you in the break room!" 
    
#     MJ
# Storage 
# They can carry more than 5 pounds if they really try 

    m  "Hum hum hum…"
    b "Hiya, MJ! I see you're hard at work."
    b "But it is break time now."
    m  "Oh! I didn’t notice. Thanks for telling me."
    b "Of course."

    menu sirtalkalot:
        "Carrying":
            b "Did you bring all these boxes in here?"
            m  "Yep! I was helping Kendra."
            m  "Guess what? Turns out I can carry more than five pounds if I really try."
            b "Wow! That’s great to hear."
            m  "But only for a few seconds though. Which means I keep having to put stuff down and pick them up again."
            m  "At this rate, though, I’ll probably start getting better at it, soon."
            b "Aw. Well, that’s okay. You don’t need to force yourself if you really can’t handle it."
            m  "Hah! That’s funny. Good one, Barby!" 
            m  "Assistant manager saying there’s no need to push yourself if you can’t handle a task… that’s a good one!" 
            b "What?" 
            m  "I’m just kidding with you, Barby. I know you mean it." 
            b "Oh! Okay!" 
            b "... I know I’m not the best assistant manager; is there anything I can do to, um. Do better than we are right now?" 
            m  "Hm… I think you’ll learn with time. We still have a while together as a team, so you can take some effort every day and learn how to work with each employee and their strengths!" 
            b "Woah… you’re right! Thanks, MJ!" 
            m  "And be sure to learn how to work with your own, too." 
            b "I’ll try my best!"
            jump sirtalkalot
        "Why work here?":
            b "So… how’d you start working here?"
            m "It’s nothing complicated. My… old job wasn’t working out, they had positions open, so I applied. Then here I am."
            b "What was your old job?"
            m "Haha, it wasn’t really much of a job, really. I just sang and played different instruments wherever for whoever hired me."
            b "Oh! That sounds fun."
            m "It was. Unfortunately, it couldn’t pay the bills, so I… needed something more stable."
            b "What about now? What do you do now?"
            m "I work here at SFC, of course!"
            b "And… what do you usually do here?"
            m "I usually walk around and talk to people. I’m pretty good at that."
            m "And now, picking up packages that weigh more than five pounds."
            Barby “Oh… I see!”
            b "Oh… I see!"
            b "That still doesn’t actually explain what their job is…"
            m "Why did you start working here?"
            b "Me? Uh. It was just. Job, y’know. Job that hired." 
            m "Are you unsatisfied with your work here?"
            b "No, no, no, no! Not at all! Very satisfied here!" 
            m "... Wow. That was a reaction."
            m "You’re not in trouble or anything, Barby. It’s not like I’m management."
            b "... Right."
            b "I’m management."
            m "You sure are!"
            jump sirtalkalot
        "Humming":
            b "You were humming a cute ‘lil tune earlier!"
            m "Oh? I was?"
            b "Yeah! May I know what it was?"
            m "It's probably one of my older compositions."
            b "Really? That's so cool!"
            m "Aw, thank you, but it's nothing special, really." 
            m "I could probably come up with something better if I had the time, which… I don't really have much of these days."
            b "Oh… but it's still really nice though!"
            m "I 'preciate it!"
            jump sirtalkalot

        #Click Breakroom (Haven’t talked to Everyone)
    b "How about I check if everyone’s realized it’s breaktime, first."
    #Deez
    b "Hiya, Deez! Taking your break already, are you?"
    b "You’re the only one who got the memo right away, haha! I had to tell everyone else."
    d "What? No."
    b "No?"
    d "I’m not taking a break. I’m working."
    b "Oh!"
    b "Well! It’s break time. So, y’know, you can, like, take a break!"
    d "Yeah. Well… I don’t need a break; I’m stronger than that."
    m "Deez, you know that taking a break and taking care of your health- mental and physical- is the strongest thing to do!"
    d "..."
    # small text, whisper
    d "...Yeah some people, but not me… I’m built… better."
    b "What?"
    d "You heard what I said."
    m "Of course he did!" 
    a "Hi everyone! What’re we talking about? :D" 
    k "Barby was just greeting Deez!"
    a "Hi, Deez!"
    a "I mean- hi to you, too, Kendra! And MJ! And Barby!"
    k "H-Hi, Apollo!"
    m "Hey, she greeted you first, Deez!"
    d "Yeah. Thank you…"
    d "I mean. That’s so- expected… That’s what I did. Expect…"
    b "Hiya, Apollo!"
    a "Yeah! Not to interrupt! You were talking to Deez?"
    b "Yep!"

    menu jumpy:
        "Vocabulary":
            b "By the way, you have an interesting vocabulary."
            d "What is that supposed to mean."
            b "Oh, it’s just, um, interesting! I just wonder where you got it from."
            d "This is how I was taught. Is there something wrong with the way I was taught?"
            a "A-"
            k "N-Not exactly, but… don’t you think there’s still more you can learn?"
            m "Yes! They say you never stop learning no matter what age."
            d "I don’t know if I need to learn more, though. I know plenty."
            m "Well Deez, you know what they say. The smarter you are, the more that you learn."
            d "Wait, really?"
            d "I knew that, but. I'm surprised you know that."
            d "But I'm always learning… other things. So. If you want to, you can… show me things, too, so it’s, like. Multiplied."
            k "Hey… haha! You don't have to keep insisting that you know everything…"
            b "*cough* But even if you do…"
            k "Yeah- e-even if you do, we'll help you learn more things!"
            a "Ooh! We’re having team learning sessions! Yay! I’m so happy we can do this together!"
            d "Okay."
            a "Aw, I’m excited, too, Deez!"
            jump jumpy
        "Family":
            b "What’s your family- or friends, or whoever- think about you working at the big SFC?"
            a "Aw!! Family! A-"
            d "My sister, she’s always been rather {i}passionate{/i} when it comes to me pursuing my career."
            d "But when I told her I was going to be interning for SFC, she seemed surprised."
            d "Which I don’t really understand. She always expected nothing less from me."
            m "I can kind of relate. My sister was also really surprised when she found out I was working at SFC, but that’s probably because she expected nothing from me, haha!"
            d "Well, between you and me, my skillset is on a different level than yours."
            d "So it makes sense that the expectations from your family aren't as high as mine." 
            m "That makes sense!"
            b "What about the rest of your family?"
            d "My brother supports me a LOT."
            d "He says I’m a master and will become prime minister, but I’m setting my mind towards something better."
            b "Haha, well, they do say ‘SFC, from the pearly gates above!’ You can’t get much higher than that, they say."
            k "Who’s 'they'?"
            m "SFC."
            a "SFC."
            k "Ah. Wh-where?"
            d "They must be right."
            a "It’s their sign-off!" 
            b "Yeah. It’s a weird sign-off, but hey. SFC moment."
            jump jumpy
        "Email from your school?":
            b "Deez, I wanted to ask… I think your school email is on my computer?"
            k "O-Oh, I can explain! He needed to check something on his account, but he didn’t have his own computer yet at the time."
            b "He has one now? Where’d he get one-."
            k "And mine wasn’t working so… we used your computer to log onto his account. Since you weren’t there." 
            k "S-Sorry."
            b "Oh– it’s alright! I was just wondering."
            d "The email lady is on my school account now. I want to get rid of her but she can’t be moved."
            m "Hail-E? She’s just gonna be there."
            d "Ah. A virus."
            a "Oh, she’s just the company’s chatbot! She’s very helpful." 
            d "She’s… not…"
            k "I-is she a bot?"
            m "... Kendra."
            k "Huh?"
            jump jumpy
    k "Hey, Barby, have you told anyone about… the thing?"
    b "Huh? Which thing?"
    k "Haha, forget I asked!"
    a "Aw! Kendra! You can ask anything! No need to be scared- there’s no dumb questions after all."
    d "Forgetting. That’s something Barby does. Knee slap."
    b "HUH?"
    a "It’s- it’s true! That was a good attempt at, like, a pun or something… I think."
    Kendra “Agh! Ah! Don’t… ahhh… that was what I was…”
    k "Agh! Ah! Don’t… ahhh… that was what I was…"
    b "KENDRA…"
    m "Wow!?"
    m "Amnesia, right? I figured a while back ago, actually."
    m "Am I the last person to canonically find out?"
    b "...Ah..."
    d "It’s not like Barby told anyone."
    b "H-hey, now… okay… I wasn’t, like- ahh…"
    b "I wasn’t trying to be secretive or anything- sorry… I just didn’t think it was a big deal!"
    m "Losing your leg and your memories, not thinking any of that was important?"
    b "...Sorry."
    b "... Aw man, everyone’s looking at me, now."
    a "O- Yeah :(" 
    b "I just didn’t want it to be a big deal- I’ll live with it!"
    b "It’s not like I can change the fact that this stuff happened to me or anything."
    b "The last thing I want is to give you guys a whole ‘nother something else to worry about, y’know? We’re just. Chillin’."
    m "... Pfft. Yikes."
    d "Yes. You’re giving us the cold shoulder."
    k "D-dude, what?" 
    b "Wow, good one, Deez!"
    a "Barb- *ahem*" 
    a "Barby, come on, we said we’d help accommodate for your fittin’ into your new prosthetic!" 
    a "We can surely accommodate your memory issues, too. You don’t have to worry about it weighing anybody down, honest!"
    k "Yeah… I just."
    k "I-I don’t mean to be nosy or anything, but I wish you were more honest with us."
    b "... Agh… I’m sorry."
    m "Hey, Barby, what's with the look? It's not like anyone hates you or anything."
    m "We’re just concerned."
    d "This guy keeps panicking. I think it would be wise to do something about this."
    d "Okay, Barby. I already know what you’re going to say, but you don’t have to not tell me or anyone else just because I already know… okay?"
    d "You can turn to me because my head is full of thoughts, good thoughts, and I can give you some of them. Not all! I still need some, but I have so many that I can give you some."
    d "Hand on your shoulder…"
    d "... And also, you can look up to me. Not only literary, but also physiality."
    b "Man… everyone… Oh, gosh…"
    b "{i}Internal monologue… Aw man… I’m supposed to be the one helping them… They’re all being so supportive…{/i}"
    m "You know, I usually tune your narration out, but this calls for an intervention someday."
    k "That’s- haha, no offense, but, that’s what I was thinking!"
    d "Yes. A Barby intention."
    k "Haha! You know, m-maybe we can call it that!"
    m "Where we all tell Barby to accept accommodation so he stops freaking out at every little possibility of inconveniencing someone?"
    d "Yes, he needs to stop. Grown ass man."
    b "H-hey!"
    k "Haha, don’t be so mean to him Deez, he’s dealing with a lot and just doesn’t want to worry any of us, but… haha, we just end up more worried when he doesn’t tell us, y-yeah."
    m "I like how we’re doing this in front of him."
    b "I don’t—?"
    a "Guys, I—" 
    d "It is quite inconvenient that he keeps worrying about being inconvenient."
    k "We just don't want you to feel the need to be so… so… caged up?"
    m "Even in a professional way, it’s a lot more helpful to know about things that are troubling you."
    b "Aghh… Yeah. Okay, okay, I, yeah… I guess I kinda needed to hear that…"
    b "Especially if, like, it’s ALL of you? Man. It’s that bad, isn’t it?"
    b "I’ll… I’ll try. I’ll try my best!"
    d "Phew."
    k "Glad you’re… uh, yeah! Thanks for… hearing our little- what was it called?"
    d "Barby intermission."
    k "—our Barby intervention out." 
    m "Hurray!"

    a "{i}Everyone’s all talking together… I keep trying to make an input but… hrm.{/i}"
    b "{i}Nudge nudge. Go, go! Feel free to share!{/i}"
    a "{i} Oh! Okay! Ahem. {/i}"

    a "It’s good that you’re all here! I was actually about to call for a team meeting."
    a "But before that… could I make one teeny tiny request?" 
    a "I, uhm… I just want to thank you guys for being such a great team so far, I’m really happy to work with all of you so— Can we take a little picture?" 
    k "Awh, Apollo… really?"
    m "Haha, that sounds like a great idea!"
    d "Hmm. Guess there’s nothing wrong with that."
    b "Well, c’mon everyone, let's squeeze together! Say, uhh—"
    d "Greaseeee."
    e "Greaseeee!" 

#CG?
    a "Ohh… this looks fantastic! Thank you everyone, I’m so happy… I’m going to frame this!" 
    k "{i}I… okay. Just talk to her.{/i}"
    k "Ahh… Apollo? I-I just… can we talk, actually? Somewhere—"
    b "{i} You got this! Thumbs up, thumbs up!{/i}!"
    k "Ahh— like in private? Y-yeah! It’s nothing too important s-so… aahhh…" 
    a "Oh! Oh I — I think—" 
    b "{i} Cheering you oooon!{/i}"
    a "O-of course! I’d be happy to, Kendra, even if it’s a small thing… you can tell me anything and everything, haha!"
    a "We’ll be back in a bit!"
# they leave the scene 
    b "Well… I guess we could just go to the meeting room while we wait,  since she was about to call a meet, anyway."
    jump teammeetingpt2

label teammeetingpt2:
    k "..."
    a "Okay— I know we had a meeting agenda, but… we have… something else to discuss."
    a "There were some… changes that corporate called me about while Kendra and I were talking and it’s not the uhm—"
    b "Oh gosh, don’t tell me it’s more bad news…"
    a "I-it’s not!! I swear haha, It’s nothing {i}too horrible{/i}, Just a deadline change—"
    d "Deadline change?! That’s cucumbersome…"
    m "Do you mean cumbersome?"
    d "MJ, you can’t say that in the office…"
    b "W-wait, maybe it’s an extension! They saw how unreasonable the project's due date was so… they gave us more time?"
    a "Aahh, I love your optimism, but… they pushed it just a smidge closer— Just, like… in {b}four days{/b}." 
    b "WHAAAT?!"

    # Calender pops up 
# Tuesday October 27
# Deadline in 4 days

    m "Oh! Oh dear. That’s NOT a smidge."
    d "This is chickeneyed!"
    a "A-ahh ahh! Let’s- let’s calm down guys! {i}Wait uhm okay—{/i} I hear you, I see you, and I understand your concerns—"
    d "No offense, you don’t understand anything."
    a "AaaAAahh… sorry—" 
    d "I just said no offense. This is not offensive, I am helping you…"
    b "Four days isn’t enough time to do ANYTHING!"
    d "Yeah, what he said."
    a "Ough… sorrsies…" 
    m "It’s no problem; I can pick up all the slack." 
    b "I don’t think that’s going to be enough! Four days?" 
    a "I-I know this is terrible! But we made a lot of progress yesterday, right? And today?" 
    m "Hm… 'a lot' if the deadline was in over 30 days. Which it used to be." 
    k "I-I have a question. If we end up having to work overtime to finish the project, are we… getting paid for it?" 
    a "I tried, I really really tried to negotiate with the higher ups about it, but they still said no." 
    a "It's a full turn key contract- so we only get any bonuses if we finish the product in a way that's satisfying enough for the clients, and they, uh, feel like giving the employees bonuses!" 
    a "So, so maybe if we work hard enough? And do really really well?"
    m "You heard her, though. We {i} could{/i} get a bonus by the end."
    b "But no guaranteed overtime."
    k "Oh… I see. That’s- that’s too bad! I-I… am I still doing all this work?" 
    a "I… I don’t know, Kendra…" 
    m "It seems like we’re about to get even more work, unfortunately."
    k "Haha… hah! No... no breaks for me, I guess!"
    k "I-I should... ooohhh... oh god I’m so... I feel like my head is going to explode!"

    b "K-Kendra? Are you okay? Maybe you should head to the clinic—"
    k "{b}NO. IT’S… FINE. I WILL BE FINE.{/b}"
    k "{b}I… I need to get back to work.{/b}"

# kendra leave? 

    a "... Oh death… I-I— I should…"
    b "It’s fine, I’ll… check up on her."

# OVERWORLD TIME (outside manager room)
# THUD THUD THUD
# CRASH
# (kendra banging her head on the computer then breaking the screen)
# kendra groaning 

#VA note: Kendra is wailing and groaning about her head hurting. She sounds more angry at herself than in pain. 

    k "{b}My head… it- my head hurts.{/b}"
    b "K-Kendra? Is… everything okay? What’s that noise…?!"
    k "{b}It needs to stop.{/b}"

#IF POSSIBLE ONLY IDK there’s a sickening THUD each time Kendra talks

    k "{b}I Need.{/b}"
#THUD
    k "{b}“To.{/b}"
#THUD
    k "{b}Stop.{/b}"
#THUD

#Thudding continues

# overworld control access
# go to cubicles 

# sfx, thudding footsteps
# loud grunt/screaming like every step she takes is painful
    k "{b}A A A A{/b}"

# long hallway

    # door closing (breakroom door closing sound)
    jump encounterday2
    
label encounterday2:
    b "Kendra? Did—did something happen to you—?"

# kendra cg
# scary… reverb on voice
    b "...Oh god…"

# pause, let the atmosphere sink in
# barby’s in like trance like state kind of so muffle, under water style, apollo voice

    a "Barby?"

# apollo’s voice becomes a bit clearer but reverby

    a "What’s going– AAAAAAH!"
# mj and deez are off screen here, so make them quiet, muffled, also under water style
    m "Did someone scream?"
    d "Yes."
    m " Stay out here, Deez, let me check…"
# muffled footsteps, footsteps stop  (MJ sees face reacts but doesn’t say anything? Or make them say something)
    m "OH. OH DEAR."
# barby voice is still reverb
    b "Kendra...?"
    a "Oh, oh, oh no… this is… oh…"
    a "Mmm… manager decision...!" 
    a "... We’re refusing this deadline. I-I can’t— We can’t—!!" 
    a "Call— we need to call the clinic, the hospital, anyone!" 
    m "Let’s, aahh— let’s calm down, okay? Let’s think this through—" 
    a "I-I’m sorry, right I uhm, where’s my phone—" 
    a "We need to tell the higher ups what happened… and ask… um…" 
    m "Kendra? Hey, let’s get you… somewhere." 

# The CG shifts and its mouth opens as if it’s a talking sprite. SQUELCH SQUELCH her JAW is breaking and is MUSHY   make her talk slowly cause her jaw is breaking every time it moves up and down
# her audio is so weird and pops up on screen as blue text weird glitchy instead of normal subtitles


    k "{b}Don’t worry. I’ll get all of it done.{/b}"
    m "Wh…what?" 
    k "{b}Turn my computer on. I will handle it.{/b}"

#VA note: She’d be sobbing quietly at this point, sniffle sniffle
    a "..."
    b "Kendra? D-Do you want to–"
    k "{b}I said I’ll get it done. Turn. It. On.{/b}"
    b "... okay." 

–# lightfilter is GONE its normal bogo render lighting now
# all the music stopped
# go to overworld, everyone(except kendra) is standing next to the door
#Click Anyone
    “...”
    #Deez
# blubur note: only time deez ask question, deez very vulnerable and genuine

    d "...What happened…? Do we call someone?"
    d "I don’t know… what do I do?"

#Barby himself is too overwhelmed to have an answer

    b "... I don’t know."

#walk to cubicles, when you get there barby just goes to cubicle automatically and 
#screen black
# VA NOte: “ah” is like… low and subtle and shaky
    b "Ah… It’s broken."






# return
