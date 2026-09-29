### TODO: Is this file unused? ###

# default employee_id = ""

# transform down:
#     ypos 100
# screen officewalk():
#     tag menu

#     imagebutton:
#         idle "mj_standing.png"
#         hover "mj_standing_hover.png"
#         xpos 0.5
#         ypos 0.5
#         action [SetVariable("employee_id", "M.J Grey"), Jump("officemeet")]

label donetalking:
    $ quick_menu = True
    b "I think that's everyone! I haven't seen Dave around... he's probably working from home again."
    b "He doesn't live too far from here, so if I ship his ID now, he should receive it soon!"
    b "Just gotta get on my computer."
#sfx_computer

label officewalk5:





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

label officewalkday4:
    # overworld in front of Manager office
    b "We should probably check on our ‘non-compliant’? Friends…"


    #Apollo & MJ

    # in front of Manager room 
    a "...so that’s basically what happened…"
    a "Ahh, sorry for telling you this. I know it’s personal stuff and whatever but you have your whole… family situation too, and I figured…"
    a "I don’t know. Maybe you’d know something?"
    a "I don’t wanna put this on anyone else, haha… they’re kind of counting on me to keep everything together."
    m "Your team member has failed to use their connections with the Grey family to establish business relations! You may resolve this by contacting your Human Resources department to handle the issue."
    a "I know it's important, MJ, I do! I love my family! But… ahh. I… oh death, can't say I shouldn't have done it— but I also shouldn't say I should have but…"
    a "Did—did you really cut all your ties with them…?"
    m "Contact between SFC and the Grey family is currently being established."
    a "S-so it {b}is{/b} possible to—um— make amends after pulling something like, well, what you did?!"
    m "Compromise is the best display of competence when working in a team!"
    a "O-okay, haha… thank you… MJ…"
    m "Always here to help!"
    a "It's nice to hear you and your family… are talking again?"
    m "..."
    m "Thanks to our exceptional PR team, the failures of past circumstances only impact those who deserve to take the fall!"
    m "Employees who do not reach the minimum standards of performance should not be considered for their originally proposed value, of course."
    a "But MJ… y-you’ve been doing so much! Can’t your family see that?" 
    m "Employee Grey has had their performance depreciating for a while! Be sure to spend more time on work rather than unrelated and unproductive activities."
    a "..."

    #Kendra & Deez

    # cubicles
    d "I know what happened to you."
    k "..."
    d "I learned a lot over the past few days, and a lot of it is because… I spent a lot of time with you and helping you." 
    d "So. That's how you know I know."
    d "I know what happened to you." 
    d "... because everyone talks to me about these things as if I don't know it. And… maybe I'm listening just to see that they know it correctly… but it's weird that people say it like-..."
    d "Um...Anyway, it's because, since you and MJ are cousin lab experiments, this happened to you. And I can diagnose that it is not good."
    d "It's bad for your health, being eaten by bugs. They don't make Prozempic anymore. I don’t want to be the bringer of bad views, but that’s the sad truth. Because the blue bugs don’t know that, so they wouldn't have told you."
    k "..."
    d "You know, Kendra, there are good bugs, too. These blue bugs aren't being good for you, so you should…maybe. Let them fly somewhere out a window. Let them on a bug vacation or let them near a lamp. I in cyst."
    d "..."
    k "Why are you telling me this?"
    d "... uhm. There are other bugs. Sometimes they can sit on you, but they shouldn’t be eating you."
    d "I'm saying… stop with these bugs. You keep saying to leave you alone and let you work but these bugs don’t seem to let you do that. They’re in your way and it’s affecting you. "
    d "...I don’t like seeing you being swarmed by them. You don’t deserve bugs that bug you."
    k "... Can you make it stop?"
    d "..."
    d "I. Maybe—"
    k "You can do it?"
    d "..."
    d ". . ."
    d "Yes. I will do it. Now."
    # kendra start sobbing
    d "..."
    d "Ah. Oh no—"
    d "Kendra? You seem upset—"
    k "It won't stop. It hurts. I can't take it. I can't."
    d "... I'm—."
    d "..." 
    # deez leaves 
    # a bit ANGRY
    k "I have to get a grip. I have to."

    #Ryann Glenn
    # itd be kind of funny if after office walk you walk around and then ryann is just there or the camera slowly pans to him 

    # SFX audience cheer as if hes a celebrity 
    # scene stops and stuff to wait for audience to stop cheering 
    # Apollo Deez appear here too

    a "Barby, when they get here, we gotta make sure we tell them we don't need any extra he—..."
    a "..."
    d "..."
    r "Hey, how are you, all? I'm Ryann Glenn."
    # music change as he talks
    r "I work at the warehouse and, ahh, we just wanted to check up on your team."
    a "A-ah! Hi, there! I'm Apollo, the manager! I take it your name is Ryann. Glenn…!"
    r "Yep, that's my name."
    a "This is Deez, he's our… he's the one who's gonna tour you! Ahaha, yes!"
    r "Hey, man, I'm not looking for a formal tour or anything. We at the warehouse were just concerned you hadn't given us the go ahead to ship out yet?"
    d "Why is he talking like that? It's not a cutscene."
    b "O-oh! Hahaha… right, um, we've just had so much to do over here and, y’know you get so caught up in it!"
    r "Cool, yeah, I get ya."
    r "But what are you getting caught up inn if we haven’t shipped out yet?"
    d "You're not supposed to say ‘in' like that."
    a "It’s so nice the warehouse is sending someone to help! But, uh…"
    a "Ahahaha, we'll give the go ahead soon, I prommy!"
    a "Deez is gonna tell you about… all the stuff, haha!" 
    d "(going to shit myself) Hi."
    d "Let us go to a more… dignified place to talk. About business. Because I am very good at that."
    r "Sure, mann."
    d "Wh-why do you say it like that."
    b "You can't just say that to someone, Deez."
    r "It's okay, I don't take offense or anything. I don't know what he means, though. "
    b "Stay safe! Have a safe tour!"
    r "I don't see why it wouldn't be…!"
    b "I should go check on my emails…"
    jump minigame4

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

