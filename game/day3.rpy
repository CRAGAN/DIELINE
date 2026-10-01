image mj_scene = Movie(channel="movie_dp", play = "videos/mj.webm", loop=False,  size=(1920, 1080))


label day3:
    #Intro
# Calendar pop up
    scene black
    $ quick_menu = False
    pause 2.0
    centered "{color=#FFFFFF}Wednesday Oct 28{/color}"
    centered "{color=#FFFFFF}3 days left{/color}"
    stop music
    
    $ quick_menu = True
    b "...Apollo texted to go to the break room as soon as I got here?"
    b "...I need to go to Kendra's cubicle."
    play music "audio/Music/Free Horror Ambience (Dark Project).mp3" loop fadein 1
    $ quick_menu = False
    jump kendratalking3

   

    #Minigames

    #Break Time
    # cubicle, forced dialogue
  

    #Kendra
    # cubicle
label kendracubic:
    scene room_2
    
    show blue:
        blend 'multiply' alpha 0.3
    show overlay:
        blend 'multiply'
    show borders
    show m defaultt at up, center:
        xoffset -250
    show ken monster at downward, center:
        xoffset 250
    with fade
    m_sub "Hey Kendra! Need a hand there?"
    show m default
    k "..."
    show m happyt
    m_sub "Is that a yes? I’ll take it as a yes."
    show m happy
    b "Hi, Kendra... and hi MJ, too." 
    show m defaultt
    m_sub "Hey Barby! Just seeing if Kendra needs any help." 
    m_sub "Though I don’t think she’s keen on talking right now. She’s, um, really busy!"
    show m default
    b "Oh! Uh, yeah... I don't think she's very responsive— Wait, what are you doing?"
    show m defaultt
    m_sub "Oh! You know, just taking some of the workload off of her. These files were sitting there so—"
    show m default
    show ken monstertt at shaking
    k "Leave me alone, I need to work." 
    show ken monster at downward
    show m hmt
    m_sub "No problemo, have a good day!"
    show m hm with dissolve

    b "Wait—! Oh... Alright."
    #Click Kendra again
        
    b "K-Kendra? Hey, are you okay—"
    show ken monstertt at shaking, up
    k "Urrgh, I said. Leave. Me. Alone!"
    show ken monster
    b "Ouugh, she yelled at me...! She must hate me and find me annoying..."
    b "I-I’m sorry... yeah, I’ll go..."


    #Click Kendra Again etc etc etc 
    #b "... I don’t think she wants to talk, right now."
    #Team Meeting - VOICED ACTED
    scene black with fade
    #Note: let apollo talk less barby talk more  as she starts stressing real hard, barby kind of steps in
    jump meeting3
