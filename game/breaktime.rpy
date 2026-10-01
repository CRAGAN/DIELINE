# DAY1 BREAKTIME

label breaktime1:
    $ storage = False
    $ janitor = False
    $ bathroom = False
    $ managerroom = False
    $ quick_menu = False
    play music "audio/Music/Breaktime/Breaktime Draft 3.mp3" loop
    if talkedtodeez and talkedtokendra and talkedtomj and talkedtoapollo:
        scene black with dissolve
        $ quick_menu = True
        b "Ough... I gotta go to the conference room... team meeting..."
        b "So much talking to people..."
        jump meeting
    
    call screen breaktime1
label deezandapollo:
    # Apollo & Deez 
    if not talkedtodeez and not talkedtoapollo:
        $ talkedtodeez = True
        $ talkedtoapollo = True
        scene room_1 
        show overlay:
            blend 'multiply' alpha 0.3
        show apo defaultt at right:
            xoffset -250
        show de shy at left, downward:
            
            xoffset 250
        with fade
        $ quick_menu = True
        a "Oh! Hi Deez, what’s up?"
        show apo default
        show de shyt
        d "Thank you... um... Ms. Knight for this wonderful ID you’ve bestowed upon me."
        d "This is so sweet. So spectacular. I love it so much..."

        #VA: like he’s declining a gift 
        show de defaultt at up
        d "But I do not need this."
        d "Ms. Apollo Knight. Manager, Ms. Apollo Knight." 
        show de default
        show apo awkwardt at downward
        a"Oh! Just Apollo’s fine—uhm... You don’t like it, then? I’m sorry, I know my handwriting is a mess, but I could try to just print it out and—"
        show de surprisedt
        show apo awkward at jumper
        d "Noo! No!!! It’s, it’s— I love. It’s... I love it. This ID, I’ll treasure it so bad. So good."
        show apo awkwardt at downward
        show de surprised 
        a"Are... are you sure? You said you didn’t need it; I don’t want to force you or anything"
        show apo awkward
        #VA: Almost like he’s hyperventilating, like its very clear he is pretending he likes it but doing a terrible job at it 
        show de thinkingt
        d "I want it. So bad. I just... I’ll keep it."
        show apo defaultt at up
        a "Ah! Erm... okay! Do what you want with it, alright?"
        show de defaultt
        d "A firm nation." 
        show apo default at jumper
        show de default at jump
        b "Hiya, folks! Do you need anything?"
        a "Oh! Hi, Barby! Just talking about the IDs. What’s up?"
        default aboutids = False
        default ears = False
        default smalltalk = False
        while not (aboutids and ears and smalltalk):
        
            menu:
                "The real IDs’ quality..." if not aboutids:
                    $ aboutids = True
                    $ quick_menu = True
                    b "The actual ID’s are... kind of not the best themselves."
                    b "MJ’s is already fading out, and it’s just the first day."

                    #VA: a bit proudly
                    show de happyt at jumper
                    d "Well, mine never fades."
                    show de calmt at downward
                    d "It’s laminated."
                    show de calm 
                    show apo defaultt
                    a"Laminated with love."
                    show apo default at jumper
                    show de default at jump
                # return

                "Ears?" if not ears:
                    $ ears = True
                    $ quick_menu = True
                    b "Happy Halloween, by the way!"
                    b "I noticed your costumes! You’ve both got little pointy ears?"
                    show apo defaultt 
                    a"My older brother plays a table top roleplaying game with his friends sometimes; it looks so fun!"
                    a"I’ve always wanted to try it, so I went as an elf!"
                    show apo default
                    b "Ohh... that sounds so fun..."
                    b "Maybe after work,we could try it out together sometime? For fun? We have enough people in the office for a party, after all." 
                    b "How about you, Deez?"

                    #VA Deez: randomly saying the movie, kind of tuning out the conversation  
        
                    show de defaultt at downward
                    d "Elf the Movie."
                    show apo default at jumper
                    show de default at jump
                # return

                "Small talk?" if not smalltalk:
                    $ smalltalk = True 
                    $ quick_menu = True

                    b "Right! Deez, have you heard about how Apollo and I met?"
                    show de defaultt
                    d "I know you guys are familiar with each other."
         
                    show de default at jump
                    b "Yeah! Familiar enough."
                    b "But have you heard how we met?"
                    show de thinkingt at downward
                    d "I’ve heard something, but you can share more details."
                    show de thinking
                    b "Oh... Well, it was ‘cause Apollo was really cool."
                    d "Yeah."
                    show apo defaultt at downward

                    a"Aw... Barbs..."
                    a"Well, Barby here got hired after a while of internship, but basically continued to work as a glorified intern for the next couple of years..."
                    show apo default
                    b "Yeah! It kind of... wasn’t the best, but when I started working with Apollo, well, I tried my best to help her out. Especially with her... technology." 
                    b "How’d the Skycloud meet go, by the way?"
                    show apo defaultt
                    a"I’ll host a team meeting to talk about that later!"
                    show apo default at jumper
                    show de defaultt
                    d "I’m really good at using Skycloud, too. I’ve met so many meetings in that app."
                    show de thinking at jump
                    b "Woah! An expert!?" 
                    show apo defaultt
                    a"Anyways, he helped me out a bunch and I helped tidy up his... reputation, so he’d start getting paid better, haha!"
                    show apo defaultt
                    b "Teamwork makes the dreamwork!"
                    b "Everyone else knows the gist of the story at this point. Just needed to catch you up so things make more sense while you’re here!"
                    show apo default at jumper
                
                    show de defaultt
                    d "Oh, yeah, I knew that."
                    b "Aw. He’s so knowledgeable. Apollo, you gotta hear him talk about things more."
                    show apo default at jumper
                    show de default at jump
                    a"I’m sure you did, you– you... geenieweenie, you Alberto Einsteino!" 
                    b "I’m so sorry. What is a geenieweenie."
                    show de calmt
                    d "I know what that is. Arigathanks for the compliment."
                    show de calm
                    show apo defaultt at jumper
                    a"Oh Barby, you silly goose! It means a wonderful genius!"
                    show apo default at jumper
                    show de default at jump
                    # return
        show apo defaultt at jumper
        a"Oh right! Now that you’re here, Deez... Do you wanna set up your email soon?"
        show apo default at downward
        show de thinkingt at jumper
        d "I know how to do that, too, but you can, like. Watch if you want."
        show apo default at up
        show de shy
        b "I’ll leave you to it, then!"
    
        jump breaktime1
    else:
        scene room_1
        show lighter:
            blend 'add' alpha 0.3
        show barby_standing_pants:
            zoom 0.6 xpos 0.2 ypos 0.16
            
        show apollo_standing:
            zoom 0.8
            xpos 0.5
            ypos 0.2
                
        show deez_standing:
            xpos 0.35
            ypos 0.1    
            zoom 0.65 xzoom -1
        b_id "They seem busy."
        jump breaktime1


