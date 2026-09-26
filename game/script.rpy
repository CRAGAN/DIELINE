define b = Character("Barby")
define a = Character("Apollo", image= "i_apo", callback=name_callback,cb_name="Apollo", color = "#383d70")
define k = Character("Kendra", image= "i_ken", callback=name_callback,cb_name="Kendra", color = "#70384e")
define m = Character("MJ", image= "i_m", callback=name_callback,cb_name="MJ", color = "#3f7038")
define d = Character("Deez", image= "i_de", callback=name_callback,cb_name="Deez", color = "#523870")

default see_ids = False
define talked = 0

transform zoomin:
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    easein 0.5 zoom 1.3

label start:
    #scene bg barbyclocksin
    #sfx clockin
    
    b "Shucks... I haven’t seen her since we got discharged."
    b "It should be fine. It should be normal."
    b "I can’t waste time overthinking."

    # Barby walks into manager room cg
    #sfx walking
    scene apollomanagersroom with fade
    b "...Hiya, Apollo—I mean—boss! Good to see you again!"
    a "Oh, good morning Barby! Y—you don’t have to call me boss, I’m just your regular ol’ Apollo!" 
    b "Oh! Snap! Sorry, boss. SHOOT! AH!"
    a "Haha, every time you call me boss, I’m calling you boss, too! It’s only fair with all those emails you’ve sent with my name."
    b "Aw—hey, you know it was an accident... You have my account, too. How’d {i}you{/i} not get confused?"
    a "I triple dipple check all the time!"
    
    b "Wow! Please don’t say that word again." 
    a "Uhh... okay? But really, Apollo’s just fine and dandy."
    scene managerroom with dissolve
    show overlay:
        blend 'multiply'
    show apo defaultt at downward, center
    a "And hey, congratulations on {i}your{/i} promotion...! I mean look at you, ohoho, assistant manager now? You’re totally killing it!"
    show apo default at center, jumper
    b "Ahh...! Thank you. Killing it, haha, just like. The."
    show apo awkward at jumper
    b "Truck."
    show apo worried at up
    a "Oh!"
    # add image of sensin and truck
    scene picture:
        subpixel True
        zoom 1.5 xoffset -500
        easein 20 zoom 1.2 xoffset -200
    with dissolve
    a "The truck that killed our old manager?"

    a "Yes, it was a sudden end, but that's just the cycle of life and death: a truly beautifully inevitable part of us all. I hope Mr. Sensin is resting easy now."

    b "...Wow."

    a "He’s in good hands now—I’d know! Teehee!"
    b "At least that was taken care of..." 
    # back to the scene
    scene managerroom
    show overlay:
        blend 'multiply'
    show apo default at jumper, center
    with dissolve
    b "Speaking of, have you heard back from your insurance? About the accident?" 
    show apo worriedt at downward
    a "Oh goodness, no, I haven’t! Have you? I’m worried..." 
    show apo worried
    b "Agh, don’t be worried!"
    b "I’ll handle it for both of us :)! I don’t have too much to do yet, since it seems like a lot of my responsibilities are waiting on others." 
    show apo worriedt at downward
    a "Are you sure? I know we’re supposed to fill it out together... Sorry, but being the new manager sure has me a little frazzled. Maybe I can still help out—?" 
    show apo worried
    b "You’ve got a whole team to handle. I'd be happy to help out!"
    b "That’s what {i}assistant manager{/i} means, after all. Let me {i}assist{/i} my manager."
    show apo defaultt at downward, center
    a "I—you’re right. We got this, we have to stay positive for our first day! Well, if you’re up for it... here!"
    # IDs come out
    # sfx_id1
    a "I know we just clocked in, but it’s a pretty easy task. Could you distribute the new IDs to the team?" 
    a "I’d do it myself, but I have to attend this online conference with corporate. I have yet to figure out how to log into Skycloud Meet, haha..."
    show apo default
    $ picked = []
    menu idchoice:
        set picked
        "Skycloudmeet?":
            b "We switched to Skycloud Meet already?"
            show apo awkwardt at downward
            a "Err, yeah. It’s supposed to work better with the other Sera, Fim & Co. software we’re using, yet..."
            show apo defaultt
            a "It’s kinda complicated. I’m not good at technology— but I’m positive I’ll figure it out!"
            show apo default
            jump idchoice
            # return to choices

        "But I don't know the team.":
            b "Ah, but I don’t even know who’s part of the team yet."
            show apo defaultt
            a "It’s okay, you already know most of them by now! All their names and faces are on their IDs too, so you can figure it out easy peasy!"
            show apo default
            jump idchoice
            # return to choices

        "Sure! Easy!":
            
            jump id_see 
            

