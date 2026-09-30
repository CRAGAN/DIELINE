label start:
    #scene bg barbyclocksin
    #sfx clockin
    window hide
    $ quick_menu = False
    voice "audio/Barby/Day 1 Intro/barby_line001.mp3"
    b_sub "Shucks... I haven’t seen her since we got discharged."
    voice "audio/Barby/Day 1 Intro/barby_line002.mp3"
    b_sub "It should be fine. It should be normal."
    voice "audio/Barby/Day 1 Intro/barby_line003.mp3"
    b_sub "I can’t waste time overthinking."

    # Barby walks into manager room cg
    #sfx walking
    scene apollomanagersroom with fade
    voice "audio/Barby/Day 1 Intro/barby_line004.mp3"
    b_sub "...Hiya, Apollo—I mean—boss! Good to see you again!"
    voice "audio/Apollo/Day 1 Intro/apollo_line001.mp3"
    a_sub "Oh, good morning Barby! Y—you don’t have to call me boss, I’m just your regular ol’ Apollo!" 
    voice "audio/Barby/Day 1 Intro/barby_line005.mp3"
    b_sub "Oh! Snap! Sorry, boss. SHOOT! AH!"    
    voice "audio/Apollo/Day 1 Intro/apollo_line002.mp3"
    a_sub "Haha, every time you call me boss, I’m calling you boss, too! It’s only fair with all those emails you’ve sent with my name."
    voice "audio/Barby/Day 1 Intro/barby_line006.mp3"
    b_sub "Aw—hey, you know it was an accident... You have my account, too. How’d {i}you{/i} not get confused?"
    voice "audio/Apollo/Day 1 Intro/apollo_line003.mp3"
    a_sub "I triple dipple check all the time!"
    voice "audio/Barby/Day 1 Intro/barby_line007.mp3"
    b_sub "Wow! Please don’t say that word again." 
    voice "audio/Apollo/Day 1 Intro/apollo_line004.mp3"
    a_sub "Uhh... okay? But really, Apollo’s just fine and dandy."
    scene managerroom with dissolve
    show overlay:
        blend 'multiply'
    show apo defaultt at downward, center
    voice "audio/Apollo/Day 1 Intro/apollo_line005.mp3"
    $ quick_menu = True
    a_sub "And hey, congratulations on {i}your{/i} promotion...! I mean look at you, ohoho, assistant manager now? You’re totally killing it!"
    show apo default at center, jumper
    voice "audio/Barby/Day 1 Intro/barby_line008.mp3"
    b_sub  "Ahh...! Thank you. Killing it, haha, just like. The."
    show apo awkward at jumper
    voice "audio/Barby/Day 1 Intro/barby_line009.mp3"
    b_sub "Truck."
    show apo worried at up
    voice "audio/Apollo/Day 1 Intro/apollo_line006.mp3"
    a_sub "Oh!"
    # add image of sensin and truck
    scene picture:
        subpixel True
        zoom 1.5 xoffset -500
        easein 20 zoom 1.2 xoffset -200
    with fade
    voice "audio/Apollo/Day 1 Intro/apollo_line007.mp3"
    a_sub "The truck that killed our old manager?"
    voice "audio/Apollo/Day 1 Intro/apollo_line008.mp3"
    a_sub "Yes, it was a sudden end, but that's just the cycle of life and death: a truly beautifully inevitable part of us all. I hope Mr. Sensin is resting easy now."
    voice "audio/Barby/Day 1 Intro/barby_line010.mp3"
    b_sub "...Wow."
    voice "audio/Apollo/Day 1 Intro/apollo_line009.mp3"
    a_sub "He’s in good hands now—I’d know! Teehee!"
    voice "audio/Barby/Day 1 Intro/barby_line011.mp3"
    b_sub "At least that was taken care of..." 
    # back to the scene
    scene managerroom
    show overlay:
        blend 'multiply'
    show apo default at jumper, center
    with dissolve
    voice "audio/Barby/Day 1 Intro/barby_line012.mp3"
    b "Speaking of, have you heard back from your insurance? About the accident?" 
    show apo worriedt at downward
    voice "audio/Apollo/Day 1 Intro/apollo_line010.mp3"
    a "Oh goodness, no, I haven’t! Have you? I’m worried..." 
    show apo worried
    voice "audio/Barby/Day 1 Intro/barby_line013.mp3"
    b "Agh, don’t be worried!"
    voice "audio/Barby/Day 1 Intro/barby_line014.mp3"
    b "I’ll handle it for both of us :)! I don’t have too much to do yet, since it seems like a lot of my rensibilities are waiting on others." 
    show apo worriedt at downward
    voice "audio/Apollo/Day 1 Intro/apollo_line011.mp3"
    a "Are you sure? I know we’re supposed to fill it out together... Sorry, but being the new manager sure has me a little frazzled. Maybe I can still help out—?" 
    show apo worried
    voice "audio/Barby/Day 1 Intro/barby_line015.mp3"
    b "You’ve got a whole team to handle. I'd be happy to help out!"
    voice "audio/Barby/Day 1 Intro/barby_line016.mp3"
    b "That’s what {i}assistant manager{/i} means, after all. Let me {i}assist{/i} my manager."
    show apo defaultt at downward, center
    voice "audio/Apollo/Day 1 Intro/apollo_line012.mp3"
    a "I—you’re right. We got this, we have to stay positive for our first day! Well, if you’re up for it... here!"
    # IDs come out
    # sfx_id1
    voice "audio/Apollo/Day 1 Intro/apollo_line013.mp3"
    a "I know we just clocked in, but it’s a pretty easy task. Could you distribute the new IDs to the team?" 
    voice "audio/Apollo/Day 1 Intro/apollo_line014.mp3"
    a "I’d do it myself, but I have to attend this online conference with corporate. I have yet to figure out how to log into Skycloud Meet, haha..."
    show apo default
    $ picked = []
    menu idchoice:
        set picked
        "Skycloudmeet?":
            voice "audio/Barby/Day 1 Intro/barby_line017.mp3"
            b "We switched to Skycloud Meet already?"
            show apo awkwardt at downward
            voice "audio/Apollo/Day 1 Intro/apollo_line015.mp3"
            a "Err, yeah. It’s supposed to work better with the other Sera, Fim & Co. software we’re using, yet..."
            show apo defaultt
            voice "audio/Apollo/Day 1 Intro/apollo_line016.mp3"
            a "It’s kinda complicated. I’m not good at technology— but I’m positive I’ll figure it out!"
            show apo default
            jump idchoice
            # return to choices

        "But I don't know the team.":
            voice "audio/Barby/Day 1 Intro/barby_line018.mp3"
            b "Ah, but I don’t even know who’s part of the team yet."
            show apo defaultt
            voice "audio/Apollo/Day 1 Intro/apollo_line017.mp3"
            a "It’s okay, you already know most of them by now! All their names and faces are on their IDs too, so you can figure it out easy peasy!"
            show apo default
            jump idchoice
            # return to choices

        "Sure! Easy!":
            
            jump id_see 
            