label mjandkendra:
    # MJ & Kendra? hallway
    
    if not talkedtokendra and not talkedtomj:
        $ talkedtokendra = True
        $ talkedtomj = True
        scene room_3 
        show overlay:
            blend 'multiply' alpha 0.3
        show borders1
        show m hmt at right:
            xoffset -250
        show ken surprised at jumper, left:
            xoffset 250
        with fade
        $ quick_menu = True
        m "You ever think it’s crazy how we kinda look related?"
        show m hm
        show ken surprisedt at downward
        k "We-we do?" 
        show m defaultt
        show ken surprised
        m "Y’know. Blonde hair, green eyes. Everyone in my family has green eyes, which is kind of weird since it’s recessive to brown." 
        show m default
        show ken awkwardt
        k "Huh. Barby also has green eyes."
        show ken awkward
        m "Yeah, but, everyone in my family also has either blonde or brown hair, and he doesn’t exactly... well, maybe..." 
        show ken defaultt at jumper
        k "Oh! Speaking of! Hi Barby!" 
        show ken default
        b "Hiya!"

        #Related?
        default related = False
        default costumes = False
        default mjsfamily = False
        while not (related and costumes and mjsfamily):
        
            menu:
                "Related" if not related:
                    $ related = True
                    $ quick_menu = True
                    
                    show ken default
                    show m default
                    b "Maybe you could trace each other’s family trees?"
                    show ken defaultt
                    k "Oh, you know I- I don’t have one...!"
                    show ken default
                    b "Right..." 
                    show m hmt
                    m "Aw man. It would’ve been really fun to find out if we were cousins."
                    
                    m "How about your family tree?"
                    show m hm
                    b "Me?"
                    show ken awkwardt
                    k "He doesn’t, um, have one either...I think?" 

                        #VA Barby: happily said, not in an offended way. 
                    show ken surprised at jumper
                    b "I have parents."
                    show ken surprisedt
                    k "Oh! You told me you were adopted?"
                    show ken awkward at downward
                    b "Yeah!"
                    b "Wait... ohh... okay, I see." 
                    # return
                    show ken default
                    show m default
        #MJ’s Family?
                "MJ's Family" if not mjsfamily:
                    $ mjsfamily = True
                    $ quick_menu = True

                    b "Everyone in your family has green eyes?" 
                    show m defaultt
                    m "Yeah. The grass is green, the trees are green, the Greys are green." 

                    #VA Kendra: attempting to make a joke
                    show ken defaultt
                    k "Are they Greens grey?"
                    show ken default
                    show m defaultt
                    m "No. They’re green, too."
                    show m default
                    # return

                "Costumes" if not costumes:
                    $ costumes = True
                    $ quick_menu = True

                    b "Happy Halloween, guys! What’re your costumes, if you don’t mind me asking?"
                    show m defaultt
                    m "My costume? Um... oh! Yes. I am a guardian of the night."
                    show m default
                    b "Oh! A night guard."
                    show m defaultt
                    m "Yes. Totally."
                    m "Cinco Noches con Alfredo."
                    show m default
                    b "How about you, Kendra?"

                    #VA Kendra: She is flustered because she forgot about Halloween
                    show ken awkwardt at downward
                    k "C-costumes?! Oh pfft, yeah I remember that—"
                    show ken awkwardt
                    k "I ahh—I'm uhm, a garden? Yes, totally."
                    show ken awkward
                    b "Oh yeah! That checks out! Is that why you’re wearing the flower clips?"
                    show ken awkwardt
                    k "Mm... Mhm! Yes, nothing... else."
                    show ken surprised at up
                    k "Oh, my break is almost done...!"
                    show m hmt at jumper
                    m "We have the same break?"
                    show m hm
                    show ken awkwardt at jumper
                    k "R-right; I cut my break in half so I can spend the rest of it finishing things."
                    show m defaultt
                    m "I can help if you need?" 
                    show m default
                    b "I can help, too...!"
                    show ken awkwardt
                    k "Oh, um, thanks— both of you— but I think I can handle it... it’s not for this job, it’s for my other work..." 
                    show ken awkward at downward
                    b "Oh... I’d love to help but..."
                    show m defaultt at jumper
                    m "I can still help!" 
                    show m default at downward
                    b "MJ, I don’t know if we’re allowed to; we wouldn't want to do anything against company policy... right?"
                    m ":)"
                    show m defaultt at up
                    m "You’re right, Barby."
                    show ken awkwardt at jumper
                    k "Well, I’ll have to do that now!" 
                    show ken awkward
                    show m defaultt at downward
                    m "I can help by supporting you."
                    show m default
                    show ken awkwardt at downward
                    k "Um... okay!"
                    b "Ah- I’d... like to do that, too, but... I’ve got things I need to do..."
                    # what does he need to do i dont know chat how do we close off this part i dont know they need to stop talking </3

        b "...What do I need to do. How do I stop talking."
        jump breaktime1
    else :
        
        scene room_3 
        show lighter:
            blend 'add' alpha 0.3
        show borders1
        show barby_standing_pants:
            zoom 0.2 xpos 0.2 ypos 0.48
                
        show mj_standing:
                zoom 0.3 xpos 0.5
                ypos 0.45
        
        show kendra_standing:
            xpos 0.4
            ypos 0.45
            zoom 0.3
        b_id "They seem busy."
        jump breaktime1
            # then when you talked to everyone barby goes “ough i gotta go to the conference room for our team meeting soon"  - and i guess maybe you have to walk over there and click it???  Or teleport them

# DAY2 BREAKTIME
label breaktime2:
    #     Kendra in manager offis
    $ quick_menu = False
    if talkedtoapollo and talkedtokendra and talkedtomj:
        $ breakroom_unlocked = True
    call screen breaktime2 with fade

