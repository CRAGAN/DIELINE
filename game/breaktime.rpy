# DAY1 BREAKTIME

label breaktime1:
    $ storage = False
    $ janitor = False
    $ bathroom = False
    $ managerroom = False

    if talkedtodeez and talkedtokendra and talkedtomj and talkedtoapollo:
        b "Ough... I gotta go to the conference room... team meeting..."
        b "So much talking to people..."
        jump meeting

    call screen breaktime1
label deezandapollo:
    # Apollo & Deez 
    if not talkedtodeez and not talkedtoapollo:
        $ talkedtodeez = True
        $ talkedtoapollo = True
        scene room_1 
        show overlay:
            blend 'multiply' alpha 0.3
        show apo defaultt at right:
            xoffset -250
        show de shy at left, downward:
            
            xoffset 250
        with fade
        
        a "Oh! Hi Deez, what’s up?"
        show apo default
        show de shyt
        d "Thank you... um... Ms. Knight for this wonderful ID you’ve bestowed upon me."
        d "This is so sweet. So spectacular. I love it so much..."

        #VA: like he’s declining a gift 
        show de defaultt at up
        d "But I do not need this."
        d "Ms. Apollo Knight. Manager, Ms. Apollo Knight." 
        show de default
        show apo awkwardt at downward
        a"Oh! Just Apollo’s fine—uhm... You don’t like it, then? I’m sorry, I know my handwriting is a mess, but I could try to just print it out and—"
        show de surprisedt
        show apo awkward at jumper
        d "Noo! No!!! It’s, it’s— I love. It’s... I love it. This ID, I’ll treasure it so bad. So good."
        show apo awkwardt at downward
        show de surprised 
        a"Are... are you sure? You said you didn’t need it; I don’t want to force you or anything"
        show apo awkward
        #VA: Almost like he’s hyperventilating, like its very clear he is pretending he likes it but doing a terrible job at it 
        show de thinkingt
        d "I want it. So bad. I just... I’ll keep it."
        show apo defaultt at up
        a "Ah! Erm... okay! Do what you want with it, alright?"
        show de defaultt
        d "A firm nation." 
        show apo default at jumper
        show de default at jump
        b "Hiya, folks! Do you need anything?"
        a "Oh! Hi, Barby! Just talking about the IDs. What’s up?"
        default aboutids = False
        default ears = False
        default smalltalk = False
        while not (aboutids and ears and smalltalk):
            menu:
                "The real IDs’ quality..." if not aboutids:
                    $ aboutids = True
                    b "The actual ID’s are... kind of not the best themselves."
                    b "MJ’s is already fading out, and it’s just the first day."

                    #VA: a bit proudly
                    show de happyt at jumper
                    d "Well, mine never fades."
                    show de calmt at downward
                    d "It’s laminated."
                    show de calm 
                    show apo defaultt
                    a"Laminated with love."
                    show apo default at jumper
                    show de default at jump
                # return

                "Ears?" if not ears:
                    $ ears = True
                    b "Happy Halloween, by the way!"
                    b "I noticed your costumes! You’ve both got little pointy ears?"
                    show apo defaultt 
                    a"My older brother plays a table top roleplaying game with his friends sometimes; it looks so fun!"
                    a"I’ve always wanted to try it, so I went as an elf!"
                    show apo default
                    b "Ohh... that sounds so fun..."
                    b "Maybe after work,we could try it out together sometime? For fun? We have enough people in the office for a party, after all." 
                    b "How about you, Deez?"

                    #VA Deez: randomly saying the movie, kind of tuning out the conversation  
        
                    show de defaultt at downward
                    d "Elf the Movie."
                    show apo default at jumper
                    show de default at jump
                # return

                "Small talk?" if not smalltalk:
                    $ smalltalk = True 

                    b "Right! Deez, have you heard about how Apollo and I met?"
                    show de defaultt
                    d "I know you guys are familiar with each other."
         
                    show de default at jump
                    b "Yeah! Familiar enough."
                    b "But have you heard how we met?"
                    show de thinkingt at downward
                    d "I’ve heard something, but you can share more details."
                    show de thinkingk
                    b "Oh... Well, it was ‘cause Apollo was really cool."
                    d "Yeah."
                    show apo defaultt at downward

                    a"Aw... Barbs..."
                    a"Well, Barby here got hired after a while of internship, but basically continued to work as a glorified intern for the next couple of years..."
                    show apo default
                    b "Yeah! It kind of... wasn’t the best, but when I started working with Apollo, well, I tried my best to help her out. Especially with her... technology." 
                    b "How’d the Skycloud meet go, by the way?"
                    show apo defaultt
                    a"I’ll host a team meeting to talk about that later!"
                    show apo default at jumper
                    show de defaultt
                    d "I’m really good at using Skycloud, too. I’ve met so many meetings in that app."
                    show de thinking at jump
                    b "Woah! An expert!?" 
                    show apo defaultt
                    a"Anyways, he helped me out a bunch and I helped tidy up his... reputation, so he’d start getting paid better, haha!"
                    show apo defaultt
                    b "Teamwork makes the dreamwork!"
                    b "Everyone else knows the gist of the story at this point. Just needed to catch you up so things make more sense while you’re here!"
                    show apo default at jumper
                
                    show de defaultt
                    d "Oh, yeah, I knew that."
                    b "Aw. He’s so knowledgeable. Apollo, you gotta hear him talk about things more."
                    show apo default at jumper
                    show de default at jump
                    a"I’m sure you did, you– you... geenieweenie, you Alberto Einsteino!" 
                    b "I’m so sorry. What is a geenieweenie."
                    show de calmt
                    d "I know what that is. Arigathanks for the compliment."
                    show de calm
                    show apo defaultt at jumper
                    a"Oh Barby, you silly goose! It means a wonderful genius!"
                    show apo default at jumper
                    show de default at jump
                    # return
        show apo defaultt at jumper
        a"Oh right! Now that you’re here, Deez... Do you wanna set up your email soon?"
        show apo default at downward
        show de thinkingt at jumper
        d "I know how to do that, too, but you can, like. Watch if you want."
        show apo default at up
        show de shy
        b "I’ll leave you to it, then!"

        jump breaktime1
    else:
        scene room_1
        show lighter:
            blend 'add' alpha 0.3
        show barby_standing_pants:
            zoom 0.6 xpos 0.2 ypos 0.16
            
        show apollo_standing:
            zoom 0.8
            xpos 0.5
            ypos 0.2
                
        show deez_standing:
            xpos 0.35
            ypos 0.1    
            zoom 0.65 xzoom -1
        b "they seem busy."
        jump breaktime1