label id_see:
    voice "audio/Barby/Day 1 Intro/barby_line019.mp3"
    b "Alright, no problem, then! I can do that."
    show apo defaultt
    voice "audio/Apollo/Day 1 Intro/apollo_line018.mp3"
    a "Sweet! Here you go!"
    $ quick_menu = False    
    show apo default
    hide apo with dissolve

    call screen id_screen with dissolve

   
label rooms:
    $ storage = False
    $ janitor = False
    $ bathroom = False
    $ managerroom = False
    $ quick_menu = False

    if talkedtodeez and talkedtokendra and talkedtomj: 
        scene black with dissolve
        voice "audio/Barby/Day 1 ID/barby_line0142.mp3"
        $ quick_menu = True
        b "I think that’s everyone! I haven't seen Dave around... he's probably working from home again."
        voice "audio/Barby/Day 1 ID/barby_line0143.mp3"
        b "He doesn't live too far from here, so if I ship his ID now, he should receive it soon!"
        voice "audio/Barby/Day 1 ID/barby_line0144.mp3"
        b "Just gotta get on my computer."
        $ current_room = 2
        $ talkedtokendra = False
        $ talkedtoapollo = False
        $ talkedtomj = False
        $ talkedtodeez = False
        #call screen email_minigame # FROG OVER HERE
        jump breaktime1
    call screen rooms with fade
    # call screen officewalkl
    # if current_id == "M.J Grey":
    #     b "Alright, gotta go check on some things!"
    #     m "Okay! Let me know if you need help!"
    #     b "Let me know if—! Aww man."
    #     m "I win, heh." 
    #     call screen officewalk