label kendratalking22:
    $ talkedtokendra = True
    scene managerroom
    show overlay:
        blend 'multiply'
    show ken surprised at center, up
    $ quick_menu = True    
    b "Hiya, Kendra! That's a lot of work you seem to be handling during break time."
    show ken surprisedt
    k "Huh! O-oh! It's break time?"
    show ken 
    k "Sorry! I-I got so swept up in all this work, haha!"
    k "I'll just finish these last few things!"
    show ken surprised
    b "Need any help with it?"
    show ken awkwardt
    k "Um. I mean- it's..."
    show ken awkward
    b "Let me help you sort these files while we chat."
    show ken awkwardt at downward
    k "A-ah. Uh. Sure! I mean, I don't mind — I DO mind, but in a good way — like, it's helpful."
    k "Thank... you!" 
    show ken awkward
    b "Of course!"
    $ manager = False
    $ somanytasks = False
    $ whyallthejobs = False
    while not (manager and somanytasks and whyallthejobs):
        menu yapp:
            "Manager" if not manager:
                $ manager = True
                
                b "You were transferred in, right? What's it like, working with Apollo as a new manager?"
                show ken awkwardt at up
                k "It's- it's been fine! Apollo is so kind and understanding and– and..."
                k "N-No problems with her at all."
                show ken awkward
                b "Are you sure? You sound... kind of not."
                show ken awkwardt
                
                k "No, there's no issue at all, haha! Even if — even if it feels like she doesn't like me, haha..."
                show ken worried
                b "What?! What gave you that impression?" 
                show ken worriedt
                k "Ahh don't tell her I said that, okay?! I-I don't want to get on her bad side any more than I already have..."
                show ken worried
                b "I think you'd have to commit something more {i}grave{/i}  than murder to get on Apollo's bad side."
                # sfx laugh track 
                b "{i}That wasn't even good?{/i}"
                b "B-but do go on!" 
                show ken worriedt at downward
                k "Well... there was this one time where, uhm, we got into a small disagreement."
                k "I-I wanted to, like, get everything done, all in one go! S-sure, it was a little... impractical, but we just HAD to finish it, a-and I know I deliver well even if I push myself a {i}little{/i} too hard sometimes but—"
                show ken stressedt
                k "But she kept— kept insisting there wasn't enough time to get everything done a-and to be practical and not to burn out and I..." 
                k "Gosh... I mean, she says really nice things but sometimes she looks at me... especially after the accident, I..."
                k "Ugh... I-I don't know. She's... cool. I just don't know what she thinks of me."
                show ken worried
                b "Kendra... I... I wanna say just not to worry about it, but..." 
                b "I know it isn't that simple. Especially for people whose opinion matters to you." 
                b "I'm just sorry you feel that way; she's not like that. I'm sure she doesn't hate you. Or. Blame you for anything." 
                b "No one does." 
                show ken worriedt
                k "Sigh. Like, I-I know I shouldn't let what others think get to me, either! But... it just does." 
                show ken worried
                b "Aw... It's okay to feel that way..." 
                show ken surprisedt at jumper
                k "I know you two know each other well and she seems like a great, uh, coworker!"
                show ken surprised
                b "Yeah! Honestly we're like... friends at this point."
                show ken surprisedt 
                k "R-really?, like actual friends? From coworkers?"
                show ken surprised
                b "Yeah? Why?"
                show ken awkwardt
                k "Oh, I was just wondering. It's just... some people think that it's unprofessional to do that. Being friends with people from work."
                k "B-but I guess it's nice to see that you're, um, willing to get close with people even if they start out as workmates."
                k "Maybe I shouldn't be surprised. I should've known you were, like, chill like that."
                show ken defaultt 
                k "... ever since I got to know you more, you've been nothing but nice to me."
                k "Y-You and Apollo, really. You both seem like really kind people."
                k "Even if things are hectic right now, I-I think you guys are trying your best to make things work and manage everyone to their strengths."
                show ken surprised
                b "Oh! That's- that's really nice of you to say. Thank you."
                show ken surprisedt 
                k "I-It's nothing."
                k "..."
                k "Um, d-do you mind if I tell you something personal?"
                show ken surprised
                b "Of course. Whatever you're, uh, comfy with!"
                show ken awkwardt
                k "Most of my life, I never thought about getting close to people. I was always, like, too busy anyway to get close to anyone, so I didn't see the point..." 
                k "But things have been changing recently." 
                k "It's been nice getting to know people, even if it's hard, and even painful sometimes. It's, um, been pretty nice, actually..." 
                show ken awkward
                b "Aw... Well, I'd love to help you two become friends!" 
                show ken awkwardt
                k "Oh? Aw, really? Thank you so much..." 
                b "Yeah! How about... uh, remember that roller skating idea you mentioned yesterday? What if we all went together?" 
                show ken surprisedt
                k "{i}Oh.{/i}" 
                show ken awkwardt
                k "Um — well, if you're more comfortable with that, then yeah! Haha! Of course!" 
                k "Cause... like. Person you know- better, more comfortable coming with them- yeah- haha! Of course!"
                k "All three of us."
                show ken awkward
                b "Alright! I'll let her know!"
                b "Actually... hold on. It might be better for you to tell her. See how she feels about it first hand,"
                b "Maybe it'll help ease your nerves, you know?"
                show ken awkwardt
                k "Ough... ooh... okay...! Yeah, sure! Yeah, yeah, you're right. After all of this is over, yeah I'll... ask her!"
                show ken default
                k "Thanks... really." 
                b "Yeah! Please, um, feel free to let me know if you need anything. Even if it's not necessarily for work..."
              
            "So many tasks..." if not somanytasks:
                $ somanytasks = True
                b "About yesterday's team meeting... that was a lot of jobs you were assigned."
                b "Now that I think about it, it feels a little unfair to unload so much on you... you sure you can handle it?"
                
                b "Especially when we don't even know what the product we're doing all this for is..."
                show ken awkwardt
                k "Oof... y-yeah, but I get it, Don't worry! I can handle it no problem; it's my job, after all! Even with the... circumstances."
                k "It's just a shame Dave isn't here anymore. He used to help with a lot of this." 
                show ken awkward at jumper
                b "Yeah. Wonder how he's doing... the divorce must've been that bad if he still hasn't shown up in person." 
                show ken worriedt
                k "Yeah... I wonder. I hope he's doing alright."
                show ken worried
                b "...Hey, I know you're like the best fit for the jobs, but I still wanna help out."
                show ken surprisedt
                k "O-Oh? Um, sure?"
                show ken surprised
                b "Are there any other responsibilities I can help you with that aren't too... {i}you know{/i}, hard on the leg?"
                show ken surprisedt at downward
                k "Um, i-if you're offering...! I have a really hard time with emails. Do you, um, think you could do those? If you'd be willing, I can give you my work account- if, if that's okay!"
                show ken surprised
                b "That's my specialty! And sure, as long as you're comfortable!"
                show ken awkwardt
                k "Y-yeah, it's not like I have anything crazy there... but, gosh, thank you..."
                b "Ooh, how about... what kind of food do you like?"
                show ken awkwardt
                k "Oh, you don't have to worry about that! I always forget to eat anyway, haha."
                show ken awkward
                b "What?! Kendra..."
                b "Alright, I'm getting you food, too."
                show ken surprisedt at jumper
                k "Aah, you– you really don't have to! Do any of these things." 
                show ken surprised
                b "Kendra,please,take the help; it's only fair. You're already helping us so much!"  #(Note the change from comma to semicolon for better flow) 
                b "And besides it's not too much effort for me to do any of these things. It's okay- I gotta make breakfast for myself and my roommate,anyway." #(Note the change from comma to semicolon for better flow) 
                show ken defaultt
                k "Barby... thank you so much."
                show ken default
                b "Anytime!"
            
            "Why all the jobs?" if not whyallthejobs:
                $ whyallthejobs = True
                b "Actually, if it's alright, I've been curious since last meeting... it sounded like you have had lots of experience in doing all sorts of jobs!"
                b "It's really impressive! I just wanted to know how you have so much?" 
                show ken defaultt
                k "Ahh, oh jeez, it's nothing... I've just been working for a {i}looong{/i} time, haha!"
                show ken default
                b "Really...? Wow, maybe she's older than she looks..." 
                show ken awkwardt at downward
                k "I-I'm not {i}old{/i} old!! I swear! I've just uhh, been through so many jobs, like, since I was a kid." 
                show ken default
                b "Ah— no no sorry! I was just muttering to myself but—ah, since you were a kid? L-like part timing as a teen?" 
                show ken defaultt
                k "Uhh, nooo... since I was like, 5 or sooo... I don't really remember." 
                show ken surprised
                b "W-what?! That's so young! My condolences—wait, I mean—"
                show ken defaultt
                k "Hahaha, no, it's alright! I kinda had to since I was just by myself for a long time... b-but you don't need to worry anymore! I think... I think I'm pretty happy now." 
                k "Uhh yeaah, I am maybe... more than a little stressed out over the tasks given to me,but I really am doing alright!"  #(Note the change from comma to semicolon for better flow) 
                k "I-I don't think you really remember,but I've adopted a kid,andI co-parent with a friend,not to mention this lovely job and great coworkers! It's all l could ever ask for..."  #(Note the change from comma to semicolon for better flow) 
                show ken default
                b "That's... wonderful Kendra,really! I'm happy for you..."  #(Note the change from comma to semicolon for better flow) 
                b "And happy to, uh, be a part of it and see you happy."
                show ken fear at jumper
                b "Maybe we can just be more than great coworkers in the future!" 
                show ken feart
                k "H-huh?! More— aha... more than great coworkers?!"
                show ken surprised
                b "Of course! Maybe... great friends, soon?" 
                show ken defaultt
                k "... pfft—! Hahaha, I uhh, think we're already on track, Barby."
                show ken default
                b "Haha, I'm glad! I think so too."
        
    #return
    show ken surprised at jumper
    b "Ah snap, I should leave you to it! Gotta wrap everything up so you can take your break, right?"
    show ken defaultt
    k "Ohh uhh— yeah! Right, I've got lots to do so..."
    k "Still though, thank you for this talk. I-I feel a lot better. Bye Barby, I-I'll see you in the break room?"
    show ken default
    b "You betcha! See you Kendra!" 
    scene black with fade
    jump breaktime2
    #Apollo 
