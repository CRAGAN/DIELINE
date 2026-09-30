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
    
    
    jump room5
label room5:
    scene black
    pause 2
    call screen rooms5 with fade
# Not yet transformed fully but hints she's in the process
label apolloweirdtime:

    $ quick_menu = True
    b "Uhh, hiya Apollo...! Sorry for sleeping—"
    scene managerroom 
    show overlay:
        blend 'multiply'
    show black:
        blend 'multiply' alpha 0.2
    show blue:
        blend 'multiply' alpha 0.3

    show apo nervoust at jumper, center
    voice "audio/Apollo/Day 5/apollo_line138.mp3"
    a "BARBYYY! OH MY DEATH, YOU’RE AWAKEEE! I’M SO HAPPY, HAHAHA!"
    voice "audio/Apollo/Day 5/apollo_line139.mp3"
    a "Oh goodness... I’m so very sorry Barby!! You must’ve been utterly exhausted, working nonstop like that?! It’s GOOD you slept. I... I truly wouldn’t know what to do with myself if you..."
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line289.wav"
    show apo nervous
    b "Apollo..."
    voice "audio/Apollo/Day 5/apollo_line140.mp3"
    show apo weirdt
    a "I-I couldn’t have pushed you any harder than I already have, hahaha— {i}{b}I’m such a bad manager.{/i}{/b} I’m so sorry... I’ll be better, I promise." 
    voice "audio/Apollo/Day 5/apollo_line141.mp3"
    show apo feart
    a "{i}You forgive me... right?{/i}"
    voice "audio/Apollo/Day 5/apollo_line142.mp3"
    show apo nervoust at shaking, center, up
    a "Hahaha, you believe me, Barby — right? Right right right right right right RIGHT RIGHT RIGHT—!!" 
    #K  inda want that textbox scary thing where everything is going crazy and the text is flying out of the text box at the end
    # would be cool if you could cut it out auto skip to next line after voiceline	
    show apo nervous at downward
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line290.wav"
    b "Y-YES! Yes, Apollo, I do, I swear—!! Hah, uhh— actually, i-it’s the last day, I should go do my usual rounds—"
    voice "audio/Apollo/Day 5/apollo_line143.mp3"
    show apo awkwardt
    a "Oh, but you know, they haven’t exactly been feeling their best either... so down in the dumps, the poor things." 
    voice "audio/Apollo/Day 5/apollo_line144.mp3"
    a "I just feel like we’re not really... connecting. As a team. Right now."
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line291.wav"
    show apo awkward
    b "O-oh, I see.. Well, you can leave the bonding to me, I’ll bridge the—"
    voice "audio/Apollo/Day 5/apollo_line146.mp3"
    show apo nervoust at jumper
    a "Ahaha, you know what? Maybe I’LL do it this time! Yes— maybe I can be the one to encourage them to cross the finish line! It IS my job afterall. My responsibility, as their manager!"
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line292.wav"
    show apo nervous
    b "...Are you sure? Have you slept at all since—"
    voice "audio/Apollo/Day 5/apollo_line147.mp3"
    show apo nervoust
    a "Haha, of course, of course! They probably just need a little morale boost, that's all!! I can raise their spirits... Hahaha—"
    show apo nervous
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line293.wav"
    b "I-I mean I can still handle that...! I’ve been doing it since the start!" 
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line294.wav"
    b "Listen— you look kind of stressed. Do you need anything? I could get you coffee! Or, or handle some of your work, even—"
    voice "audio/Apollo/Day 5/apollo_line148.mp3"
    show apo fear at forward
    show black:
        easein 5 alpha 0.8
    a "{sc=2}B   a  r R   b    Y."
    # CAN THIS TEXT SHAKE AND FLOAT – maybe put it around the screen instead of on the text box
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line295.wav"
    b "...!!!"
    show apo nervoust at downward
    voice "audio/Apollo/Day 5/apollo_line149.mp3"
    a "Haha sorry, that came out wrong... Barby, can you go do your little minigames?"
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line296.wav"
    b "... M-my what?"
    voice "audio/Apollo/Day 5/apollo_line150.mp3"
    a "Silly billy! Your computer things! Your beep-boop-beep things, the ones you do everyday, haha!"
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line297.wav"
    b "Oh! I... my emails? Y-yes, of course, I can do that—"
    scene black
    voice "audio/Apollo/Day 5/apollo_line151.mp3"
    a "Perfect! Off you go, my favorite assistant manager!"
    
    # barby wants to pipe up but awkwardly leaves the room
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line298.wav"
    b "...What was THAT?! Gosh. Apollo, she seems so..."
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line299.wav"
    b "..."
    scene room_1
    
    
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line300.wav"
    b "...The sooner we finish this project, the sooner things can get better."
    jump minigameday5
