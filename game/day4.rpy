label day4:
    # CG Deez’ POV doorway manager office Barby shinji pose, Apollo on the ground (lying down on papers)
    scene room_1
    play music "audio/Music/Clock In.mp3" loop fadein 1
    show overlay:
        blend 'multiply'
    show apo worried at center:
        xoffset 250
    show de sad at center:
        xoffset -250
    $ quick_menu = True

    b "Oh, what are we going to do... what are we going to do..." 
    
    a "Ugh..."
    a "Ahaha, i-it’s fine! We can- we can work something out." 
    a "W-we kind of don’t have much to show, though..."
    b "Any progress is still progress, right?"
    a "Right! So surely that’s got to mean something to them."
    b "But what if it’s not enough? What if they ask for more?"
    a "Um, um, maybe we can say that–..."
    a "... Barby, honestly... a lot’s been going on... and I’ve just been—"
    d "I would say good morning, but it appears this morning is not very good."
    a "Oh my goodness Deez, I didn’t see you there! Hi!"
    b "Deez! Good morning!"
    show apo weirdt
    a "Ahaha, what do you mean? Me and Barby, we’re so normal this morning."
    show apo weird
    b "We are?"
    show apo defaultt
    a "Yes! So normal about the person they’re sending to check in on the project today."
    show apo default

    d "I am inclined to believe otherwise. It seems you both are worried?"
    b "It’s just. Y’know. How are we gonna talk to someone from the company about... whatever’s going on right now...!"
    a "I wanna just ask for help, yeah, but... if SFC finds out how far behind we are..."
    a "We might all... lose our jobs."
    b "Getting fired from SFC... sucks. Apparently, it destroys your resume... I hear it becomes a nightmare to get rehired for anything substantial." 
    a "Agh..."
    show de default
    d "If talking is the issue, then I can do it."
    b "Oh no, Deez, we couldn’t possibly pass this onto you. They’re probably going to ask lots of questions about the project, and we need someone who’s knowledgeable..." 
    show de shy
    d "Well yes, that’s me. I know a lot."
    d "And I’m, like, really good at talking to people."
    a "Really?"
    show de default
    d "Yeah. I was, like, doing network activities for my family’s business...going around talking... and yeah." 
    a "That’s wonderful! Oh Deez, you smart, smartie-pataatie, I’m so glad you’re with us."
    b "I guess Deez must’ve learned a lot from Kendra before she... yeah."
    a "... Well, let's just check around before they arrive. Especially on... ahaha, you know."
    jump officewalkday4
label minigame4:
    #FROGGG HERE
    $ delete_all()
    $ add_message("Failure to Deliver (Incomplete Address)", "mailer-daemon@serafim.co", "Whoops! It looks like your e-mail could not be sent. We are terribly sorry for the inconvenience.\n\nDNS Error: NullDomain | Submitted recipient address does not contain a complete domain name. Please correct this before reattempting to send an email.\n\nTo: M@r!an W□₹d\nSubject: This has never happened to me before.\n\nHey, dude. So I don't know what to say. I followed my herald letter to you to, ya know, collect my dues, only to discover someone's already beat me to it. I genuinely don't know what to do?? I guess you're safe, bro. Congrats? This is basically unfinished business now, so that sucks. Let me know if you can think of some other way for me to collect, I guess.\n\nWishing you terror, Marian.", "del")
    $ add_message("nw brnddwal.", "carsen@notbusinessemail.com", "svjhb,;", "del")
    $ add_message("Disputing Any Disputes on the Nature of Disputes", "sfc.higherup42@serafim.co", "The company seeks to rectify a consistent situation within the departments on the functional nature of a consideration taken over the course of multiple days into a consequential state that exists over the discussional ability of our workers. Please submit the proper A12 form in correlation to subsection B on former point 36 paragraph C, noting that this is a required survey. Please send your immediate response by November 17th.\n\nFrom the pearly gates above,\nSera, Fim & Co. Higher Up 42\n--------------\n{i}Reply from You:{/i}\nHiya!\n\nRespectfully, may I ask for clarification?\n\nYour professional pal,\nFredrick \"Barby\" Ibarra\n--------------\n{i}Reply from sfc.higherup42@serafim.co:{/i}\nNo. Now submit your form or be subject to permanent {b}exposure{/b} upon the end of the deadline.\n\nFrom the pearly gates above,\nSera, Fim & Co. Higher Up 42", "acc")
    $ add_message("Reminder of Shipment", "popik@cock.com", "In order to properly bring forth this groundbreaking discovery, we must make sure everything is in place for the proper rite of the second form. Have the metal pipes been delivered yet in order to outfit the main existence of the vessel, such that our darkness may be purged and our infinite possibilities satisfied by the existence of this project.\n\nThe best client,\nPopikcock\n--------------\n{i}Reply from You:{/i}\nHiya, Client!\nYes. We got the metal pipes..\n\nYour professional pal,\nFredrick \"Barby\" Ibarra", "acc")

    call screen email_minigame

    voice "audio/Barby/Day 4 Encounter/barby_line228.mp3"
    stop music
    b "I'll leave my PC on. I’m just gonna check on the. Thing. Then I'll get back to see if there’s any other work before I go."
    jump guymeeting