label apollotalking22: #apollo at cubicles
    $ talkedtoapollo = True
    scene room_2
    show borders
    show overlay:
        blend 'multiply'
    show apo default at center
    with dissolve
    $ quick_menu = True
    b "Hiya, Apollo! It's break time."
    show apo defaultt
    a "Oh hi Barbs! Aaahhh it is? Oh cracker jackers, I lost track of time!"
    show apo default
    b "Ah! Haha! You really need to stop saying things like that!"
    show apo defaultt
    a "I'll just finish up over here, first! Moving my things from the cubicle to the new office is taking a bit, but I need to catch a breath, anyway. How ‘bout a chat?"
    show apo default
    $ kendraworry = False
    $ amiweird = False
    $ dnd = False
    while not (kendraworry and amiweird and dnd):
        menu yappy:
            "Kendra" if not kendraworry:
                $ kendraworry = True

                b "I'm a little concerned... that was a lot of roles we pushed on Kendra, wasn't it?"
                show apo worriedt
                a "Yeah... I'm a big bunch worried, too."
                a "But I don't know who else we could've given it to. She's, like, the best and only pick for all those tasks, after all."
                show apo worried
                b "That's true, but still... isn't that a lot for one person?"
                b "Maybe we should, like... do something about it?"
                show apo worriedt
                a "I agree! I've been trying to think of something, honestly, but..."
                a "Who else could do those things, honestly? :(" 
                a "I know MJ is already helping her out a bit! And she's teaching Deez, so when he figures things out, he can help more! Especially since he said he already knows most of the stuff, anyway."
                show apo hm
                b "I just, you know, it feels bad..." 
                b "But we also have a lot to do on our ends..." 
                show apo worriedt
                a "Yeah... man... I. I should apologize to her." 
                a "I'm the manager; I'm the one managing this whole thing... she shouldn't have to get overworked." 
                a "Ogh... and to think I did it all in a team meeting in front of everyone... ogh... ough..." 
                a "I'm such a dummy! I'm sorry, Kendra..." 
                show apo worried
                b "... Hey." 
                b "You... maybe you should talk to her... you know?" 
                show apo worriedt
                a "... I dunno... would she even want to talk to me? She must—she must hate me after everything I've done!" 
                show apo worried
                b "Hey,it's worth a shot,right?" 
                b "And don't worry, I'm sure she doesn't hate you or is upset with you about it..." 
                b "If anything, she looks... just nervous about getting it done right. So, honestly, she might need the encouragement."
                b "And if there's anyone I know who's great at giving that... well..."
                show apo surprised at jumper
                a "?"
                show apo happyt at jumper
                a "Aw, shucks, Barby!"
                a "You're right. It's worth a shot. I'll talk with her."
                a "Thanks a lot... I think I needed that big ol' push, haha."
                show apo happy
                b "Of course! Anything for my buddy boss!"
                show apo defaultt at up
                a "Heeey... hahaha! That's why you're my favorite assistant manager!"
                show apo default
   
            "Am I acting weird?" if not amiweird:
                $ amiweird = True
                b "Hey, Apollo... have I been acting weird since the accident?"
                show apo worriedt at jumper
                a "Oh nooo! No, no, no, Barby!"
                show apo nervoust
                a "... Well. Actually... yes..."
                show apo worriedt
                a "You just seem to respond to things like you don't really remember them? Or not as much? It kinda catches me off guard sometimes ‘cause you're not usually this forgetful."
                show apo worried
                b "Oh... Well, yeah... well."
                b "It's just some sort of thing... But it'll get better!"
                b "I remember more and more at a time, so it's probably just some... post- accident stuff."
                show apo worriedt
                a "Yeah... MJ said that sometimes people get post- traumatic amnesia or something... but that it doesn't usually last this long."
                show apo worried
                b "Really? I-I mean it's not really amnesia, it's just a bit of forgetting! Nothing too serious!"
                show apo worriedt
                a "Barby..."
                a "You can always open up to me about things, you know? Not only as your manager, but as your friend too..."
                show apo worried
                b "Mngh— it's really okay Apollo! Don't worry about me, I'm aye-okay! I'm doing better everyday!" 
                show apo awkwardt
                a "Okay... well, if you're sure it'll be okay, then I'm sure it'll be okay..."
                show apo worriedt
                a "But — listen, Barbs. You're still alrighty and tighty, no matter how frazzled and shaken the accident might've left you."
                show apo worried
                b "Yeah... thanks! I just... I don't wanna drag anything down, haha!"
                show apo worriedt
                a "You never do! Honestly, I'm worried I might be..."
                show apo worried
                b "Really??? Why?"
                show apo awkwardt
                a "Well- my... thingy. It's been hard to type and write, which is, like, most of my job!"
                a "And, to be honest, I'm still kinda stressing. I feel like I'm really not good at... or maybe not even cut out for this kinda thing... I know it's really, really not good to admit!"
                show apo awkward
                b "Apollo, you're trying your best. You're literally just learning how to do all of this, and, well, I think you've been getting better!"
                show apo awkwardt
                a "Ough, aw, thank you!"
                a "Hey, if you think I'm doing okay, then, you're doing okayer!! Hehe! So, don't worry about ‘acting weird' or anything after the accident."
                a "...Except."
                a "Oh shucks. Insurance."
                show apo awkward
                b "Don't worry! I've been handling it!"
                show apo happyt at jumper
                a "Oh! Okie! Thank you!" 
                a "I keep getting calls from emails and lawyers, actually." 
                show apo awkward
                b "Me, too. It's like- I think it's a call from work- something important- cause they don't even say they're calling about the crash until later."
                
                a "Right?? So you end up answering and listening to them all and aghh!!!"
                show apo default
            
            "Dungeons & Dragons" if not dnd:
                $ dnd = True
                b "We talked about playing a tabletop sometime, right?"
                show apo happy at jumper
                a "Oh death, yes yes!! I would love to play with everyone! Maybe... maybe we can play with our whole team after this project!" 
                a "Haha, I should use my new boss—err, managerial powers to make everyone attend a required job mandated roleplay thing!" 
                a "OH! That sounds bad uhh— I'm kidding, haha! If they don't want to play, I don't want to force them!"
                show apo awkwardt
                a "Only if they want to; it's not everyone's cup of coco after all..."
                show apo awkward
                b "Oh, well I'm sure there's at least one person here who'd love to play with us, and we'll make it easy for new players!"
                b "Nothing too intense, I could be the dungeon master for our first campaign! Just something short and sweet— I can see it now, a fantasy amusement park adventure full of twist and turns!"
                show apo defaultt
                a "Ohh that sounds like a lot of fun! Hehe, surely it'll be a rollercoaster of a ride!" 
                show apo default
                b "I was just wondering– what classes would our team be? Just in theory."
                show apo awkwardt
                a "In D&D? OMD, like classic fantasy, player handbook style?"
                show apo awkward
                b "Yeah, yeah. Like... I think you'd play a pretty good cleric."
                show apo surprised
                a "A cleric? What do they do?"
                
                b "Ohh you know, if you're our manager, you can totally be our cult leader cleric? Haha, joking, I mean you'd be a great healer—"
                show apo weirdt
                a "WHAT? HUH? CULT? ME IN A CULT? WHAAAT? HAAHAAHAAHAAA—"
                show apo weird
                b "Hahahaha...?"
                show apo weirdt
                a "You're so silly! Let's talk about something else!"
                show apo default

    b "Oh, do you need help moving your things, actually?"
    show apo happy
    a "Aww thanks Barbs, but I'm good! Go take your well deserved break!"
    b "Well, if you say so! See you in the break room!" 
    scene black with fade
    jump breaktime2