label mjandkendra:
    # MJ & Kendra? hallway
    
    if not talkedtokendra and not talkedtomj:
        $ talkedtokendra = True
        $ talkedtomj = True
        scene room_3 
        show overlay:
            blend 'multiply' alpha 0.3
        show borders1
        show m hmt at right:
            xoffset -250
        show ken surprised at jumper, left:
            xoffset 250
        with fade
        m "You ever think it’s crazy how we kinda look related?"
        show m hm
        show ken surprisedt at downward
        k "We-we do?" 
        show m defaultt
        show ken surprised
        m "Y’know. Blonde hair, green eyes. Everyone in my family has green eyes, which is kind of weird since it’s recessive to brown." 
        show m default
        show ken awkwardt
        k "Huh. Barby also has green eyes."
        show ken awkward
        m "Yeah, but, everyone in my family also has either blonde or brown hair, and he doesn’t exactly... well, maybe..." 
        show ken defaultt at jumper
        k "Oh! Speaking of! Hi Barby!" 
        show ken default
        b "Hiya!"

        #Related?
        default related = False
        default costumes = False
        default mjsfamily = False
        while not (related and costumes and mjsfamily):
            menu:
                "Related" if not related:
                    $ related = True
                    show ken default
                    show m default
                    b "Maybe you could trace each other’s family trees?"
                    show ken defaultt
                    k "Oh, you know I- I don’t have one...!"
                    show ken default
                    b "Right..." 
                    show m hmt
                    m "Aw man. It would’ve been really fun to find out if we were cousins."
                    
                    m "How about your family tree?"
                    show m hm
                    b "Me?"
                    show ken awkwardt
                    k "He doesn’t, um, have one either...I think?" 

                        #VA Barby: happily said, not in an offended way. 
                    show ken surprised at jumper
                    b "I have parents."
                    show ken surprisedt
                    k "Oh! You told me you were adopted?"
                    show ken awkward at downward
                    b "Yeah!"
                    b "Wait... ohh... okay, I see." 
                    # return
                    show ken default
                    show m default
        #MJ’s Family?
                "MJ's Family" if not mjsfamily:
                    $ mjsfamily = True

                    b "Everyone in your family has green eyes?" 
                    show m defaultt
                    m "Yeah. The grass is green, the trees are green, the Greys are green." 

                    #VA Kendra: attempting to make a joke
                    show ken defaultt
                    k "Are they Greens grey?"
                    show ken default
                    show m defaultt
                    m "No. They’re green, too."
                    show m default
                    # return

                "Costumes" if not costumes:
                    $ costumes = True

                    b "Happy Halloween, guys! What’re your costumes, if you don’t mind me asking?"
                    show m defaultt
                    m "My costume? Um... oh! Yes. I am a guardian of the night."
                    show m default
                    b "Oh! A night guard."
                    show m defaultt
                    m "Yes. Totally."
                    m "Cinco Noches con Alfredo."
                    show m default
                    b "How about you, Kendra?"

                    #VA Kendra: She is flustered because she forgot about Halloween
                    show ken awkwardt at downward
                    k "C-costumes?! Oh pfft, yeah I remember that—"
                    show ken awkwardt
                    k "I ahh—I'm uhm, a garden? Yes, totally."
                    show ken awkward
                    b "Oh yeah! That checks out! Is that why you’re wearing the flower clips?"
                    show ken awkwardt
                    k "Mm... Mhm! Yes, nothing... else."
                    show ken surprised at up
                    k "Oh, my break is almost done...!"
                    show m hmt at jumper
                    m "We have the same break?"
                    show m hm
                    show ken awkwardt at jumper
                    k "R-right; I cut my break in half so I can spend the rest of it finishing things."
                    show m defaultt
                    m "I can help if you need?" 
                    show m default
                    b "I can help, too...!"
                    show ken awkwardt
                    k "Oh, um, thanks— both of you— but I think I can handle it... it’s not for this job, it’s for my other work..." 
                    show ken awkward at downward
                    b "Oh... I’d love to help but..."
                    show m defaultt at jumper
                    m "I can still help!" 
                    show m default at downward
                    b "MJ, I don’t know if we’re allowed to; we wouldn't want to do anything against company policy... right?"
                    m ":)"
                    show m defaultt at up
                    m "You’re right, Barby."
                    show ken awkwardt at jumper
                    k "Well, I’ll have to do that now!" 
                    show ken awkward
                    show m defaultt at downward
                    m "I can help by supporting you."
                    show m default
                    show ken awkwardt at downward
                    k "Um... okay!"
                    b "Ah- I’d... like to do that, too, but... I’ve got things I need to do..."
                    # what does he need to do i dont know chat how do we close off this part i dont know they need to stop talking </3

        b "...What do I need to do. How do I stop talking."
        jump breaktime1
    else :
        
        scene room_3 
        show lighter:
            blend 'add' alpha 0.3
        show borders1
        show barby_standing_pants:
            zoom 0.2 xpos 0.2 ypos 0.48
                
        show mj_standing:
                zoom 0.3 xpos 0.5
                ypos 0.45
        
        show kendra_standing:
            xpos 0.4
            ypos 0.45
            zoom 0.3
        b "they seem busy."
        jump breaktime1
            # then when you talked to everyone barby goes “ough i gotta go to the conference room for our team meeting soon"  - and i guess maybe you have to walk over there and click it???  Or teleport them


