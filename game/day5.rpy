label day5:
    scene black
    pause 2.0

    scene room_2
    show borders
 
    centered "October 30, Friday"
    centered "1 day left."
    #if you click anyone a second time barby goes "..."
    #sfx_dooropen
    #Managers room
    # cutscene plays, doesnt need to be voice acted, but could be
    #b "Uhh, hiya Apollo...! Sorry for sleeping—"
    # a "BARBYYY! OH MY DEATH, YOU’RE AWAKEEE! I’M SO HAPPY, HAHAHA!"
    jump room5
label room5:
    scene black
    pause 2
    call screen rooms5 with fade
# Not yet transformed fully but hints she's in the process
label apolloweirdtime:
    a "Oh goodness... I’m so very sorry Barby!! You must’ve been utterly exhausted, working nonstop like that?! It’s GOOD you slept. I... I truly wouldn’t know what to do with myself if you..."
    b "Apollo..."
    a "I-I couldn’t have pushed you any harder than I already have, hahaha— {i}{b}I’m such a bad manager.{/i}{/b} I’m so sorry... I’ll be better, I promise." 
    a "{i}You forgive me... right?{/i}"
    a "Hahaha, you believe me, Barby — right? Right right right right right right RIGHT RIGHT RIGHT—!!" 
    #K  inda want that textbox scary thing where everything is going crazy and the text is flying out of the text box at the end
    # would be cool if you could cut it out auto skip to next line after voiceline	
    b "Y-YES! Yes, Apollo, I do, I swear—!! Hah, uhh— actually, i-it’s the last day, I should go do my usual rounds—"
    a "Oh, but you know, they haven’t exactly been feeling their best either... so down in the dumps, the poor things." 
    a "I just feel like we’re not really... connecting. As a team. Right now."
    b "O-oh, I see.. Well, you can leave the bonding to me, I’ll bridge the—"
    a "Ahaha, you know what? Maybe I’LL do it this time! Yes— maybe I can be the one to encourage them to cross the finish line! It IS my job afterall. My responsibility, as their manager!"
    b "...Are you sure? Have you slept at all since—"
    a "Haha, of course, of course! They probably just need a little morale boost, that’s all!! I can raise their spirits... Hahaha—"
    b "I-I mean I can still handle that...! I’ve been doing it since the start!" 
    b "Listen— you look kind of stressed. Do you need anything? I could get you coffee! Or, or handle some of your work, even—"
    a "{b}B   a  r R   b    Y.{/b}"
    # CAN THIS TEXT SHAKE AND FLOAT – maybe put it around the screen instead of on the text box
    b "...!!!"
    a "Haha sorry, that came out wrong... Barby, can you go do your little minigames?"
    b "... M-my what?"
    a "Silly billy! Your computer things! Your beep-boop-beep things, the ones you do everyday, haha!"
    b "Oh! I... my emails? Y-yes, of course, I can do that—"
    a "Perfect! Off you go, my favorite assistant manager!"
    
    # barby wants to pipe up but awkwardly leaves the room

    b "...What was THAT?! Gosh. Apollo, she seems so..."
    b "..."
    b "...The sooner we finish this project, the sooner things can get better."
    jump minigameday5
label minigameday5:
    jump breaktimeday5

label breaktimeday5:
    b "H-huh?!"
    b "..."
    b "I’d better go check on everyone." 
    # Lights are off, overworld time

    b "Is everyone okay...?"
    b "Hello...?"
    b "Can somebody fix the power...? The deadline’s so close, we need to—"
    #sfx_(dark)walk
    # walk in dark sounds are scary 
    
    b "...Hello?"
    # click around and no one's there 

    b "Apollo said she'd be... boosting team morale. Maybe they're all in the breakroom."
    #sfx_doorcreak
    # open breakroom 
    # apollo, only silhouette with faint outline of normal sprite 

    b "Apollo...?"
    #sfx_/or ambiance? maybe there can be like (like in walten files theres that creepy long static sound? It sounds like an AC/some machine running)
    # all her dialogue is floating text, not in text box
    a "Hmm? Oh, Barby! Hahaha, gosh, what a predicament. It's so dark in here I almost missed you! I missed you. I really did... Thank the stars you’re here."
    # talking about something important

    b "Huh? I-I... I missed you too?? A-anyway, we need to fix the power... we can’t get anything done like this! We’re SO close to the deadline, we can’t fall behind now."
    a "Oh, hahaha! You’re so right, Barby! So smart! We should fix it, we CAN fix it! We won’t let a teeny tiny power outage get us down, Haha!"
    b "R-right! So..."
    b "We should tell the others about this..." 
    a "Aha... ahahaha!"
    a "Hahaha! You’re so silly, Barby." 
    # music stop
    
    a "We’re all here."
    a "This IS a team meeting."
    #sfx_lighton
    # Lights On
    jump lightson