label minigames3:
        # FROG OVER HERE
        $ delete_all()
        $ add_message("Newest Brand Deal.", "carsen@notbusinessemail.com", "carsen. brand deal.\n\ni didnt get to thank you for teaching me how to cook (food. not the other kind) or talk to u at all after actually\n\ndidnt realize the accident hit that hard . not a pun. idk if u noticed but u could barely hold anything without dropping it like u were shaking and every time i pointed it out u were like \"okat, team! lets finish cooking first!! we can talk abt that stuff later!!\" and muttering \"kendra\" like respectfully wth is wrong with u\n\nthe food was rlly good tho\ntook some to work and it stayed warm in the new containers we got\n\nalso i washed the dishes again so dw\n--------------\n{i}Reply from You:{/i}\nHiya, Carsen!\nWish I could respond more but I got a lot to do right now!\nI'm so so sorry that I didn't clean up! I'll do better, I promise. So, so sorry.\n\nI was just thinking about Kendra, haha! Nothing weird sorry just we had a pretty crazy work day.\nThank you for the brand deal.\n--------------\n{i}Reply from carsen@notbusinessemail.com:{/i}\nits ok i can wash a few dishes lol\nyeah srry idk yk i dont rlly get any of that stuff, but gl with kendra rooting for u\n\nsrry if txts weird work kinda draining\n--------------\n{i}Reply from You:{/i}\nWDYM ROOTING FOR ME???\n--------------\n{i}Reply from carsen@notbusinessemail.com:{/i}\nwith kendra lol\nanyways i haven't even heard abt how ur day went bro like wheres the reenactment roleplay thing lmao where my play at\njk just be safe and lmk if u need anything\n--------------\n{i}Reply from You:{/i}\nThat's not it! Sorry! It's that she was just we kept working together on stuff don't have time to keep chatting I have so much work right now, bye!", "acc")
        $ add_message("DON'T TRASH THIS EMAIL!!", "CoolchipzYT@abcfunmail.edu", "DON'T TRASH THIS EMAIL!!\n\nThere was once a little girl named Marian Ward who lived in Cedarville West Virginia. Her dad was the local cobbler and he was teaching her the trade. Marian didn't have any friends because she was ugly and smelled like shit, so she drew a face on the first steel-toed shoe (left shoe) she ever cobbled and named it Shoe.\n\nOne day, at 3:00AM, it was thunderstorming! Marian was scared, so she grabbed Shoe and went to stare at her reflection in the mirror until she wasn't scared. Unfortunately, she remembered she was ugly and she ran out of her house.\n\nMarian couldn't see where she was and fell down the town's local big chasm in the middle of the town where she was in. She falled for a long time, and at the bottom, all the townspeople and her three bullied were there. It was she was scared.\n\n\"No one can see you in the Chasm.\" The townspeople said.\n\nOne of the bullies was mean and he took Shoe, taking it from Marian, who couldn't stop him because scary. He put Shoe on and kicked Marian until she accidentally died. And nobody ever found out.\n\nIn revenge, Marian will come to you tonight and take you're left leg and give you some amnesia and turn you ginger.", "del")
        $ add_message("Your Responsibilities", "sfc@serafim.co", "Kendra Bell,\nYou have failed to show sufficient productivity today. Please fix this behavior before we have to take action.\n\nFrom the pearly gates above,\nSera, Fim & Co. Higher Ups\n--------------\n{i}Reply from You:{/i}\nHiya!\nThis isn’t Kendra, but I am her assistant manager and she is doing the best she can. I will speak with her today about this. Thank you.\n\nYour professional pal,\nFredrick \"Barby\" Ibarra", "acc")
        $ add_message("Reminder and Concern", "sfc@serafim.co", "Mr. Ibarra,\n\nYou can do it! No more giving feedback that is indisposed to the positive vibes we have been predisposing you to have!\n\nFrom the pearly gates above,\nSera, Fim & Co. Higher Ups\n--------------\n{i}Reply from You:{/i}\nHiya, Higher Ups,\nVery sorry about the improper vibe disposition. I will do my best to correct this shortly.\n\nYour professional pal,\nFredrick \"Barby\" Ibarra", "acc")
        $ add_message("Importance of This Project", "popik@cock.com", "The world is changing, and so is the way we should commune with the nature of it we must sit down in proper fashion and style and meet with the deeper question as our very soul finds its essence pouring out from them, cleansing the negative flow that clogs the essence of their effluvium. It is only with this proper recourse that we can act in the fashion needed in our daily process.\n\nThe best client,\nPopikcock\n--------------\n{i}Reply from You:{/i}\nHiya, Client!\nI understand everything you are saying. We will keep this in mind when preparing the marketing pitch.\n\nYour professional pal,\nFredrick \"Barby\" Ibarra", "acc")

        call screen email_minigame
        
        jump mjtalking3

