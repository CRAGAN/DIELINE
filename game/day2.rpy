label day2:
    #Calendar appears: October 27th, Tuesday
    # Deadline: >30 days
    # idea to just make it generally greater than because its like, people don't feel the pressure that much knowing there's a lot of time left
    $ talkedtokendra = False
    $ talkedtoapollo = False
    $ talkedtomj = False
    $ talkedtodeez = False
    $ day = 2
    
    scene black
    centered "October 27th, Tuesday"
    centered "Deadline: >30 days"
    
    b "Another day at work. Alright, we got this!"
    b "Huh... no reply from Dave, yet. Wonder where he is."
    b "Well I better get to work, soon. Let’s not dilly dally."
    jump rooms2
label rooms2:
    $ storage = False
    $ janitor = False
    $ bathroom = False
    $ managerroom = False
    call screen rooms2

label minigametime:
        b "...Huh. Dave's still working remotely. He hasn't replied to any emails..."
        b "Odd."
        b "Well, I better get back to work!"
        
        #call screen email_minigame # FROG OVER HERE
        $ talkedtokendra = False
        $ talkedtoapollo = False
        $ talkedtomj = False
        $ talkedtodeez = False
        jump breaktime2

label teammeetingpt2:
    show ken worried at downward, center
    
    k "..."
    show ken worried at left with move
    show apo awkwardt at center
    a "Okay— I know we had a meeting agenda, but... we have... something else to discuss."
    a "There were some... changes that corporate called me about while Kendra and I were talking and it's not the uhm—"
    show apo awkward at jumper
    b "Oh gosh, don't tell me it's more bad news..."
    show apo nervoust at squish
    a "I-it's not!! I swear haha, It's nothing {i}too horrible{/i}, Just a deadline change—"
    show apo surprised at jumper
    show de surprisedt at jump, right
    d "Deadline change?! That's cucumbersome..."
    show de surprised
    show apo surprised:
        easein 0.5 xoffset -150
    show m thinkingt at downward, center:
        xoffset 250
    m "Do you mean cumbersome?"
    show m thinking
    show de shyt at downward
    d "MJ, you can't say that in the office..."
    show de default at jumper
    show m default at up
    b "W-wait, maybe it's an extension! They saw how unreasonable the project's due date was so... they gave us more time?"
    show apo awkwardt
    a "Aahh, I love your optimism, but... they pushed it just a smidge closer— Just, like... in {b}four days{/b}." 
    show apo fear at downward
    show de fear
    show ken fear
    show m fear
    b "WHAAAT?!"

    "'Tuesday October 27'"
    "'Deadline in 4 days'"
    show m feart
    m "Oh! Oh dear. That's NOT a smidge."
    show m fear
    show de feart at shaking, downward
    d "This is chickeneyed!"
    show de fear
    show apo nervoust at jumper
    a "A-ahh ahh! Let's- let's calm down guys! {i}Wait uhm okay—{/i} I hear you, I see you, and I understand your concerns—"
    show de angryt at up
    show apo fear at jumper
    d "No offense, you don't understand anything."
    show de angry 
    show apo feart at downward, shaking
    a "AaaAAahh... sorry—" 
    show apo fear
    show de sadt at downward
    d "I just said no offense. This is not offensive, I am helping you..."
    show de sad
    b "Four days isn't enough time to do ANYTHING!"
    show de defaultt at jumper
    d "Yeah, what he said."
    show de default
    show apo worriedt at up
    a "Ough... sorrsies..." 
    show apo worried
    show m hmt at jump
    m "It's no problem; I can pick up all the slack." 
    show m hm
    b "I don't think that's going to be enough! Four days?" 
    show apo worriedt
    a "I-I know this is terrible! But we made a lot of progress yesterday, right? And today?" 
    show apo worried
    show m thinkingt
    m "Hm... 'a lot' if the deadline was in over 30 days. Which it used to be." 
    show m thinking
    k "I-I have a question. If we end up having to work overtime to finish the project, are we... getting paid for it?" 
    show apo worriedt
    a "I tried, I really really tried to negotiate with the higher ups about it, but they still said no." 
    a "It's a full turn key contract- so we only get any bonuses if we finish the product in a way that's satisfying enough for the clients, and they, uh, feel like giving the employees bonuses!" 
    a "So, so maybe if we work hard enough? And do really really well?"
    show apo worried
    show m defaultt
    m "You heard her, though. We {i} could{/i} get a bonus by the end."
    show m hm at downward
    b "But no guaranteed overtime."
    show ken worriedt at downward
    k "Oh... I see. That's- that's too bad! I-I... am I still doing all this work?" 
    show ken worried
    a "I... I don't know, Kendra..." 
    show m hmt at jump
    m "It seems like we're about to get even more work, unfortunately."
    show m hm
    show ken awkwardt at shaking, up
    k "Haha... hah! No... no breaks for me, I guess!"
    show ken feart
    k "I-I should... ooohhh... oh god I'm so... I feel like my head is going to explode!"
    show ken fear at jump
    b "K-Kendra? Are you okay? Maybe you should head to the clinic—"
    show ken feart at jumper, shaking
    show apo fear
    show de fear
    show m fear
    k "{b}NO. IT'S... FINE. I WILL BE FINE.{/b}" with vpunch
    k "{b}I... I need to get back to work.{/b}"
    show ken fear:
        easein 0.5 1000

