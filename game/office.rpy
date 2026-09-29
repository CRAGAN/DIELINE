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











# Clicking around anywhere else in the area
label encounter4:
    scene room_3:
        zoom 1.4
    show 
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

