# DAY 1
label mjtalking:
    window hide
    if talkedtomj == False:
        $ talkedtomj = True

        scene mjcubicle with fade
        voice "audio/Barby/Day 1 ID/barby_line048.mp3"
        b_sub "Hiya! MJ Grey, was it?"
        voice "audio/MJ/Day 1 OW/MJ_line001.mp3"
        m_sub "That I am! MJ Grey, here at your service. How can I help you, Barby?"
        voice "audio/Barby/Day 1 ID/barby_line049.mp3"
        b_sub "Oh, um, I’m actually here to help you!"
        voice "audio/MJ/Day 1 OW/MJ_line002.mp3"
        m_sub "Oh, no, no, no, please, allow me to help you out. It’s no problem."
        voice "audio/Barby/Day 1 ID/barby_line050.mp3"
        b_sub "I appreciate it! Thank you! But it {i}is{/i} my job to assist, as the assistant manager."
        voice "audio/MJ/Day 1 OW/MJ_line003.mp3"
        m_sub "Yes, but your wellbeing is my wellbeing! If you let me help you out, then you’re also helping me out in a way. It’s a win-win, isn’t it?"
        voice "audio/Barby/Day 1 ID/barby_line051.mp3"
        b_sub "...Sure..!"
        voice "audio/Barby/Day 1 ID/barby_line052.mp3"
        b_sub "Uhh, Here's your ID!"
       
       

        pause 0.2
        show overlay:
            blend 'multiply'
        
        show mj_id at forward, center:
            yoffset -300
        with dissolve
        $ renpy.pause(1.5, hard=True)
        #sfx_id2
        voice "audio/MJ/Day 1 OW/MJ_line004mp3"
        m_sub "Neat, thanks. Hey, I don’t look bad."
        voice "audio/Barby/Day 1 ID/barby_line053.mp3"
        b_sub "Yeah... you and I worked together before, right?"
        voice "audio/MJ/Day 1 OW/MJ_line005.mp3"
        m_sub "Yes? What about it?"
        voice "audio/Barby/Day 1 ID/barby_line054.mp3"
        b_sub "That’s what I thought! Just jogging my memory."
        voice "audio/MJ/Day 1 OW/MJ_line006.mp3"
        m_sub "Huh? It wasn’t that long ago though."
   
        
        hide mj_id with dissolve
        scene room_2 
        show lighter:
            blend 'add' alpha 0.3
        show borders:
            blend 'multiply'
        show overlay:
            blend 'multiply'
        
        show m default at up, center
        with fade
        voice "audio/Barby/Day 1 ID/barby_line055.mp3"
        $ quick_menu = True
        b "Yeah... time flies!"
        default whatdoesitstandfor = False
        default whatdepartmentareyoufrom = False
        default howsworkmj = False
        default howslifemj = False

        while not (whatdepartmentareyoufrom and whatdoesitstandfor and howsworkmj and howslifemj):
            menu:
                
                "What does it stand for?" if not whatdoesitstandfor:
                    $ whatdoesitstandfor = True
                    voice "audio/Barby/Day 1 ID/barby_line056.mp3"
                    b "Can I ask what MJ stands for?" 
                    show m defaultt at up
                    voice "audio/MJ/Day 1 OW/MJ_line007.mp3"
                    m "Oh, it’s nothing special. Just plain old MJ, haha!"
                    show m default at jumper
                    voice "audio/Barby/Day 1 ID/barby_line057.mp3"
                    b "They didn’t answer the question. Aww..." 
                    show m happyt at downward
                    voice "audio/MJ/Day 1 OW/MJ_line008.mp3"
                    m "I’m surprised it isn’t written on my ID, actually. Not that it’s an issue. I like being MJ more anyway."
                    show m happy
                    voice "audio/Barby/Day 1 ID/barby_line058.mp3"
                    b "Oh! If that’s the case, then you can just be MJ."
                    voice "audio/Barby/Day 1 ID/barby_line059.mp3"
                    b "Follow your heart."
                    show m defaultt at downward, center
                    voice "audio/MJ/Day 1 OW/MJ_line009.mp3"
                    m "Hm! Apollo says that sometimes."
                    show m default 
                    voice "audio/Barby/Day 1 ID/barby_line060.mp3"
                    b "Yeah."
                "What department are you from?" if not whatdepartmentareyoufrom:
                    $ whatdepartmentareyoufrom = True
                    voice "audio/Barby/Day 1 ID/barby_line061.mp3"
                    b "Just to make sure— with the whole name being faded and everything— what exactly {i}is{/i} your job title?"
                    voice "audio/MJ/Day 1 OW/MJ_line010.mp3"
                    m "Hmm? What do you mean?"
                    show m happyt at downward
                    voice "audio/MJ/Day 1 OW/MJ_line011.mp3"
                    m "I am a part of the team, if that’s what you were wondering."
                    show m happy
                    voice "audio/Barby/Day 1 ID/barby_line062.mp3"
                    b "Oh yes, of course."
     
                "How's work?" if not howsworkmj:
                    $ quick_menu = True
                    $ howsworkmj = True
                    voice "audio/Barby/Day 1 ID/barby_line063.mp3"
                    b "So, how's work been so far?"
                    show m hmt
                    voice "audio/MJ/Day 1 OW/MJ_line012.mp3"
                    m "Well, we don't know what our job actually is yet, but we're making good progress!"
                    show m hm
                    voice "audio/Barby/Day 1 ID/barby_line064.mp3"
                    b "That's true—I just got here, but it looks like a lot’s already being done?"
                    show m defaultt at jumper
                    voice "audio/MJ/Day 1 OW/MJ_line013.mp3"
                    m "Yep! Everyone here is so hardworking."
                    voice "audio/MJ/Day 1 OW/MJ_line014.mp3"
                    m "You know, the intern offered me coffee even though I didn’t ask for it. How kind." 
                    show m default
                    voice "audio/Barby/Day 1 ID/barby_line065.mp3"
                    b "I’m glad you’ve been experiencing a positive work environment. It looks like the intern got the memo!"
                    voice "audio/Barby/Day 1 ID/barby_line066.mp3"
                    b "We’ve... always tried to make things as nice as possible for each other. We’re all in the same boat, after all."
                
                "How's life?" if not howslifemj:
                    
                    $ howslifemj = True
                    voice "audio/Barby/Day 1 ID/barby_line067.mp3"
                    b "Outside all of that, how are you?"
                    show m defaultt at jumper
                    voice "audio/MJ/Day 1 OW/MJ_line015.mp3"
                    m "It’s all been fine and dandy on my end!"
                    voice "audio/MJ/Day 1 OW/MJ_line016.mp3"
                    m "Though the recent uptick in work has left me with less time to practice my music, which is a bummer."
                    show m default
                    voice "audio/Barby/Day 1 ID/barby_line068.mp3"
                    b "Aw, I’m sorry to hear that. Hopefully you can play some more... after this project? I mean- I’d love to hear you play!"
                    show m happyt at jumper
                    voice "audio/MJ/Day 1 OW/MJ_line017.mp3"
                    m "Aww, thank you. Maybe one day. Though I’m probably rusty by now."
                    voice "audio/MJ/Day 1 OW/MJ_line018.mp3"
                    m "How about you?" 
                    show m happy
                    voice "audio/Barby/Day 1 ID/barby_line069.mp3"
                    b "Me? Like... if I do any music?"
                    show m thinkingt
                    voice "audio/MJ/Day 1 OW/MJ_line019.mp3"
                    m "I meant how’s your life."
                    show m thinking
                    voice "audio/Barby/Day 1 ID/barby_line070.mp3"
                    b "My life... oh god... the life insurance..."
                    voice "audio/Barby/Day 1 ID/barby_line071.mp3"
                    b "Sorry ‘bout that! Talkin’ to myself again, haha! Classic. Haha! Hah!"
                    voice "audio/Barby/Day 1 ID/barby_line072.mp3"
                    b "... MJ. Why am I like this?"
                    show m defaultt at up
                    voice "audio/MJ/Day 1 OW/MJ_line020.mp3"
                    m "What? No, it's fine you’re not cringe or anything. It’s okay, I’ve been tuning out when you talk to yourself, so no worries about me hearing anything I’m not supposed to!"
                    show m default
                    voice "audio/Barby/Day 1 ID/barby_line073.mp3"
                    b "Oh, phew."
                    voice "audio/Barby/Day 1 ID/barby_line074.mp3"
                    b "... wait...! Have you been doing that this whole conversation?!"
                    show m happyt at jumper
                    voice "audio/MJ/Day 1 OW/MJ_line021.mp3"
                    m "xD"
                    show m default at downward
                    
        voice "audio/Barby/Day 1 ID/barby_line075.mp3"
        b "Alright, gotta go check on some things!"
        voice "audio/MJ/Day 1 OW/MJ_line022.mp3"
        m "Okay! Let me know if you need help!"
        voice "audio/Barby/Day 1 ID/barby_line076.mp3"
        b "Let me know if—! Aww man."
        voice "audio/MJ/Day 1 OW/MJ_line023.mp3"
        m "I win, heh."
        $ quick_menu = False

    else: 
        $ quick_menu = True
        m "I'm a little busy right now..."
        

    jump rooms

