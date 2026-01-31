# CREDITS!!!!

label credits:
    stop music fadeout 1.0
    if good_date:
        play music "there is romance.mp3" fadein 1.0 loop
    else:
        play music "leaving home.mp3" fadein 1.0 loop
    window hide
    scene black

    show text "Credits" with dissolve
    pause 2
    show text "Introduction Written by Annie Bloom"

    $ renpy.full_restart()