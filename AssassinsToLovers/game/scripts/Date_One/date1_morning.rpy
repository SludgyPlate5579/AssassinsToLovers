# Start of date one

label date1_morning:
    scene sitting room

    "You sit on your throne, head still woozy and your heart still pounding. Luckily, today isn’t as busy as usual."
    "You are surprisingly well rested, despite your strange dream the other night. It truly did rile you up, as you haven’t felt such things in a while."
    "All of your previous spouses never really fit the bill, but damn- your butler was HOT last night, both as your butler and your assassin."
    "Figmund Sreud would’ve definitely read into that. Like, do you really want to be assassinated? Did you have a thing for your b-"

    "Your heart stops as your thoughts are rudely interrupted with a knock."
    "You pause to feel your face, checking to see if any heat has stayed. You pray you aren’t flushed and you call out, "

    menu:
        "Come in.":
            pass
    
    show butler yassified
    with moveinright

    "Your butler arrives with a plate of crackers and cheese, paired with a glass of wine. He gently sets it down but for some reason you can’t help but give him the up-down."
    "Staring at him, you notice his skin is so glossy, his hair shines with a radiance that could almost blind you, and oh, his eyes. So dreamy-"

    "Wow. Seems like he caught on. Your butler gives you a puzzled look and awkwardly clears his throat. When he opens his mouth, you stare at his lips, and listen to his deep, velvety voice,"

    b2 "Are you alright?"

    "You can’t help but stare and silently nod, while you start to feel the heat once more. Your butler gently twitches his brow, a little concerned."

    b2 "My, are you getting sick? Should I get the medic?"

    "The butler reaches towards you and you snap out of it, scooting back."

    p "I’m fine. Don’t worry. This room is just hot."

    "To your words, the butler opens the window slightly, letting in the cold winter breeze."

    b2 "Is that better?"

    "You respond with a nod, fighting the urge to shiver. You can’t help but look down at the platter, thinking back on your strange dream the other night, it’s hard for you to really want to eat anything offered by them."

    menu:
        "Make the butler eat it first.":
            p "I can’t possibly indulge alone, here, take a piece."
            "You motion over to the platter, patiently waiting for your butler to sample the food. With no hesitation, the butler thanks you then takes a piece of cheese, placing it on a cracker and eating it."
            "You can’t help but watch as he tries eating as neatly as he can, licking a crumb off of the corner of his mouth. God how you wish you were-"
            "You snap out of it. God, you are a freak! This is embarrassing to even watch!"
        "Eat":
            pass
        "Reject the platter.":
            "You grunt and focus on your stack of papers. You’ve got really important things to do, after all."
            p "Please take your plate and go. I don’t need anything to eat right now. Leave me be, I need to attend to these pressing matters."
            hide butler yassified
            with moveoutright
            "The lie rolls off your tongue with ease, and despite the heat making you want to keep him there, you realize that focusing on your work soothes it slightly."
            menu:
                "Work.":
                    "The rest of your day goes by smoothly as you sign off on multiple bills, pushing for the invasion and takeover of the neighboring kingdom."
                    "You’re confident you will win, as the kingdom you want to attack is nothing but a freebie. You only kept them safe because they were useful to you before, but now, not so much. God, you’re horrible."
                    "Anyways, when you finish up with everything, you wander the halls, somehow finding yourself tailing your butler."
                    jump date2_garden
    
    "You let out a soft sigh as you reach down and take yourself a morsel. You take a bite and then reach for your glass of wine, sipping from it as carefully as you can."
    "You take in the aroma and taste, clearing it of any sort of dangerous poison. It was a bit embarrassing for you to let your dream control your actions, but here you were, doing it anyway."
    "When the platter is finished, you look over at the window, then back to the butler. "

    p "Go take these dishes out for me, please. I would like to have the rest of the day to myself."

    "The butler says nothing but gives you a small nod, picking up your glass and the platter, then leaving."

    hide butler yassified
    with moveoutright

    "As he leaves, you can’t help but linger on that small seed of doubt that your dream truly wasn’t something made up. You need to look further. You wander the castle, discreetly watching the butler and him doing all of his duties. Nothing seemed off, but you still needed to watch, just in case."

    jump date2_garden