#Kendra
label kendratalking:
    scene kendraintro
    
    if talkedtokendra == False:
        $ talkedtokendra = True
        
        voice "audio/Barby/Day 1 ID/barby_line077.mp3"
        
        b_sub "Oh! Hiya, Kendra! Do you— do you need help with that?"
        voice "audio/Kendra/Day 1 OW/kendra_line001.mp3"
        k_sub "AH! BARBY! UHH, ahem! Thanks but—it’s ahh... it’s all good, yeah. I'm almost done here."
        voice "audio/Kendra/Day 1 OW/kendra_line002.mp3"
        k_sub "A-Anyways haha, I never got to properly thank you for the hairclip!" 
        voice "audio/Kendra/Day 1 OW/kendra_line003.mp3"
        k_sub "So! Thanks! Yes!"
        voice "audio/Barby/Day 1 ID/barby_line078.mp3"
        b_sub "Right! All of them look so good on you!"
        voice "audio/Kendra/Day 1 OW/kendra_line004.mp3"
        k_sub "Huh? But...you—you only gave me this one..."
        voice "audio/Barby/Day 1 ID/barby_line079.mp3"
        b_sub "Oh! How about the other ones in your hair?"
        voice "audio/Kendra/Day 1 OW/kendra_line005.mp3"
        k_sub "I...do you not remember? Is uhm, everything okay?"
        voice "audio/Barby/Day 1 ID/barby_line080.mp3"
        b_sub "Ah, well, after the accident, my memory’s a little spotty, haha! Oops."
        voice "audio/Barby/Day 1 ID/barby_line081.mp3"
        b_sub "Concussion, coma... both went away, so the amnesia should, too! Hopefully I don’t, uh, fumble anything before then."
        voice "audio/Kendra/Day 1 OW/kendra_line005.mp3"
        k_sub "You... you really forgot everything? Oh, I see... I’m— I’m really sorry..."
        voice "audio/Kendra/Day 1 OW/kendra_line006.mp3"
        k_sub "About the accident..."
        voice "audio/Barby/Day 1 ID/barby_line082.mp3"
        b_sub "It’ll come back to me!!! I’ll try my hardest!"
        voice "audio/Kendra/Day 1 OW/kendra_line007.mp3"
        k_sub "Okay... if you say so."
        voice "audio/Barby/Day 1 ID/barby_line083.mp3"
        b_sub "..."
        voice "audio/Kendra/Day 1 OW/kendra_line008.mp3"
        k_sub "..."
    
        #sfx_id2
        # ID pops out
        show overlay:
            blend 'multiply'
        
        show kendra_id at forward, center:
            yoffset -300
        with dissolve
        $ renpy.pause(1.5, hard=True)
        voice "audio/Barby/Day 1 ID/barby_line084.mp3"
        b_sub "Here’s your ID, by the way!"


        voice "audio/Kendra/Day 1 OW/kendra_line009.mp3"
        k_sub "Oh! Uhm, thank you." 




        hide kendra_id with dissolve
        scene storage 
        show lighter:
            blend 'add' alpha 0.3
        show overlay:
            blend 'multiply' alpha 0.3
        show ken default at center, up
        with fade

        #ID goes away, UI comes out
        default compliment = False
        default rollerskating = False
        default howsworkkendra = False
        default howslifekendra= False
        while not (compliment and rollerskating and howsworkkendra):
            
            menu:
                "Compliment" if not compliment:
                    $ compliment = True
                    voice "audio/Barby/Day 1 ID/barby_line085.mp3"
                    
                    b "You’ve got a really cool surname. It’s got a nice ring to it."
                    show ken defaultt
                    voice "audio/Kendra/Day 1 OW/kendra_line010.mp3"
                    k "Oh, uh, thanks! It isn’t my birth name but..."
                    voice "audio/Kendra/Day 1 OW/kendra_line011.mp3"
                    k "Everyone at my work- well, the theater one, called me ‘Bell’. ‘Cause I looked like one, and they said I was really noisy whenever I reacted to anything."
                    show ken default
                    voice "audio/Barby/Day 1 ID/barby_line086.mp3"
                    b "Ah! Well... I thought it suited you for other reasons; I’ve only talked to you for a bit, and you don’t sound super noisy. Not that you’re quiet! Just that you’re, like. Yeah."
                    voice "audio/Barby/Day 1 ID/barby_line087.mp3"
                    b "So you basically picked it?"
                    show ken awkwardt
                    voice "audio/Kendra/Day 1 OW/kendra_line012.mp3"
                    k "Aha, ha? Yeah... I don’t remember if I had a family or anything before I started working— and... basically living— at the soup kitchen."
                    voice "audio/Kendra/Day 1 OW/kendra_line013.mp3"
                    k "I just kept working, and it became my life!" 
                    voice "audio/Kendra/Day 1 OW/kendra_line014.mp3"
                    k "So that’s how I learned to do most of the things I do...!"
                    show ken awkward
                    voice "audio/Barby/Day 1 ID/barby_line088.mp3"
                    b "Ohh! Yeah, we’re like... forgetting twinsies."
                    show ken awkwardt
                    voice "audio/Kendra/Day 1 OW/kendra_line015.mp3"
                    k "Oh. Aha. Yeah..."
                    show ken awkward
                    voice "audio/Barby/Day 1 ID/barby_line089.mp3"
                    b "...Yeah. Just for now! Until I remember again."
                    show ken default
                    # return to choices

                "Roller skating" if not rollerskating:
                    $ rollerskating = True
                    voice "audio/Barby/Day 1 ID/barby_line090.mp3"
                    
                    b "I heard you do roller skating? I think that’s really neat! I’ve always wanted to learn how to do that."
                    show ken awkwardt
                    voice "audio/Kendra/Day 1 OW/kendra_line016.mp3"
                    k "Hah, yeah, I do quite a lot of, ahh—things...!"
                    voice "audio/Kendra/Day 1 OW/kendra_line017.mp3"
                    k "I don’t know if you, erm, remember this but, like... we planned on going roller skating together!" 
                    show ken worriedt
                    voice "audio/Kendra/Day 1 OW/kendra_line018.mp3"
                    k "It’s—it’s not important anymore though, o-of course! Especially since ahh—"
                    voice "audio/Kendra/Day 1 OW/kendra_line019.mp3"
                    k "Your... leg. I was... yeah, I was wondering if your leg was, uhm, okay?"
                    show ken worried
                    voice "audio/Barby/Day 1 ID/barby_line091.mp3"
                    b "Ah... my leg?"
                    #VA: Kendra is visibly shaken recalling the accident, says "accident" in a low voice/whisper 
                    show ken worriedt
                    voice "audio/Kendra/Day 1 OW/kendra_line020.mp3"
                    k "Well... it looked pretty bad in the a-accident, and you’ve been a little wobbly while we talk."
                    #VA: Whispers "accident" 
                    show ken worried
                    voice "audio/Barby/Day 1 ID/barby_line092.mp3"
                    b "Oh, you saw the... {i}accident{/i}?"
                    show ken worriedt
                    voice "audio/Kendra/Day 1 OW/kendra_line021.mp3"
                    k "I was, uh, the one who called the emergency hotline..."
                    show ken worried
                    voice "audio/Barby/Day 1 ID/barby_line093.mp3"
                    b "Oh..."
                    voice "audio/Barby/Day 1 ID/barby_line094.mp3"
                    b "Um, I’ve healed a lot! So maybe... maybe we can still roller skate? I mean. If you still want to-! Even if I don’t remember..."
                    show ken awkwardt
                    voice "audio/Kendra/Day 1 OW/kendra_line022.mp3"
                    k "It’s...it’s whatever— I-I mean— don’t, uhm... don’t worry too hard about it! Maybe next time, when you’re..."
                    voice "audio/Kendra/Day 1 OW/kendra_line023.mp3"
                    k "...Feeling better." 
                    show ken awkward
                    voice "audio/Barby/Day 1 ID/barby_line095.mp3"
                    b "Okay..."
                    show ken default
                    # return to choices

                "How's work?" if not howsworkkendra:
                    $ howsworkkendra = True
                    voice "audio/Barby/Day 1 ID/barby_line096.mp3"
                    
                    b "How’s work been for ya?"
                    show ken defaultt
                    voice "audio/Kendra/Day 1 OW/kendra_line024.mp3"
                    k "Which one?"
                    show ken default
                    voice "audio/Barby/Day 1 ID/barby_line097.mp3"
                    b "Oh... this one?"
                    show ken defaultt
                    voice "audio/Kendra/Day 1 OW/kendra_line025.mp3"
                    k "Ahh, it’s like— you know, the usual. So much of this and that, it’s a little crazy compared to my other jobs!"
                    voice "audio/Kendra/Day 1 OW/kendra_line026.mp3"
                    k "Honestly, how can you guys manage this much work {i}all{/i} the time?"
                    show ken default
                    voice "audio/Barby/Day 1 ID/barby_line098.mp3"
                    b "Ough... sorry you have to deal with all that..."
                    show ken awkwardt
                    voice "audio/Kendra/Day 1 OW/kendra_line027.mp3"
                    k "But it’s okay! I-I’ve almost finished with everything before our team meet, so... it’s fineee."
                    show ken awkward
                    voice "audio/Barby/Day 1 ID/barby_line099.mp3"
                    b "Oh! Wow! That’s really... Wow! Congrats and, uh, good job? Color me surprised!"
                    show ken awkwardt
                    voice "audio/Kendra/Day 1 OW/kendra_line028.mp3"
                    k "Ahaha, it’s—it’s nothing! I’m just trying my best, like everyone else!"
                    show ken default
                    # return to choices

                "How's life?" if not howslifekendra:
                    $ howslifekendra = True
                    voice "audio/Barby/Day 1 ID/barby_line100.mp3"
                    
                    b "How’s life?"
                    show ken awkwardt
                    voice "audio/Kendra/Day 1 OW/kendra_line029.mp3"
                    k "Uh... good."
                    voice "audio/Kendra/Day 1 OW/kendra_line030.mp3"
                    k "Yeah— ahh, yes. Just alright! Nothing too bad, I suppose."
                    voice "audio/Kendra/Day 1 OW/kendra_line031.mp3"
                    k "How about... you?"
                    show ken awkward
                    voice "audio/Barby/Day 1 ID/barby_line101.mp3"
                    b "Me!?"
                    #
                    #VA: Dont shout too loud for the words in caps but shift the tone!
                    voice "audio/Barby/Day 1 ID/barby_line102.mp3"
                    b "I’m not really thinking ‘bout it too much. I’m mostly thinking about you, WAIT. LIKE. HOW YOU’RE DOING??? Yeahh... like an assistant manager thinks about employees and— wellbeing..."
                    show ken surprisedt
                    voice "audio/Kendra/Day 1 OW/kendra_line032.mp3"
                    k "ME?! AHAHA OH! Oh like— like normal amounts of thinking about me! Your— your uhm, underling?"
                    show ken fear
                    voice "audio/Barby/Day 1 ID/barby_line0103.mp3"
                    b "UNDERLING!?"
                    show ken feart
                    voice "audio/Kendra/Day 1 OW/kendra_line033.mp3"
                    k "S-SORRY! I mean, teammate! Like I said I’m..."
                    show ken awkwardt
                    voice "audio/Kendra/Day 1 OW/kendra_line034.mp3"
                    k "Good." 
                    show ken awkward
                    voice "audio/Barby/Day 1 ID/barby_line0104.mp3"
                    b "Me. Me, too."
                
                    # return to choices
        voice "audio/Barby/Day 1 ID/barby_line105.mp3"
        b "Well, I hope you the best, uh, finishing up what you gotta do before the meet!"
        voice "audio/Kendra/Day 1 OW/kendra_line035.mp3"
        k "Ah! You’re going? Thank... thank you!"
        jump rooms
    else:
        m "I'm a little busy right now..."
        jump rooms
