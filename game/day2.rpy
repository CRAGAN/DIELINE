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
        
        call screen email_minigame # FROG OVER HERE
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

    centered "Calender pops up"
    centered "Tuesday October 27"
    centered "Deadline in 4 days"

    m "Oh! Oh dear. That's NOT a smidge."
    d "This is chickeneyed!"
    a "A-ahh ahh! Let's- let's calm down guys! {i}Wait uhm okay—{/i} I hear you, I see you, and I understand your concerns—"
    d "No offense, you don't understand anything."
    a "AaaAAahh... sorry—" 
    d "I just said no offense. This is not offensive, I am helping you..."
    b "Four days isn't enough time to do ANYTHING!"
    d "Yeah, what he said."
    a "Ough... sorrsies..." 
    m "It's no problem; I can pick up all the slack." 
    b "I don't think that's going to be enough! Four days?" 
    a "I-I know this is terrible! But we made a lot of progress yesterday, right? And today?" 
    m "Hm... 'a lot' if the deadline was in over 30 days. Which it used to be." 
    k "I-I have a question. If we end up having to work overtime to finish the project, are we... getting paid for it?" 
    a "I tried, I really really tried to negotiate with the higher ups about it, but they still said no." 
    a "It's a full turn key contract- so we only get any bonuses if we finish the product in a way that's satisfying enough for the clients, and they, uh, feel like giving the employees bonuses!" 
    a "So, so maybe if we work hard enough? And do really really well?"
    m "You heard her, though. We {i} could{/i} get a bonus by the end."
    b "But no guaranteed overtime."
    k "Oh... I see. That's- that's too bad! I-I... am I still doing all this work?" 
    a "I... I don't know, Kendra..." 
    m "It seems like we're about to get even more work, unfortunately."
    k "Haha... hah! No... no breaks for me, I guess!"
    k "I-I should... ooohhh... oh god I'm so... I feel like my head is going to explode!"

    b "K-Kendra? Are you okay? Maybe you should head to the clinic—"
    k "{b}NO. IT'S... FINE. I WILL BE FINE.{/b}"
    k "{b}I... I need to get back to work.{/b}"

# kendra leave? 

    a "... Oh death... I-I— I should..."
    b "It's fine, I'll... check up on her."

# OVERWORLD TIME (outside manager room)
# THUD THUD THUD
# CRASH
# (kendra banging her head on the computer then breaking the screen)
# kendra groaning 
label kendragobrr:
#VA note: Kendra is wailing and groaning about her head hurting. She sounds more angry at herself than in pain. 

k "{b}My head... it- my head hurts.{/b}"
b "K-Kendra? Is... everything okay? What's that noise...?!"
k "{b}It needs to stop.{/b}"

#IF POSSIBLE ONLY IDK there's a sickening THUD each time Kendra talks

k "{b}I Need.{/b}"
#THUD
k "{b}To.{/b}"
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


