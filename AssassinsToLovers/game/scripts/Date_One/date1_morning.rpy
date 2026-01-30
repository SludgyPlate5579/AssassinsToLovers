# Start of date one

label date1_morning:
    scene throne_room day

    "You sit on your throne, head still woozy and your heart still pounding. Luckily, today isn’t as busy as usual."
    "You are surprisingly well rested, despite your strange dream the other night. It truly did rile you up, as you haven’t felt such things in a while."
    "All of your previous spouses never really fit the bill, but damn- your butler was HOT last night, both as your butler and your assassin."
    "Figmund Sreud would’ve definitely read into that. Like, do you really want to be assassinated? Did you have a thing for your b-"

    "Your heart stops as your thoughts are rudely interrupted with a knock."
    "You pause to feel your face, checking to see if any heat has stayed. You pray you aren’t flushed and you call out, "

    menu:
        "Come in.":
            pass
    
    "Your butler arrives with a plate of crackers and cheese, paired with a glass of wine. He gently sets it down but for some reason you can’t help but give him the up-down."
    "Staring at him, you notice his skin is so glossy, his hair shines with a radiance that could almost blind you, and oh, his eyes. So dreamy-"

    "Wow. Seems like he caught on. Your butler gives you a puzzled look and awkwardly clears his throat. When he opens his mouth, you stare at his lips, and listen to his deep, velvety voice,"

    define b = Character("Butler", color="#476fd3c1")

    b "Are you alright?"

    "You can’t help but stare and silently nod, while you start to feel the heat once more. Your butler gently twitches his brow, a little concerned."

    b "My, are you getting sick? Should I get the medic?"

    "The butler reaches towards you and you snap out of it, scooting back."

    p "I’m fine. Don’t worry. This room is just hot."

    "To your words, the butler opens the window slightly, letting in the cold winter breeze."

    b "Is that better?"

    "You respond with a nod, fighting the urge to shiver. You can’t help but look down at the platter, thinking back on your strange dream the other night, it’s hard for you to really want to eat anything offered by them."

    menu:
        "Make the butler eat it first.":
            p "I can’t possibly indulge alone, here, take a piece."
            "You motion over to the platter, patiently waiting for your butler to sample the food. With no hesitation, the butler thanks you then takes a piece of cheese, placing it on a cracker and eating it."
            "You can’t help but watch as he tries eating as neatly as he can, licking a crumb off of the corner of his mouth. God how you wish you were-"
            "You snap out of it. God, you are a freak! This is embarrassing to even watch!"
        "Eat":
            pass
    
    "You let out a soft sigh as you reach down and take yourself a morsel. You take a bite and then reach for your glass of wine, sipping from it as carefully as you can."
    "You take in the aroma and taste, clearing it of any sort of dangerous poison. It was a bit embarrassing for you to let your dream control your actions, but here you were, doing it anyway."

    ""

    return