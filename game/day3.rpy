label day3:
    #Intro
# Calendar pop up
    scene black
    pause 2.0
    centered "Wednesday Oct 28"
    centered "3 days left"

    

    b "...Apollo texted to go to the break room as soon as I got here?"
    b "...I need to go to Kendra's cubicle."

   

    #Minigames

    #Break Time
    # cubicle, forced dialogue
  

    #Kendra
    # cubicle
label kendracubic:
    m "Hey Kendra! Need a hand there?"
    k "..."
    m "Is that a yes? I’ll take it as a yes."
    b "Hi, Kendra... and hi MJ, too." 
    m "Hey Barby! Just seeing if Kendra needs any help." 
    m "Though I don’t think she’s keen on talking right now. She’s, um, really busy!"
    b "Oh! Uh, yeah... I don't think she's very responsive— Wait, what are you doing?"
    m "Oh! You know, just taking some of the workload off of her. These files were sitting there so—"
    k "Leave me alone, I need to work." 
    m "No problemo, have a good day!"
    b "Wait—! Oh... Alright."

    #Click Kendra again
    b "K-Kendra? Hey, are you okay—"
    k "Urrgh, I said. Leave. Me. Alone!"
    b "Ouugh, she yelled at me...! She must hate me and find me annoying..."
    b "I-I’m sorry... yeah, I’ll go..."


    #Click Kendra Again etc etc etc 
    b "... I don’t think she wants to talk, right now."
    #Team Meeting - VOICED ACTED
    #Note: let apollo talk less barby talk more  as she starts stressing real hard, barby kind of steps in
    a "Ahaha... thank you all again for uhm, coming to the team meeting everyone...!"
    b "Ahh, but... Kendra’s not here, yet..."
    m "I don’t think Kendra’s currently available to participate. No worries, I’m happy to relay anything to her."
    a "Knowing our deadline is in two days, I can’t help but be just a little bit worried about our pace so far!"
    a "With Kendra and Dave both... {i}unavailable{/i}, I’m not sure we can even get close to finishing this project."
    b "So... let’s start this with. How’s everyone feeling?" 
    m "A-Okay."
    # deez arms and legs  are not feeling alright
    d "My arms and legs are feeling. Alright."
    a "..."
    b "Okay... this is. A situation. It looks like most of us are getting a little overwhelmed."
    m "Well that’s no big deal. I can just pick up the pace."
    a "I don’t know, MJ... we’re still so behind, and there’s just so much that needs to be done, I don’t think you should..."
    m "Are you doubting me?" 
    a "No! No, I’m just–"
    m "Then I can handle it."
    b "Okay, wait, MJ. I think. We need to take a second. Not just for us, but you, too. You’re doing a lot, so maybe we- including you- need to take a break. Take it easier."
    m "...A break?"
    b "Especially after what happened to Kendra."
    m "If that’s the case, you should all take a break."
    m "I just need a list of the things that have to be done by today and I’ll get it done. Then we can be finished!"
    b "No- We’re not putting all the work on you..."
    b "Um, no offense, MJ! Not that anyone here doubts that you can do it."
    d "I’m also sure MJ could do it..."
    b "But, as they say, {i}there’s no ‘I’ in team{/i}."
    m "Oh Barby, you’d make a great comedian, you know that?" 
    d "No he would not. His career would all be based on stating the obvious."
    d "Hmm. There is also an ‘e’ in team."
    a "Yeah, and an ‘a’, for amazing!"
    d "Wait... there is also a ‘m’. That is MJ."
    a "Oh, but there’s no ‘j’... only the ‘m’."
    #VA note: the ‘please’ is really desperate 
    b "Regardless of what letters are in the word team, I really think you should really slow down and take a break. {i}Please{/i}?" 
    m "Haha."
    m "If none of you are going to help reach the deadline, then I will."
    m "I think. This meeting is adjourned. :)"
    m "I’m going back to work." 
    # mj leave
    a "Oh... they even took my job..."
    a "..."
    b "..."
    b "I should check on them." 
    a "...please do."
    d "...they’ll be fine. They’re strong. They’re... they’re not going to fold easily. Right?"
    a "...so was Dave."
    b "So was Kendra."
    b "I’m going." 

    #Encounter
    #overwrld outside of manager office. Silence

    # cubicles
    #Kendra
    b "...Hiya, Kendra."
    k "..."
    b "Have you seen MJ?"
    k "...They listened to you."
    # sHE RRSPONDED???
    b "Huh?"
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

    # about to ask are they okay but stops cause he doesnt wanna ask questions, so he instead states that everything will be fine
    d "Are they...?"
    d "... I'm sure everything's going to come out the way they're supposed to."

    # black screen
    # sad, but stern 
    b "No." 

    # black screen 

    # end

    jump day4