#DEEZ
label deeztalking:
    scene deezcoffee with fade
    if talkedtodeez == False:
        $ talkedtodeez = True
        voice "audio/Barby/Day 1 ID/barby_line0106.mp3"
        b_sub "Hiya, there! Do you need help with that coffee machine?"
        #VA Deez: say this in a slightly cocky way more than nervous. Like "pssh! Haha Im such a capable person." 
        voice "audio/Deez/Day 1 OW/deez_line001.mp3"
        d_sub "No, I can fix—IT WAS BROKEN WHEN I FOUND IT—I SWEAR."
        voice "audio/Barby/Day 1 ID/barby_line0107.mp3"
        b_sub "That’s okay! It happens. We call it the {i}breakroom{/i} for a reason, haha!"
        voice "audio/Deez/Day 1 OW/deez_line002.mp3"
        d_sub "..."

        #VA: in a low tone, a little awkward and sad that they didnt get the joke  
        voice "audio/Barby/Day 1 ID/barby_line0108.mp3"
        b_sub "...Cause things always break."

        #(or edited in voiceline) sfx_badjoke
        voice "audio/Barby/Day 1 ID/barby_line0109.mp3"
        b_sub "AHEM— I don't think we’ve met before. I’m Fredrick Ibarra! But people just call me Barby." 
        voice "audio/Barby/Day 1 ID/barby_line0110.mp3"
        b_sub "What’s your name?"
        voice "audio/Deez/Day 1 OW/deez_line003.mp3"
        d_sub "Right...introductions. I am a fresh catch, as they say in um. Finance."
        voice "audio/Deez/Day 1 OW/deez_line004.mp3"
        d_sub "Daniel Emil Elazar Zémiermalng."
        voice "audio/Deez/Day 1 OW/deez_line005.mp3"
        d_sub "My name is too long so you can call me {i}Deez{/i} for short."

        # change name in textbox to real nametag
        voice "audio/Barby/Day 1 ID/barby_line011.mp3"
        b_sub "That I knew! Here’s your ID."
        


        # change name in textbox to real nametag

        b_sub "That I knew! Here’s your ID."
        #sfx_id2
        # ID pops out
        show overlay:
            blend 'multiply'
        show deez_id at forward, center:
            yoffset -300
        with dissolve
        $ renpy.pause(1.5, hard=True)
        voice "audio/Deez/Day 1 OW/deez_line006.mp3"
        d_sub "...Oh."
        voice "audio/Deez/Day 1 OW/deez_line007.mp3"
        d_sub "It looks low budget. I-I don’t like it."
        voice "audio/Barby/Day 1 ID/barby_line0112.mp3"
        b_sub "Oh! Yes! The. Interns don’t actually get IDs... So our manager, Ms. Apollo Knight, made this for you herself!"
        #VA Deez: Flustered tone to feigning interest 
        voice "audio/Deez/Day 1 OW/deez_line008.mp3"
        d_sub "OH! Uh—wow! It’s sooo-sooo good for a hand-made card! Explenditure!"
        voice "audio/Deez/Day 1 OW/deez_line009.mp3"
        d_sub "She got my...pupils, my orbs right."
        voice "audio/Deez/Day 1 OW/deez_line010.mp3"
        d_sub "I love it."


        # deadpan
        scene room_4
        show chairs
        show lighter:
            blend 'add' alpha 0.3
        show overlay:
            blend 'multiply' alpha 0.3
        show de default at center, up
        
        with fade
        voice "audio/Barby/Day 1 ID/barby_line0113.mp3"
        $ quick_menu = True
        b "I’ll be sure to tell her!"

        #ID goes away, UI comes out
        default welcome = False
        default fixcoffeemachine = False
        default howsworkdeez = False
        default howslifedeez = False
        while not (welcome and fixcoffeemachine and howslifedeez and howsworkdeez):
            
            menu:
                "Welcome!" if not welcome:
                    $ welcome = True
                    voice "audio/Barby/Day 1 ID/barby_line0114.mp3"
                    
                    b "Welcome to the team! I also started out as an unpaid intern, so I understand the boat you’re in."
                    voice "audio/Barby/Day 1 ID/barby_line0115.mp3"
                    b "Please let me know if you need anything!"
                    show de defaultt
                    voice "audio/Deez/Day 1 OW/deez_line011.mp3"
                    d "Thank you for the warm regards."
                    voice "audio/Deez/Day 1 OW/deez_line012.mp3"
                    d "But I disagree. I’m not on the boat, I’m paid."
                    show de default
                    voice "audio/Barby/Day 1 ID/barby_line0116.mp3"
                    b "... Paid {i}money{/i}?"
                    show de defaultt
                    voice "audio/Deez/Day 1 OW/deez_line013.mp3"
                    d "What else would I be paid in?"
                    show de default
                    voice "audio/Barby/Day 1 ID/barby_line0117.mp3"
                    b "A sense of fulfilment."
                    voice "audio/Barby/Day 1 ID/barby_line0118.mp3"
                    b "Resume fodder?" 
                    show de defaultt at downward
                    voice "audio/Deez/Day 1 OW/deez_line014.mp3"
                    d "Oh. That, too, but economic currency is also there on the list."

                    #VA: Switch up is super fast! "I gotta tell the boss - Apollo about this" is happy and excited, and "DAMN IT" is stupidly sudden and fast yell before it goes back to normal 
                    show de default
                    voice "audio/Barby/Day 1 ID/barby_line0119.mp3"
                    b "Well, it’s good to know that the system’s changing for the better! I gotta tell the boss- DAMN IT- Apollo about this!" 
                    show de shyt
                    voice "audio/Deez/Day 1 OW/deez_line015.mp3"
                    d "Until further notice, I will not be paid yet. But I will when they do compensate me. Which is soon. It will happen. Percentagely."
                    show de shy
                    voice "audio/Barby/Day 1 ID/barby_line0120.mp3"
                    b "Oh."
                    voice "audio/Barby/Day 1 ID/barby_line0121.mp3"
                    b "Cool."
                    show de default at up
                    voice "audio/Deez/Day 1 OW/deez_line016.mp3"
                    d "Likewise."
                    # return to question menu

                "Where did you learn to fix coffee machines?" if not fixcoffeemachine:
                    $ fixcoffeemachine = True
                    
                # pan to coffee machine
                    voice "audio/Barby/Day 1 ID/barby_line0122.mp3"
                    b "Haha. So. Um. Where'd ya learn how to fix coffee machines?"
                    show de shyt
                    voice "audio/Deez/Day 1 OW/deez_line017.mp3"
                    d "Di- Du- I’m a neutral born learner. I’m very complement in the ways of engineering machinery."
                    show de shy
                    voice "audio/Barby/Day 1 ID/barby_line0123.mp3"
                    b "Oh! Alright?!"
                    voice "audio/Barby/Day 1 ID/barby_line0124.mp3"
                    b "You do engineering! That’s awesome! I took mechanics courses in an early college program during senior high- not the same thing, but you get me?"
                    voice "audio/Barby/Day 1 ID/barby_line0125.mp3"
                    b "Never went to college past that, though."
                    voice "audio/Barby/Day 1 ID/barby_line0126.mp3"
                    b "More convenient to pursue a job instead, am I right?" 
                    #VA Deez: say the words in italics as a whisper, or a mumble to himself 
                    show de surprisedt at jumper
                    voice "audio/Deez/Day 1 OW/deez_line018.mp3"
                    d "{i}Oh no{/i}—uh! I mean. Yeah! I relate to that experience, we are quart similar, like, like. Uh. I’m in college, and I’m doing a job!"
                    show de surprised at downward
                    voice "audio/Barby/Day 1 ID/barby_line0127.mp3"
                    b "Wow! That’s commendable, really! Don’t go into debt though, haha!"
                    show de defaultt at up
                    voice "audio/Deez/Day 1 OW/deez_line019.mp3"
                    d "Impossible for me to do that. It’s very easy not to."
                    show de default
                    voice "audio/Barby/Day 1 ID/barby_line0128.mp3"
                    b "{i}Right.{/i}"
                    # back to questions?

                "How's work?" if not howsworkdeez:
                    $ howsworkdeez = True
                    voice "audio/Barby/Day 1 ID/barby_line0129.mp3"
                    
                    
                    b "How’s work been for you?"
                    show de calmt
                    voice "audio/Deez/Day 1 OW/deez_line020.mp3"
                    d "It’s an experience of ease."
                    show de calm
                    voice "audio/Barby/Day 1 ID/barby_line0130.mp3"
                    b "That’s words. In a sentence." 
                    show de default
                    voice "audio/Deez/Day 1 OW/deez_line021.mp3"
                    d "Paragraph."
                    # back to questions?

                "How's life?" if not howslifedeez:
                    #VA: said like "how’s the wife?" 
                    $ howslifedeez = True
                    voice "audio/Barby/Day 1 ID/barby_line0131.mp3"
                    

                    b "So... how’s the life? Outside of work, y’know." 
                    show de defaultt
                    voice "audio/Deez/Day 1 OW/deez_line022.mp3"
                    d "I’m not deceased yet. So it’s going as it should."
                    show de default
                    voice "audio/Barby/Day 1 ID/barby_line0132.mp3"
                    b "Congratulations, then! What’ve you been up to? Hobbies, other responsibilities?"
                    show de defaultt
                    voice "audio/Deez/Day 1 OW/deez_line023.mp3"
                    d "I do a lot of things. Like. Uhhhhhhh...."
                    show de shy
                    voice "audio/Deez/Day 1 OW/deez_line024.mp3"
                    d "..."
                    show de shyt
                    voice "audio/Deez/Day 1 OW/deez_line025.mp3"
                    d "An abundant amount. It’s a lot I can’t think of because there are so surplus."
                    #VA: Barby feels sad for Deez
                    show de shy
                    voice "audio/Barby/Day 1 ID/barby_line0133.mp3"
                    b "...Sounds like you’re drowning in abundance."
                    show de defaultt
                    voice "audio/Deez/Day 1 OW/deez_line026.mp3"
                    d "You look like you have hobbies."
                    show de default
                    voice "audio/Barby/Day 1 ID/barby_line0134.mp3"
                    b "Depends who you ask!"
                    show de defaultt
                    voice "audio/Deez/Day 1 OW/deez_line027.mp3"
                    d "I’m asking you."
                    show de default
                    voice "audio/Barby/Day 1 ID/barby_line0135.mp3"
                    b "Well. Well- what do you consider a hobby?"
                    voice "audio/Barby/Day 1 ID/barby_line0136.mp3"
                    b "Haha, why are we talking about me." 
                    show de defaultt
                    voice "audio/Deez/Day 1 OW/deez_line028.mp3"
                    d "You keep talking at me so I’m talking at you."
                    show de default
                    voice "audio/Barby/Day 1 ID/barby_line0137.mp3"
                    b "That’s. So. Cool."
                    voice "audio/Barby/Day 1 ID/barby_line0138.mp3"
                    b "Since you asked so nicely, my favorite hobbies are making the work environment a friendly place for you and your work family."
                    show de defaultt
                    voice "audio/Deez/Day 1 OW/deez_line029.mp3"
                    d "That’s one hobby. You said it like it was plural."
                    #VA Barby: coughs
                    show de default
                    voice "audio/Barby/Day 1 ID/barby_line0139.mp3"
                    b " "
                    voice "audio/Deez/Day 1 OW/deez_line030.mp3"
                    d "Why."
                    # back to questions?
        voice "audio/Barby/Day 1 ID/barby_line0140.mp3"
        $ quick_menu = True
        b "It was nice chatting with you, but I gotta get back to work."
        voice "audio/Barby/Day 1 ID/barby_line0141.mp3"
        b "Thanks, Deez! I’ll be sure to hold onto that. Your name. Tryna be better at remembering things."
        show de defaultt
        voice "audio/Deez/Day 1 OW/deez_line031.mp3"
        d "Clockwise."
        show de default
        jump rooms

    else:
        "we've already talked!"
        jump rooms
    
