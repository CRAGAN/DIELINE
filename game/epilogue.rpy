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
    scene black
    pause 2
    $ quick_menu = False
    scene beforept
    $ renpy.pause(21.0, hard=True)
    pause 3
    jump pptcutscene
label pptcutscene:
    show screen skipcutscene("cutscene_end")

    scene ppttime with dissolve
    $ renpy.pause(372, hard=True)

    hide screen skipcutscene
    jump cutscene_end

label cutscene_end:
    scene black
    hide screen skipcutscene
    pause 3
    b_sub "...Hiya, folks."
    b_sub "I don’t know if I ever got to tell you how much you all mean to me."
    b_sub "... I hope you can forgive me for being selfish and opening up at a time like this. But I just…"
    b_sub "I know you’re all going through so much, too."
    # barby’s mouth opens and neon colors inside
    # lowkey first time he’s opened up properly
    b_sub "But I’ve been feeling down."
    # As he pulls the limp friend pile over in an embrace
    # goes black
    # text like silent film text 
    centered "It’s okay!" 
    centered "You tried your best."
    # friends image
    centered "{color=#F5F5F5}Congratulations! You did it!"
    # friends zoom into Kendra
    # switches to silent film text (black screen with white text)
    centered "{color=#F5F5F5}Congratulations! You helped us when we really needed it!"
    # friends zoom into MJ
    # switches to silent film text (black screen with white text)
    centered "{color=#F5F5F5}Congratulations! It’s finally over! You crossed the finish line!"
    # friends zoom into Deez
    # switches to silent film text (black screen with white text)
    centered "{color=#F5F5F5}Congratulations! You knew what to do when things got compile-cated."
    # friends zoom into Apollo
    # switches to silent film text (black screen with white text)
    voice "audio/Apollo/Day 5/Pre-Chase/apollo_line180.mp3"
    centered "{color=#F5F5F5}Congratulations! Thank you for being there for all of us."

    # barby face, barby smile
    centered "{color=#F5F5F5}Congratulations, everyone! We did it!"

    # pop up just like the dates in the other days

    # November 1, Sunday
    # Every day ever left
    $ renpy.full_restart()