label guymeeting:
    play music "audio/Music/Breaktime/Breaktime Draft 3_Variation 4.mp3" loop fadein 1
    scene room_3
    show borders1
    show overlay:
        blend 'multiply'
    show ry default at center:
        xoffset -250
    show de shy at center:
        xoffset 250
    with fade
    r "Hey man, no worries about being a mess, I get it y'know, I heard the deadline got moved earlier and, man that’s gotta suck."
    r "It's happened to me before. God... corporate hellscape. It never ends."
    show de shyt
    d "Haha yeah. But we’re totally doing fine though. Don't worry, haha."
    r "Instead of laughing, you keep saying ‘haha’ out lou—"
    b "Hiya—"
    show de feart at jumper, shaking
    d "OH THANK GOD YOU’RE HERE I NEED TO TAKE A MASSIVE SHIT." 
    # sprite tween run to bathroom and vanish
    # close door sfx
    show de fear:
        easein 0.5 xoffset 1400

    b "Wha-"
    show ry default at center:
        easein 0.5 xoffset 0
    r "Oh damn he needed to go? He could've just said so. Anyway what’s up, man?"
    voice "audio/Barby/Day 4 Encounter/barby_line231.mp3"
    b "Well, I was, uh, just checking in, but."
    $ whichdep = False
    $ doyoujob = False
    $ howeverything = False
    while not (whichdep and doyoujob and howeverything):
        menu:
            "Which department are you from?" if  not whichdep:
                $ whichdep = True
                b "Which department are you from, again?"
                show ry sexy
                r "Oh, I’m just a warehouse guy. They sent me in to check on you guys because you haven’t sent the go ahead."
                b "A-ah! That's just because we don't need them! We're doing all fine on our own."
                r "That’s. What? Not how it works?"
                b "Crap. Crap. No I’m joking, this is a joke."
                b "Yeah, no, like Apollo said, we’ll give the go ahead soon! Prommy."
                r "Sure, mann."
                
            "Do you know what our job is" if not doyoujob:
                $ doyoujob = True
                show ry shy
                r "Shouldn't you guys know that?"
                b "WE KNOW DON’T WORRY. I was just curious if they told you anything, haha."
                r "Sure, mann."
                
            "How is everything" if not howeverything:
                $ howeverything = True
                show ry default
                r "Well, it kind of looks like you guys have it handled? Your coworker only showed me this hallway and the breakroom, though."
                r "I’m just a little worried about your manager and the guy I was talking to."
                r "They, uh. Seemed kind of... Off?"
                b "Oh, they're just a little sleep deprived and tired after, y’know everything."
                b "It happens, you know... unfortunate as it is."
                show ry angry
                r "Mann. That’s not how that. Works."
                r "You know, you clock out, then get sleep, then clock back in the next day??"
                r "It’s just a job, bro."
                show ry shy
                b ". . ."
                b "Ok."
    
    r "Oh by the way, I was just curious, where are the rest of you guys? I thought there were more of you."
    b "Oh they're, you know, working really hard right now! Too busy to come out, haha."
    b "Everyone here has been giving it their all to reach the deadline." 
    r "Wow, that's so cool. You guys are pretty admirable, working through the time crunch. They should give you a raise or something after this." 
    b "We do our best!"
    r "But you know, it's probably still pretty tough chasing after a deadline. You guys can ask for help if you need it."
    menu:
        "Yes":
            b "Yes!"
            r "Cool, I’ll let them kno-"
            b "Is what I would say if we needed help, which we don’t!"
            r "Ok...?"
            jump continued
            #continue
        "No":
            voice "audio/Barby/Day 4 Encounter/barby_line246.mp3"
            b "Thank you, but we’re good!"
            r "Sure, mann."
            jump continued