label minigameday5:
    jump breaktimeday5

label breaktimeday5:
    $ quick_menu = False
    show black:
        alpha 0.3
        easein 0.5 alpha 0.6
    pause 0.9
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line301.wav"
    b "H-huh?!"
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line302.wav"
    b "..."
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line303.wav"
    b "I’d better go check on everyone." 
    # Lights are off, overworld time
    scene room_2
    show borders

    show black:
        alpha 0.8
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line304.wav"
    b "Is everyone okay...?"
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line305.wav"
    b "Hello...?"
    scene room_3
    show borders1
    show black:
        alpha 0.9
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line306.wav"
    b "Can somebody fix the power...? The deadline’s so close, we need to—"
    #sfx_(dark)walk
    # walk in dark sounds are scary 
    
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line307.wav"
    b "...Hello?"
    # click around and no one's there 
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line308.wav"
    b "Apollo said she'd be... boosting team morale. Maybe they're all in the breakroom."
    #sfx_doorcreak
    scene black
    pause 2 
    # open breakroom 
    # apollo, only silhouette with faint outline of normal sprite 
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line309.wav"
    b "Apollo...?"
    scene room_4
    show black:
        alpha 0.95
    pause 2.0
    show deez monstershadow:
        alpha 0.0
    show kendra monstershadow:
        alpha 0.0
    show mj monstershadow:
        alpha 0.0
    show apo boot at center
    #sfx_/or ambiance? maybe there can be like (like in walten files theres that creepy long static sound? It sounds like an AC/some machine running)
    # all her dialogue is floating text, not in text box
    voice "audio/Apollo/Day 5/apollo_line152.mp3"
    a_sub "Hmm? Oh, Barby! Hahaha, gosh, what a predicament. It's so dark in here I almost missed you! I missed you. I really did... Thank the stars you’re here."
    # talking about something important
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line310.wav"
    b_sub "Huh? I-I... I missed you too?? A-anyway, we need to fix the power... we can’t get anything done like this! We’re SO close to the deadline, we can’t fall behind now."
    voice "audio/Apollo/Day 5/apollo_line153.mp3"
    a_sub "Oh, hahaha! You’re so right, Barby! So smart! We should fix it, we CAN fix it! We won’t let a teeny tiny power outage get us down, Haha!"
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line311.wav"
    b_sub "R-right! So..."
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line312.wav"
    b_sub "We should tell the others about this..." 
    voice "audio/Apollo/Day 5/apollo_line154.mp3"
    a_sub "Aha... ahahaha!"
    voice "audio/Apollo/Day 5/apollo_line155.mp3"
    a_sub "Hahaha! You’re so silly, Barby." 
    # music stop
    voice "audio/Apollo/Day 5/apollo_line156.mp3"
    
    show deez monstershadow at center:
        alpha 0.0 xoffset -500
        easein 3 alpha 0.8
    show kendra monstershadow:
        alpha 0.0  xoffset 500
        easein 2 alpha 0.8
    show mj monstershadow at center:
        alpha 0.0 
        easein 4 alpha 0.8
    a_sub "We’re all here."
    voice "audio/Apollo/Day 5/apollo_line157.mp3"
    a_sub "This IS a team meeting."
    
    # Lights On
    jump lightson

label lightson:
    voice "audio/Apollo/Day 5/apollo_line158.mp3"
    a "... Oh. What’s with that face? Why do you look so—"
    voice "audio/Apollo/Day 5/apollo_line159.mp3"
    a "No. Haha, you don’t look too good. That’s unfortunate. I’m sorry."
    # Sooooo much work 
    voice "audio/Apollo/Day 5/apollo_line160.mp3"
    a "I’m so, so sorry you have to do so much work."
    voice "audio/Apollo/Day 5/apollo_line161.mp3"
    a "You look like—"
    voice "audio/Apollo/Day 5/apollo_line162.mp3"
    a "..."