#     MJ
# Storage 
# They can carry more than 5 pounds if they really try 
label mjtalking22:
    $ talkedtomj = True
    scene storage
    show overlay:
        blend 'multiply'
    show m default at center
    with dissolve
    $ quick_menu = True
    m  "Hum hum hum..."
    b "Hiya, MJ! I see you're hard at work."
    b "But it is break time now."
    show m defaultt
    m  "Oh! I didn't notice. Thanks for telling me."
    show m default
    b "Of course."
    $ carry = False
    $ whyworkhere = False
    $ humm = False
    while not (carry and whyworkhere and humm):
        menu sirtalkalot:
            "Carrying" if not carry:
                $ carry = True

                b "Did you bring all these boxes in here?"
                show m defaultt
                m  "Yep! I was helping Kendra."
                m  "Guess what? Turns out I can carry more than five pounds if I really try."
                show m default
                b "Wow! That's great to hear."
                show m thinkingt
                m  "But only for a few seconds though. Which means I keep having to put stuff down and pick them up again."
                m  "At this rate, though, I'll probably start getting better at it, soon."
                show m default at up
                b "Aw. Well, that's okay. You don't need to force yourself if you really can't handle it."
                show m defaultt
                m  "Hah! That's funny. Good one, Barby!" 
                m  "Assistant manager saying there's no need to push yourself if you can't handle a task... that's a good one!" 
                show m default
                b "What?" 
                show m defaultt
                m  "I'm just kidding with you, Barby. I know you mean it." 
                b "Oh! Okay!" 
                b "... I know I'm not the best assistant manager; is there anything I can do to, um. Do better than we are right now?" 
                show m defaultt
                m  "Hm... I think you'll learn with time. We still have a while together as a team, so you can take some effort every day and learn how to work with each employee and their strengths!" 
                show m default
                b "Woah... you're right! Thanks, MJ!" 
                show m defaultt
                m  "And be sure to learn how to work with your own, too." 
                show m default
                b "I'll try my best!"
           
            "Why work here?" if not whyworkhere:
                $ whyworkhere = True
                b "So... how'd you start working here?"
                show m hmt
                m "It's nothing complicated. My... old job wasn't working out, they had positions open, so I applied. Then here I am."
                show m default
                b "What was your old job?"
                show m defaultt
                m "Haha, it wasn't really much of a job, really. I just sang and played different instruments wherever for whoever hired me."
                show m default
                b "Oh! That sounds fun."
                show m hmt
                m "It was. Unfortunately, it couldn't pay the bills, so I... needed something more stable."
                show m hm
                b "What about now? What do you do now?"
                show m defaultt
                m "I work here at SFC, of course!"
                show m default
                b "And... what do you usually do here?"
                show m defaultt
                m "I usually walk around and talk to people. I'm pretty good at that."
                show m hmt
                m "And now, picking up packages that weigh more than five pounds."
                show m hm
                b "Oh... I see!"
                
                b "That still doesn't actually explain what their job is..."
                show m hmt
                m "Why did you start working here?"
                show m hm
                b "Me? Uh. It was just. Job, y'know. Job that hired." 
                show m hmt
                m "Are you unsatisfied with your work here?"
                show m hm
                b "No, no, no, no! Not at all! Very satisfied here!" 
                show m thinkingt
                m "... Wow. That was a reaction."
                m "You're not in trouble or anything, Barby. It's not like I'm management."
                show m hm 
                b "... Right."
                b "I'm management."
                show m defaultt
                m "You sure are!"
                show m default

            "Humming" if not humm:
                $ humm = True
                b "You were humming a cute ‘lil tune earlier!"
                show m defaultt
                m "Oh? I was?"
                show m default
                b "Yeah! May I know what it was?"
                show m defaultt
                m "It's probably one of my older compositions."
                show m default
                b "Really? That's so cool!"
                show m happyt
                m "Aw, thank you, but it's nothing special, really." 
                m "I could probably come up with something better if I had the time, which... I don't really have much of these days."
                show m default
                b "Oh... but it's still really nice though!"
                m "I 'preciate it!"
    scene black with fade
    jump breaktime2
          

        #Click Breakroom (Haven't talked to Everyone)
label deeztalking22:
    $ talkedtodeez = True
    scene room_4
    show overlay:
        blend 'multiply'
    show de default at center
    $ quick_menu = True
    b "Hiya, Deez! Taking your break already, are you?"
    b "You're the only one who got the memo right away, haha! I had to tell everyone else."
    show de defaultt

    d "What? No."
    show de default
    b "No?"
    show de defaultt
    d "I'm not taking a break. I'm working."
    show de default
    b "Oh!"
    b "Well! It's break time. So, y'know, you can, like, take a break!"
    show de shyt
    d "Yeah. Well... I don't need a break; I'm stronger than that."
    show de shy
    show m thinkingt at right, up
    m "Deez, you know that taking a break and taking care of your health- mental and physical- is the strongest thing to do!"

    d "..."
    # small text, whisper
    show de sadt
    d "...Yeah some people, but not me... I'm built... better."
    show de default at jumper
    b "What?"
    show de surprisedt
    d "You heard what I said."
    show de default
    m "Of course he did!" 
    show apo happyt at center:
        xoffset 250
    a "Hi everyone! What're we talking about? :D" 
    show apo happy
    show ken defaultt at left
    k "Barby was just greeting Deez!"
    show ken default
    show apo happyt
    a "Hi, Deez!"
    a "I mean- hi to you, too, Kendra! And MJ! And Barby!"
    show apo default
    k "H-Hi, Apollo!"
    show de default
    show m defaultt
    m "Hey, she greeted you first, Deez!"
    show m default
    show de shyt
    d "Yeah. Thank you..."
    d "I mean. That's so- expected... That's what I did. Expect..."
    show de default
    b "Hiya, Apollo!"
    a "Yeah! Not to interrupt! You were talking to Deez?"
    b "Yep!"
    $ vocab = False
    $ family = False
    $ emailschool = False
    while not (vocab and family and emailschool):
        menu jumpy:
            "Vocabulary" if not vocab:
                $ vocab = True
                show de default
                b "By the way, you have an interesting vocabulary."
                d "What is that supposed to mean."
                b "Oh, it's just, um, interesting! I just wonder where you got it from."
                show de angry
                d "This is how I was taught. Is there something wrong with the way I was taught?"
                show apo awkward
                a "A-"
                show de default
                k "N-Not exactly, but... don't you think there's still more you can learn?"
                m "Yes! They say you never stop learning no matter what age."
                show de shy
                d "I don't know if I need to learn more, though. I know plenty."
                m "Well Deez, you know what they say. The smarter you are, the more that you learn."
                d "Wait, really?"
                d "I knew that, but. I'm surprised you know that."
                d "But I'm always learning... other things. So. If you want to, you can... show me things, too, so it's, like. Multiplied."
                k "Hey... haha! You don't have to keep insisting that you know everything..."
                b "*cough* But even if you do..."
                k "Yeah- e-even if you do, we'll help you learn more things!"
                a "Ooh! We're having team learning sessions! Yay! I'm so happy we can do this together!"
                d "Okay."
                a "Aw, I'm excited, too, Deez!"
            "Family" if not family:
                $ family = True
                show de default
                show apo default
                show m default
                show ken default
                b "What's your family- or friends, or whoever- think about you working at the big SFC?"
                a "Aw!! Family! A-"
                d "My sister, she's always been rather {i}passionate{/i} when it comes to me pursuing my career."
                d "But when I told her I was going to be interning for SFC, she seemed surprised."
                d "Which I don't really understand. She always expected nothing less from me."
                m "I can kind of relate. My sister was also really surprised when she found out I was working at SFC, but that's probably because she expected nothing from me, haha!"
                d "Well, between you and me, my skillset is on a different level than yours."
                d "So it makes sense that the expectations from your family aren't as high as mine." 
                m "That makes sense!"
                b "What about the rest of your family?"
                d "My brother supports me a LOT."
                d "He says I'm a master and will become prime minister, but I'm setting my mind towards something better."
                b "Haha, well, they do say ‘SFC, from the pearly gates above!' You can't get much higher than that, they say."
                k "Who's 'they'?"
                m "SFC."
                a "SFC."
                k "Ah. Wh-where?"
                d "They must be right."
                a "It's their sign-off!" 
                b "Yeah. It's a weird sign-off, but hey. SFC moment."

            "Email from your school?" if not emailschool:
                $ emailschool = True
                b "Deez, I wanted to ask... I think your school email is on my computer?"
                k "O-Oh, I can explain! He needed to check something on his account, but he didn't have his own computer yet at the time."
                b "He has one now? Where'd he get one-."
                k "And mine wasn't working so... we used your computer to log onto his account. Since you weren't there." 
                k "S-Sorry."
                b "Oh– it's alright! I was just wondering."
                d "The email lady is on my school account now. I want to get rid of her but she can't be moved."
                m "Hail-E? She's just gonna be there."
                d "Ah. A virus."
                a "Oh, she's just the company's chatbot! She's very helpful." 
                d "She's... not..."
                k "I-is she a bot?"
                m "... Kendra."
                k "Huh?"
    jump breakroomtalkday2 
