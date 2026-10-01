init python:
    config.has_autosave = False
    config.has_quicksave = False 

define b = Character("Barby", image="barby", color = "#c84204")
define a = Character("Apollo", image= "i_apo", callback=name_callback,cb_name="Apollo", color = "#f04a82")
define k = Character("Kendra", image= "i_ken", callback=name_callback,cb_name="Kendra", color = "#1465ab")
define m = Character("MJ", image= "i_m", callback=name_callback,cb_name="MJ", color = "#43882e")
define d = Character("Deez", image= "i_de", callback=name_callback,cb_name="Deez", color = "#994aaf")
define t = Character("Team")
define r = Character("Ryann", image= "i_ry", callback=name_callback,cb_name="Ryann", color = "#703838")

# Subtitled text style
define b_sub = Character("Barby", who_outlines=[ (3, "#000000") ], what_outlines=[ (5, "#000005") ],show_is_sub=True, color = "#c84204")
define a_sub = Character("Apollo", who_outlines=[ (3, "#000000") ], what_outlines=[ (5, "#000005") ], image= "i_apo", callback=name_callback,cb_name="Apollo", color = "#ee90b0", show_is_sub=True)
define k_sub = Character("Kendra", image= "i_ken",  who_outlines=[ (3, "#000000") ], what_outlines=[ (5, "#000005") ], callback=name_callback,cb_name="Kendra", color = "#1465ab", show_is_sub=True)
define m_sub = Character("MJ", image= "i_m",  who_outlines=[ (3, "#000000") ], what_outlines=[ (5, "#000005") ], callback=name_callback,cb_name="MJ", color = "#43882e", show_is_sub=True)
define d_sub = Character("Deez", image= "i_de",  who_outlines=[ (3, "#000000") ], what_outlines=[ (5, "#000005") ], callback=name_callback,cb_name="Deez", color = "#994aaf", show_is_sub=True)

# During ID card talk
define b_id = Character("Barby", show_is_sub=True, show_is_id=True, color = "#c84204")
define a_id = Character("Apollo", image= "i_apo", callback=name_callback,cb_name="Apollo", color = "#ee90b0", show_is_sub=True, show_is_id=True)
# define m_id = Character("MJ", image= "i_m", callback=name_callback,cb_name="MJ", color = "#3f7038", show_is_sub=True, show_is_id=True)
# define k_id = Character("Kendra", image= "i_ken", callback=name_callback,cb_name="Kendra", color = "#70384e", show_is_sub=True,show_is_id=True)
# define d_id = Character("Deez", image= "i_de", callback=name_callback,cb_name="Deez", color = "#523870", show_is_sub=True,show_is_id=True)

default see_ids = False
define talked = 0

transform zoomin:
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    easein 0.5 zoom 1.3
label splashscreen:
    play music "audio/Music/Minigames/E-Minigame Rush.mp3" loop

    scene splashscreenbg:
        yoffset 0
    with fade
    pause 1.0
    show spooktoberlogo at center:
        yoffset -400 zoom 0.8
    pause 1.0
    centered "\n\n\n\n\n\n{cps=25}{sc=1}{color=#FFFFFF}Made for Spooktober 2026 Game Jam!"
    with dissolve
    hide spooktoberlogo with dissolve
    show logo2 at center:
        yoffset -400
    with dissolve
    pause 2.0
    centered "\n\n\n\n\n\n{cps=25}{sc=1}{color=#FFFFFF}Delve And Murder:\n Nevermore Studios"
    centered "\n\n\n\n\n\n{cps=25}{sc=1}{color=#FFFFFF}CONTENT WARNING: \nPotentially Eyestraining Colors, Epilepsy Warning, Cartoon “Gore” (Fantasy Transformations),\nDisturbing Imagery, Distressing Themes, Jumpscares(?), Arachnophobia warning, Bugs, \nPink Mold, Foul Language, J*b, 9-to-5, Employment 16+ \nThis game does not contain blood or real gore, \nbut there are cartoony artistic renditions of scenes that could be considered gruesome."
    centered "\n\n\n\n\n\n{cps=25}{sc=1}{color=#FFFFFF}reach that quota but most importantly-"
    centered "\n\n\n\n\n\n{cps=25}{sc=1}{color=#FFFFFF}have fun~!"
    hide logo2 with dissolve
    pause 2.0
    scene splashscreenbg:
        easein 2 yoffset -1080
    stop music fadeout 2
    pause 5
    return dissolve
image main_menu_art:
    "gui/lineart.png"
    pause 1.0
    "gui/lineart1.png"
    pause 1.0
    "gui/lineart2.png"
    pause 1.0
    repeat
image circle:
    "gui/circle1.png"
    pause 0.5
    "gui/circle2.png"
    pause 0.5
    "gui/circle3.png"
    pause 0.5
    repeat
