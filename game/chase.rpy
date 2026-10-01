image chase_movie = Movie(channel="movie_dp", play = "videos/chase/chase_start.webm", loop=False)
image chase_qte_failed_kick = Movie(channel="movie_dp", play = "videos/chase/chase_qte_failed_kick.webm", loop=False)


# TODO: REPLACE WITH CORRECT FILENAMES #
image chase_qte_move = Movie(channel="movie_dp", play = "videos/chase/chase_qte_move.webm", loop=False)
image chase_qte_crawl = Movie(channel="movie_dp", play = "videos/chase/chase_qte_crawl.webm", loop=False)
image chase_qte_hop = Movie(channel="movie_dp", play = "videos/chase/chase_qte_hop.webm", loop=False)
image chase_temp_jumpscare = Movie(channel="movie_dp", play = "videos/chase/temp_jumpscare.webm", loop=False)
image chase_crawl_jumpscare = Movie(channel="movie_dp", play = "videos/chase/chase_qte_crawl_scare.webm", loop=False, size=(1920, 1080))



label qte_start:
    scene chase_movie with dissolve
    $ time = 1.5
    $ time_max = 1.5
    $ interval = 0.1
    $ timer_started = False
    $ renpy.stop_skipping()
    $ qte_clicked = False    
    $ renpy.pause(30, hard = True)


    call screen qte


screen qte:

    if not timer_started:
        timer 1 action SetVariable("timer_started", True)

    if timer_started:
        timer interval repeat True action If(time > 0.0, true=SetVariable('time', time - interval), false=[])

        if (time <= 0.0):
            timer 0.9 action If(qte_clicked, true=Jump("qte_move"), false=[Hide("qte"), Jump("qte_failed_kick")])

        if not qte_clicked:
            vbox:
                xalign 0.5
                yalign 0.5


                textbutton "K I C K":
                    xalign 0.5
                    action SetVariable("qte_clicked", True)

                bar:
                    value AnimatedValue(value=time, range=time_max, delay=0.1)
                    range time_max
                    xalign 0.5
                    xmaximum 300
                    if time < (time_max*0.33):
                        left_bar "#f00"





label qte_failed_kick:
    #$ renpy.pause(0.9, hard = True)
    scene black with dissolve
    $ renpy.pause(1, hard = True)
    scene chase_temp_jumpscare with dissolve
    $ renpy.pause(3, hard = True)
    scene black with dissolve
    jump qte_start



label qte_move:
    scene chase_qte_move with dissolve
    $ renpy.pause(3.5, hard = True)
    $ time = 1
    $ time_max = 1
    $ interval = 0.1
    $ timer_started = False
    $ renpy.stop_skipping()
    $ qte_clicked = False
    $ qte_hop = False   
    $ qte_crawl = False

    call screen qte2

label temp_jump:
    scene black with dissolve    
    $ renpy.pause(2, hard = True)    
    scene chase_temp_jumpscare with dissolve
    $ renpy.pause(3, hard = True)
 
    jump qte_start        

screen qte2:

    if not timer_started:
        timer 1 action SetVariable("timer_started", True)

    if timer_started:
        timer interval repeat True action If(time > 0.0, true=SetVariable('time', time - interval), false=[])

        if (time <= 0.0):
            $ renpy.log(qte_clicked)
            timer 0.3 action If(qte_clicked, If(qte_crawl, true=Jump("qte_crawl"), false=Jump("qte_hop")), false=[Hide("qte"), Jump("temp_jump")])

        if not qte_clicked:
            vbox:
                xalign 0.5
                yalign 0.5


                textbutton "CRAWL":
                    xalign 0.5
                    action [SetVariable("qte_clicked", True), SetVariable("qte_crawl", True)]

                textbutton "HOP":
                    xalign 0.5
                    action [SetVariable("qte_clicked", True), SetVariable("qte_hop", True)]


                bar:
                    value AnimatedValue(value=time, range=time_max, delay=0.1)
                    range time_max
                    xalign 0.5
                    xmaximum 300
                    if time < (time_max*0.33):
                        left_bar "#f00"

label qte_crawl:
    scene chase_qte_crawl with dissolve
    $ renpy.pause(10, hard = True)
    scene black with dissolve
    $ renpy.pause(1, hard = True)   
    scene chase_crawl_jumpscare with dissolve
    $ renpy.pause(3, hard = True)    
    scene black with dissolve
    $ renpy.pause(1, hard = True)       
    jump qte_start

label qte_hop:
    scene chase_qte_hop with dissolve
    $ renpy.pause(37, hard = True)
    jump chase