label meeting:
    $ talked = 0
    scene room_2
    show overlay:
        blend 'multiply'
    show apo defaultt at center:
        xoffset -150
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line043.mp3"
    a "Hello everyone! I’m so glad you all made it! It’s nice to see you all again, it’s been such a long time!"
    show ken defaultt at left
    show apo default
    voice "audio/Kendra/Day 1 TM/kendra_line036.mp3"
    k "Uhh yeah, I guess it’s been a while, huh. I think– I think uh around 6 weeks, right?"
    show de defaultt at right
    show ken default
    d "Yes."
    show ken awkwardt
    show de default
    voice "audio/Kendra/Day 1 TM/kendra_line037.mp3"
    k "Deez, you weren’t even here 6 weeks ago???"
    show ken awkward
    show de shyt
    d "I knew that."
    show de default 
    show apo defaultt
    show ken surprised
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line044.mp3"
    a "I have a few announcements regarding our latest project!"
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line045.mp3"
    a "But, before we begin, I have one thing to address..."
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line046.mp3"
    a "I’m sure you’re all wondering about my suddenly horrible handwriting and Barby’s little wobble bobble."
    show apo default
    voice "audio/Barby/Day 1 TM/barby_line146.mp3"
    b worriedt "My {b}{i}what{/i}{/b}!?"
    show m defaultt at center:
        xoffset 250
    voice "audio/MJ/Day 1 TM/MJ_line024.mp3"
    m "Uh-Well I wasn’t gonna ask out of courtesy, buuut if you’re open to talking about it, I’m all ears."
    show m default
    show de defaultt
    d "According to my informittants, he usually wears shorts since he hates pants."
    d "He is hiding something most suspicious. That is a flaw in fashion. Everybody would know that wearing shorts for a workday is not very formal attire."
    show de thinkingt
    d "That’s the real wobble bobble."
    show de default
    voice "audio/Kendra/Day 1 TM/kendra_line038.mp3"
    k "Did– did you mean informants or-? {i}And I didn’t say anything about him hating it—{/i}"
    show de defaultt
    d "I meant what I said, and I said what I meant."
    show de shy
    show apo defaultt
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line047.mp3"
    a "So intellectual of you Deez, so observant! And you just got here!"
    show apo default
    voice "audio/Barby/Day 1 TM/barby_line147.mp3"
    b "Wait- I don’t hate pants- what-!?" 
    show apo awkwardt
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line048.mp3"
    a "So uhm unfortunately, this is what happened to my left hand..."
    show m hmt
    #CG_She rolls up her sleeves and reveals super scarred left arm from hand till shoulder
    voice "audio/MJ/Day 1 TM/MJ_line025.mp3"
    m "Oh goodness."
    show m hm
    show de surprised
    #VA: genuinely shocked but trying to be nonchalant, like a short sigh/exhale
    d "..."
    show ken worried
    voice "audio/Kendra/Day 1 TM/kendra_line039.mp3"
    k "Agh..."
    voice "audio/Barby/Day 1 TM/barby_line148.mp3"
    b "Yeah..." 
    show apo awkwardt
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line049.mp3"
    a "And you all already know what happened to Barby’s leg—"
    show apo awkward
    voice "audio/Barby/Day 1 TM/barby_line149.mp3"
    b "WHAT!?" 
    # 
    show apo defaultt
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line050.mp3"
    a "You don’t need to adjust too much for me, but please take it easy on him since he just got his prosthetic fitted recently."
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line051.mp3"
    a "I hope you all can make accommodations for him!"
    show apo awkward
    show ken worried
    voice "audio/Kendra/Day 1 TM/kendra_line040.mp3"
    k "!?!?!??!"
    show de surprisedt
    d "PROZEMPIC!?!??!"
    show m hm
    show de surprised
    voice "audio/MJ/Day 1 TM/MJ_line026.mp3"
    m "Oh?!?!?"
    voice "audio/Barby/Day 1 TM/barby_line150.mp3"
    b "{i}I’M BEING OUTED!?{/i}"
    show apo worriedt
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line052.mp3"
    a "OH! Did— did you not tell them Barby?! I’m so sorry, I thought you told everyone!!" 
    show apo worried
    voice "audio/Barby/Day 1 TM/barby_line151.mp3"
    b "..."
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line053.mp3"
    a "..."
    show m hmt
    show de default
    voice "audio/MJ/Day 1 TM/MJ_line027.mp3"
    m "Do you need help with that?" 
    show m hm
    show ken worriedt
    voice "audio/Kendra/Day 1 TM/kendra_line041.mp3"
    k "MJ!? I—I don’t know if you can really help with that!"
    show ken worried
    show m hm
    voice "audio/MJ/Day 1 TM/MJ_line028.mp3"
    m "What? Just trying to offer accomodation like Apollo said."
    show m hmt
    voice "audio/MJ/Day 1 TM/MJ_line029.mp3"
    m "By the way, Deez... Prozempic isn’t really a thing. Osempic doesn’t produce Prozac as far as I’m aware." 
    show de angryt
    d "Errrgh... noted..." 
    
    d "I didn’t ask... no one asked... Who’s MJ talking to, huh..."
    show de shy
    voice "audio/Barby/Day 1 TM/barby_line152.mp3"
    b "Okay... thank you... but I don’t really need all that extra help! I’m really okay- most of my job is on the computer, anyways..." 
    voice "audio/Barby/Day 1 TM/barby_line153.mp3"
    b "We have more important things to talk about right now, haha...!" 
    show ken awkwardt
    voice "audio/Kendra/Day 1 TM/kendra_line042.mp3"
    k "Are we just gonna—"
    show ken awkward
    voice "audio/Barby/Day 1 TM/barby_line154.mp3"
    b "A–Apollo??"
    show apo worriedt
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line054.mp3"
    a "Ah yes, of course! Haha, thank you all for your cooperation! Moving on—"
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line055.mp3"
    a "The meeting with the higher ups was... definitely something! I think I could explain this better with a little help!"
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line056.mp3"
    a "Barby, if you could please help me demonstrate what happened?" 
    show apo worried
    voice "audio/Barby/Day 1 TM/barby_line155.mp3"
    b "Sure!"
    show ken awkwardt
    voice "audio/Kendra/Day 1 TM/kendra_line043.mp3"
    k "Oh uhh, was the meeting really that bad? W-why do we need a little—play thing?" 
    show ken awkward
    show m happyt
    voice "audio/MJ/Day 1 TM/MJ_line030.mp3"
    m "Apollo does this when things are hard to explain. Please, go on, boss!" 
    show m happy
    show apo worriedt
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line057.mp3"
    a "A... You can just call me Apollo, MJ! Haha."
    show apo worried
    
    "..."
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line058.mp3"
    scene meetingbg
    show overlay:
        blend 'multiply' alpha 0.5
    show apol happy
    show barb neutral
    show dee neutral
    show mjj neutral
    show kend neutral
    show meetingfg 

    with fade
    a_sub "Ahem! Hello, I am the big boss here to give you your project! Ask me anything!"
    voice "audio/Barby/Day 1 TM/barby_line156.mp3"
    
    b_sub "Hiya big boss! I have a few questions to ask, such as what {i}is{/i} our client’s new product we’re supposed to market?"
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line059.mp3"
    a_sub "Oh, silly manager, it’s not a product, it’s a lifestyle!" 
    voice "audio/Barby/Day 1 TM/barby_line157.mp3"
    b_sub "Okay, what is this lifestyle we are trying to promote?"
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line060.mp3"
    a_sub "It’s a life changing lifestyle to promote healthier and happier clients! A way of existence, if you will."
    voice "audio/Kendra/Day 1 TM/kendra_line044.mp3"
    k_sub "Wait what? How—how are we supposed to promote this?"
    voice "audio/Barby/Day 1 TM/barby_line158.mp3"
    b_sub "Stay in character, please...!"
    voice "audio/Kendra/Day 1 TM/kendra_line045.mp3"
    k_sub "O...okay! How are we supposed to promote this, big boss?"
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line061.mp3"
    a_sub "By promoting the lifestyle with the same great enthusiasm you’re bringing into this meeting right now!"
    voice "audio/MJ/Day 1 TM/MJ_line031.mp3"
    m_sub "Ah. So it’s not an actual... item?"
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line062.mp3"
    a_sub "Oh, it is! But it’s more than that." 
    d_sub "Raising my hand."
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line063.mp3"
    a_sub "Yes, little sweet intern—"
    voice "audio/Barby/Day 1 TM/barby_line159.mp3"
    b_sub "Noo....he’s Apollo..."
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line064.mp3"
    a_sub "Ough—I’m sorry—"
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line065.mp3"
    a_sub "I mean manager!" 
    d_sub "Oh. Um. Uh..."
    
    d_sub "Aaa... Ohh! Ohhhh! S-So we weren’t given any information but have to do it, anyway? That’s like... a paradox."

    d_sub "Deez would know what that means..."
    d_sub "But Apollo, me, doesn’t know what we’re supposed to do?" 
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line066.mp3"
    a_sub "Haha, no, no! Not if you think {i}outside{/i} the box."
    voice "audio/Kendra/Day 1 TM/kendra_line046.mp3"
    k_sub "B—but. Ahem. In character. How the heck are we supposed to think outside the box, i-if— If we don’t even know what we’re doing?"
    voice "audio/Kendra/Day 1 TM/kendra_line047.mp3"
    k_sub "This—This doesn’t make any sense at all! Why are they so vague? I—I don’t like this! Ugh... this is g—gonna make everything harder..."
    voice "audio/MJ/Day 1 TM/MJ_line032.mp3"
    m_sub "I’m sorry you’re going through this confusion. Let me think of what I can do to help."
    d_sub "Since everyone is no longer doing voices I will stop doing voices, too."
    voice "audio/Barby/Day 1 TM/barby_line160.mp3"
    b_sub "Aw man."
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line067.mp3"
    a_sub "It’s okay, Barbyyy! You’ll get ‘em next time."
    voice "audio/MJ/Day 1 TM/MJ_line0393.mp3"
    m_sub "Maybe I can ask the client directly to help ease the situation."
    d_sub "Well, {i}yeah{/i} MJ, that’s what a marketing employee’s {i}supposed{/i} to do, haha. Hah."
    d_sub "A-anyway uhh, I totally agree with everyone here. We just have to figure out big boss’ super easy puzzle words."
    voice "audio/MJ/Day 1 TM/MJ_line034.mp3" 
    m_sub "Thanks for your cooperation and understanding. The intern’s right! We just have to figure it out, then it’ll be fine."
    d_sub "{i}Yeah. I’m always right.{/i}"
    voice "audio/Kendra/Day 1 TM/kendra_line048.mp3"
    k_sub "O–okay, I think? None of you are, err, really helping here! Is there anything else they said that was important?"
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line068.mp3"
    a_sub "I’m sorry but... I really didn’t get anything other than it being such a {i} convenient and life changing product that will make consumers feel sweeter than the sweet release{/i}."
    voice "audio/MJ/Day 1 TM/MJ_line035.mp3"
    m_sub "...Death reference? Was that just an Apollo thing or...?"
    voice "audio/Barby/Day 1 TM/barby_line161.mp3"
    b_sub "No, they actually said that. She told me earlier."
    voice "audio/MJ/Day 1 TM/MJ_line036.mp3"
    m_sub "They ACTUALLY said that?"
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line069.mp3"
    a_sub "Yeah, no. They did." 
    voice "audio/Kendra/Day 1 TM/kendra_line049.mp3"
    k_sub "Okay—I think we need to make a game plan now, we can’t just sit by and—and not do anything!"
    voice "audio/MJ/Day 1 TM/MJ_line037.mp3"
    m_sub "That's about right! Honestly, if we can do this as efficiently as possible, it'll be smooth sailing from here."
    voice "audio/MJ/Day 1 TM/MJ_line038.mp3"
    m_sub "Which is why I think we should contact the clients directly ourselves, first."
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line070.mp3"
    a_sub "Aha... but, I just spoke with them—"
    voice "audio/Kendra/Day 1 TM/kendra_line050.mp3"
    k_sub "I was thinking, maybe, i-if we did it through emails we can have a more cohesive backlog of all the information they give us...! All our questions included."
    d_sub "Uhm, actually— some of us still have A LOT of other responsibilities besides the project - like uhh, general work... things."
    voice "audio/Kendra/Day 1 TM/kendra_line051.mp3"
    k_sub "Yeah, that's true! I have some uhh, prior commitments I gotta do for SFC, too! I promised to help account for all the losses when the truck..."
    voice "audio/Kendra/Day 1 TM/kendra_line052.mp3"
    k_sub "Yeah... a lot of things inside it got damaged, too. Not to mention..."
    voice "audio/Barby/Day 1 TM/barby_line162.mp3"
    b_sub "Is she looking at me—"
    voice "audio/Barby/Day 1 TM/barby_line163.mp3"
    b_sub "Oh, nevermind, she looked away."
    voice "audio/Kendra/Day 1 TM/kendra_line053.mp3"
    k_sub "Ahem— not to mention things outside work..."
    voice "audio/MJ/Day 1 TM/MJ_line039.mp3"
    m_sub "We all have more to do besides this contract."
    voice "audio/MJ/Day 1 TM/MJ_line040.mp3"
    m_sub "So! Bosses, what would it be?"
    voice "audio/Kendra/Day 1 TM/kendra_line054.mp3"
    k_sub "Oh Y-yeah, Apollo, um, sorry... Not to step on your toes or anything, haha. You're the manager after all!"
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line071.mp3"
    a_sub "Ahaha, right! Noo, it’s fineee...haha!"
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line072.mp3"
    a_sub "Ahem—I couldn’t agree more! These are such great ideas, team, I’m so proud! Sooo..."
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line073.mp3"
    a_sub "MJ, since you brought it up I’ll make you in charge of contacting our clients for more information, as well as any potential sponsors!"
    voice "audio/MJ/Day 1 TM/MJ_line041.mp3"
    m_sub "No problem! I’ll do whatever you need me to."
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line074.mp3"
    a_sub "Kendra, you can stick to your regular storage room management."
    voice "audio/Kendra/Day 1 TM/kendra_line055.mp3"
    k_sub "A-alright! Understood."
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line075.mp3"
    a_sub "Ah, Deez— I... maybe you can just observe?"
    d_sub "Huh? But—I can be sooo useful! I can- I can do a lot of things!" 
    voice "audio/Kendra/Day 1 TM/kendra_line056.mp3"
    k_sub "Uh, I can help him out! Here, Deez, you could come with me. I can show you how I, uh, manage the storage!" 

    d_sub "If you read my resume, you’d know I already know how to do all of that. But... If you want."
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line076.mp3"
    a_sub "Great!"
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line076.mp3"
    a_sub "Barby, you can sort through what other SFC departments might be contacting us about! As well as filling out any forms we might need."
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line078.mp3"
    a_sub "Oh and maybe just checking on everyone, making sure they’re doing what they’re supposed to- Don’t worry, I’ll also be doing that with you!"
    voice "audio/Barby/Day 1 TM/barby_line164.mp3"
    b_sub "You got it!"
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line079.mp3"
    a_sub "And I’ll be in charge of the overall presentation, organizing all the contact info, budget, timeline, and minutes of the meeting."
    voice "audio/MJ/Day 1 TM/MJ_line042.mp3"
    m_sub "Shouldn’t you have a secretary for that last one? Especially with your hand—"
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line077.mp3"
    a_sub "Oh! Uh... I suppose you’re right. If Deez and Kendra finish up their mentoring thing, maybe he can do it? Would you, Deez?"
    voice "audio/Apollo/Day 1 Team Meeting/apollo_line078.mp3"
    a_sub "Aha, Not to take your assistant from you, Kendra?"
    voice "audio/Kendra/Day 1 TM/kendra_line057.mp3"
    k_sub "Huh!?"
    voice "audio/MJ/Day 1 TM/MJ_line043.mp3"
    m_sub "What is with these two?"
    voice "audio/Kendra/Day 1 TM/kendra_line058.mp3"
    k_sub "No, no, no, it’s okay! Yeah! Go ahead. I mean, I just offered to show him around so he could help out, haha! Instead of just, uh, watching. S-so if there’s other things for him to do already..."
    d_sub "I can do {b}ALL{/b} of it."
    voice "audio/MJ/Day 1 TM/MJ_line044.mp3"
    m_sub "I’m sure you can."

    d_sub "Wait... really? I mean- yeah. Of course I can."
    voice "audio/Barby/Day 1 TM/barby_line165.mp3"
    b_sub "That’s great!"
    voice "audio/Barby/Day 1 TM/barby_line166.mp3"
    b_sub "Wait... hold on..."

    $ said = []
    menu chat:
        set said
        "Digital Marketing":
            $ talked += 1
            voice "audio/Barby/Day 1 TM/barby_line167.mp3"
            b_sub "But... uh, how about digital marketing? Gathering the data of what an effective marketing campaign means nowadays, all of that..."
            a_sub "Oh... you’re right. Dave used to be pretty good at that."
            voice "audio/Kendra/Day 1 TM/kendra_line059.mp3"
            k_sub "I-I used to do that for a volunteering program that I was handling once."
            voice "audio/Apollo/Day 1 Team Meeting/apollo_line079.mp3"
            a_sub "You did? Wait... that’d be perfect! Could you, uh, handle that, too, Kendra?"
            voice "audio/Kendra/Day 1 TM/kendra_line060.mp3"
            k_sub "I mean... sure, haha! I could do that!"
            voice "audio/Barby/Day 1 TM/barby_line168.mp3"
            b_sub "Great!"
            a_sub "Is there anything else?"
            voice "audio/Barby/Day 1 TM/barby_line169.mp3"
            b_sub "Hm..."
            if talked < 3:
                jump chat
            else:
                voice "audio/Barby/Day 1 TM/barby_line179.mp3"
                b_sub "That’s everything I can think of right now."
                voice "audio/Apollo/Day 1 Team Meeting/apollo_line101.mp3"
                a_sub "Wonderful! I think that’s all for our meeting?"
                m_sub "Yeah."
                d_sub "Yes."
                voice "audio/Kendra/Day 1 TM/kendra_line069.mp3"
                k_sub "Uhuh..."
                voice "audio/Apollo/Day 1 Team Meeting/apollo_line102.mp3"
                a_sub "Awesome! Alright, team! We got this, I believe in us!"
                voice "audio/Apollo/Day 1 Team Meeting/apollo_line103.mp3"
                a_sub "Well, that’s all for today! Thank you so so much for your cooperation! Have a good {i}Knight’s{/i} rest- haha- and I’ll see you tomorrow!"
                d_sub "I get it. That’s her last name. Hahaha."
                jump clockingout
        "Social Media":
            $ talked += 1
            voice "audio/Barby/Day 1 TM/barby_line170.mp3"
            b_sub "How about... social media? It’s pretty big when it comes to advertising nowadays... Do we have anyone who’s good with that?"
            a_sub "Haha... Well, not me... Deez, you’re probably the youngest one here, right?"
            d_sub "No—"
            a_sub "Would you be able to do anything about that?"
            d_sub "I’m... yes. I’m very social."
            a_sub "Great!" 
            voice "audio/Kendra/Day 1 TM/kendra_line061.mp3"
            k_sub "Um... I-I don’t know if..."
            voice "audio/MJ/Day 1 TM/MJ_line045.mp3"
            m_sub "Yeah... I see what you mean, Kendra."
        
            m_sub "I mean, I’d offer to help but I just don’t know too much about that myself, either! My expertise lies somewhere else, sadly."
            voice "audio/Kendra/Day 1 TM/kendra_line062.mp3"
            k_sub "... I-I could help him out with that if needed, haha... sometimes I have to, um, help with social media sites of the programs I’m part of."
            a_sub "Oh! Um... that’s great! Well, if you want, you could handle that, too!"
            voice "audio/Kendra/Day 1 TM/kendra_line063.mp3"
            k_sub "Sure...!"
            a_sub "If that’s okay with you, Deez?"
            d_sub "I can help her..."
            a_sub "Perfect."
            a_sub "Okie dokie, is that everything?"
            voice "audio/Barby/Day 1 TM/barby_line171.mp3"
            b "Um... let me see..."
            if talked < 3:
                jump chat
            else:
                voice "audio/Barby/Day 1 TM/barby_line179.mp3"
                b_sub "That’s everything I can think of right now."
                voice "audio/Apollo/Day 1 Team Meeting/apollo_line101.mp3"
                a_sub "Wonderful! I think that’s all for our meeting?"
            
                m_sub "Yeah."
                d_sub "Yes."
                voice "audio/Kendra/Day 1 TM/kendra_line069.mp3"
                k_sub "Uhuh..."
                voice "audio/Apollo/Day 1 Team Meeting/apollo_line102.mp3"
                a_sub "Awesome! Alright, team! We got this, I believe in us!"
                voice "audio/Apollo/Day 1 Team Meeting/apollo_line103.mp3"

                a_sub "Well, that’s all for today! Thank you so so much for your cooperation! Have a good {i}Knight’s{/i} rest- haha- and I’ll see you tomorrow!"
                d_sub "I get it. That’s her last name. Hahaha."
                jump clockingout
        "Picking up deliveries":
            $ talked += 1
            voice "audio/Barby/Day 1 TM/barby_line172.mp3"
            b_sub "We’re gonna have some deliveries coming in from other departments, right? Or things we have to pick up from other buildings?"
            voice "audio/Apollo/Day 1 Team Meeting/apollo_line92.mp3"
            a_sub "You’re right! For this project and other things, correct?" 
            voice "audio/Apollo/Day 1 Team Meeting/apollo_line93.mp3"
            a_sub "Who’s gonna be in charge of going down and getting them?"
            voice "audio/Barby/Day 1 TM/barby_line173.mp3"
            b_sub "Um, I’m gonna mostly be on the computer doing... pretty monotonous things, so maybe a walk around could be good for me, haha."
            voice "audio/Apollo/Day 1 Team Meeting/apollo_line94.mp3"
            a_sub "Barby... we’re not making you do that..."
            voice "audio/Apollo/Day 1 Team Meeting/apollo_line95.mp3"
            a_sub "Agh... maybe I should-"
            voice "audio/MJ/Day 1 TM/MJ_line047.mp3"
            m_sub "Nuh uh. Let’s not have you carrying things here."
            voice "audio/MJ/Day 1 TM/MJ_line048.mp3"
            m_sub "I can carry anything under 5 pounds very easily, so I could handle it!"
            voice "audio/Barby/Day 1 TM/barby_line174.mp3"
            b_sub "...MJ... I don’t think any of the deliveries are going to be under 5 pounds."
            voice "audio/MJ/Day 1 TM/MJ_line049.mp3"
            m_sub "Oh... Well..." 
            voice "audio/Apollo/Day 1 Team Meeting/apollo_line96.mp3"
            a_sub "Deez?"
            voice "audio/Barby/Day 1 TM/barby_line175.mp3"
            b_sub "Would he know where the other departments are?" 

            d_sub "Of course I do."
            voice "audio/Apollo/Day 1 Team Meeting/apollo_line97.mp3"
            a_sub "Wow! That settles it, then!"
            voice "audio/Kendra/Day 1 TM/kendra_line064.mp3"
            k_sub "Um. I don’t think..."
            voice "audio/Kendra/Day 1 TM/kendra_line065.mp3"
            k_sub "Apollo... I-I don’t think he does..."
            voice "audio/Apollo/Day 1 Team Meeting/apollo_line98.mp3"
            a_sub "But, he just said—"
            voice "audio/Barby/Day 1 TM/barby_line176.mp3"
            b_sub"Kendra was really fast at bringing things around, earlier."
            voice "audio/Kendra/Day 1 TM/kendra_line066.mp3"
            k_sub "Huh?"
            voice "audio/Barby/Day 1 TM/barby_line177.mp3"
            b_sub "I mean... she seems, like, really trustworthy with this kind of stuff."
            voice "audio/Kendra/Day 1 TM/kendra_line067.mp3"
            k_sub "I mean, yeah, I could bring things around pretty quick...! I-if you need me to."
            voice "audio/Apollo/Day 1 Team Meeting/apollo_line99.mp3"
            a_sub "Oh yeah! She’s always zooming around with those roller skates! Not to mention, she’s never broken anything she’s transported, I think."
            d_sub "U- Ah- E... O. Yeah... Yeah."
            voice "audio/MJ/Day 1 TM/MJ_line050.mp3"
            m_sub "Kendra can carry a lot more than I can, I have to admit."
            voice "audio/Apollo/Day 1 Team Meeting/apollo_line100.mp3"
            a_sub "Okay! Kendra can handle things that need picking up. Does that settle it?"
            voice "audio/Kendra/Day 1 TM/kendra_line068.mp3"
            k_sub "O-oohh... I see, okay. I-I can do that too, I guess..." 
            voice "audio/Barby/Day 1 TM/barby_line178.mp3"
            b_sub "Let’s see..."
            if talked < 3:
                jump chat
            else:
                voice "audio/Barby/Day 1 TM/barby_line179.mp3"
                b_sub "That’s everything I can think of right now."
                voice "audio/Apollo/Day 1 Team Meeting/apollo_line101.mp3"
                a_sub "Wonderful! I think that’s all for our meeting?"
                m_sub "Yeah."
                d_sub "Yes."
                voice "audio/Kendra/Day 1 TM/kendra_line069.mp3"
                k_sub "Uhuh..."
                voice "audio/Apollo/Day 1 Team Meeting/apollo_line102.mp3"
                a_sub "Awesome! Alright, team! We got this, I believe in us!"
                voice "audio/Apollo/Day 1 Team Meeting/apollo_line103.mp3"
                a_sub "Well, that’s all for today! Thank you so so much for your cooperation! Have a good {i}Knight’s{/i} rest- haha- and I’ll see you tomorrow!"
                d_sub "I get it. That’s her last name. Hahaha."
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
    a "{i}Then I said ‘Wait! What about him?! He can’t consent and sign or anything!’"
    a "{i}'Oh its okay, we signed it for him! Come to work within 6-7 weeks or you’re BOTH fired! Goodbye!'{/i}"
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

    