label lightson:
    a "... Oh. What’s with that face? Why do you look so—"
    a "No. Haha, you don’t look too good. That’s unfortunate. I’m sorry."
    # Sooooo much work 

    a "I’m so, so sorry you have to do so much work."
    a "You look like—"
    a "..."

# apollo pauses for a while

    a "You know..."
    a "You look like you need some help. Hahaha... why don’t you open up to the team?"
    # very very slow quicktime
    menu:
        "[Yes...] N O !!!": #← text shakes like crazy
            # like, the player would select "yes" but it’s weird and shaky and swaps to "no" 
            b "NO! NO, NO, NO! I DON’T!"
            # VA note: like fighting off the thought of opening up despite desperately needing support
            b "Please. I don’t."
        "[No.]":
            #VA note: hushed, under breath, horrified but trying to keep voice steady
            b "I don’t need anything right now."
            # continuing ^^ but faltering closer to the end
            b "Maybe later. We don’t have much time. Sorry—"
        "[Run out of time]":
            b "I... I—"
            a "Shh, shh, it’s okay, Barby. You just need a great big hug..."
            #DEATH SCREEN (black screen core, save the jumpscare for actual chase) 
            # you slowly step out of the room
            #sfx_slowstep

    a "Where... where are you going?"
    b "I just... I need to take a break."
    
    # slam door closed
    # Apollo’s voice is more muffled now (sfx)
    #sfx_doorslam

    a "Hahaha, oh, you’re so funny, Barby! The breakroom’s RIGHT here, you frazzled little ol’ scatterbrain! Take a break with {b}US{/b}!" 
    b " I THOUGHT THAT WAS A TEAM MEETING!?!?!?"
    a "Haha! Team meetings ARE breaks— from being aloneeee!!"
    a "C’mon, you don’t want to be alone, do you? That’s not very nice of you, Barby. Didn’t you say teamwork makes the dream work?"
    a "{b}{i}So why aren’t you cooperating with me?{/b}{/i}" 
    b "{i}Ah...{/i}"
    a "Why...? Why why why WHY WHY WHY WHY?! COME BACK, BARBY! COME BACK, COME BACK, COME BACK!!!" 
    
    #  put banging of door with voiceline
    # loop banging door while waiting for player response
    menu loop:
        set picked
        "Take a Break":
            b "I'm taking a break!!"
            a "Hahahahaaa!"
            #VA note: wrong way said singsong
            a "Ohhh Barby-warby, wrong way!"
            a "Let’s have a break together! Hahaha!"
            jump loop
            # back to choice menu (only Keep working left)
            
        "Keep working":
            b "Y-you said we needed to stay positive and keep working!! I-I already took my break, remember?! I slept in! THAT was my break! I'm gonna—! I have to get back to work!!"
            # pause between lines
            a "..."
            a "Okay! You’re right. You can go to work."
            jump prechase