label meeting3:
    play music "audio/Music/Working Overtime 2m.mp3" loop fadein 1
    $ quick_menu = False
    scene meetingbg
    show overlay:
        blend 'multiply' alpha 0.5
    show apol happy
    show barb neutral
    show dee neutral
    show mjj neutral
    show meetingfg
    voice "audio/Apollo/Day 3 TM/apollo_line126.mp3"
    a_sub "Ahaha... thank you all again for uhm, coming to the team meeting everyone...!"
    show barb pensive
    voice "audio/Barby/Day 3 TM/barby_line196.mp3"
    b_sub "Ahh, but... Kendra’s not here, yet..."
    show mjj happy
    voice "audio/MJ/Day 3 TM/MJ_line063.mp3"
    m_sub "I don’t think Kendra’s currently available to participate. No worries, I’m happy to relay anything to her."
    show apol pensive
    voice "audio/Apollo/Day 3 TM/apollo_line127.mp3"
    a_sub "Knowing our deadline is in two days, I can’t help but be just a little bit worried about our pace so far!"
    voice "audio/Apollo/Day 3 TM/apollo_line128.mp3"
    a_sub "With Kendra and Dave both... {i}unavailable{/i}, I’m not sure we can even get close to finishing this project."
    show barb neutral
    voice "audio/Barby/Day 3 TM/barby_line197.mp3"
    b_sub "So... let’s start this with. How’s everyone feeling?" 
    voice "audio/MJ/Day 3 TM/MJ_line064.mp3"
    m_sub "A-Okay."
    # deez arms and legs  are not feeling alright
    voice "audio/Deez/Day 3 TM/deez_line071.mp3"
    d_sub "My arms and legs are feeling. Alright."
    voice "audio/Apollo/Day 3 TM/apollo_line129.mp3"
    a_sub "..."
    show barb pensive
    voice "audio/Barby/Day 3 TM/barby_line198.mp3"
    b_sub "Okay... this is. A situation. It looks like most of us are getting a little overwhelmed."
    voice "audio/MJ/Day 3 TM/MJ_line065.mp3"
    m_sub "Well that’s no big deal. I can just pick up the pace."
    voice "audio/Apollo/Day 3 TM/apollo_line130.mp3"
    a_sub "I don’t know, MJ... we’re still so behind, and there’s just so much that needs to be done, I don’t think you should..."
    show mjj shocked
    voice "audio/MJ/Day 3 TM/MJ_line066.mp3"
    m_sub "Are you doubting me?" 
    show apol shocked
    voice "audio/Apollo/Day 3 TM/apollo_line131.mp3"
    a_sub "No! No, I’m just–"
    show apol neutral
    voice "audio/MJ/Day 3 TM/MJ_line067.mp3"
    m_sub "Then I can handle it."
    show barb shocked
    voice "audio/Barby/Day 3 TM/barby_line199.mp3"
    b_sub "Okay, wait, MJ. I think. We need to take a second. Not just for us, but you, too. You’re doing a lot, so maybe we- including you- need to take a break. Take it easier."
    voice "audio/MJ/Day 3 TM/MJ_line068.mp3"
    m_sub "...A break?"
    show barb pensive
    voice "audio/Barby/Day 3 TM/barby_line200.mp3"
    b_sub "Especially after what happened to Kendra."
    voice "audio/MJ/Day 3 TM/MJ_line069.mp3"
    m_sub "If that’s the case, you should all take a break."
    voice "audio/MJ/Day 3 TM/MJ_line070.mp3"
    m_sub "I just need a list of the things that have to be done by today and I’ll get it done. Then we can be finished!"
    voice "audio/Barby/Day 3 TM/barby_line201.mp3"
    b_sub "No- We’re not putting all the work on you..."
    voice "audio/Barby/Day 3 TM/barby_line202.mp3"
    b_sub "Um, no offense, MJ! Not that anyone here doubts that you can do it."
    show dee pensive
    voice "audio/Deez/Day 3 TM/deez_line072.mp3"
    d_sub "I’m also sure MJ could do it..."
    voice "audio/Barby/Day 3 TM/barby_line203.mp3"
    b_sub "But, as they say, {i}there’s no ‘I’ in team{/i}."
    show mjj happy
    voice "audio/MJ/Day 3 TM/MJ_line071.mp3"
    m_sub "Oh Barby, you’d make a great comedian, you know that?" 
    show dee neutral
    show barb neutral
    voice "audio/Deez/Day 3 TM/deez_line073.mp3"
    d_sub "No he would not. His career would all be based on stating the obvious."
    show dee happy 
    voice "audio/Deez/Day 3 TM/deez_line074.mp3"
    d_sub "Hmm. There is also an ‘e’ in team."
    show apol happy
    voice "audio/Apollo/Day 3 TM/apollo_line132.mp3"
    a_sub "Yeah, and an ‘a’, for amazing!"
    voice "audio/Deez/Day 3 TM/deez_line075.mp3"
    d_sub "Wait... there is also a ‘m’. That is MJ."
    voice "audio/Apollo/Day 3 TM/apollo_line133.mp3"
    a_sub "Oh, but there’s no ‘j’... only the ‘m’."
    #VA note: the ‘please’ is really desperate 
    show barb pensive
    voice "audio/Barby/Day 3 TM/barby_line204.mp3"
    b_sub "Regardless of what letters are in the word team, I really think you should really slow down and take a break. {i}Please{/i}?" 
    voice "audio/MJ/Day 3 TM/MJ_line072.mp3"
    m_sub "Haha."
    show dee neutral
    show apol pensive
    show barb neutral
    voice "audio/MJ/Day 3 TM/MJ_line073.mp3"
    m_sub "If none of you are going to help reach the deadline, then I will."
    voice "audio/MJ/Day 3 TM/MJ_line074.mp3"
    m_sub "I think. This meeting is adjourned. :)"
    voice "audio/MJ/Day 3 TM/MJ_line075.mp3"
    m_sub "I’m going back to work." 
    # mj leave
    hide mjj ha[py] with dissolve
    voice "audio/Apollo/Day 3 TM/apollo_line134.mp3"
    a_sub "Oh... they even took my job..."
    voice "audio/Apollo/Day 3 TM/apollo_line135.mp3"
    a_sub "..."
    voice "audio/Barby/Day 3 TM/barby_line205.mp3"
    b_sub "..."
    voice "audio/Barby/Day 3 TM/barby_line206.mp3"
    b_sub "I should check on them." 
    voice "audio/Apollo/Day 3 TM/apollo_line136.mp3"
    a_sub "...please do."
    voice "audio/Deez/Day 3 TM/deez_line076.mp3"
    d_sub "...they’ll be fine. They’re strong. They’re... they’re not going to fold easily. Right?"
    voice "audio/Apollo/Day 3 TM/apollo_line137.mp3"
    a_sub "...so was Dave."
    voice "audio/Barby/Day 3 TM/barby_line207.mp3"
    b_sub "So was Kendra."
    voice "audio/Barby/Day 3 TM/barby_line208.mp3"
    b_sub "I’m going." 

    #Encounter
    #overwrld outside of manager office. Silence
    $ quick_menu = True
    stop music
    scene room_2
    show blue:
        blend 'multiply' alpha 0.3
    show overlay:
        blend 'multiply'
    show borders
    show ken monster at downward, center
    with fade
    voice "audio/Barby/Day 3 Encounter/barby_line209.mp3"
    b "...Hiya, Kendra."
    voice "audio/Kendra/Day 3 Encounter/kendra_line086.mp3"
    k "..."
    voice "audio/Barby/Day 3 Encounter/barby_line210.mp3"
    b "Have you seen MJ?"
    show ken monstertt
    voice "audio/Kendra/Day 3 Encounter/kendra_line087.mp3"
    k "...They listened to you."
    # sHE RRSPONDED???
    show ken monster
    voice "audio/Barby/Day 3 Encounter/barby_line211.mp3"
    b "Huh?"
    show ken monstertt
    voice "audio/Kendra/Day 3 Encounter/kendra_line088.mp3"
    k "They’re taking a break."
    voice "audio/Barby/Day 3 Encounter/barby_line212.mp3"
    b "They are? Where are they going?"
    voice "audio/Kendra/Day 3 Encounter/kendra_line089.mp3"
    k "..."
    voice "audio/Barby/Day 3 Encounter/barby_line213.mp3"
    b "..."
    voice "audio/Barby/Day 3 Encounter/barby_line214.mp3"
    b "Okay. Thank you, Kendra."

    #Kendra Again
    voice "audio/Barby/Day 3 Encounter/barby_line215.mp3"
    b "I should check on MJ."
    $ quick_menu = False
    jump encounter3

    #go to breakroom
