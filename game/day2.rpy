image meetingroom = Movie(play="images/bg overworld/meetingroom.webm", loop = True)
label day2:
    #Calendar appears: October 27th, Tuesday
    # Deadline: >30 days
    # idea to just make it generally greater than because its like, people don't feel the pressure that much knowing there's a lot of time left
    $ talkedtokendra = False
    $ talkedtoapollo = False
    $ talkedtomj = False
    $ talkedtodeez = False
    $ day = 2
    $ quick_menu = False
    scene black with fade
    centered "{color=#FFFFFF}October 27th, Tuesday{/color}"
    centered "{color=#FFFFFF}Deadline: >30 days{/color}"
    play music "audio/Music/Working Overtime 2m.mp3" loop fadein 1
    $ quick_menu = True
    b "Another day at work. Alright, we got this!"
    b "Huh... no reply from Dave, yet. Wonder where he is."
    b "Well I better get to work, soon. Let’s not dilly dally."
    jump rooms2
label rooms2:
    $ storage = False
    $ janitor = False
    $ bathroom = False
    $ managerroom = False
    $ quick_menu = False

    call screen rooms2 with fade

label minigametime:
        scene black
        $ quick_menu = False

        b "...Huh. Dave's still working remotely. He hasn't replied to any emails..."
        b "Odd."
        b "Well, I better get back to work!"
        play music "audio/Music/Minigames/E-Mployment_.mp3" loop fadein 1
        
        #call screen email_minigame # FROG OVER HERE
        play music "audio/Music/Breaktime/Breaktime Draft 3_Variation 2.mp3" loop fadein 1
        $ talkedtokendra = False
        $ talkedtoapollo = False
        $ talkedtomj = False
        $ talkedtodeez = False

        jump breaktime2 