label prechase:
    # let player do something before chase scene (timer) 
    # Rush in the bathroom? Stare in the mirror? 
    # Bathroom door you keep open
    #Mirror could have cracks because deez transformed in there
    # Maybe cracks of him almost breaking down too 
    # Like to show he’s on the brink
    # Lights are still flashing 
    # 1st person POV so blubur doesnt have to draw more for this darn day
    #sfx_lightflash
    #VA note: Heavy breathing
    b "Hah... hah..."
    b "..."

    # barby hum the melody that MJ was playing
    # At some point when the lights flickers on and off again, a split second of # something horrifying in the mirror
    # Barby goes AHH!! 

    b "AAAHH!!"

    # Lights go back on
    #sfx_lighton

    b "Hah... Oh, I’m just... tired."

    # And THEN lights on, the door sound effect plays
    # So you can peek away from the bathroom to see apollo (AND CO.) standing outside the breakroom door

    #sfx_apollomonsterwalk
    #VA Apollo: I want to see Apollo do a take of this line below sing songy👀 

    a "Barby? Where are you? Oh dear... I don’t see you in your cubicle."
    a "Have you... have you lost motivation? HAHA—It's okay, we're here for you. Maybe if we work together, you'll feel more efficient."
    a "Hahaha, yes... it's time. It's time for us to join you—"

    # maybe it can be like

    t "{b}AND GET BACK TO WORK.{/b}"

    #Scary chase music starts here

    b "I... I don't need the help... I think I can handle it."

    # All at the same time/same voiceline?
    # in editing (for Cole): reverse reverb 

    a "Your help means so much."
    d "You always believe in me."
    k "You make the work easier to handle."
    m "Haha. I guess you won in the end." 

    t "{b}I   t’ S  t im  E  Fo  r   US  t o    g iV e   b  A   C k .{/b}" 

    # make them speak all out of sync

    a "Hihihi, Let's start with a BIIIIG hug!" 

    #Apollo’s arms wide open, you can see all the other coworkers

    t "{b}Thank you, Barby{/b}" 
    t "{b}Thank you for everything.{/b}"
    # said at the same time
    # CUT. BLACK.
    # chase
    jump chase

label chase:
    b "I don’t want a hug."
    b "I DONT WANT A HUG!"    
    #Barby "AGHH" sound effect for when player succeed

    #sfx_apollomonstergrab
    #sfx_struggle
    #sfx_takeoffleg
    #sfx_throwleg
    #sfx_getup
    #sfx_crawl
    #sfx_hop
    #Apollo & co. grabs your prosthetic leg QuickTime choice
    #( in any scenario, failing is gonna be jumpscare and die)
# fight back, pull it away from them
# bad , harder QTE
# If success→ go to "Pull away from them choices)
# take it off
# Good, same pace QTE
# If success→ go to Take it off: you fall on the ground
# Pull away from them choices
# Click door next to u (get item to throw at them)
# QTE hard time It right to throw bucket at her
# Success-> keep running (forward and forward until next room)
# pull with raw force
# QTE hard super hard almost impossible
# Success → Take it off: you fall on the ground choices
# Take it off: you fall on the ground choices
# get up
# crawl
# Get up:
# hop (QuickTime event stressful)
# Crawl:
# QuickTime event stressful hard mode crazy insane multiple QTE click crawl as it appears on your screen 


# CLICK THE DOOR TO THE MANAGER ROOM
# MANAGER ROOM


# let the voices pile up all together, one big voiceline but the text flashing separately

    t "{b}OPEN THE DOOR!{/b}"
    t "{b}OPEN THE DOOR!!!{/b}"
    a "IM SORRY! I'M SORRY FOR MAKING YOU DO SO MUCH WORK!"
    k "STOP IT, PLEASE! LET ME IN, LET ME DO THE WORK! LET ME DO MY JOB!" 
    m "LET. ME. FINISH. MY WORK!! LET IT BE DONE, LET IT BE OVER, PLEASE, PLEASE, PLEASE, LET IT END!"
    d "I CAN DO IT!!! I CAN DO IT!! I’M GOOD! I'M GOOD!!! TELL ME I’M GOOD ENOUGH!"

    menu:
        "It’s okay it’s okay!":
            # WRONG!!! WRONGGG ANSWER
            a "IT'S NOT OKAY! IT'S NOT, IT'S NOT!! LET ME MAKE IT OKAY!! I’M BEGGING YOU, PLEASE!!"
# return to dialogue
        "STOP!":
            b "I’VE SET MY BOUNDARIES! DON’T FUCKING BREAK THEM! LEAVE ME THE FUCK ALONE! I NEED MY GODDAMN SPACE. I DON’T WANT A HUG. I DON’T!!"
# pause. Sound effects die down. Everything goes quiet again except Apollo’s voice

#VA note: Apollo starts crying, like make this sooo wet cat pathetic  
    a "..."
    a "I’m sorry... I’m so, so so sorry... please forgive me, Barby..."
    a "I’ll... I’ll leave you alone..."  
    jump pcminigame
# Stops knocking
# silence

label pcminigame:
    b "Apollo? Are you still there?"

# silence VERY LONG
    b "Apollo?"

    a "... please, don’t give up on me."
    a "Not you, too..."
    a "You’re... you’re the only family I’ve got, now..."
    jump clockingout
label clockingoutend:
    b "I did it."
    b "...We’re done."  