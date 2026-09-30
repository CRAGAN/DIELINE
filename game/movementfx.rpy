
transform talk:
    matrixcolor BrightnessMatrix(-0.2)
transform rc:
    xoffset 0.70
    yoffset 170
transform rcc:
    xoffset 0.60
    yoffset 170
transform downward:
    easein 0.1 yoffset 0
    easein 0.5 yoffset 5

transform up:
    linear 0.3 yoffset 5
    linear 0.5 yoffset 0
transform shaking:
    linear 0.1 xoffset -5 yoffset 5
    linear 0.1 xoffset -6 yoffset -1
    linear 0.1 xoffset 5 yoffset 5
    linear 0.1 xoffset -4 yoffset 4
    linear 0.1 xoffset 0 yoffset 0
    repeat
transform fd:
    alpha 1.0
    linear 0.5 alpha 0.0
transform squish:

    yzoom 1.0
    linear 0.05 xzoom 0.98  yoffset 5
    linear 0.08 yzoom 0.98 xzoom 1.03
    linear 0.11 yzoom 1.0 xzoom 1.0 yoffset -1.10
    yoffset 0
transform floating:
    subpixel True
    easein 2 yoffset 10
    easein 2 yoffset -5
    repeat
    yzoom 1.0
    repeat
transform dance:
    linear 0.34 xoffset 50 yoffset 0
    linear 0.2 yoffset 10
    linear 0.34 xoffset -50 yoffset 0
    linear 0.2 yoffset 10
    repeat
transform sunset:
    matrixcolor (TintMatrix("#fffbe2"))
transform sunset2:
    matrixcolor (TintMatrix("#ffd6c4"))

transform snow:
    alpha 1.0
    linear 10 alpha 0.0
    pause 4
    linear 9 alpha 1.0
    repeat
transform snow2:
    alpha 1.0
    linear 9 alpha 0.0
    pause 2
    linear 9 alpha 1.0
    repeat
transform snow3:
    alpha 1.0
    linear 9 alpha 0.0
    pause 5
    linear 9 alpha 1.0
    repeat
transform jumper:
    yoffset 0
    linear 0.05 yoffset 20
    linear 0.09 yoffset 18
    linear 0.3 yoffset 0

transform jump:
    linear 0.09 yoffset 10
    linear 0.05 yoffset 20
    linear 0.08 yoffset 0

transform wavy:

        linear 0.3 xzoom 1 yzoom 1
        linear 0.4 xzoom 0.5 yzoom 1
        linear 0.3 xzoom 1 yzoom 1
        linear 0.4 xzoom 0.5 yzoom 1
        repeat
transform forward:
    linear 0.3 zoom 1.05

transform small_wobble:
    subpixel True
    anchor (0.5, 0.5)
    align (0.5, 0.5)
    zoom 1.05
    block:
        linear 1.0 xoffset 5 yoffset 3 rotate 1.3 blur 2
    block:
        linear 1.0 xoffset 0 yoffset 0 rotate 0 blur 1
    block:
        linear 1.0 xoffset -5 yoffset -3 rotate -1.3 blur 4
    block:
        linear 1.0 xoffset 0 yoffset 0 rotate 0 blur 2
    repeat
transform small_wobble1:
    subpixel True
    anchor (0.5, 0.5)
    align (0.5, 0.5)
    zoom 1.05
    block:
        linear 1.2 xoffset 5 yoffset 3 rotate 1.5 blur 4
    block:
        linear 1.2 xoffset 0 yoffset 0 rotate 0 blur 2
    block:
        linear 1.2 xoffset -5 yoffset -3 rotate -1.5 blur 4
    block:
        linear 1.2 xoffset 0 yoffset 0 rotate 0 blur 2
    repeat
transform small_wobbletrans:
    subpixel True
    anchor (0.5, 0.5)
    align (0.5, 0.5)
    zoom 1.05
    block:
        linear 1.0 xoffset 3 yoffset 2 rotate 0.5 blur 5
    block:
        linear 1.0 xoffset 0 yoffset 0 rotate 0 blur 3
    block:
        linear 1.0 xoffset -3 yoffset -2 rotate -0.5 blur 4
    block:
        easein 1.0 xoffset 0 yoffset 0 rotate 0 blur 0
