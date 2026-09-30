label day3:
    #Intro
# Calendar pop up
    scene black
    pause 2.0
    centered "Wednesday Oct 28"
    centered "3 days left"

    

    b "...Apollo texted to go to the break room as soon as I got here?"
    b "...I need to go to Kendra's cubicle."
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
    jump mjtalking3
label meeting3:
    $ quick_menu = False
    scene meetingbg
    show overlay:
        blend 'multiply' alpha 0.5
    show apol happy
    show barb neutral
    show dee neutral
    show mjj neutral
    show meetingfg
    a_sub "Ahaha... thank you all again for uhm, coming to the team meeting everyone...!"
    show barb pensive
    b_sub "Ahh, but... Kendra’s not here, yet..."
    show mjj happy
    m_sub "I don’t think Kendra’s currently available to participate. No worries, I’m happy to relay anything to her."
    show apol pensive
    a_sub "Knowing our deadline is in two days, I can’t help but be just a little bit worried about our pace so far!"
    a_sub "With Kendra and Dave both... {i}unavailable{/i}, I’m not sure we can even get close to finishing this project."
    show barb neutral
    b_sub "So... let’s start this with. How’s everyone feeling?" 
    m_sub "A-Okay."
    # deez arms and legs  are not feeling alright
    d_sub "My arms and legs are feeling. Alright."
    a_sub "..."
    show barb pensive
    b_sub "Okay... this is. A situation. It looks like most of us are getting a little overwhelmed."
    
    m_sub "Well that’s no big deal. I can just pick up the pace."
    a_sub "I don’t know, MJ... we’re still so behind, and there’s just so much that needs to be done, I don’t think you should..."
    show mjj shocked
    m_sub "Are you doubting me?" 
    show apol shocked
    a_sub "No! No, I’m just–"
    show apol neutral
    m_sub "Then I can handle it."
    show barb shocked
    b_sub "Okay, wait, MJ. I think. We need to take a second. Not just for us, but you, too. You’re doing a lot, so maybe we- including you- need to take a break. Take it easier."
    
    m_sub "...A break?"
    show barb pensive
    b_sub "Especially after what happened to Kendra."
    m_sub "If that’s the case, you should all take a break."
    m_sub "I just need a list of the things that have to be done by today and I’ll get it done. Then we can be finished!"
    b_sub "No- We’re not putting all the work on you..."
    b_sub "Um, no offense, MJ! Not that anyone here doubts that you can do it."
    show dee pensive
    d_sub "I’m also sure MJ could do it..."
    b_sub "But, as they say, {i}there’s no ‘I’ in team{/i}."
    show mjj happy
    m_sub "Oh Barby, you’d make a great comedian, you know that?" 
    show dee neutral
    show barb neutral
    d_sub "No he would not. His career would all be based on stating the obvious."
    show dee happy 
    d_sub "Hmm. There is also an ‘e’ in team."
    show apol happy
    a_sub "Yeah, and an ‘a’, for amazing!"
    
    d_sub "Wait... there is also a ‘m’. That is MJ."
    a_sub "Oh, but there’s no ‘j’... only the ‘m’."
    #VA note: the ‘please’ is really desperate 
    show barb pensive
    b_sub "Regardless of what letters are in the word team, I really think you should really slow down and take a break. {i}Please{/i}?" 
    m_sub "Haha."
    show dee neutral
    show apol pensive
    show barb neutral
    m_sub "If none of you are going to help reach the deadline, then I will."
    m_sub "I think. This meeting is adjourned. :)"
    m_sub "I’m going back to work." 
    # mj leave
    hide mjj ha[py] with dissolve
    a_sub "Oh... they even took my job..."
    a_sub "..."
    b_sub "..."
    b_sub "I should check on them." 
    a_sub "...please do."
    d_sub "...they’ll be fine. They’re strong. They’re... they’re not going to fold easily. Right?"
    a_sub "...so was Dave."
    b_sub "So was Kendra."
    b_sub "I’m going." 

    #Encounter
    #overwrld outside of manager office. Silence
    $ quick_menu = True
    scene room_2
    show blue:
        blend 'multiply' alpha 0.3
    show overlay:
        blend 'multiply'
    show borders
    show ken monster at downward, center
    with fade
    b "...Hiya, Kendra."
    k "..."
    b "Have you seen MJ?"
    show ken monstertt
    k "...They listened to you."
    # sHE RRSPONDED???
    show ken monster
    b "Huh?"
    show ken monstertt
    k "They’re taking a break."
    b "they are? Where are they going?"
    k "..."
    b "..."
    b "Okay. Thank you, Kendra."

    #Kendra Again
    b "I should check on MJ."


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

    m "!"
    scene black
    b "Oh, I’m sorry, did I interrupt? I-I didn’t mean to."
    m "No... no..."
    # MJs voicelines get progressively worse and start layering and being just evhossnon top of eadh other  until they yell last line ans transform 

    m "Wait, I’m working! I’m working, I swear."

    b "I-It’s okay, MJ, you can take a break, it’s okay–"
  
    m "No! I’m not– I’m not supposed to–"
    m "I’m a hard worker! I work so hard!"
    m "I know! I know it's not enough. No matter how hard I work it’s not enough. So I’ll keep working!"

    m "I’ll stop wanting to be something else!! I’m not supposed to be here but I'll sure try my best to act like it!!"

    b "No, no, please, you can- you can be whatever you want to be-"
    m "STOP! STOP LOOKING AT ME!"
    m "I GAVE IT ALL UP FOR WHAT. NOTHING?"
    m "I’M GONNA DIE IN HERE. I’M NEVER LEAVING I’M STUCK HERE FOREVER."
    m "I NEVER WANTED THIS I NEVER WANTED TO BE HERE."
    # concern trying to call out to them but trying to be consoling/comforting
    b "MJ-" 
    # MJ snaps back to "normal" before devolving again
    m "If I just work hard enough, if I keep it all tidy and keep on a BIIIG smile, then one day I can leave!"
    m "But it’s never hard enough! It’ll never be enough! I’LL NEVER BE ENOUGH, GOD I’LL NEVER BE ENOUGH!"
    m "STOP WATCHING ME."
    m "I’LL GET BACK TO WORK!"
    # everything stops
    # silence

    # slowly growing up and up

    # uncomfortable silence

    # black

    # shot changes to behind barbys head
    menu:
        "Take a break":
            b "Please take a break—"
            m "Get out of my way."
            # JUMPSCARE DIE
            # GAME OVER

        "Get back to work":
            b "...Can you still work? Like this?"
            # MJ silent 
            m "Of course. :)"
            m "Whatever I can do to help."
            m "Your wellbeing is my wellbeing."

            b "Okay."
            b "I’ll... I’ll let you do your work."

    # leave breakroom
    # deez is standing right outside
    scene black 
    # about to ask are they okay but stops cause he doesnt wanna ask questions, so he instead states that everything will be fine
    d_sub "Are they...?"
    d_sub "... I'm sure everything's going to come out the way they're supposed to."

    # black screen
    
    pause 2.0
    # sad, but stern 
    b_sub "No." 

    # black screen 

    # end

    jump day4