label breaktime4:
    # Fade in the hallway again but empty

    b "Is Deez still in the bathroom?"

    # cubicle
    #Kendra
    b "..."
    k "sobbing"

    # manager office front
    #MJ
    b "..."
    m "humming"

    #Manager Office (inside)
    # apollo sitting there
    b "..."
    a "Hm? Hi, Barby. I'm working right now. What's up?"
    menu:
        "Deez":
            b "Looking for Deez."
            a "I'm pretty sure he was touring that guy?"
    # leave dialogue (can click again)
        "You?":
            b "What's up with you?"
            a "Oh, haha. I've just been fixing the PowerPoint presentation to pitch, uh, how to present the product's value to our client. For them to use when advertising it."
            a "... haha, funny you ask, but most of the progress didn't save last night so, haha, I'm just fixing that up right now!"
            b "Oh shoot…"
            a "Don't worry too much about it, I still remember how I did it, anyways, I just have to put it in again. Hah…"
    # leave dialogue (can click again)
        "Nothing":
            b "Nothing, just checking in."
            a "Neat!"
# leave dialogue (can click again

# Clicking around anywhere else in the area
label encounter4:
    #Click bathroom door
    # not VA'd except screams and groans from Deez
    b "Hey, Deez? Are you in there?"
    # knock
    b "Daniel?"
    # groans and oahh
    d "Fine. Just fine. I just- aghhh…"
    d "Taking a massive shit."
    b "O-oh…"
    b "Y-yeah, why do they call it a {i}rest{/i} room, you're fighting for your life in there."
    # sfx bad joke but cut it off Barby talking
    b "That was so bad, sorry."
    d "Ughh…"
    b "Sorry…"
    d "No… don't sorry… I'm just…"
    d "AGH."
    # Deez make a few groans before AGHHHH AHHHHHH (his head splits open) but it could be mistaken for a really bad sht , but the sfx is fcking scary and the static stops
    b "ARE YOU OKAY!?"
    # silence. Not even static
    # silence 
    # silence  6.7 sec

    # door opens. Deez is standing there staring front
    # staring. Silence 6.7 sec
    # silence.

    d "Normal."
    # static comes back
    # he steps out
    # sfx footstep
    # barby turns as he comes out
    # moment of pause
    # deez turns to the right.
    # hes clickable now
    # steps, stands for 3 seconds, steps, stands for 3 seconds (clickable during standing for 3 seconds)
    # he enters the breakroom

    #If player clicks him early
    b "Deez, wait. Stop. You have something on your—"
    # deez stops
    # flash black
    # hand lets go and reaches out to barby (can just be one img) ID YOU VANT DO IT I WILL DO IT ITS GONNA JUST BE A HAND BUT PURPLE JUNPSCARE FIRST PERSON 
    # sfx jumpscare 
    # black screen
    # return back to the moment he open door
    jump breakroom4

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
            d "You think I can't do it." You {i}always{/i} think I can’t do it.”
            b "I… I think you should stop trying."
            d ". . ." “stop trying? STOP TRYING? STOP TRYING???”
            b "Like. That you should take a break."
            d ".  .  ." “take a break? take a break, TAKE A BREAK, TAKE A BREAK, TAKE A BREAK? TAKE A BREAK???”
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
