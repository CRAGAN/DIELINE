label day4:
    label day4intro:
    # CG Deez’ POV doorway manager office Barby shinji pose, Apollo on the ground (lying down on papers)

    b "Oh, what are we going to do… what are we going to do…" 
    a "Ugh…"
    a "Ahaha, i-it’s fine! We can- we can work something out." 
    a "W-we kind of don’t have much to show, though..."
    b "Any progress is still progress, right?"
    a "Right! So surely that’s got to mean something to them."
    b "But what if it’s not enough? What if they ask for more?"
    a "Um, um, maybe we can say that–..."
    a "... Barby, honestly… a lot’s been going on… and I’ve just been—"
    d "I would say good morning, but it appears this morning is not very good."
    a "Oh my goodness Deez, I didn’t see you there! Hi!"
    b "Deez! Good morning!"
    a "Ahaha, what do you mean? Me and Barby, we’re so normal this morning."
    b "We are?"
    a "Yes! So normal about the person they’re sending to check in on the project today."
    d "I am inclined to believe otherwise. It seems you both are worried?"
    b "It’s just. Y’know. How are we gonna talk to someone from the company about… whatever’s going on right now…!"
    a "I wanna just ask for help, yeah, but… if SFC finds out how far behind we are…"
    a "We might all… lose our jobs."
    b "Getting fired from SFC… sucks. Apparently, it destroys your resume… I hear it becomes a nightmare to get rehired for anything substantial." 
    a "Agh…"
    d "If talking is the issue, then I can do it."
    b "Oh no, Deez, we couldn’t possibly pass this onto you. They’re probably going to ask lots of questions about the project, and we need someone who’s knowledgeable…" 
    d "Well yes, that’s me. I know a lot."
    d "And I’m, like, really good at talking to people."
    a "Really?"
    d "Yeah. I was, like, doing network activities for my family’s business…going around talking… and yeah." 
    a "That’s wonderful! Oh Deez, you smart, smartie-pataatie, I’m so glad you’re with us."
    b "I guess Deez must’ve learned a lot from Kendra before she… yeah."
    a "... Well, let's just check around before they arrive. Especially on… ahaha, you know."
    jump officewalkday4
    label minigame4:
    b "I'll leave my PC on. I’m just gonna check on the. Thing. Then I'll get back to see if there’s any other work before I go."
    jump guymeeting

label guymeeting:
    r "Hey man, no worries about being a mess, I get it y'know, I heard the deadline got moved earlier and, man that’s gotta suck."
    r "It's happened to me before. God… corporate hellscape. It never ends."
    d "Haha yeah. But we’re totally doing fine though. Don't worry, haha."
    r "Instead of laughing, you keep saying ‘haha’ out lou—"
    b "Hiya—"
    d "OH THANK GOD YOU’RE HERE I NEED TO TAKE A MASSIVE SHIT." 
    # sprite tween run to bathroom and vanish
    # close door sfx

    b "Wha-"
    r "Oh damn he needed to go? He could've just said so. Anyway what’s up, man?"
    b "Well, I was, uh, just checking in, but."
    menu loops:
        "Which department are you from?":
            b "Which department are you from, again?"
            r "Oh, I’m just a warehouse guy. They sent me in to check on you guys because you haven’t sent the go ahead."
            b "A-ah! That's just because we don't need them! We're doing all fine on our own."
            r "That’s. What? Not how it works?"
            b "Crap. Crap. No I’m joking, this is a joke."
            b "Yeah, no, like Apollo said, we’ll give the go ahead soon! Prommy."
            r "Sure, mann."
            jump loops
        "Do you know what our job is":
            r "Shouldn't you guys know that?"
            b "WE KNOW DON’T WORRY. I was just curious if they told you anything, haha."
            r "Sure, mann."
            jump loops
        "How is everything":
            r "Well, it kind of looks like you guys have it handled? Your coworker only showed me this hallway and the breakroom, though."
            r "I’m just a little worried about your manager and the guy I was talking to."
            r "They, uh. Seemed kind of… Off?"
            b "Oh, they're just a little sleep deprived and tired after, y’know everything."
            b "It happens, you know… unfortunate as it is."
            r "Mann. That’s not how that. Works."
            r "You know, you clock out, then get sleep, then clock back in the next day??"
            r "It’s just a job, bro."
            b ". . ."
            b "Ok."
            jump loops
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
            r "Ok…?"
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