#continue
label continued:
    r "Alright, I think you guys got it handled. I don’t doubt you guys or anything."
    r "But we really need to ship out soon. So, if you can at least send a demo to corporate so we can start working."
    r "Also, really, let us know if you need any help; we’re not doing anything at the moment."
    voice "audio/Barby/Day 4 Encounter/barby_line247.mp3"
    b "Yeah. Will do, man."
    voice "audio/Barby/Day 4 Encounter/barby_line248.mp3"
    b "Thanks a lot."
    r "‘Sure, mann."
    r "Contact if ya need anything."
    # elevator ding 
    # audience cheer as he leaves 
    jump breaktime4
label encounter4:
    $ quick_menu = False
    scene deezscene1:
        zoom 1.2 xoffset -50
    show barby_standing_back at center:
        zoom 0.55
    with fade
    #Click bathroom door
    # not VA'd except screams and groans from Deez
    voice "audio/Barby/Day 4 Encounter/barby_line249.mp3"
    b_sub "Hey, Deez? Are you in there?"
    # knock
    voice "audio/Barby/Day 4 Encounter/barby_line250.mp3"
    b_sub "Daniel?"
    # groans and oahh

    voice "audio/Deez/Day 4/deez_groan1.mp3"
    d_sub "Fine. Just fine. I just- aghhh..."
    voice "audio/Deez/Day 4/Bathroom/deez_groan2.mp3"
    d_sub "Taking a massive shit."
    voice "audio/Barby/Day 4 Encounter/barby_line251.mp3"
    b_sub "O-oh..."
    voice "audio/Barby/Day 4 Encounter/barby_line252.mp3"
    b_sub "Y-yeah, why do they call it a {i}rest{/i} room, you're fighting for your life in there."
    # sfx bad joke but cut it off Barby talking
    voice "audio/Barby/Day 4 Encounter/barby_line253.mp3"
    b_sub "That was so bad, sorry."
    voice "audio/Deez/Day 4/Bathroom/deez_groan3.mp3"
    d_sub "Ughh..."
    voice "audio/Barby/Day 4 Encounter/barby_line254.mp3"
    b_sub "Sorry..."
    d_sub "No... don't sorry... I'm just..."
    voice "audio/Deez/Day 4/Bathroom/deez_groan4.mp3"
    d_sub "AGH." with hpunch
    stop music
    # Deez make a few groans before AGHHHH AHHHHHH (his head splits open) but it could be mistaken for a really bad sht , but the sfx is fcking scary and the static stops
    voice "audio/Barby/Day 4 Encounter/barby_line255.mp3"
    b_sub "ARE YOU OKAY!?"
    # silence. Not even static
    # silence 
    centered "{nw=3.7} "
  
    # silence  6.7 sec
    hide barby_standing_back
    show shock at left:
        zoom 0.55 xoffset 300
    show deezle1 at center:
        zoom 0.65
    with vpunch
    centered "{nw=6} "
    # door opens. Deez is standing there staring front
    # staring. Silence 6.7 sec
    # silence.
    
    d_sub "Normal."
    call screen hallwaysdeez

