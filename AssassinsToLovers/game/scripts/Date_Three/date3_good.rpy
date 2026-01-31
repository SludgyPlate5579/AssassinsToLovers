# good route for date 3

label date3_good:
    scene black
    with fade

    "After walking with the butler to your room, you truly notice the heat from earlier was gone, but what replaced that subtle lust was something greater."
    "You felt… nervous? Butterflies swarmed in your stomach, dancing and playing around to your gradually increasing heart rate."
    "You asked this man to dinner, for god's sake, and now you’re already going to your bedroom? Even your previous suitors have never gotten this far. "

    scene bedroom night

    "You finally reach your room, where your butler reaches out to you, pulling you inside and shutting the door behind you. You’re taken aback, with how direct he is, but before any words come out, the butler presses you against the door, looking into your eyes."
    "You notice something gently shift within his eyes, quite literally, as his blue eyes slowly shift to a yellow. You get a rush of adrenaline, the reason unknown to you. Something’s off, and you can’t exactly put it together just yet."

    b2 "You knew, didn’t you?"

    "Their face starts to shift ever so slightly, your butler’s previously more masculine face shifts into something more rounded and feminine, and his once beautiful long black hair starts to lose its color and length. They look at you with a small smirk."

    b2 "I guess there was no point in trying to hide anymore, huh?"

    "It finally clicked, and you can’t help but stare, there was no dream."

    menu:
        "So it was you after all...":
            "You look at your once butler, a strange mix of fear and anticipation coming over you. As they lean in you couldn’t help but let them get closer. Was your fear from your soon-to-be murderer being so close? Or was it from your lack of intimacy beforehand? Will they find you appea-"

            a "What’s wrong now? Cat got your tongue, hm?"

            "Her voice echoed throughout your body."
            "You hated this feeling, the feeling of uncertainty. You’re a tyrant. A merciless one. You get what you want, and it’s to make this feeling go away."

            window hide
            if gender == "male":
                show male kiss
            else if gender == "female":
                show female kiss
            else:
                "idk what you did"
            
            "You pull the assassin in and gently kiss her, feelings exploding into pure bliss. She doesn't seem to mind though, as her hands find their way over onto both sides of your face, gently cupping your cheeks. You both pull away eventually before you look into her shimmering citrine eyes."

            p "Tell me, what is your true name?"

            a "Nyx… my name is Nyx…"

            "Her breath was slightly rugged, her eyes matching yours. Looking at her so flushed was satisfying on its own; satisfying enough to make you lean in for more."

            jump credits