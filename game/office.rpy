### TODO: Is this file unused? ###
image deezscene1 = Movie(play="images/cg/deeze scene.1.webm", loop = True)
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
    
    # deez stops
    # flash black
    # hand lets go and reaches out to barby (can just be one img) ID YOU VANT DO IT I WILL DO IT ITS GONNA JUST BE A HAND BUT PURPLE JUNPSCARE FIRST PERSON 
    # sfx jumpscare 
    # black screen
    # return back to the moment he open door