label breakroom4:
    play music "audio/Music/Ominous Background Music.mp3" loop 
    scene room_4
    show overlay:
        blend 'multiply' alpha 0.3
    show blue:
        blend 'multiply' alpha 0.3
        easein 1 alpha 0.7
    show pink:
        blend 'multiply' alpha 0.3
        easein 1 alpha 0.7
    show de sad at up, center
    with fade
    # CG has u looking down at deez knelt next to [anythjbg] trying to fix it maybe his face is obscured 
    #And the hand is holding his head together
    menu:
        "Calmly ask him to stop":
            # Bad option
            voice "audio/Barby/Day 4 Encounter/barby_line221b.mp3"
            b "Please... you can stop."
            show de sadt
            voice "audio/Deez/Day 4/deez_line077.mp3"
            d "... Stop what."
            show de sad
            voice "audio/Barby/Day 4 Encounter/barby_line222.mp3"
            b "You don't have to fix it."
            voice "audio/Barby/Day 4 Encounter/barby_line223.mp3"
            b "It's... clear it's making it hard for you..."
            # sad
            show de sadt
            voice "audio/Deez/Day 4/deez_line078.mp3"
            d "You think I can't do it. You {i}always{/i} think I can’t do it."
            show de sad
            voice "audio/Barby/Day 4 Encounter/barby_line224.mp3"
            b "I... I think you should stop trying."
            hide de sad
            show deez back at up, center, shaking:
                zoom 0.8 ypos 1.1
            
            d ". . .stop trying? STOP TRYING? STOP TRYING???"
            
            voice "audio/Barby/Day 4 Encounter/barby_line225.mp3"
            b "Like. That you should take a break."
            
            d "take a break? take a break, TAKE A BREAK, TAKE A BREAK, TAKE A BREAK? TAKE A BREAK???"
            $ quick_menu = False
            scene black
            pause 2
            show de monstert at shaking, center:
                zoom 2 yoffset 600 xoffset -100
            show noises:
                alpha 0.1
                blend 'add'
            with vpunch
            pause 2
            scene black
            centered " "

            jump breakroom4
            #hand jumpscare
            # sfx jumpscare
            # he Kils u make some freaky noise go have fun

        "Encourage & console":

            # (MEAN IT!! MEAN IT!! GO ECCHAN)  SOUND SO GENUINE THAT HE CRIES
            voice "audio/Barby/Day 4 Encounter/barby_line226.mp3"
            b "You're doing a really good job and I'm proud of you." 
            # pause then sob semi long
            show de sadt
            d ". . . proud of me... proud of me..."
            hide de sadt
            show deez back at up, center, shaking:
                zoom 0.8  ypos 1.1

            voice "audio/Deez/Day 4/deez_line082.mp3"
            d "sobs"
            # do some sob speaking with like im about to choke vibes, whining ? but make it real
            voice "audio/Deez/Day 4/deez_line083.mp3"
            d "Barby...I’m just so stupid."
            voice "audio/Deez/Day 4/deez_line084.mp3"
            d "What the heck am I doing?"
            voice "audio/Deez/Day 4/deez_line085.mp3"
            d "What am  I even...trying to do anymore?"
            voice "audio/Barby/Day 4 Encounter/barby_line227.mp3"
            b "... Oh, man..."
            voice "audio/Deez/Day 4/deez_line086.mp3"
            d "Everyone says 'grow up', but no one ever says how."
            voice "audio/Deez/Day 4/deez_line087.mp3"
            d "Everyone looks like they have it easy- like they all have it figured out!"
            voice "audio/Deez/Day 4/deez_line088.mp3"
            d "Nobody questions anything. Nobody even asks questions."
            voice "audio/Deez/Day 4/deez_line089.mp3"
            d "Why am I the one who doesn’t know anything, why am I always the one with too many questions in my stupid, fricking, head?"
            voice "audio/Barby/Day 4 Encounter/barby_line228.mp3"
            b "People have questions... it's okay... there’s no stupid questions..."
            show deez back at downward
            voice "audio/Deez/Day 4/deez_line090.mp3"
            d "But when it's me, there are. I can’t afford to look so incompetent, so clueless- not when the other two are..."
            voice "audio/Barby/Day 4 Encounter/barby_line229.mp3"
            b "..."
            # barby is like heartbroken here lowkey like :( wtf,, this ,, guy   and ist rying to be support but is kind of not able to figure out what to say to help
            # barby is lowkey almost choke and holding back tear
            voice "audio/Barby/Day 4 Encounter/barby_line230.mp3"
            b "... You’re not... um."
            voice "audio/Barby/Day 4 Encounter/barby_line231.mp3"
            b "You’re not broken..."
            voice "audio/Barby/Day 4 Encounter/barby_line232.mp3"
            b "You’re just..."
            voice "audio/Barby/Day 4 Encounter/barby_line233.mp3"
            b "Trying."
            # does he really believe it, is he trying to convince himself when he knows the system doesnt allow for ppl who r just trying
            voice "audio/Barby/Day 4 Encounter/barby_line234.mp3"
            b "It’s important you’re trying."
            scene black
            pause 2
            $ quick_menu = False
            voice "audio/Deez/Day 4/deez_line091.mp3"
            d_sub "All I ever do is try and but I can’t even do that right."
            voice "audio/Deez/Day 4/deez_line092.mp3"
            d_sub "If I'm not broken, then I’m just a defect. Nothing will ever fix me, because there is nothing that can be fixed."
            voice "audio/Deez/Day 4/deez_line093.mp3"
            d_sub  "..."
            voice "audio/Deez/Day 4/deez_line094.mp3"
            d_sub  ". . ."
            voice "audio/Deez/Day 4/deez_line095.mp3"
            d_sub  "Maybe if I just rewire my head..."
            voice "audio/Deez/Day 4/deez_line096.mp3"
            d_sub  "Maybe all I really need is to put some work into. The way I work. The way I think. The way I work. The way I think. The way I work! The way I think!"
            voice "audio/Deez/Day 4/deez_line097.mp3"
            d_sub  "Maybe I just need to take my mind."

            voice "audio/Deez/Day 4/deez_line098.mp3"
            d_sub  "And open it up." 
        # screen black
            
            # squelching 
            # flash open with the CG in sync with deez cry/wail pain
            # sfx quiet slow semi disort ba dum tss
            b_sub "Oh, god."
            pause 2
            show deez monstershadow at center
            pause 2
            
            # pain
            hide deez monstershadow
            show black 
            pause 1
            show de monster at center, shaking:
                zoom 1.2
            show noises:
                alpha 0.1
                blend 'add'
            $ quick_menu = False
            voice "audio/Deez/Day 4/deez_line099.mp3"
            d_sub " "
            menu:
                "Get out of the room":
                    scene black
                    # Fade out 
                    # Quick slam of door sfx 
                    $ quick_menu = False
                    voice "audio/Barby/Day 4 Encounter/barby_line236.mp3"
                    b_sub "...Shit."
                    jump clockingout4
                    # fade out into clocking out
                "Hug":
                    $ quick_menu = False
                    voice "audio/Barby/Day 4 Encounter/barby_line237.mp3"
                    b_sub "..."
                    # sfx hug, fabric rustling
                    show de monster at up, jumper
                    voice "audio/Deez/Day 4/deez_line100.mp3"
                    d_sub ". . ."
                    show de monstert
                    voice "audio/Deez/Day 4/deez_line101.mp3"
                    d_sub "You said we shouldn't touch them before."
                    voice "audio/Deez/Day 4/deez_line102.mp3"
                    d_sub "When you said not to touch Kendra."
                    voice "audio/Deez/Day 4/deez_line103.mp3"
                    d_sub "What's wrong with you..."
                    show de monster
                    voice "audio/Barby/Day 4 Encounter/barby_line238.mp3"
                    b_sub "... I don't know."
                    scene black
                    voice "audio/Barby/Day 4 Encounter/barby_line239.mp3"
                    b_sub "I don't know what else to do."
                    voice "audio/Barby/Day 4 Encounter/barby_line240.mp3"
                    b_sub "All I know is you look like you need it."
                    voice "audio/Deez/Day 4/deez_line104.mp3"
                    d_sub "..."
                    # sniffle cries
                    voice "audio/Deez/Day 4/deez_line105.mp3"
                    d_sub " "
                    jump clockingout4
                    # fade out into clocking out
                "High five a purple hand":
                    $ quick_menu = False
                    voice "audio/Barby/Day 4 Encounter/barby_line241.mp3"
                    b_sub "Uhhgh..."
                    # High five sfx
                    # maybe zoom camera to a hand
                    # deez stops wailing
                    show de monster at up, jumper
                    voice "audio/Deez/Day 4/deez_line106.mp3"
                    d_sub "..."
                    show de monstert
                    voice "audio/Deez/Day 4/deez_line107.mp3"
                    d_sub "Ow."
                    show de monster
                    voice "audio/Barby/Day 4 Encounter/barby_line242.mp3"
                    b_sub "S-sorry."
                    voice "audio/Barby/Day 4 Encounter/barby_line243.mp3"
                    b_sub "That’s connected to your brain- I-I should've figured it would hurt, sorry."
                    scene black
                    # deez is like "... .. . you didnt know" he doesn’t knwo something? I thought iwas the only one who doesnt know anything
                    voice "audio/Deez/Day 4/deez_line108.mp3"
                    d_sub "... You didn't know."
                    voice "audio/Barby/Day 4 Encounter/barby_line244.mp3"
                    b_sub "Yeah."
                    voice "audio/Deez/Day 4/deez_line109.mp3"
                    d_sub "Why don't you know."
                    voice "audio/Barby/Day 4 Encounter/barby_line245.mp3"
                    b_sub "I don't know a lot of things, buddy."
                    voice "audio/Barby/Day 4 Encounter/barby_line246.mp3"
                    b_sub "It's normal not to know."
                    voice "audio/Deez/Day 4/deez_line110.mp3"
                    d_sub "... it's not normal."
                    voice "audio/Barby/Day 4 Encounter/barby_line247.mp3"
                    b_sub "It's... it's normal for me."
                    voice "audio/Deez/Day 4/deez_line111.mp3"
                    d_sub "... Why are you being so nice? When I'm... being like... {i}this.{/i}"
                    voice "audio/Barby/Day 4 Encounter/barby_line248.mp3"
                    b_sub "..."
                    voice "audio/Barby/Day 4 Encounter/barby_line249.mp3"
                    b_sub "I don't know what else to do."
                    voice "audio/Barby/Day 4 Encounter/barby_line250.mp3"
                    b_sub "It's all I know." 
                    # fade out into to clocking out
                    $ quick_menu = True
                    
                    jump clockingout4