# kendra leave? 
    show apo worriedt at downward
    a "... Oh death... I-I— I should..."
    show apo worried
    b "It's fine, I'll... check up on her."

# OVERWORLD TIME (outside manager room)
# THUD THUD THUD
# CRASH
# (kendra banging her head on the computer then breaking the screen)
# kendra groaning 
label kendragobrr:
#VA note: Kendra is wailing and groaning about her head hurting. She sounds more angry at herself than in pain. 
scene room_1
k "{b}My head... it- my head hurts.{/b}"
b "K-Kendra? Is... everything okay? What's that noise...?!"
k "{b}It needs to stop.{/b}"

#IF POSSIBLE ONLY IDK there's a sickening THUD each time Kendra talks

k "{b}I Need.{/b}" with hpunch
#THUD
k "{b}To.{/b}" with hpunch
#THUD
k "{b}Stop.{/b}" with hpunch
#THUD

#Thudding continues
centered " " with hpunch

# overworld control access
# go to cubicles 
pause 1.0
scene room_2 with fade
# sfx, thudding footsteps
centered " " with vpunch
# loud grunt/screaming like every step she takes is painful
k "{b}A A A A{/b}" with vpunch
scene room_3 with fade

# long hallway

# door closing (breakroom door closing sound)
jump encounterday2

label encounterday2:
scene kendramonster1 with fade
b "Kendra? Did—did something happen to you—?"
pause 2.0
# kendra cg
scene black 
pause 2.0
scene kendramonster2 
pause 2.0
b "..."
# scary... reverb on voice
b "...Oh god..."
scene black
pause 2.0
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
with vpunch
# pause, let the atmosphere sink in
# barby's in like trance like state kind of so muffle, under water style, apollo voice

a "Barby?"

# apollo's voice becomes a bit clearer but reverby

a "What's going– AAAAAAH!"
# mj and deez are off screen here, so make them quiet, muffled, also under water style
m "Did someone scream?"
d "Yes."
m " Stay out here, Deez, let me check..."
# muffled footsteps, footsteps stop  (MJ sees face reacts but doesn't say anything? Or make them say something)
m "OH. OH DEAR."
# barby voice is still reverb
b "Kendra...?"
a "Oh, oh, oh no... this is... oh..."
a "Mmm... manager decision...!" 
a "... We're refusing this deadline. I-I can't— We can't—!!" 
a "Call— we need to call the clinic, the hospital, anyone!" 
m "Let's, aahh— let's calm down, okay? Let's think this through—" 
a "I-I'm sorry, right I uhm, where's my phone—" 
a "We need to tell the higher ups what happened... and ask... um..." 
m "Kendra? Hey, let's get you... somewhere." 

# The CG shifts and its mouth opens as if it's a talking sprite. SQUELCH SQUELCH her JAW is breaking and is MUSHY   make her talk slowly cause her jaw is breaking every time it moves up and down
# her audio is so weird and pops up on screen as blue text weird glitchy instead of normal subtitles

show ken monstertt
k "{b}Don't worry. I'll get all of it done.{/b}"
show ken monsterr
m "Wh...what?" 
show ken monstertt
k "{b}Turn my computer on. I will handle it.{/b}"
show ken monsterr
#VA note: She'd be sobbing quietly at this point, sniffle sniffle
a "..."
b "Kendra? D-Do you want to–"
show ken monstertt
k "{b}I said I'll get it done. Turn. It. On.{/b}"
b "... okay." 
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
show overlay:
    blend 'multiply' 
show de fear at shaking, downward, center
with fade
"..."
#Deez
# blubur note: only time deez ask question, deez very vulnerable and genuine
show de feart
d "...What happened...? Do we call someone?"
d "I don't know... what do I do?"

#Barby himself is too overwhelmed to have an answer
show de fear
b "... I don't know."
menu:
    "walk to cubicle":
        scene room_2 
        show borders
        with fade
        "..."
        b "Ah... It's broken."
        jump day3
#walk to cubicles, when you get there barby just goes to cubicle automatically and 
#screen black
# VA NOte: "ah" is like... low and subtle and shaky