label breakroomtalkday2:
    
    k "Hey, Barby, have you told anyone about... the thing?"
    b "Huh? Which thing?"
    k "Haha, forget I asked!"
    a "Aw! Kendra! You can ask anything! No need to be scared- there's no dumb questions after all."
    d "Forgetting. That's something Barby does. Knee slap."
    b "HUH?"
    a "It's- it's true! That was a good attempt at, like, a pun or something... I think."
    k "Agh! Ah! Don't... ahhh... that was what I was..."
    k "Agh! Ah! Don't... ahhh... that was what I was..."
    b "KENDRA..."
    m "Wow!?"
    m "Amnesia, right? I figured a while back ago, actually."
    m "Am I the last person to canonically find out?"
    b "...Ah..."
    d "It's not like Barby told anyone."
    b "H-hey, now... okay... I wasn't, like- ahh..."
    b "I wasn't trying to be secretive or anything- sorry... I just didn't think it was a big deal!"
    m "Losing your leg and your memories, not thinking any of that was important?"
    b "...Sorry."
    b "... Aw man, everyone's looking at me, now."
    a "O- Yeah :(" 
    b "I just didn't want it to be a big deal- I'll live with it!"
    b "It's not like I can change the fact that this stuff happened to me or anything."
    b "The last thing I want is to give you guys a whole ‘nother something else to worry about, y'know? We're just. Chillin'."
    m "... Pfft. Yikes."
    d "Yes. You're giving us the cold shoulder."
    k "D-dude, what?" 
    b "Wow, good one, Deez!"
    a "Barb- *ahem*" 
    a "Barby, come on, we said we'd help accommodate for your fittin' into your new prosthetic!" 
    a "We can surely accommodate your memory issues, too. You don't have to worry about it weighing anybody down, honest!"
    k "Yeah... I just."
    k "I-I don't mean to be nosy or anything, but I wish you were more honest with us."
    b "... Agh... I'm sorry."
    m "Hey, Barby, what's with the look? It's not like anyone hates you or anything."
    m "We're just concerned."
    d "This guy keeps panicking. I think it would be wise to do something about this."
    d "Okay, Barby. I already know what you're going to say, but you don't have to not tell me or anyone else just because I already know... okay?"
    d "You can turn to me because my head is full of thoughts, good thoughts, and I can give you some of them. Not all! I still need some, but I have so many that I can give you some."
    d "Hand on your shoulder..."
    d "... And also, you can look up to me. Not only literary, but also physiality."
    b "Man... everyone... Oh, gosh..."
    b "{i}Internal monologue... Aw man... I'm supposed to be the one helping them... They're all being so supportive...{/i}"
    m "You know, I usually tune your narration out, but this calls for an intervention someday."
    k "That's- haha, no offense, but, that's what I was thinking!"
    d "Yes. A Barby intention."
    k "Haha! You know, m-maybe we can call it that!"
    m "Where we all tell Barby to accept accommodation so he stops freaking out at every little possibility of inconveniencing someone?"
    d "Yes, he needs to stop. Grown ass man."
    b "H-hey!"
    k "Haha, don't be so mean to him Deez, he's dealing with a lot and just doesn't want to worry any of us, but... haha, we just end up more worried when he doesn't tell us, y-yeah."
    m "I like how we're doing this in front of him."
    b "I don't—?"
    a "Guys, I—" 
    d "It is quite inconvenient that he keeps worrying about being inconvenient."
    k "We just don't want you to feel the need to be so... so... caged up?"
    m "Even in a professional way, it's a lot more helpful to know about things that are troubling you."
    b "Aghh... Yeah. Okay, okay, I, yeah... I guess I kinda needed to hear that..."
    b "Especially if, like, it's ALL of you? Man. It's that bad, isn't it?"
    b "I'll... I'll try. I'll try my best!"
    d "Phew."
    k "Glad you're... uh, yeah! Thanks for... hearing our little- what was it called?"
    d "Barby intermission."
    k "—our Barby intervention out." 
    m "Hurray!"

    a "{i}Everyone's all talking together... I keep trying to make an input but... hrm.{/i}"
    b "{i}Nudge nudge. Go, go! Feel free to share!{/i}"
    a "{i} Oh! Okay! Ahem. {/i}"

    a "It's good that you're all here! I was actually about to call for a team meeting."
    a "But before that... could I make one teeny tiny request?" 
    a "I, uhm... I just want to thank you guys for being such a great team so far, I'm really happy to work with all of you so— Can we take a little picture?" 
    k "Awh, Apollo... really?"
    m "Haha, that sounds like a great idea!"
    d "Hmm. Guess there's nothing wrong with that."
    b "Well, c'mon everyone, let's squeeze together! Say, uhh—"
    d "Greaseeee."
    "Greaseeee!" 

    #CG?
    scene teamphoto
    $ quick_menu = False
    a_sub "Ohh... this looks fantastic! Thank you everyone, I'm so happy... I'm going to frame this!" 
    k_sub "{i}I... okay. Just talk to her.{/i}"
    k_sub "Ahh... Apollo? I-I just... can we talk, actually? Somewhere—"
    b_sub "{i} You got this! Thumbs up, thumbs up!{/i}!"
    k_sub "Ahh— like in private? Y-yeah! It's nothing too important s-so... aahhh..." 
    a_sub "Oh! Oh I — I think—" 
    b_sub "{i} Cheering you oooon!{/i}"
    a_sub "O-of course! I'd be happy to, Kendra, even if it's a small thing... you can tell me anything and everything, haha!"
    a_sub "We'll be back in a bit!"
# they leave the scene 
    b_sub "Well... I guess we could just go to the meeting room while we wait,  since she was about to call a meet, anyway."
    jump teammeetingpt2