# apollo pauses for a while
    voice "audio/Apollo/Day 5/apollo_line163.mp3"
    a "You know..."
    voice "audio/Apollo/Day 5/apollo_line164.mp3"
    a "You look like you need some help. Hahaha... why don’t you open up to the team?"
    # very very slow quicktime
    menu:
        "[Yes...] N O !!!": #← text shakes like crazy
            # like, the player would select "yes" but it’s weird and shaky and swaps to "no" 
            voice "audio/Barby/Barby_Day5_ApolloChase/barby_line313.wav"
            b "NO! NO, NO, NO! I DON’T!"
            # VA note: like fighting off the thought of opening up despite desperately needing support
            voice "audio/Barby/Barby_Day5_ApolloChase/barby_line314.wav"
            b "Please. I don’t."
        "[No.]":
            #VA note: hushed, under breath, horrified but trying to keep voice steady
            voice "audio/Barby/Barby_Day5_ApolloChase/barby_line315.wav"
            b "I don’t need anything right now."
            # continuing ^^ but faltering closer to the end
            voice "audio/Barby/Barby_Day5_ApolloChase/barby_line316.wav"
            b "Maybe later. We don’t have much time. Sorry—"
        "[Run out of time]":
            voice "audio/Barby/Barby_Day5_ApolloChase/barby_line317.wav"
            b "I... I—"
            voice "audio/Apollo/Day 5/apollo_line165.mp3"
            a "Shh, shh, it’s okay, Barby. You just need a great big hug..."
            #DEATH SCREEN (black screen core, save the jumpscare for actual chase) 
            # you slowly step out of the room
            #sfx_slowstep
    voice "audio/Apollo/Day 5/apollo_line166.mp3"
    a "Where... where are you going?"
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line318.wav"
    b "I just... I need to take a break."
    
    # slam door closed
    # Apollo’s voice is more muffled now (sfx)
    #sfx_doorslam
    voice "audio/Apollo/Day 5/apollo_line167.mp3"
    a "Hahaha, oh, you’re so funny, Barby! The breakroom’s RIGHT here, you frazzled little ol’ scatterbrain! Take a break with {b}US{/b}!" 
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line319.wav"
    b " I THOUGHT THAT WAS A TEAM MEETING!?!?!?"
    voice "audio/Apollo/Day 5/apollo_line168.mp3"
    a "Haha! Team meetings ARE breaks— from being aloneeee!!"
    voice "audio/Apollo/Day 5/apollo_line169.mp3"
    a "C’mon, you don’t want to be alone, do you? That’s not very nice of you, Barby. Didn’t you say teamwork makes the dream work?"
    voice "audio/Apollo/Day 5/apollo_line169.mp3"
    a "{b}{i}So why aren’t you cooperating with me?{/b}{/i}" 
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line320.wav"
    b "{i}Ah...{/i}"
    voice "audio/Apollo/Day 5/apollo_line170.mp3"
    a "Why...? Why why why WHY WHY WHY WHY?! COME BACK, BARBY! COME BACK, COME BACK, COME BACK!!!" 
    
    #  put banging of door with voiceline
    # loop banging door while waiting for player response
    menu loop:
        set picked
        "Take a Break":
            voice "audio/Barby/Barby_Day5_ApolloChase/barby_line321.wav"
            b "I'm taking a break!!"
            voice "audio/Apollo/Day 5/apollo_line171.mp3"
            a "Hahahahaaa!"
            #VA note: wrong way said singsong
            voice "audio/Apollo/Day 5/apollo_line172.mp3"
            a "Ohhh Barby-warby, wrong way!"
            voice "audio/Apollo/Day 5/apollo_line173.mp3"
            a "Let’s have a break together! Hahaha!"
            jump loop
            # back to choice menu (only Keep working left)
            
        "Keep working":
            voice "audio/Barby/Barby_Day5_ApolloChase/barby_line322.wav"
            b "Y-you said we needed to stay positive and keep working!! I-I already took my break, remember?! I slept in! THAT was my break! I'm gonna—! I have to get back to work!!"
            # pause between lines
            voice "audio/Apollo/Day 5/apollo_line174.mp3"
            a "..."
            voice "audio/Apollo/Day 5/apollo_line175.mp3"
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
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line323.wav"
    b "Hah... hah..."
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line324.wav"
    b "..."

    # barby hum the melody that MJ was playing
    # At some point when the lights flickers on and off again, a split second of # something horrifying in the mirror
    # Barby goes AHH!! 
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line325.wav"
    b "AAAHH!!"

    # Lights go back on
    #sfx_lighton
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line326.wav"
    b "Hah... Oh, I’m just... tired."

    # And THEN lights on, the door sound effect plays
    # So you can peek away from the bathroom to see apollo (AND CO.) standing outside the breakroom door

    #sfx_apollomonsterwalk
    #VA Apollo: I want to see Apollo do a take of this line below sing songy👀 
    voice "audio/Apollo/Day 5/apollo_line176.mp3"
    a "Barby? Where are you? Oh dear... I don’t see you in your cubicle."
    voice "audio/Apollo/Day 5/apollo_line177.mp3"
    a "Have you... have you lost motivation? HAHA—It's okay, we're here for you. Maybe if we work together, you'll feel more efficient."
    voice "audio/Apollo/Day 5/apollo_line178.mp3"
    a "Hahaha, yes... it's time. It's time for us to join you—"

    # maybe it can be like

    t "{b}AND GET BACK TO WORK.{/b}"

    #Scary chase music starts here
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line327.wav"
    b "I... I don't need the help... I think I can handle it."

    # All at the same time/same voiceline?
    # in editing (for Cole): reverse reverb 
    voice "audio/Apollo/Day 5/apollo_line179.mp3"
    a "Your help means so much."
    d "You always believe in me."
    k "You make the work easier to handle."
    m "Haha. I guess you won in the end." 

    t "{b}I   t’ S  t im  E  Fo  r   US  t o    g iV e   b  A   C k .{/b}" 

    # make them speak all out of sync
    voice "audio/Apollo/Day 5/apollo_line180.mp3"
    a "Hihihi, Let's start with a BIIIIG hug!" 

    #Apollo’s arms wide open, you can see all the other coworkers

    t "{b}Thank you, Barby{/b}" 
    t "{b}Thank you for everything.{/b}"
    # said at the same time
    # CUT. BLACK.
    # chase
    jump chase

