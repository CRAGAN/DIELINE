# DAY1 BREAKTIME

label breaktime1:
    $ storage = False
    $ janitor = False
    $ bathroom = False
    $ managerroom = False

    if talkedtodeez and talkedtokendra and talkedtomj and talkedtoapollo:
        scene black with dissolve
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
            $ quick_menu = False
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
        $ quick_menu = False
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
            $ quick_menu = False
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
    if talkedtoapollo and talkedtokendra and talkedtomj:
        $ breakroom_unlocked = True
    call screen breaktime2
label kendratalking22:
    $ talkedtokendra = True
    scene managerroom
    show overlay:
        blend 'multiply'
    show ken surprised at center, up
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
    jump breaktime2
    #Apollo 
label apollotalking22: #apollo at cubicles
    $ talkedtoapollo = True
    scene room_2
    show overlay:
        blend 'multiply'
    show apo default at center
    with dissolve
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
                show apo angryt at jumper
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
    jump breaktime2
          

        #Click Breakroom (Haven't talked to Everyone)
label deeztalking22:
    $ talkedtodeez = True
    scene room_4
    show overlay:
        blend 'multiply'
    show de default at center
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
                b "By the way, you have an interesting vocabulary."
                d "What is that supposed to mean."
                b "Oh, it's just, um, interesting! I just wonder where you got it from."
                d "This is how I was taught. Is there something wrong with the way I was taught?"
                a "A-"
                k "N-Not exactly, but... don't you think there's still more you can learn?"
                m "Yes! They say you never stop learning no matter what age."
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
    a "Ohh... this looks fantastic! Thank you everyone, I'm so happy... I'm going to frame this!" 
    k "{i}I... okay. Just talk to her.{/i}"
    k "Ahh... Apollo? I-I just... can we talk, actually? Somewhere—"
    b "{i} You got this! Thumbs up, thumbs up!{/i}!"
    k "Ahh— like in private? Y-yeah! It's nothing too important s-so... aahhh..." 
    a "Oh! Oh I — I think—" 
    b "{i} Cheering you oooon!{/i}"
    a "O-of course! I'd be happy to, Kendra, even if it's a small thing... you can tell me anything and everything, haha!"
    a "We'll be back in a bit!"
# they leave the scene 
    b "Well... I guess we could just go to the meeting room while we wait,  since she was about to call a meet, anyway."
    jump teammeetingpt2