label encounter3:

    scene black
    pause 2.0
    scene mj sohot:
        zoom 1.2
        easein 40 zoom 1.0
    with fade
    #mj play flute
    pause 3.0
    voice "audio/MJ/Day 3 Encounter/MJ_line076.mp3"

    scene mj_scene
    $ renpy.pause(47)
    # m_sub "!"
    # scene black
    # voice "audio/Barby/Day 3 Encounter/barby_line216.mp3"
    # b_sub "Oh, I’m sorry, did I interrupt? I-I didn’t mean to."
    # voice "audio/MJ/Day 3 Encounter/MJ_line077.mp3"
    # m_sub "No... no..."
    # # MJs voicelines get progressively worse and start layering and being just evhossnon top of eadh other  until they yell last line ans transform 
    # voice "audio/MJ/Day 3 Encounter/MJ_line078.mp3"
    # m_sub "Wait, I’m working! I’m working, I swear."
    # voice "audio/Barby/Day 3 Encounter/barby_line217.mp3"
    # b_sub "I-It’s okay, MJ, you can take a break, it’s okay–"
    # voice "audio/MJ/Day 3 Encounter/MJ_line079.mp3"
    # m_sub "No! I’m not– I’m not supposed to–"
    # voice "audio/MJ/Day 3 Encounter/MJ_line080.mp3"
    # m_sub "I’m a hard worker! I work so hard!"
    # voice "audio/MJ/Day 3 Encounter/MJ_line081.mp3"
    # m_sub "I know! I know it's not enough. No matter how hard I work it’s not enough. So I’ll keep working!"
    # voice "audio/MJ/Day 3 Encounter/MJ_line082.mp3"
    # m_sub "I’ll stop wanting to be something else!! I’m not supposed to be here but I'll sure try my best to act like it!!"
    # voice "audio/Barby/Day 3 Encounter/barby_line218.mp3"
    # b_sub "No, no, please, you can- you can be whatever you want to be-"
    # voice "audio/MJ/Day 3 Encounter/MJ_line083.mp3"
    # m_sub "STOP! STOP LOOKING AT ME!"
    # voice "audio/MJ/Day 3 Encounter/MJ_line084.mp3"
    # m_sub "I GAVE IT ALL UP FOR WHAT. NOTHING?"
    # voice "audio/MJ/Day 3 Encounter/MJ_line085.mp3"
    # m_sub "I’M GONNA DIE IN HERE. I’M NEVER LEAVING I’M STUCK HERE FOREVER."
    # voice "audio/MJ/Day 3 Encounter/MJ_line086.mp3"
    # m_sub "I NEVER WANTED THIS I NEVER WANTED TO BE HERE."
    # # concern trying to call out to them but trying to be consoling/comforting
    # voice "audio/Barby/Day 3 Encounter/barby_line219.mp3"
    # b_sub "MJ-" 
    # # MJ snaps back to "normal" before devolving again
    # voice "audio/MJ/Day 3 Encounter/MJ_line087.mp3"
    # m_sub "If I just work hard enough, if I keep it all tidy and keep on a BIIIG smile, then one day I can leave!"
    # voice "audio/MJ/Day 3 Encounter/MJ_line088.mp3"
    # m_sub "But it’s never hard enough! It’ll never be enough! I’LL NEVER BE ENOUGH, GOD I’LL NEVER BE ENOUGH!"
    # voice "audio/MJ/Day 3 Encounter/MJ_line089.mp3"
    # m_sub "STOP WATCHING ME."
    # voice "audio/MJ/Day 3 Encounter/MJ_line090.mp3"
    # m_sub "I’LL GET BACK TO WORK!"

    # everything stops
    # silence

    # slowly growing up and up

    # uncomfortable silence

    # black

    # shot changes to behind barbys head
    scene black
    pause 2.0

    scene kendrabgmonster
    show m monster
    play music "audio/Music/Ominous Background Music.mp3" loop
    menu:
        "Take a break":
            $ quick_menu = False 
            voice "audio/Barby/Day 3 Encounter/barby_line220.mp3"
            b_sub "Please take a break—"
            voice "audio/MJ/Day 3 Encounter/MJ_line091.mp3"
            m_sub "Get out of my way."
            pause 2
            show m monstershadow at center
            pause 2
            
            # pain
            hide m monstershadow
            show black 
            $ renpy.pause(1, hard=True)
            show m monster at center, shaking:
                zoom 1.2
            show noises:
                alpha 0.1
                blend 'add'
            $ renpy.pause(2, hard=True)                
            jump encounter3
            # JUMPSCARE DIE
            # GAME OVER

        "Get back to work":
            voice "audio/Barby/Day 3 Encounter/barby_line221a.mp3"
            $ quick_menu = False            
            b_sub "...Can you still work? Like this?"
            # MJ silent 
            voice "audio/MJ/Day 3 Encounter/MJ_line092.mp3"
            m_sub "Of course. :)"
            voice "audio/MJ/Day 3 Encounter/MJ_line093.mp3"
            m_sub "Whatever I can do to help."
            voice "audio/MJ/Day 3 Encounter/MJ_line094.mp3"
            m_sub "Your wellbeing is my wellbeing."
            
            b_sub "Okay."
            b_sub "I’ll... I’ll let you do your work."
    scene black
    # leave breakroom
    # deez is standing right outside
    pause 1
    scene room_3
    show borders1
    show blue:
        blend 'multiply' alpha 0.3
    show noises:
        alpha 0.1
        blend 'add'
    show overlay:
        blend 'multiply' 
    show de sad at downward, center
    with fade
    $ quick_menu = True
    d "..."
    #Deez
    # blubur note: only time deez ask question, deez very vulnerable and genuine
    show de sadt
    # about to ask are they okay but stops cause he doesnt wanna ask questions, so he instead states that everything will be fine
    d "Are they...?"
    d "... I'm sure everything's going to come out the way they're supposed to."

    # black screen
    scene black 
    stop music
    pause 2.0
    # sad, but stern 
    stop music
    $ quick_menu = False
    
    b_sub "No." 

    # black screen 
    scene black 
    pause 2

    # end

    jump day4