label chase:
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line328.wav"
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line328.wav"
    b "I don’t want a hug."
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line329.wav"
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
    voice "audio/Apollo/Day 5/apollo_line181.mp3"
    a "IM SORRY! I'M SORRY FOR MAKING YOU DO SO MUCH WORK!"
    k "STOP IT, PLEASE! LET ME IN, LET ME DO THE WORK! LET ME DO MY JOB!" 
    m "LET. ME. FINISH. MY WORK!! LET IT BE DONE, LET IT BE OVER, PLEASE, PLEASE, PLEASE, LET IT END!"
    d "I CAN DO IT!!! I CAN DO IT!! I’M GOOD! I'M GOOD!!! TELL ME I’M GOOD ENOUGH!"

    menu:
        "It’s okay it’s okay!":
            # WRONG!!! WRONGGG ANSWER
            voice "audio/Apollo/Day 5/apollo_line182.mp3"
            a "IT'S NOT OKAY! IT'S NOT, IT'S NOT!! LET ME MAKE IT OKAY!! I’M BEGGING YOU, PLEASE!!"
# return to dialogue
        "STOP!":
            voice "audio/Barby/Barby_Day5_ApolloChase/barby_line330.wav"
            b "I’VE SET MY BOUNDARIES! DON’T FUCKING BREAK THEM! LEAVE ME THE FUCK ALONE! I NEED MY GODDAMN SPACE. I DON’T WANT A HUG. I DON’T!!"
# pause. Sound effects die down. Everything goes quiet again except Apollo’s voice

#VA note: Apollo starts crying, like make this sooo wet cat pathetic  
    voice "audio/Apollo/Day 5/apollo_line183.mp3"
    a "..."
    voice "audio/Apollo/Day 5/apollo_line184.mp3"
    a "I’m sorry... I’m so, so so sorry... please forgive me, Barby..."
    voice "audio/Apollo/Day 5/apollo_line185.mp3"
    a "I’ll... I’ll leave you alone..."  
    jump pcminigame
# Stops knocking
# silence

label pcminigame:
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line331.wav"
    b "Apollo? Are you still there?"

# silence VERY LONG
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line332.wav"
    b "Apollo?"
    voice "audio/Apollo/Day 5/apollo_line186.mp3"
    a "... please, don’t give up on me."
    voice "audio/Apollo/Day 5/apollo_line187.mp3"
    a "Not you, too..."
    voice "audio/Apollo/Day 5/apollo_line188.mp3"
    a "You’re... you’re the only family I’ve got, now..."
    jump clockingout
label clockingoutend:
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line333.wav"
    b "I did it."
    voice "audio/Barby/Barby_Day5_ApolloChase/barby_line334.wav"
    b "...We’re done."  