label breakroom4:
    # CG has u looking down at deez knelt next to [anythjbg] trying to fix it maybe his face is obscured 
    #And the hand is holding his head together
    menu:
        "Calmly ask him to stop":
            # Bad option
            b "Please… you can stop."
            d "... Stop what."
            b "You don't have to fix it."
            b "It's… clear it's making it hard for you…"
            # sad
            d "You think I can't do it. You {i}always{/i} think I can’t do it."
            b "I… I think you should stop trying."
            d ". . .stop trying? STOP TRYING? STOP TRYING???"
            b "Like. That you should take a break."
            d "take a break? take a break, TAKE A BREAK, TAKE A BREAK, TAKE A BREAK? TAKE A BREAK???"
            #hand jumpscare
            # sfx jumpscare
            # he Kils u make some freaky noise go have fun

        "Encourage & console":
            # (MEAN IT!! MEAN IT!! GO ECCHAN)  SOUND SO GENUINE THAT HE CRIES
            b "You're doing a really good job and I'm proud of you." 
            # pause then sob semi long
            d ". . . proud of me… proud of me…"
            d "sobs"
            # do some sob speaking with like im about to choke vibes, whining ? but make it real
            d "Barby…I’m just so stupid."
            d "What the heck am I doing?"
            d "What am  I even…trying to do anymore?"
            b "... Oh, man…"
            d "Everyone says 'grow up', but no one ever says how."
            d "Everyone looks like they have it easy- like they all have it figured out!"
            d "Nobody questions anything. Nobody even asks questions."
            d "Why am I the one who doesn’t know anything, why am I always the one with too many questions in my stupid, fricking, head?"
            b "People have questions… it's okay… there’s no stupid questions…"
            d "But when it's me, there are. I can’t afford to look so incompetent, so clueless- not when the other two are…"
            b "..."
            # barby is like heartbroken here lowkey like :( wtf,, this ,, guy   and ist rying to be support but is kind of not able to figure out what to say to help
            # barby is lowkey almost choke and holding back tear
            b "... You’re not… um."
            b "You’re not broken…"
            b "You’re just…"
            b "Trying."
            # does he really believe it, is he trying to convince himself when he knows the system doesnt allow for ppl who r just trying
            b "It’s important you’re trying."

            d "All I ever do is try andbut I can’t even do that right."
            d "If I'm not broken, then I’m just a defect. Nothing will ever fix me, because there is nothing that can be fixed."
            d "..."
            d ". . ."
            d "Maybe if I just rewire my head…"
            d "Maybe all I really need is to put some work into. The way I work. The way I think. The way I work. The way I think. The way I work! The way I think!"
            d "Maybe I just need to take my mind."
            d " And open it up." 
    # screen black
    # squelching 
    # flash open with the CG in sync with deez cry/wail pain
    # sfx quiet slow semi disort ba dum tss
    b "Oh, god."
    # pain
    d "cry, wail"
    menu:
        "Get out of the room":
            # Fade out 
            # Quick slam of door sfx 
            Barby "...Shit."
            # fade out into clocking out
        "Hug":
            b "..."
            # sfx hug, fabric rustling
            d ". . ."
            d "You said we shouldn't touch them before."
            d "When you said not to touch Kendra."
            d "What's wrong with you…"
            b "... I don't know."
            b "I don't know what else to do."
            b "All I know is you look like you need it."
            d "..."
            # sniffle cries
            d "sniffle, cry"
            # fade out into clocking out
        "High five a purple hand":
            b "Uhhgh…"
            # High five sfx
            # maybe zoom camera to a hand
            # deez stops wailing
            d "..."
            d "Ow."
            b "S-sorry."
            b "That’s connected to your brain- I-I should've figured it would hurt, sorry."
            # deez is like "... .. . you didnt know" he doesn’t knwo something? I thought iwas the only one who doesnt know anything
            d "... You didn't know."
            b "Yeah."
            d "Why don't you know."
            b "I don't know a lot of things, buddy."
            b "It's normal not to know."
            d "... it's not normal."
            b "It's… it's normal for me."
            d "... Why are you being so nice? When I'm… being like... {i}this.{/i}"
            b "..."
            b "I don't know what else to do."
            b "It's all I know." 
            # fade out into to clocking out

label clockingout4:
    b "ok."
    #Go to cubicles
    b "Wait a second… why is…"
    b "That's. A lot of emails."
    # OPEN MINIGAME

label conkingout4:
    # Computer turns off
    # Reflection on screen? (jsut use sprite but make him look rlly bad)

    # You conk out


    jump day5