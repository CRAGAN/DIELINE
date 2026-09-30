label day4:
    # CG Deez’ POV doorway manager office Barby shinji pose, Apollo on the ground (lying down on papers)
    scene room_1
    show overlay:
        blend 'multiply'
    show apo worried at center:
        xoffset 250
    show de sad at center:
        xoffset -250
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
    b "I'll leave my PC on. I’m just gonna check on the. Thing. Then I'll get back to see if there’s any other work before I go."
    jump guymeeting

label guymeeting:
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
            b "Thank you, but we’re good!"
            r "Sure, mann."
            jump continued
#continue
label continued:
    r "Alright, I think you guys got it handled. I don’t doubt you guys or anything."
    r "But we really need to ship out soon. So, if you can at least send a demo to corporate so we can start working."
    r "Also, really, let us know if you need any help; we’re not doing anything at the moment."
    b "Yeah. Will do, man."
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
    b_sub "Hey, Deez? Are you in there?"
    # knock
    b_sub "Daniel?"
    # groans and oahh
    d_sub "Fine. Just fine. I just- aghhh..."
    d_sub "Taking a massive shit."
    b_sub "O-oh..."
    b_sub "Y-yeah, why do they call it a {i}rest{/i} room, you're fighting for your life in there."
    # sfx bad joke but cut it off Barby talking
    b_sub "That was so bad, sorry."
    d_sub "Ughh..."
    b_sub "Sorry..."
    d_sub "No... don't sorry... I'm just..."
    d_sub "AGH." with hpunch
    # Deez make a few groans before AGHHHH AHHHHHH (his head splits open) but it could be mistaken for a really bad sht , but the sfx is fcking scary and the static stops
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
            b "Please... you can stop."
            show de sadt
            d "... Stop what."
            show de sad
            b "You don't have to fix it."
            b "It's... clear it's making it hard for you..."
            # sad
            show de sadt
            d "You think I can't do it. You {i}always{/i} think I can’t do it."
            show de sad
            b "I... I think you should stop trying."
            hide de sad
            show deez back at up, center, shaking:
                zoom 0.8 ypos 1.1
            d ". . .stop trying? STOP TRYING? STOP TRYING???"
            
            b "Like. That you should take a break."
            
            d "take a break? take a break, TAKE A BREAK, TAKE A BREAK, TAKE A BREAK? TAKE A BREAK???"
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
            b "You're doing a really good job and I'm proud of you." 
            # pause then sob semi long
            show de sadt
            d ". . . proud of me... proud of me..."
            hide de sadt
            show deez back at up, center, shaking:
                zoom 0.8  ypos 1.1
            d "sobs"
            # do some sob speaking with like im about to choke vibes, whining ? but make it real
            d "Barby...I’m just so stupid."
            d "What the heck am I doing?"
            d "What am  I even...trying to do anymore?"
            b "... Oh, man..."
            d "Everyone says 'grow up', but no one ever says how."
            d "Everyone looks like they have it easy- like they all have it figured out!"
            d "Nobody questions anything. Nobody even asks questions."
            d "Why am I the one who doesn’t know anything, why am I always the one with too many questions in my stupid, fricking, head?"
            b "People have questions... it's okay... there’s no stupid questions..."
            show deez back at downward
            d "But when it's me, there are. I can’t afford to look so incompetent, so clueless- not when the other two are..."
            b "..."
            # barby is like heartbroken here lowkey like :( wtf,, this ,, guy   and ist rying to be support but is kind of not able to figure out what to say to help
            # barby is lowkey almost choke and holding back tear
            b "... You’re not... um."
            b "You’re not broken..."
            b "You’re just..."
            b "Trying."
            # does he really believe it, is he trying to convince himself when he knows the system doesnt allow for ppl who r just trying
            b "It’s important you’re trying."
            scene black
            pause 2
            $ quick_menu = False
            d_sub "All I ever do is try and but I can’t even do that right."
            d_sub "If I'm not broken, then I’m just a defect. Nothing will ever fix me, because there is nothing that can be fixed."
            d_sub  "..."
            d_sub  ". . ."
            d_sub  "Maybe if I just rewire my head..."
            d_sub  "Maybe all I really need is to put some work into. The way I work. The way I think. The way I work. The way I think. The way I work! The way I think!"
            d_sub  "Maybe I just need to take my mind."
            
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
            d_sub " "
            menu:
                "Get out of the room":
                    scene black
                    # Fade out 
                    # Quick slam of door sfx 
                    b_sub "...Shit."
                    jump clockingout4
                    # fade out into clocking out
                "Hug":
                    b_sub "..."
                    # sfx hug, fabric rustling
                    show de monster at up, jumper
                    d_sub ". . ."
                    show de monstert
                    d_sub "You said we shouldn't touch them before."
                    d_sub "When you said not to touch Kendra."
                    d_sub "What's wrong with you..."
                    show de monster
                    b_sub "... I don't know."
                    scene black
                    b_sub "I don't know what else to do."
                    b_sub "All I know is you look like you need it."
                    d_sub "..."
                    # sniffle cries
                    
                    d_sub " "
                    jump clockingout4
                    # fade out into clocking out
                "High five a purple hand":
                    b_sub "Uhhgh..."
                    # High five sfx
                    # maybe zoom camera to a hand
                    # deez stops wailing
                    show de monster at up, jumper
                    d_sub "..."
                    show de monstert
                    d_sub "Ow."
                    show de monster
                    b_sub "S-sorry."
                    b_sub "That’s connected to your brain- I-I should've figured it would hurt, sorry."
                    scene black
                    # deez is like "... .. . you didnt know" he doesn’t knwo something? I thought iwas the only one who doesnt know anything
                    d_sub "... You didn't know."
                    b_sub "Yeah."
                    d_sub "Why don't you know."
                    b_sub "I don't know a lot of things, buddy."
                    b_sub "It's normal not to know."
                    d_sub "... it's not normal."
                    b_sub "It's... it's normal for me."
                    d_sub "... Why are you being so nice? When I'm... being like... {i}this.{/i}"
                    b_sub "..."
                    b_sub "I don't know what else to do."
                    b_sub "It's all I know." 
                    # fade out into to clocking out
                    $ quick_menu = True
                    jump clockingout4

label clockingout4:
    scene black
    
    b "ok."
    #Go to cubicles

    b "Wait a second... why is..."
    scene room_2
    show borders
    show blue:
        blend 'multiply' alpha 0.3
        easein 1 alpha 0.7
    b "That's. A lot of emails."
    # OPEN MINIGAME
    jump day5

label conkingout4:
    # Computer turns off
    # Reflection on screen? (jsut use sprite but make him look rlly bad)

    # You conk out


    jump day5