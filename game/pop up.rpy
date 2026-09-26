default time_left = 10.0
screen clock():
    timer 1.0 repeat True action If(time_left > 1.0, SetScreenVariable("time_left", time_left - 1.0))
    vbox:
        xalign 0.9
        yalign 0.05
        text "Time Remaining: [time_left]" size 30 color "#fff"
    if time_left <= 5.0:
    
        frame:
            xpos 0.3 ypos 0.2
            background "#ffcccc"
            xsize 500
            ysize 500
            vbox:
                spacing 10
                xalign 0.5
                yalign 0.5
                text "FIVE SECONDS LEFT!!!"
                null height 20
                textbutton "{b}X":
                    action Hide("clock")
        