label teammeetingpt2:
    play music "audio/Music/Working Overtime 2m.mp3" loop fadein 1
    scene meetingroom
    show overlay:
        blend 'multiply'
    show ken worried at downward, center
    voice "audio/Kendra/Day 2 TM/kendra_line070.mp3"
    $ quick_menu = True
    
    k "..."
    show ken worried at left with move
    show apo awkwardt at center
    voice "audio/Apollo/Day 2 TM/apollo_line104.mp3"
    a "Okay— I know we had a meeting agenda, but... we have... something else to discuss."
    voice "audio/Apollo/Day 2 TM/apollo_line105.mp3"
    a "There were some... changes that corporate called me about while Kendra and I were talking and it's not the uhm—"
    show apo awkward at jumper
    voice "audio/Barby/Day 2 TM/barby_line180.mp3"
    b "Oh gosh, don't tell me it's more bad news..."
    show apo nervoust at squish
    voice "audio/Apollo/Day 2 TM/apollo_line106.mp3"
    a "I-it's not!! I swear haha, It's nothing {i}too horrible{/i}, Just a deadline change—"
    show apo surprised at jumper
    show de surprisedt at jump, right
    voice "audio/Deez/Day 2 TM/deez_line063.mp3"
    d "Deadline change?! That's cucumbersome..."
    show de surprised
    show apo surprised:
        easein 0.5 xoffset -150
    show m thinkingt at downward, center:
        xoffset 250
    voice "audio/MJ/Day 2 TM/MJ_line051.mp3"
    m "Do you mean cumbersome?"
    show m thinking
    show de shyt at downward
    voice "audio/Deez/Day 2 TM/deez_line064.mp3"
    d "MJ, you can't say that in the office..."
    show de default at jumper
    show m default at up
    voice "audio/Barby/Day 2 TM/barby_line181.mp3"
    b "W-wait, maybe it's an extension! They saw how unreasonable the project's due date was so... they gave us more time?"
    show apo awkwardt
    voice "audio/Apollo/Day 2 TM/apollo_line107.mp3"
    a "Aahh, I love your optimism, but... they pushed it just a smidge closer— Just, like... in {b}four days{/b}." 
    show apo fear at downward
    show de fear
    show ken fear
    show m fear
    voice "audio/Barby/Day 2 TM/barby_line182.mp3"
    b "WHAAAT?!"

    "'Tuesday October 27'"
    "'Deadline in 4 days'"
    show m feart
    voice "audio/MJ/Day 2 TM/MJ_line052.mp3"
    m "Oh! Oh dear. That's NOT a smidge."
    show m fear
    show de feart at shaking, downward
    voice "audio/Deez/Day 2 TM/deez_line065.mp3"
    d "This is chickeneyed!"
    show de fear
    show apo nervoust at jumper
    voice "audio/Apollo/Day 2 TM/apollo_line108.mp3"
    a "A-ahh ahh! Let's- let's calm down guys! {i}Wait uhm okay—{/i} I hear you, I see you, and I understand your concerns—"
    show de angryt at up
    show apo fear at jumper
    voice "audio/Deez/Day 2 TM/deez_line066.mp3"
    d "No offense, you don't understand anything."
    show de angry 
    show apo fear at downward, shaking, center
    voice "audio/Apollo/Day 2 TM/apollo_line109.mp3"
    a "AaaAAahh... sorry—" 
    show apo fear
    show de sadt at downward
    voice "audio/Deez/Day 2 TM/deez_line067.mp3"
    d "I just said no offense. This is not offensive, I am helping you..."
    show de sad
    voice "audio/Barby/Day 2 TM/barby_line183.mp3"
    b "Four days isn't enough time to do ANYTHING!"
    show de defaultt at jumper
    voice "audio/Deez/Day 2 TM/deez_line068.mp3"
    d "Yeah, what he said."
    show de default
    show apo worriedt at up
    voice "audio/Apollo/Day 2 TM/apollo_line110.mp3"
    a "Ough... sorrsies..." 
    show apo worried
    show m hmt at jump
    voice "audio/MJ/Day 2 TM/MJ_line053.mp3"
    m "It's no problem; I can pick up all the slack." 
    show m hm
    voice "audio/Barby/Day 2 TM/barby_line184.mp3"
    b "I don't think that's going to be enough! Four days?" 
    show apo worriedt
    voice "audio/Apollo/Day 2 TM/apollo_line111.mp3"
    a "I-I know this is terrible! But we made a lot of progress yesterday, right? And today?" 
    show apo worried
    show m thinkingt
    voice "audio/MJ/Day 2 TM/MJ_line054.mp3"
    m "Hm... 'a lot' if the deadline was in over 30 days. Which it used to be." 
    show m thinking
    show ken feart
    voice "audio/Kendra/Day 2 TM/kendra_line071.mp3"
    k "I-I have a question. If we end up having to work overtime to finish the project, are we... getting paid for it?" 
    show apo worriedt
    show ken fear
    voice "audio/Apollo/Day 2 TM/apollo_line112.mp3"
    a "I tried, I really really tried to negotiate with the higher ups about it, but they still said no." 
    voice "audio/Apollo/Day 2 TM/apollo_line113.mp3"
    a "It's a full turn key contract- so we only get any bonuses if we finish the product in a way that's satisfying enough for the clients, and they, uh, feel like giving the employees bonuses!" 
    voice "audio/Apollo/Day 2 TM/apollo_line114.mp3"
    a "So, so maybe if we work hard enough? And do really really well?"
    show apo worried
    show m defaultt
    voice "audio/MJ/Day 2 TM/MJ_line055.mp3"
    m "You heard her, though. We {i} could{/i} get a bonus by the end."
    show m hm at downward
    voice "audio/Barby/Day 2 TM/barby_line185.mp3"
    b "But no guaranteed overtime."
    show ken worriedt at downward
    voice "audio/Kendra/Day 2 TM/kendra_line072.mp3"
    k "Oh... I see. That's- that's too bad! I-I... am I still doing all this work?" 
    show ken worried
    voice "audio/Apollo/Day 2 TM/apollo_line115.mp3"
    a "I... I don't know, Kendra..." 
    show m hmt at jump
    voice "audio/MJ/Day 2 TM/MJ_line056.mp3"
    m "It seems like we're about to get even more work, unfortunately."
    show m hm
    show ken awkwardt at shaking, up
    voice "audio/Kendra/Day 2 TM/kendra_line073.mp3"
    k "Haha... hah! No... no breaks for me, I guess!"
    show ken feart
    voice "audio/Kendra/Day 2 TM/kendra_line074.mp3"
    k "I-I should... ooohhh... oh god I'm so... I feel like my head is going to explode!"
    show ken fear at jump
    voice "audio/Barby/Day 2 TM/barby_line186.mp3"
    b "K-Kendra? Are you okay? Maybe you should head to the clinic—"
    show ken feart at jumper, shaking
    show apo fear
    show de fear
    show m fear
    stop music
    voice "audio/Kendra/Day 2 TM/kendra_line075.mp3"
    k "{b}NO. IT'S... FINE. I WILL BE FINE.{/b}" with vpunch
    voice "audio/Kendra/Day 2 TM/kendra_line076.mp3"
    k "{b}I... I need to get back to work.{/b}"
    show ken fear:
        easein 0.5 xoffset -1000