#DAY 2


label officewalk2:
    
label mjtalking2:
    scene room_2
    show lighter:
        blend 'add' alpha 0.3
    show borders
    show mj_standing:
        zoom 0.6 ypos 0.33 xpos 0.6
    
    $ talkedtomj = True

    b "Good morning, MJ!"
    m "Good morning! How are you?"
    b "Good! How are you?"
    m "Good!"
    jump rooms2
label deeztalking2:
    #Click Deez
    scene room_3
    show lighter:
        blend 'add' alpha 0.3
    show borders1
    show deez_standing:
        xpos 0.5
        ypos 0.4
        zoom 0.25
            
                
    show kendra_standing:
        xpos 0.4
        ypos 0.45
        zoom 0.3
    $ talkedtodeez = True
    b "Good morning, Deez!"
    d "Good morning."
    b "Do you need any help with anything?"
    d "Never." 
    b "Cool!"
    jump rooms2
label kendratalking2:
    #Click Kendra
    scene room_3
    show lighter:
        blend 'add' alpha 0.3
    show borders1
    show deez_standing:
        xpos 0.5
        ypos 0.4
        zoom 0.25
            
                
    show kendra_standing:
        xpos 0.4
        ypos 0.45
        zoom 0.3
     
    $ talkedtokendra = True
    b "Good morning, Kendra!"
    k "Oh! Hi! Good morning!" 
    b "Hiya!"
    k "Hi!" 
    jump rooms2