#. dAY 3
label mjtalking3:
        play music "audio/Music/Breaktime/Breaktime Draft 3_Variation 3.mp3" fadein 1 loop
        $ talkedtomj = True
        scene room_3 
        show borders1
        show m toohappyt at center
        with fade
        m "Hi Barby!"
        show m toohappy
        b "Wha- oh, hiya MJ, what are you doing here?"
        m "Do you need any help?"
        b "Oh, it’s okay, I just finished my work." 
        m "Are you sure?"
        b "I think so?? What about you? Do you need help?"
        m "Silly Barby, I’m the one helping everyone out! Not you."
        b "But I’m the assistant manager D:"
        m "Just don’t think about it too hard, okay?"
        $ progressmj = False
        $ offeringtohelp = False
        $ interestingstories = False
        while not (progressmj and offeringtohelp and interestingstories):
            menu:
                "How’s progress doing?" if not progressmj:
                    $ progressmj = True
        
                    b "How’s your progress?"
                    m "Doing good! Like I said earlier, I can handle it."
                    b "That’s great to hear!"
                    m "You’re sure hearing it!"
                    # return
                
                "You’re always offering to help?" if not offeringtohelp:
                 
                    $ offeringtohelp = True
  
                    b "{i}MJ works so hard, I wonder if they ever do anything other than work...{/i}" 
                    b "Ah! I mean, not that it’s bad that you’re working hard, but I just worry. Earlier, when we were kinda freaking out, you just kept offering to help with everything."
                    m "That’s a perfectly valid question! Even I wonder whether I do anything else or not sometimes, haha!" 
                    b "W-Well, do you?"
                    m "Not anymore!"
                    b "... Is there something about that? Why you keep offering to help? I mean, surely you’d have more free time to do other things if not."
                    b "Like your music."
                    m "Well, even if I had more free time, it’s not like it would make a difference."
                    m "I need money to live. And I get money from working."
                    m "I’ll always love music, don’t get me wrong, but as they say, there’s no money in the arts. I learned that the hard way."
                    m "I’m probably better off contributing to society anyway, haha!"
                    b "Oh... well, please let me know if you ever need- or want- extra time for your hobbies!"
                    m "That’s nice of you to offer, but may I remind you that we have a deadline to catch? Perhaps we should deal with that first before we talk about extra time." 
                    b "Oh, r-right!"
                    # return
                "Got any interesting stories from work?" if not interestingstories:
               
                    $ interestingstories = True
                    b "You’ve been here for a while already, right? Do you have any interesting stories from work?"
                    m "Boy do I have stories!"
                    m "Mr. Sensin, may God NOT bless his soul, was my mortal enemy." 
                    b "Oh, what... what did Mr. Sensin do to you?"
                    m "Showing up to work with that stupid hat... wearing those obnoxiously loud coats and shirts and skirts and..."
                    m "And I couldn’t do anything because they were technically within company policy!"
                    m "I swore that one day, I was going to finally catch him wearing something that doesn’t comply with the dress code in any way, shape or form."
                    m "Though... I guess I’ll never get to do that. What a shame."
                    b "Oh, I’m... sorry?" 
                    b "I don’t really get why this was MJ’s problem though..."
                    m ":)"
                    # return
            
        b "Okay, I’m gonna go check on the others."
        b "Don’t forget to take your break, MJ!"
        m "Haha, you’re so funny, Barby!"
        m "Let me know if you need any help, alright?"
        b "Um, let me know if you need any help."
        m "Sure, sure. Now go on, don’t let me keep you."
        jump deeztalking3

            # cubicle, if you click MJ again after forced dialogue
        if talkedtomj == True:
            m "Hi, Barby!"
            jump breaktime3

    #Deez
    # storage roo
label deeztalking3:
    scene storage
    show overlay:
        blend 'multiply'
    show de default at center:
        xoffset 250
    show m default at center:
        xoffset -250
    with fade
    m "Need a hand there?"
    d "I don’t need hands. I have two. I am perfectly capable of doing this on my own."
    m "You sure? You looked like you were struggling there for a bit."
    d "I am not ‘struggling.’ I was... merely taking a moment to get my bear rings. I know how to do this."
    m "If you say so! But I’m right here if you need me, alright?"
    d "Yes, of course. Not that I’m going to need you, because I can do this all on my own."
    m "That you can!"
    b "Hiya folks! How are we doing?"
    m "Well, {i}someone{/i} tried to get supplies from the other building while I wasn’t looking."
    d "And I was rather successful at doing it."
    m "Sure you were!"
    d "Just as I will be successful with accomplishing this task."
    m "Uh-huh!" 
    m "You know what? I think you’ve done plenty already. Why don’t I take that off your hands?"
    d "I was carrying that."
    $ walkingaround = False
    $ whatcarry = False
    $ hearanything = False
    while not (walkingaround and whatcarry and hearanything):
        menu:
            "Walking around the office?" if not walkingaround:
                $ walkingaround = True
                b "Were you able to find your way around the offices?"
                d "Of course."
                d "I was in the parking lot and ran into this. Smelvin."
                d "His name was Smelvin and he was asking about Kendra."
                d "I pointed him in a random direction."
                b "Cause... You didn't know where the office was relative to you?"
                d "No. It’s not related to me."
                d "It was because. Safety."
                b "Oh! True. Fair enough... someone asking out of the blue where she is."
                b "...It could’ve been someone who knew her, though."
                d "He did say she hasn’t come home and... that he was worried."
                d "I just thought it was in the best interest of the. Company."
                b "Oh. Man."
                b "I guess we really have to finish this soon... maybe things will get better... after."
                b "When we have. More time to fix things."

            "What’re you even carrying?" if not whatcarry:
                $ whatcarry = True
                b "We don’t even know what the product we’re selling is; what are you even carrying?"
                d "It’s from the clients."
                m "Yeah, they’ve been sending us stuff."
                b "Any of it hint to what we’re actually supposed to be marketing?"
                d "This is a metal pipe."
                b "Wow. Is it for. Anything in particular?"
                m "Yesterday, most of the boxes I was helping Kendra carry had a bunch of rattling things in them, too. So... maybe more pipes."
                b "Is it pipes? Are we advertising pipes?"
                d "The answer is probably yes."
                b "That wouldn’t explain the whole ‘lifestyle’ thing, though..."
                d "Pipes can be a lifestyle."
                m "Y’know. Maybe they can."
                b "Agh... we have 3 days left and we still have no clue what it is..."

            "Hear anything?" if not hearanything:
                $ hearanything = True
                b "Did you hear anything on your trip?"
                d "So. People were talking about Kendra a bit."
                d "They talked about her being a hard-boiled worker and how they didn’t see her today. But..."
                d "I figured it out from the way she’s wired, but people are just now realizing  that Kendra is a lab experiment."
                b "..."
                m "I don’t think that’s right."
                d "It’s okay for you to think wrong sometimes."
                b "Um. Kendra never told me about anything like that... well, if she did, I probably wouldn’t even remember, haha."
                d "People were saying something was off-putting about her. It’s true, they put her in a machine that turned off. But it’s truly weird that people are finding out now."
                b "Has he been talking about this?"
                m "Yeah, he’s been telling me these conspiracy theories about Kendra ever since today started."
                m "It started with thinking about what’s going on with her, then..."
                m "Yeah."
                b "Oh..."
                b "Hey, buddy... yeah, I... miss her, too."
                d "She’s right here."
                b "...Yeah."
                b "Uhm... anything else?" 
                d "I know what you are."
                b "What!? What!? Why!?"
                b "What is it THIS time!?!?!?"
                d "I know your real name. It’s not Fredrick." 
                b "... I—...?"
                d "A nickname is the shortened version of your real name. Like mine, Deez. Yours does not make any sense."
                d "So, I’ve come to the consumption that your REAL name is Barblene. Hence and therefore, you are nicknamed Barby." 
                b "... Damn. {i}I didn’t even know that... {/i}"
                d "You are welcome, Barblene."
                b "You know, give it a second and I’d believe you. I got the nickname before my parents gave me the name Fredrick." 
                d "Huh?"
                d "Wait— no! Your parents are wrong! First names are called first names because they come first!" 
                b "Yeah, you know babies without names sometimes get labelled 'Baby' as a temporary name?"
                d "Uhhh— {i}YEAH{/i}! Of course! They uhm... simply added the letter r into it, yes—"
                b "My nickname has nothing to do with that. It was an incident at a barbershop."
                b "... I was a child and I went in and pretended to be a barber."
                b "... Crap this is embarrassing I should stop talking"
                d "No! You can’t, you need to tell me immediately right now." 
                b "... Okay." 
                b "So I would go up to people who were waiting to get their hair cut. And I’d say. I’m. I’m Barby the Barber."
                b "..."
                b "Like. Hiya, folks. I’m Barby the Barber."
                b ". . ."
                b "Please don’t tell anyone about this."
                d "Okay, Barblene."
    jump apollotalking3