label id_see:
    b "Alright, no problem, then! I can do that."
    show apo defaultt
    a "Sweet! Here you go!"
    show apo default
    hide apo with dissolve

    call screen id_screen with dissolve

   
label rooms:
    $ storage = False
    $ janitor = False
    $ bathroom = False
    $ managerroom = False
    if talkedtodeez and talkedtokendra and talkedtomj:
        b "I think that’s everyone! I haven't seen Dave around... he's probably working from home again."
        b "He doesn't live too far from here, so if I ship his ID now, he should receive it soon!"
        b "Just gotta get on my computer."
        $ current_room = 2
        $ talkedtokendra = False
        $ talkedtoapollo = False
        $ talkedtomj = False
        $ talkedtodeez = False
        jump breaktime1

    call screen rooms with fade
    # call screen officewalk
    # if current_id == "M.J Grey":
    #     b "Alright, gotta go check on some things!"
    #     m "Okay! Let me know if you need help!"
    #     b "Let me know if—! Aww man."
    #     m "I win, heh." 
    #     call screen officewalk


label meeting:
    $ talked = 0
    scene room_2
    show apo defaultt at center
    a "Hello everyone! I’m so glad you all made it! It’s nice to see you all again, it’s been such a long time!"
    show ken defaultt
    show apo default
    k "Uhh yeah, I guess it’s been a while, huh. I think– I think uh around 6 weeks, right?"
    show de defaultt
    show ken default
    d "Yes."
    show ken awkwardt
    show de default
    k "Deez, you weren’t even here 6 weeks ago???"
    show ken awkward
    show de shyt
    d "I knew that."
    show de default 
    show apo defaultt
    show ken surprised
    a "I have a few announcements regarding our latest project!"
    a "But, before we begin, I have one thing to address..."
    a "I’m sure you’re all wondering about my suddenly horrible handwriting and Barby’s little wobble bobble."
    show apo default
    b "My {b}{i}what{/i}{/b}!?"
    show m defaultt
    m "Well I wasn’t gonna ask out of courtesy, buuut if you’re open to talking about it, I’m all ears."
    show m default
    show de defaultt
    d "According to my informittants, he usually wears shorts since he hates pants."
    d "He is hiding something most suspicious. That is a flaw in fashion. Everybody would know that wearing shorts for a workday is not very formal attire."
    show de thinkingt
    d "That’s the real wobble bobble."
    show de default
    k "Did– did you mean informants or-? {i}And I didn’t say anything about him hating it—{/i}"
    show de defaultt
    d "I meant what I said, and I said what I meant."
    show de shy
    show apo defaultt
    a "So intellectual of you Deez, so observant! And you just got here!"
    show apo default
    b "Wait- I don’t hate pants- what-!?" 
    show apo awkwardt
    
    a "So uhm unfortunately, this is what happened to my left hand..."
    show m hmt
    #CG_She rolls up her sleeves and reveals super scarred left arm from hand till shoulder
    m "Oh goodness."
    show m hm
    show de surprised
    #VA: genuinely shocked but trying to be nonchalant, like a short sigh/exhale
    d "..."
    show ken worried
    k "Agh..."
    b "Yeah..." 
    show apo awkwardt
    a "And you all already know what happened to Barby’s leg—"
    show apo awkward
    b "WHAT!?" 
    # 
    show apo defaultt
    a "You don’t need to adjust too much for me, but please take it easy on him since he just got his prosthetic fitted recently."
    a "I hope you all can make accommodations for him!"
    show apo awkward
    show ken worried
    k "!?!?!??!"
    show de surprisedt
    d "PROZEMPIC!?!??!"
    show m hm
    show de surprised
    m "Oh?!?!?"

    b "{i}I’M BEING OUTED!?{/i}"
    #
    a "OH! Did— did you not tell them Barby?! I’m so sorry, I thought you told everyone!!" 
    b "..."

    a "..."
    m "Do you need help with that?" 
    k "MJ!? I—I don’t know if you can really help with that!"
    m "What? Just trying to offer accomodation like Apollo said."
    m "By the way, Deez... Prozempic isn’t really a thing. Osempic doesn’t produce Prozac as far as I’m aware." 
    d "Errrgh... noted..." 

    d "I didn’t ask... no one asked... Who’s MJ talking to, huh..."
    b "Okay... thank you... but I don’t really need all that extra help! I’m really okay- most of my job is on the computer, anyways..." 
    b "We have more important things to talk about right now, haha...!" 
    k "Are we just gonna—"

    b "A–Apollo??"
    a "Ah yes, of course! Haha, thank you all for your cooperation! Moving on—"
    a "The meeting with the higher ups was... definitely something! I think I could explain this better with a little help!"
    a "Barby, if you could please help me demonstrate what happened?" 
    b "Sure!"
    k "Oh uhh, was the meeting really that bad? W-why do we need a little—play thing?" 
    m "Apollo does this when things are hard to explain. Please, go on, boss!" 
    a "A... You can just call me Apollo, MJ! Haha."

    a "Ahem! Hello, I am the big boss here to give you your project! Ask me anything!"
    b "Hiya big boss! I have a few questions to ask, such as what {i}is{/i} our client’s new product we’re supposed to market?"
    a "Oh, silly manager, it’s not a product, it’s a lifestyle!" 
    b "Okay, what is this lifestyle we are trying to promote?"
    a "It’s a life changing lifestyle to promote healthier and happier clients! A way of existence, if you will."
    k "Wait what? How—how are we supposed to promote this?"
    b "Stay in character, please...!"

    k "O...okay! How are we supposed to promote this, big boss?"
    a "By promoting the lifestyle with the same great enthusiasm you’re bringing into this meeting right now!"
    m "Ah. So it’s not an actual... item?"
    a "Oh, it is! But it’s more than that." 
    d "Raising my hand."
    a "Yes, little sweet intern—"
    b "Noo....he’s Apollo..."
    a "Ough—I’m sorry—"
    a "I mean manager!" 
    d "Oh. Um. Uh..."
    
    d "Aaa... Ohh! Ohhhh! S-So we weren’t given any information but have to do it, anyway? That’s like... a paradox."

    d "Deez would know what that means..."
    d "But Apollo, me, doesn’t know what we’re supposed to do?" 
    a "Haha, no, no! Not if you think {i}outside{/i} the box."

    k "B—but. Ahem. In character. How the heck are we supposed to think outside the box, i-if— If we don’t even know what we’re doing?"
    k "This—This doesn’t make any sense at all! Why are they so vague? I—I don’t like this! Ugh... this is g—gonna make everything harder..."

    m "I’m sorry you’re going through this confusion. Let me think of what I can do to help."
    d "Since everyone is no longer doing voices I will stop doing voices, too."
    b "Aw man."

    a "It’s okay, Barbyyy! You’ll get ‘em next time."
    m "Maybe I can ask the client directly to help ease the situation."
    d "Well, {i}yeah{/i} MJ, that’s what a marketing employee’s {i}supposed{/i} to do, haha. Hah."
    d "A-anyway uhh, I totally agree with everyone here. We just have to figure out big boss’ super easy puzzle words."
    m "Thanks for your cooperation and understanding. The intern’s right! We just have to figure it out, then it’ll be fine."
    d "{i}Yeah. I’m always right.{/i}"
    k "O–okay, I think? None of you are, err, really helping here! Is there anything else they said that was important?"

    a "I’m sorry but... I really didn’t get anything other than it being such a {i} convenient and life changing product that will make consumers feel sweeter than the sweet release{/i}."
    m "...Death reference? Was that just an Apollo thing or...?"
    b "No, they actually said that. She told me earlier."
    m "They ACTUALLY said that?"
    a "Yeah, no. They did." 
    k "Okay—I think we need to make a game plan now, we can’t just sit by and—and not do anything!"

    m "That's about right! Honestly, if we can do this as efficiently as possible, it'll be smooth sailing from here."
    m "Which is why I think we should contact the clients directly ourselves, first."
    a "Aha... but, I just spoke with them—"
    k "I was thinking, maybe, i-if we did it through emails we can have a more cohesive backlog of all the information they give us...! All our questions included."
    d "Uhm, actually— some of us still have A LOT of other responsibilities besides the project - like uhh, general work... things."

    k "Kendra “Yeah, that's true! I have some uhh, prior commitments I gotta do for SFC, too! I promised to help account for all the losses when the truck..."
    k "Kendra “Yeah... a lot of things inside it got damaged, too. Not to mention..."
    b "Is she looking at me—"
    b "Oh, nevermind, she looked away."
    k "Ahem— not to mention things outside work..."
    m "We all have more to do besides this contract."
    m "So! Bosses, what would it be?"
    k "Oh Y-yeah, Apollo, um, sorry... Not to step on your toes or anything, haha. You're the manager after all!"
    a "Ahaha, right! Noo, it’s fineee...haha!"

    a "Ahem—I couldn’t agree more! These are such great ideas, team, I’m so proud! Sooo..."
    a "MJ, since you brought it up I’ll make you in charge of contacting our clients for more information, as well as any potential sponsors!"
    m "No problem! I’ll do whatever you need me to."
    a "Kendra, you can stick to your regular storage room management."
    k "A-alright! Understood."
    a "Ah, Deez— I... maybe you can just observe?"
    d "Huh? But—I can be sooo useful! I can- I can do a lot of things!" 
    k "Uh, I can help him out! Here, Deez, you could come with me. I can show you how I, uh, manage the storage!" 

    d "If you read my resume, you’d know I already know how to do all of that. But... If you want."
    a "Great!"
    a "Barby, you can sort through what other SFC departments might be contacting us about! As well as filling out any forms we might need."
    a "Oh and maybe just checking on everyone, making sure they’re doing what they’re supposed to- Don’t worry, I’ll also be doing that with you!"
    b "You got it!"
    a "And I’ll be in charge of the overall presentation, organizing all the contact info, budget, timeline, and minutes of the meeting."
    m "Shouldn’t you have a secretary for that last one? Especially with your hand—"
    a "Oh! Uh... I suppose you’re right. If Deez and Kendra finish up their mentoring thing, maybe he can do it? Would you, Deez?"

    a "Aha, Not to take your assistant from you, Kendra?"

    k "Huh!?"

    m "What is with these two?"

    k "No, no, no, it’s okay! Yeah! Go ahead. I mean, I just offered to show him around so he could help out, haha! Instead of just, uh, watching. S-so if there’s other things for him to do already..."
    d "I can do {b}ALL{/b} of it."
    m "I’m sure you can."

    d "Wait... really? I mean- yeah. Of course I can."

    b "That’s great!"
    b "Wait... hold on..."

    $ said = []
    menu chat:
        set said
        "Digital Marketing":
            $ talked += 1
            b "But... uh, how about digital marketing? Gathering the data of what an effective marketing campaign means nowadays, all of that..."
            a "Oh... you’re right. Dave used to be pretty good at that."
            k "I-I used to do that for a volunteering program that I was handling once."
            a "You did? Wait... that’d be perfect! Could you, uh, handle that, too, Kendra?"
            k "I mean... sure, haha! I could do that!"
            b "Great!"
            a "Is there anything else?"
            b "Hm..."
            if talked < 3:
                jump chat
            else:
                b "That’s everything I can think of right now."
                a "Wonderful! I think that’s all for our meeting?"
                m "Yeah."
                d "Yes."
                k "Uhuh..."
                a "Awesome! Alright, team! We got this, I believe in us!"
                a "Well, that’s all for today! Thank you so so much for your cooperation! Have a good {i}Knight’s{/i} rest- haha- and I’ll see you tomorrow!"
                d "I get it. That’s her last name. Hahaha."
                jump clockingout
        "Social Media":
            $ talked += 1
            b "How about... social media? It’s pretty big when it comes to advertising nowadays... Do we have anyone who’s good with that?"
            a "Haha... Well, not me... Deez, you’re probably the youngest one here, right?"
            d "No—"
            a "Would you be able to do anything about that?"
            d "I’m... yes. I’m very social."
            a "Great!" 
            k "Um... I-I don’t know if..."
            m "Yeah... I see what you mean, Kendra."
            m "I mean, I’d offer to help but I just don’t know too much about that myself, either! My expertise lies somewhere else, sadly."
            k "... I-I could help him out with that if needed, haha... sometimes I have to, um, help with social media sites of the programs I’m part of."
            a "Oh! Um... that’s great! Well, if you want, you could handle that, too!"
            k "Sure...!"
            a "If that’s okay with you, Deez?"
            d "I can help her..."
            a "Perfect."
            a "Okie dokie, is that everything?"
            b "Um... let me see..."
            if talked < 3:
                jump chat
            else:
                b "That’s everything I can think of right now."
                a "Wonderful! I think that’s all for our meeting?"
                m "Yeah."
                d "Yes."
                k "Uhuh..."
                a "Awesome! Alright, team! We got this, I believe in us!"
                a "Well, that’s all for today! Thank you so so much for your cooperation! Have a good {i}Knight’s{/i} rest- haha- and I’ll see you tomorrow!"
                d "I get it. That’s her last name. Hahaha."
                jump clockingout
        "Picking up deliveries":
            $ talked += 1
            b "We’re gonna have some deliveries coming in from other departments, right? Or things we have to pick up from other buildings?"
            a "You’re right! For this project and other things, correct?" 
            a "Who’s gonna be in charge of going down and getting them?"
            b "Um, I’m gonna mostly be on the computer doing... pretty monotonous things, so maybe a walk around could be good for me, haha."
            a "Barby... we’re not making you do that..."
            a "Agh... maybe I should-"
            m "Nuh uh. Let’s not have you carrying things here."
            m "I can carry anything under 5 pounds very easily, so I could handle it!"
            b "...MJ... I don’t think any of the deliveries are going to be under 5 pounds."
            m "Oh... Well..." 
            a "Deez?"
            b "Would he know where the other departments are?" 

            d "Of course I do."
            a "Wow! That settles it, then!"
            k "Um. I don’t think..."
            k "Apollo... I-I don’t think he does..."

            a "But, he just said—"
            b "Kendra was really fast at bringing things around, earlier."
            k "Huh?"
            b "I mean... she seems, like, really trustworthy with this kind of stuff."
            k "I mean, yeah, I could bring things around pretty quick...! I-if you need me to."
            a "Oh yeah! She’s always zooming around with those roller skates! Not to mention, she’s never broken anything she’s transported, I think."
            d "U- Ah- E... O. Yeah... Yeah."
            m "Kendra can carry a lot more than I can, I have to admit."
            a "Okay! Kendra can handle things that need picking up. Does that settle it?"
            k "O-oohh... I see, okay. I-I can do that too, I guess..." 
            b "Let’s see..."
            if talked < 3:
                jump chat
            else:
                b "That’s everything I can think of right now."
                a "Wonderful! I think that’s all for our meeting?"
                m "Yeah."
                d "Yes."
                k "Uhuh..."
                a "Awesome! Alright, team! We got this, I believe in us!"
                a "Well, that’s all for today! Thank you so so much for your cooperation! Have a good {i}Knight’s{/i} rest- haha- and I’ll see you tomorrow!"
                d "I get it. That’s her last name. Hahaha."
                jump clockingout

