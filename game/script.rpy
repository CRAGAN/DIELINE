# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

init python:
    def get_qte_color(current, maximum):
        # Calculate percentage left (1.0 down to 0.0)
        pct = max(0.0, min(1.0, float(current) / float(maximum)))
        
        # When time is full (pct=1), Red=0, Green=255
        # When time is empty (pct=0), Red=255, Green=0
        r = int((1.0 - pct) * 255)
        g = int(pct * 255)
        b = 0
        
        # Convert RGB integers into a Ren'Py hex string format
        return "#%02x%02x%02x" % (r, g, b)

image apollo_qte_sprite = ConditionSwitch(
    "time <= 0", "images/apollo/apollo seriousm.png",    
    "time < (time_max*0.33)", "images/apollo/apollo worried.png",
    "time < (time_max*0.67)", "images/apollo/apollo awkwardm.png",
    "True", "images/apollo/apollo defaultm.png"
)

image bg_art = ConditionSwitch(
    "time <= 0", "#300303",    
    "time < (time_max*0.33)", "#801010",
    "time < (time_max*0.67)", "#f34f4f",
    "True", "#ff8a8a"
)


# The game starts here.

label start:

    scene bg room

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    $ time = 5
    $ time_max = 5
    $ interval = 0.1
    $ timer_started = False

    # show image "images/apollo/apollo defaultm.png":
    #     zoom 0.85 xalign 0.9 yalign 0.5

    # $ renpy.pause(2)

    call screen qte

    return

screen qte:

    add "bg_art" 

    add "apollo_qte_sprite" zoom 0.85 xalign 0.9 yalign 0.5

    if not timer_started:
        timer 1 action SetVariable("timer_started", True)

    if timer_started:
        timer interval repeat True action If(time > 0.0, true=SetVariable('time', time - interval), false=[])

        if (time <= 0.0):
            timer 2.0 action [Hide("qte"), Jump("ded")]

        vbox:
            xalign 0.5
            yalign 0.5

            bar:
                value AnimatedValue(value=time, range=time_max, delay=0.1)
                range time_max
                xalign 0.5
                xmaximum 300
                if time < (time_max*0.33):
                    left_bar get_qte_color(time, time_max)
                    #left_bar "#f00"


            textbutton "Left Door":
                action [Hide("qte"), Jump("left_door")]

            textbutton "Right Door":
                action [Hide("qte"), Jump("right_door")]


label ded:
    "you died"
    return

label left_door:
    "left_door"
    return

label right_door:
    "right door"
    return