# kendra leave? 
    show apo worriedt at downward
    voice "audio/Apollo/Day 2 TM/apollo_line116.mp3"
    a "... Oh death... I-I— I should..."
    show apo worried
    voice "audio/Barby/Day 2 TM/barby_line187.mp3"
    b "It's fine, I'll... check up on her."

# OVERWORLD TIME (outside manager room)
# THUD THUD THUD
# CRASH
# (kendra banging her head on the computer then breaking the screen)
# kendra groaning 
label kendragobrr:
    #VA note: Kendra is wailing and groaning about her head hurting. She sounds more angry at herself than in pain. 
    scene room_1 
    show blue:
        blend 'multiply' alpha 0.2
    with fade

    k "{b}My head... it- my head hurts.{/b}"
    voice "audio/Barby/Day 2 TM/barby_line188.mp3"
    b "K-Kendra? Is... everything okay? What's that noise...?!"
    voice "audio/Kendra/Day 2 TM/kendra_line077.mp3"
    k "{b}It needs to stop.{/b}"

    #IF POSSIBLE ONLY IDK there's a sickening THUD each time Kendra talks
    voice "audio/Kendra/Day 2 TM/kendra_line078.mp3"
    k "{b}I Need.{/b}" with hpunch
    #THUD
    voice "audio/Kendra/Day 2 TM/kendra_line079.mp3"
    k "{b}To.{/b}" with hpunch
    #THUD
    voice "audio/Kendra/Day 2 TM/kendra_line080.mp3"
    k "{b}Stop.{/b}" with hpunch
    #THUD

    #Thudding continues
    $ quick_menu = False
    centered " " with hpunch

    # overworld control access
    # go to cubicles 
    pause 3.0
    scene room_2 
    show borders
    show noises:
        alpha 0.1
        blend 'add'
    show borders

    show blue:
        blend 'multiply' alpha 0.5
    with fade
    # sfx, thudding footsteps
    centered " " with vpunch
    # loud grunt/screaming like every step she takes is painful
    voice "audio/Kendra/Day 2 TM/kendra_line081.mp3"
    $ quick_menu = True

    k "{b}A A A A{/b}" with vpunch
    $ quick_menu = False

    scene room_3 
    show noises:
        alpha 0.2
        blend 'add'
    show borders1
    show blue:
        blend 'multiply' alpha 0.8
    with fade
    # long hallway
    centered " "

    # door closing (breakroom door closing sound)
    jump encounterday2