label clockingout:
    scene room_2
    show overlay
    show apo worriedt
    a "Hey, uhm, Barby? Do you have a minute? I just wanted to talk to you about something I’ve noticed about you today..."

    a "You’ve been acting a little off all day, and I know it’s probably just some sort of first day jitters after being gone for so long but..."
    a "If there’s something wrong, you can always talk to me! Please do, I’m worried about you."
    show apo worried
    b "Oh! Aw, c’mon, Apollo... It's just stress. The usual, the normal."
    b "Am I really acting that odd!? I don’t mean to... ough... it’s really nothing I can’t handle—"
    show apo worriedt at downward
    a "Maybe... but— maybe it’s something {i}we{/i} can handle? Like... as friends, you know?"
    show apo worried
    b "Ough... uhm..."
    
    a "..."
    show apo worriedt at up
    a "Is it... is it about you being promoted to assistant manager?"
    a "I’m sorry. I don’t think I properly explained to you, um, what happened there..."
    a "Could you give me a chance to explain? Please? Just hear me out!" 
    show apo worried
    b "Yeah... alright. But- it’s not that big of a deal! Please don’t be worried about me."
    show apo worriedt at downward
    a "But Barby! I AM worried about you! I care about you lots! C’mon, just... {i}how do you say ‘be normal... ‘but nicer... {/i}"
    a "Beee... you know— Let me worry about you!" 
    show apo worried
    b "Okay... yeah... I-I get it. Sorry... thank you."
    b "You can... you can talk about it...! I’m here if you need to chat...!" 
    a "..."
    show apo worriedt
    a "Thank you..."
    a "So, it all started in the hospital..."

    show black with fade

    "..."

    hide black
    
    show apo defaultt at jumper
    a "Oh! Don’t flashback, man, I gotchu!"
    
    a "It aaalll started when I woke up in the hospital! I was wrapped like a mummy, and you were there too! Still knocked out, though." 
    a "Suddenly, a SFC agent came in with a stack of papers—and some flowers!"
    show apo default
    b "That was kind of them to bring you flowers. Not a lot of workplaces would do that."
    show apo defaultt
    a "That's exactly what they told me!"
    a "But I was like—"
    show apo worriedt
    a "Oh my death!! Aaah! WHY AM I HERE?!"
    show apo defaultt at jumper
    a "Then the agent said oho, you know your Mr. Sensin the manager died, right? And you’re the assistant manager, riiighht?"
    show apo worriedt
    a "And I went oh no! He died? I’m so sorry! Does he have a preplanned mortuary or funeral home because I can totally hook him up—"
    show apo default
    b "Apollo, your advertisement is showing."
    show apo defaultt
    a "Hey, that’s exactly what the agent said! Anyway, they told me that I’m the new manager for the team! It was shock after shock after shock!" 
    show apo default
    b "Oh no, that sounds pretty scary..."
    show apo defaultt
    a "That’s the least of it! They strutted up to me and asked {i}’So who’s your new assistant manager?’{/i} Like WHAT? I can’t decide that fast!"
    a "I didn't know what to do! I was like running through different people in my head and then I thought, oh! Barby’s really cool and loves helping people!"
    a "But, all I did was turn my head to look you in your bed, and and—" 
    a "They nodded and said {i}’Oh so Fredrick Ibarra is your new assistant? Perfect, thank you!’{/i} and started walking away!"
    a "Then I said ‘Wait! What about him?! He can’t consent and sign or anything!’{/i}"
    a "{i}’Oh its okay, we signed it for him! Come to work within 6-7 weeks or you’re BOTH fired! Goodbye!’{/i}"
    a "The worst part is that they didn't even leave the flowers, they just brought them in, showed them, and left..."
    a "And that’s the end of my flashback via post-it-notes." 
    show apo default
    b "Oh... man... I didn’t..."
    b "I didn’t realize it... all happened like that..."
    b "I’m sorry for, like, being weird about it. Man. I’m really, really sorry. Sorry that it happened and how I’ve been acting about it."
    show apo defaultt
    a "Awhh, it’s okay Barbs! I mean, I get why you’d be weird about it, I just wanted to talk to you properly."
    a "Sorry it took me so long... I had to gather my thoughts."
    a "And illustrating the post-it-notes. It was my daily hand therapy activity for today."
    a "It’s not like I didn’t think you weren’t qualified to do it, it was the opposite! I just wasn’t sure you wanted to, either... I swear I wasn’t gonna sign you up without your consent."
    a "You know how I am with boundaries! That's the first priority in any friendship."
    show apo default
    b "Yeah. Yeah, that’s true!"
    b "Thanks, Apollo. You’re right. You... always try your best to be a good friend."
    show apo defaultt
    a "Aww, really Barby? Do you... forgive me?"
    show apo default
    b "Of course! I’m sorry, too, it’s been real weird and stressful, and you having to be the manager and all..."
    b "But, hey! We got this!"
    b "We got a few weeks to work on this, and a few really cool people; we can do this! Teamwork!"
    show apo defaultt
    a "Yay! Teamwork!"
    a "Amazing! Amaze amaze!"
    a "See you tomorrow, Barby!"
    show apo default
    b "Haha! Yeah! See you tomorrow, Aporrow!"
    b "That was bad, sorry, haha."
    show apo defaultt
    a "Oh, you’re so funny Barby—..."
    
    a "But to be honest? I’ve... oooh it hurts tummy just to say this but! I’ve kinda got... like, 99 bad feelings about all of this."
    a "But! I got one good feeling ‘bout it, and that's all we need to stay positive."
    a "So let’s focus on that, and not the 99 bad ones!"
    
    jump day2

label day2:
    "hi."