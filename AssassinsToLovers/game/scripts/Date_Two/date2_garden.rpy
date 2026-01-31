# date 2 main script

label date2_garden:
    scene bedroom day
    show love:
        alpha 0.25
    show butler yassified

    "Your butler is a rather meticulous person, you’re finding. Stalking him is pretty entertaining, actually. You get to watch his beautiful figure walk through the hallways, his stoic face as he surveys documents..."

    scene sitting room
    show love:
        alpha 0.25
    show butler yassified

    "He does his duties carefully, the perfect picture of a model servant of the household. Maybe you should give him a raise." 
    
    "Or maybe you should find him a gift; surely that would be more preferable. You don’t give raises, after all. That would cost much more precious money — money that you could use to terrorize other kingdoms."

    scene black

    "But then, your butler seems to stray off the inner pathways of the castle and walks out to the vast garden. That’s strange; it’s dinnertime. What butler duties would require going to the garden when he should be getting your dinner?"

    scene garden day
    show love:
        alpha 0.25
    show butler yassified

    "Interested, you follow him through the hedge maze, up until he reaches a small clearing with flowerbeds. He gracefully kneels at a group of blooming flowers, careful hands almost caressing the different petals."

    b2 "Is there a reason why you’ve been following me?"

    "You startle and, in your haste to get away, trip over a lump on the ground. In an instant, the pull of gravity is cushioned by a strong arm, and wow, the butler is right here. In your face. Holding you."

    menu:
        "Hi… Fancy seeing you here, huh?":

            "You smile, batting your eyes. Unfazed, your butler just sets you down."

            b2 "Butler: Let’s not pretend. I’ve been feeling your eyes on me the entire day."

            "Well, it was worth a shot. You flush, stepping back."

            menu:
                "Thank you for catching me.":
                    "Back with the manners, which is strange. The butler blinks at you, then smiles."
                    b2 "Of course. It is my duty, after all."
                    menu:
                        "What are you doing here?":
                            jump what_here

        "What are you doing here?":

            jump what_here

        "You’re very pretty.":

            b2 "Excuse me?"

            "He blinks at you, like you’re stupid and he doesn’t understand what you’re saying. Which you aren't. He is, indeed, very pretty, and it’s a shame he doesn’t know that."

            p "You’re very pretty."

            "He coughs."

            b2 "Why, thank you."
            b2 "I must say, you have been acting… rather strange as of late."
            b2 "Are you alright? Perhaps you really are falling ill."
            b2 "Do I need to call for a doctor?"

            "No. Sure, you think there’s definitely something wrong with you right now, but asking for a medic would certainly be a bad idea. If an enemy hears of it, they might think they’ll be able to attack your kingdom."

            b2 "May I ask why you have been… tailing me, in that case? Unless you want to request something?"

            menu:
                "Just making sure you are doing your proper duties. In fact, what are you doing here?":
                    jump what_here
                "I wanted to eat dinner with you.":
                    b2 "..."
                    b2 "Are you certain? That is quite..."

                    p "I'm certain."

                    "There’s a pause as he stares at you. Then, he smiles."

                    "With a bow and one hand behind his back, your butler presents you with a flower. It’s a rose, dark red with delicate, swirling petals."

                    b2 "In that case, I present this to you in gratitude."
                    b2 "Let’s head to your room, shall we?"

                    jump date3_good
