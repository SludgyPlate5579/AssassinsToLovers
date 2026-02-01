# script for what_here label when you ask the butler what the's doing here

label what_here:
    "In one full motion, your butler sets you down, then presents you with a flower. It’s a rose, dark red with delicate, swirling petals."

    b2 "I was picking this out for you."

    menu:
        "Why?":
            b2 "I hear your butlers have constantly been changing."
            b2 "I wanted to thank you for your generosity so far, for letting me stay in your care."

            menu:
                "Thank you.":
                    pass
                "You should be getting my dinner.":
                    stop music fadeout 1.0
                    play music "stay the course.mp3" fadein 1.0 loop
                    show butler yassified disgusted
                    p "Hurry if you don’t want me to have you replaced."
                    b2 "Yes, your highness."

                    "How insolent. You turn on your heels and start the journey back to your room, your servant following behind you."

                    jump date3_bad
        "Oh... Thank you.":
            pass
    "You seem to have suddenly manifested manners. The butler smiles, slipping the flower behind your ear."
    "Wow. Thats... {w} Is the sun pretty strong here or is it just you?"
    "Before you can even get your bearings, your butler pulls out an intricate pocket watch, checking the time."

    b2 "It seems as if dinnertime is approaching. Shall we head to your room?"
    p "S-sure.{w=0.5} Yes.{p} That sounds...{w=0.5} that sounds great."
    p "Let’s eat together."

    "Oh. You didn’t mean to say that, but there’s no going back now. There’s a flower behind your ear, anyway. You want to talk with him. He blinks."

    b2 "Are you certain? That is quite… strange."
    p "Yes."

    jump date3_good