label encounterday2:
    scene kendramonster1 with fade
    voice "audio/Barby/Day 2 Encounter/barby_line189.mp3"
    b_sub "Kendra? Did—did something happen to you—?"
    $ renpy.pause(2.0, hard=True)
    # kendra cg
    scene black 
    $ renpy.pause(2.0, hard=True)
    scene kendramonster2 
    show noises:
        alpha 0.1
        blend 'add'
    $ renpy.pause(2.0, hard=True)
    b_sub "..."
    # scary... reverb on voice
    voice "audio/Barby/Day 2 Encounter/barby_line190.mp3"
    b_sub "...Oh god..."
    play music "audio/Music/Free Horror Ambience (Dark Project).mp3" loop fadein 1
    scene black
    $ renpy.pause(2.0, hard=True)
    camera:
        subpixel True
        zoom 4 xoffset -2500 yoffset -700 
        pause 2.0
        zoom 3 xoffset -1600 yoffset -400
        pause 2.0
        zoom 2 xoffset -800 yoffset -100
        easein 100 zoom 1.0 xoffset 0 yoffset 0

    scene kendrabgmonster at small_wobble1
    show ken monsterr at small_wobble
    show noises:
        alpha 0.1
        blend 'add'
    with vpunch
    $ renpy.pause(6.0, hard=True)
    # pause, let the atmosphere sink in
    # barby's in like trance like state kind of so muffle, under water style, apollo voice

    a_sub "Barby?"

    # apollo's voice becomes a bit clearer but reverby
    voice "audio/Apollo/Day 2 Encounter/apollo_line117.mp3"
    a_sub "What's going– AAAAAAH!"
    # mj and deez are off screen here, so make them quiet, muffled, also under water style
    voice "audio/MJ/Day 2 Encounter/MJ_line057.mp3"
    m_sub "Did someone scream?"
    d_sub "Yes."
    voice "audio/MJ/Day 2 Encounter/MJ_line058.mp3"
    m_sub " Stay out here, Deez, let me check..."
    # muffled footsteps, footsteps stop  (MJ sees face reacts but doesn't say anything? Or make them say something)
    voice "audio/MJ/Day 2 Encounter/MJ_line059.mp3"
    m_sub "OH. OH DEAR."
    # barby voice is still reverb
    voice "audio/Barby/Day 2 Encounter/barby_line191.mp3"
    b_sub "Kendra...?"
    voice "audio/Apollo/Day 2 Encounter/apollo_line119.mp3"
    a_sub "Oh, oh, oh no... this is... oh..."
    voice "audio/Apollo/Day 2 Encounter/apollo_line120.mp3"
    a_sub "Mmm... manager decision...!" 
    voice "audio/Apollo/Day 2 Encounter/apollo_line121.mp3"
    a_sub "... We're refusing this deadline. I-I can't— We can't—!!" 
    voice "audio/Apollo/Day 2 Encounter/apollo_line122.mp3"
    a_sub "Call— we need to call the clinic, the hospital, anyone!" 
    voice "audio/MJ/Day 2 Encounter/MJ_line060.mp3"
    m_sub "Let's, aahh— let's calm down, okay? Let's think this through—" 
    voice "audio/Apollo/Day 2 Encounter/apollo_line123.mp3"
    a_sub "I-I'm sorry, right I uhm, where's my phone—" 
    voice "audio/Apollo/Day 2 Encounter/apollo_line124.mp3"
    a_sub "We need to tell the higher ups what happened... and ask... um..." 
    voice "audio/MJ/Day 2 Encounter/MJ_line061.mp3"
    m_sub "Kendra? Hey, let's get you... somewhere."
    voice "audio/Apollo/Day 2 Encounter/apollo_line124.mp3"
    a_sub "..." 

    # The CG shifts and its mouth opens as if it's a talking sprite. SQUELCH SQUELCH her JAW is breaking and is MUSHY   make her talk slowly cause her jaw is breaking every time it moves up and down
    # her audio is so weird and pops up on screen as blue text weird glitchy instead of normal subtitles

    show ken monstertt
    voice "audio/Kendra/Day 2 TM/kendra_line082.mp3"
    k_sub "{b}Don't worry. I'll get all of it done.{/b}"
    show ken monsterr
    voice "audio/MJ/Day 2 TM/MJ_line062.mp3"
    m_sub "Wh...what?" 
    show ken monstertt
    voice "audio/Kendra/Day 2 Encounter/kendra_line083.mp3"
    k_sub "{b}Turn my computer on. I will handle it.{/b}"
    show ken monsterr
    #VA note: She'd be sobbing quietly at this point, sniffle sniffle
    b_sub "..."
    voice "audio/Barby/Day 2 Encounter/barby_line192.mp3"
    b_sub "Kendra? D-Do you want to–"
    show ken monstertt
    voice "audio/Kendra/Day 2 Encounter/kendra_line084.mp3"
    k_sub "{b}I said I'll get it done. Turn. It. On.{/b}"
    voice "audio/Barby/Day 2 Encounter/barby_line193.mp3"
    b_sub "... okay." 
    scene black
    # lightfilter is GONE its normal bogo render lighting now
    # all the music stopped
    # go to overworld, everyone(except kendra) is standing next to the door
    #Click Anyone
    pause 2.0
    camera:
        reset
    scene room_3
    show borders1
    show blue:
        blend 'multiply' alpha 0.3
    show noises:
        alpha 0.1
        blend 'add'
    show overlay:
        blend 'multiply' 
    show de fear at shaking, downward, center
    with fade
    $ quick_menu = True
    "..."
    #Deez
    # blubur note: only time deez ask question, deez very vulnerable and genuine
    show de feart
    d "...What happened...? Do we call someone?"
    d "I don't know... what do I do?"

    #Barby himself is too overwhelmed to have an answer
    show de fear
    voice "audio/Barby/Day 2 Encounter/barby_line194.mp3"
    b "... I don't know."
    menu:
        "walk to cubicle":
            scene room_2 
            show borders
            show blue:
                blend 'multiply' alpha 0.3
            show noises:
                alpha 0.1
                blend 'add'
            show borders
            with fade
            ## might want to change this somehow?
            " "
            show blue:
                blend 'multiply' alpha 1.0
            "..."
            show black
            b "Ah... It's broken."
            stop music
            jump day3
#walk to cubicles, when you get there barby just goes to cubicle automatically and 
#screen black
# VA NOte: "ah" is like... low and subtle and shaky


image noises:
    "images/noise.png"
    pause 0.3
    "images/noise2.png"
    pause 0.3
    "images/noise3.png"
    pause 0.3
    repeat