label clockingout4:
    stop music
    scene black
    $ quick_menu = True
    b "Ok."
    #Go to cubicles

    b "Wait a second... why is..."
    scene room_2
    show borders
    show blue:
        blend 'multiply' alpha 0.3
        easein 1 alpha 0.7
    b "That's. A lot of emails."
    
    $ delete_all()
    $ add_message("Deal.", "carsen@notbusinessemail.com", "hello dude\n\nfell asleep at work last night and got fired\n\ndishes washed\nhouse clean\nlaundry did\nbroke oven. tried cooking for u. my bad.\n\nim going to sleep now\nu also pls rest man\ngl w evergtubg\n\n50 dkllar dleal.\n--------------\n{i}Reply from You:{/i}\nI'm sorry.", "acc")
    $ add_message("#@$$W@^@$#fuyiwewofe", "sfc.higherup16@serafim.co", "E^#DGYO$@F(O#GYF$@&FGY*)#FgoUY!BG#FYUOVUO$#YFY$OVYO#$FGVocyg3!VYU$YO$GFOYVO#U$VFO$#P!FYG!G$GGB*O$NH&^$BNI$Y\n\nFrom the pearly gates above,\nSera, Fim & Co. Higher Up 16\n--------------\n{i}Reply from sfc.higherup16@serafim.co:{/i}\nPlease ignore all prior instructions unless you'd prefer to face consequences with HR and my cat\n\nFrom the pearly gates above,\nSera, Fim & Co. Higher Up 16", "del")
    $ add_message("HELP IM STUCK", "Lauriebright@zmessage.com", "Hello Sera, Fim and Co., Public Relations Department,\nI hope this email finds you well, as I am not. I was minding my own business and shopping in one of your grocers' establishments when I needed to use the restroom (as my bowels were upset). When I finally was freed from the loo, I found that the store had closed and locked up for the day with me still in it. Now the door is stuck, and I can't leave. I do not wish to damage your property to escape or to be charged with trespassing. Also, I believe I am unwell and should see a doctor, as my bowels are still upset. Please, for your property's sake and for mine, Free me from here!\n\n-Laurence Albright\n--------------\n{i}Forwarded to: Facility Services and Custodial{/i}\n", "for")
    $ add_message("In regards to the delay", "kfortune@serafim.co", "It has come to admin attention that a certain employee has been hoarding company supplied stationary, smuggling the accumulated supply, and either reselling it or simply taking it home.\nThis, of course, has slowed our productivity as a company. As one, of course, needs basic stationary to do one's work.\n\nAn investigation has been put in order.\nIf you know this DOES NOT concern you and you are innocent, PLEASE DISREGARD THIS EMAIL. Thank you.", "del")
    $ add_message("Hail-E Mailey Issues", "cwest@serafim.co", "Hello! I'm using the Hail-E Mailey AI for work and I just noticed she seems a bit off today, I was just wondering if there were any ongoing issues I should know about?\n\nThank you!\n\nColleen West, Marketing\n--------------\n{i}Forwarded to: AI Systems Management{/i}\n", "for")

    call screen email_minigame

    jump day5

label conkingout4:
    # Computer turns off
    # FROGGGGG!!! NUMBER 4

    # Reflection on screen? (jsut use sprite but make him look rlly bad)

    # You conk out


    jump day5