# DAY 3
#Office Walk
label kendratalking3:
    #Click Breakroom
    b "I need to go to Kendra’s cubicle."

    #when u enter cubicles room, auto dialogue
    #Barby slow turn to Kendra gulp!
    
    #Kendra
    b "...Good morning, Kendra...!"
    b "Here. I... I made you breakfast."
    b "It's a dish my parents used to make me. It's, uh, a soup kind of, but with rice... chicken, toasted garlic... I put an egg in this one."
    b "It’s called arroz caldo and I thought you'd like it."
    b "It’s still a little hot, so be careful."
    k "{b}... Ugh.{/b}"
    b "Okay...! I need to... uhm—"
    b "Drink sand. Bye."

    #Everyone huddled up away from Kendra in the breakroom 

    d "H-hey! Barby’s here."
    m "Right on time! Did ya see Kendra? How’s she holding up?"
    b "Aoughhhgghhggggg."
    a "She was already here when I clocked in! I don't think she went home... she's just been working... and working—"
    a "She just keeps asking for more work... I’m really worried."
    b "Oh..."
    a "I don’t know what we’re going to do... we kind of needed Kendra for a lot of things." 
    m "Should we tell the higher ups about this? Or anyone at all?" 
    d "Will they believe us? This... this doesn’t seem like a very logical event."
    b "I’m sure we can... figure something out..."
    a "We already tried to tell someone, remember? But no one picked up."
    m "That’s because it was after hours. Maybe if we try again, we’ll get someone this time." 

    #Contact Someone
    b "How about we contact the building specific emergency hotline? They’ll probably be able to respond sooner."
    a "Yeah... emergency services in this city sometimes... take a while... Right, Barby?"
    a "Oh- oh right, you don’t remember. Oopsies."
    b "I saw the report! Don’t worry; I know."
    m "Already on it."
    # call sfx
    "Hello, SFC Marketing & Public Relations Building Specific Emergency Hotline."
    "What can I do to help you?"
    d "A lot."
    m "Well said."
    d "Our coworker is income-pacidated. She is, um, very blue. And very mothy."
    "I see! If your employee is being non-compliant, then you can simply handle them better. Why not try out team building exercises to improve their cooperation?"
    b "Huh?"
    a "T-team meeting exercises?" 
    "This is standard procedure. Please comply with the procedure as employees of SFC, even if your team member may not be. You are not just employees, after all."
    " You are also representing our company’s values and lifestyle. You are all feathers under our wings."
    "So go out there and fly high!"
    a "W-wait, there’s gotta be more—!!"
    "Thank you for calling the SFC Marketing & Public Relations Building Specific Emergency Hotline."
    b "... Okay."
    a "That’s. That's it? No way..."
    d "That guy frankly sucks."
    m "I guess we just have to try our best moving forward."

    #What is happening to Kendra?
    b "What’s happening with her...? It kind of looks like she’s being eaten by moths?"
    m "Weird. Moths aren’t the ones that eat clothes, it’s usually just their larvae."
    a "Um, actually... when I went to check on her earlier, the moths were just kind of on her face? Not doing anything? At least, I don’t think they were."
    d "It might be contagious, and it's possible she'd also be consumed whole if we got into contact with—"
    b "Let’s just not try to touch her! Like, at all for now."

    #Kendra work habits
    b "You said she’s still working?"
    a "Yeah, but when I went to check on her output... she’s barely done anything."
    a "But she still keeps asking for more and more work. I tried to give her a break, but she got mad and yelled at me so I left her alone :("
    b "Man... what are we gonna do... if Kendra’s not at her full strength..." 
    a "Oh Barbs, wish I knew, I really wish I knew..."

    b "Well we have to do something! If Kendra’s not available then– then let’s pick up the slack." 
    m "Not to worry, I’m more than willing to help carry the work load."
    d "I too, can help carry the work load."
    m "Aw, thanks Deez, but you’re still just an intern. There isn’t really much you can do to help."
    d "Oh... I knew that. Of course."
    a "Are you sure MJ? There’s so much that needs to be done and–"
    m "Anything you throw at me, I can accomplish easy peasy." 
    m "Just leave it to me! I’ll get us up to speed in no time."
    b "Well-"
    b "Thanks, MJ, it’s kinda... reassuring? To see you carry this energy despite everything."
    b "But you’re not alone! I can also help out plenty."
    a "Me too! I’ll do my best to make this project a success."
    a "And Deez, don’t worry, you can still help out by helping me out!"
    d "...fine. Okay. Since you... need help, I can help you."
#DAY 5
label kendratalking5:
    b "Good morning, Kendra."
    
label mjtalking5:
    b "Good morning, MJ."

label deeztalking5:
    b "..."
    
    #if you click anyone a second time barby goes "..."
    #sfx_dooropen
    #Managers room
    # cutscene plays, doesnt need to be voice acted, but could be
    #b "Uhh, hiya Apollo...! Sorry for sleeping—"
    # a "BARBYYY! OH MY DEATH, YOU’RE AWAKEEE! I’M SO HAPPY, HAHAHA!"
