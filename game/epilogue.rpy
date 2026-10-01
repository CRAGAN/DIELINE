image beforept = Movie(play="images/cg/um we never told player he doesnt know thing.webm", loop = False)
image ppttime = Movie(play="images/cg/PPT Poo Real.webm", loop = False)
screen skipcutscene(cutscene_end):
    textbutton "SKIP":
        align (0.95, 0.05) # Position at the top right
        action Jump(cutscene_end)
label epilogue:
    scene black
    centered "{color=#F5F5F5}October 31, Saturday"
    centered "{color=#F5F5F5}0 days left."
    scene black with dissolve
    pause 1.5
    $ quick_menu = False
    scene beforept with dissolve
    $ renpy.pause(19.5, hard=True)
    
    jump pptcutscene
label pptcutscene:
    show screen skipcutscene("cutscene_end")

    scene ppttime with dissolve
    $ renpy.pause(372, hard=True)

    hide screen skipcutscene
    jump cutscene_end

label cutscene_end:
    play music "audio/Music/DEADLINE Piano Ending.mp3"
    scene black
    hide screen skipcutscene
    pause 3
    scene epilogue1
    b_sub "...Hiya, folks."
    scene epilogue2
    pause 1.0
    scene epilogue3
    pause 1.0
    scene epilogue4
    b_sub "I don’t know if I ever got to tell you how much you all mean to me."
    scene epilogue5
    b_sub "... I hope you can forgive me for being selfish and opening up at a time like this. But I just…"
    scene epilogue6
    b_sub "I know you’re all going through so much, too."
    # barby’s mouth opens and neon colors inside
    # lowkey first time he’s opened up properly
    scene epilogue7
    b_sub "But I’ve been feeling down."
    # As he pulls the limp friend pile over in an embrace
    # goes black
    # text like silent film text 
    scene black 
    pause 1.0

    centered "{color=#F5F5F5}It’s okay!" 
    centered "{color=#F5F5F5}You tried your best."
    # friends image
    scene image "ending.png" with fade
    show image "ending_lineart.png"
    #scene image "ending_lineart.png"
    centered "{color=#F5F5F5}Congratulations! You did it!"
    # friends zoom into Kendra
    # switches to silent film text (black screen with white text)
    voice "audio/Kendra/Epilogue/kendra_line101.mp3"
    centered "{color=#F5F5F5}Congratulations! You helped us when we really needed it!"
    # friends zoom into MJ
    # switches to silent film text (black screen with white text)
    voice "audio/MJ/Epilogue/MJ_line094.mp3"
    centered "{color=#F5F5F5}Congratulations! It’s finally over! You crossed the finish line!"
    # friends zoom into Deez
    # switches to silent film text (black screen with white text)
    voice "audio/Deez/Epilogue/deez_line114.mp3"
    centered "{color=#F5F5F5}Congratulations! You knew what to do when things got compile-cated."
    # friends zoom into Apollo
    # switches to silent film text (black screen with white text)
    voice "audio/Apollo/Epilogue/apollo_line189.mp3"
    centered "{color=#F5F5F5}Congratulations! Thank you for being there for all of us."

    # barby face, barby smile
    centered "{color=#F5F5F5}Congratulations, everyone! We did it!"

    # pop up just like the dates in the other days
    scene black
    voice "audio/Barby/Epilogue/barby_line300.mp3"

    centered "{color=#F5F5F5}We're done."
    scene black with fade
    pause 3
    centered "{color=#F5F5F5}November 1, Sunday"
    # Every day ever left
    #CREDITS HERE


    $ renpy.full_restart()