label apollotalking3:
    #Apollo
    # Break room
    #Bring up to apollo (MJ is there) that kendra thought she hated her
    scene room_4
    show overlay:
        blend 'multiply'
    show apo default at center:
        xoffset 250
    show m default at center:
        xoffset -250
    
    with fade
    m "Hi, Apollo!"
    a "Hello, MJ! Here to take your break?"
    m "Oh, no, I’m actually here to ask if you need any help."
    a "Aww, thank you, but it’s fine." 
    m "That’s an awful lot of paper you’re holding. Where are you taking this to?" 
    a "My office but– oh, there they go with my papers..."
    a "Oh, hello Barby."
    b "Hi Apollo! Seems like MJ got to you, haha." 
    a "Haha, yeah... they sure are enthusiastic!"
    
    # after talking to everyone
    b "Wow, MJ sure is... everywhere!" 
    b "They’re really trying to help keep the work up, that’s admirable." 
    b "I just hope they'll be alright..."
    m "Back! Just finished taking the papers where they’re needed."
    a "Wow! Um..."
    m "Is there anything else?"

    #The product
    $ product = False
    $ aboutkendra = False
    $ apollofam = False
    while not (product and aboutkendra and apollofam):
        menu:
            "The product" if not product:
                $ product = True
                b "Are we any closer to figuring out what the product actually is?"
                a "No..."
                a "I’ve been trying to make a presentation for the proposal, but I don’t know what else to put in it."
                a "All I’ve done so far is write out the introduction and decorate the slides."
                m "Would you like me to handle it for you instead?"
                a "It’s okay, MJ, you don’t know what the product is either. Unless...?"
                m "Sorry, but I have nothing either."
                a "Aww." 
                m "But maybe I could help you figure out what it is." 
                a "Oh! Yes, that would be appreciated."
                m "What we know so far is that this is more than a product– it’s a lifestyle, a life changing one."
                m "So it must be something big, something revolutionary."
                a "Yeah! What do you think it is?"
                m "..."
                m "I don’t know. We have too little information to even try guessing what it could possibly be."
                b "Oh... at least you tried?" 

            "About Kendra" if not aboutkendra:
                $ aboutkendra = True
                b "Right... did you and Kendra ever get to have your whole talk?"
                a "Ah... yesterday?"
                a "We were taking a while, y’know just chatting to get a little comfortable- when I got interrupted by the call..."
                a "I couldn't tell what we were gonna talk about, but after the higher ups talked to me, she just told me not to worry about it and that it wasn't urgent. And... the team meeting was pretty urgent."
                b "Oh. Well..."
                b "No use being secretive now."
                b "You know Kendra thought you hated her? Or just... didn’t like her in general?"
                a "WHAAAT?!"
                a "But- but I thought she hated me! Or I made her uncomfortable- or- oh my death..."
                a "Ooohhh, I guess- I guess I did... make her uncomfortable..."
                a "Oh... I feel so bad now... I didn’t mean for her to feel like that..." 
                m "Huh. That explains why you two were always so weird around each other."
                b "And. Um."
                b "Maybe we can... leave out the roller skating part. This is already a lot."
                a "Uhm, what roller skating part?"
                m "... Barby, what would that have to do with Apollo?"
                b "Oh, shoot. Well, the three of us were gonna go to break the ice. Y’know, the, uh, help with the uncertainty between the two of them..."
                m "...The. The one that was just supposed to be the two of you?"
                b "...Huh?"
                m "Uhm, well, Kendra kind of told me about it." 
                a "O-Oh, it was just supposed to be the two of you? It’s okay, I don’t want to get in the way..."
                b "What? No, it’s fine, Apollo. You’re also my friend. You can be there. It’ll be a bonding experience, all three of us!" 
                m "..."
                a "Well— well if you’re sure...! Haha." 
                b "A-Anyway!"


            #Would apollo get it or not (she would noooootttt)
            #Barby turning date night into group therapy session </3
            #barby inadvertently turning apollo into a third wheel </3 
            #While simultaneously thinking he's the third wheel </3
            # Context maybe Kendra asked MJ before before like maybe advice on how to handle the barby roller skate date (before the accident) 
            #And then now mj is like ?? The one thats supposed to be like ?? Just the two of you?

            "Apollo family" if not apollofam:
                $ apollofam = True
                b "Right, I saw an email from Annelise Knight with a familiar amount of death references."
                a "Ooohhh, from my Aunt Elise?" 
                b "Ah, she’s your aunt! Why would your aunt send spam mail?"
                a "Spam mail? Ohh, you mean those very informative letters? Ahaha, don’t worry, it’s not spam!" 
                a "Different members of my family send them to me everyday! Not just me, but to anyone who subscribes to our memorial home’s newsblast!"
                a "Speaking of, it’s almost my turn to do that, would any of you like to be part of it?"
                m "I think I’m good, Apollo."
                m "And Memorial home? Is that your family business?"
                b "Yeah! Apollo’s family runs a funeral home, uhm, it’s called Death’s Devonists Revolutional Memorial Homes, correct?"
                m "That’s name is quite on the nose, is it not?"
                a "That’s right! It’s fun since all of my aunts, uncles, brothers, sisters, mothers, fathers and cousins work there, including me!"
                a "I mainly just do advertising when I can though, I prioritize this job so don’t worry!"
                m "Wow! And I thought I had a crazy family tree." 
                b "W-what?! That’s a lot of uhh... people! How does that work, exactly?"
                a "Oh like any other family, silly! We may not all be blood related but we’re still one big happy community of people! It’s always so much fun when new people join."
                b "New people join?? Like... they get adopted or married or?"
                a "They just need to believe in The Looming, Grim Mist of the Endless Cycle of Life and Death!"
                a "Would you like to check it out? We do lots of free group therapy sessions and—"
                m "No, it’s fine! Apollo, really." 
                m "Sounds kinda... not to be rude or anything but—"
                b "{i}MJ, I think I know what you’re gonna say but... just don’t. She was weird about it last time I joked about cults—{/i}"
                a "What was that Barbs?"
                b "N-nothing! Nothing burger, I swear— I was just telling MJ that uhh... I think your family is very cool. I can't wait to meet them one day!"
                a "Ohh shucks, they can’t wait to meet you too! Ahaha!" 
    
    jump meeting3
# DAY 4
label breaktime4:
    # Fade in the hallway again but empty
    scene room_3
    show borders1
    with fade
    stop music
    b "Is Deez still in the bathroom?"
    $ quick_menu = False
    # cubicle
    scene room_2 with fade
    #Kendra
    show borders
    show ken monster
    with fade
    $ quick_menu = True    
    b "..."
    $ quick_menu = False
    voice "audio/Kendra/Day 4 Non-compliance/kendra_line095.mp3"
    k_sub "..."
 

    # manager office front
    #MJ
    scene room_1
    show m monster
    with fade
    $ quick_menu = True       
    b "..."
    $ quick_menu = False
    voice "audio/MJ/Day 4 Non-compliant/MJ_line103.mp3"
 
    m_sub "{i}humming~{/i}"
    scene managerroom
    #Manager Office (inside)
    # apollo sitting there
    show apo default at center
    play music "audio/Music/Working Overtime 1m (small speaker edition).mp3" loop fadein 1
    with fade
    $ quick_menu = True       
    b "..."
    a "Hm? Hi, Barby. I'm working right now. What's up?"
    $ deezwhere = False
    $ you = False
    $ nothing = False

    while not (deezwhere and you and nothing):
        menu:
            "Deez" if not deezwhere:
                $ deezwhere = True
                show apo happy
                b "Looking for Deez."
                a "I'm pretty sure he was touring that guy?"
        # leave dialogue (can click again)
            "You?" if not you:
                $ you = True
                show apo awkward
                b "What's up with you?"
                a "Oh, haha. I've just been fixing the PowerPoint presentation to pitch, uh, how to present the product's value to our client. For them to use when advertising it."
                a "... haha, funny you ask, but most of the progress didn't save last night so, haha, I'm just fixing that up right now!"
                b "Oh shoot…"
                a "Don't worry too much about it, I still remember how I did it, anyways, I just have to put it in again. Hah…"
        # leave dialogue (can click again)
            "Nothing" if not nothing:
                $ nothing = True
                show apo default
                b "Nothing, just checking in."
                a "Neat!"
    $ quick_menu = False
    scene black with fade
    pause 2
    play music "audio/Music/Fluorescent Light Humming - Sound Effect (HD).mp3" loop fadein 1
    jump encounter4
# leave dialogue (can click again