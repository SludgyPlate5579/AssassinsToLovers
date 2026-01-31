# This is the butler's reveal scene

default didSpeak = True

label reveal:
    play music heartwarming fadein 1.0 loop
    scene bedroom night

    "Your eyes snap open! Wide, awake, and… lustful?"

    b "Right now your heart must be experiencing searing, shooting pains."

    "Yeah, your heart is definitely searing right now. Searing for some action."
    "You can just barely make out his form within the shadows, but you instantly recognize that voice—even if it’s in a tone dripping with malice, never directed towards yourself before. Unsurprisingly, it turns out your butler was trying to kill you! Wow, that’s hot."

    b "Paralyzed from head to toe. Even if you want to scream, you can’t."

    "He begins striding towards you, slowly, like a tiger cornering its prey. As he gets closer, the moonlight of the nearby window gradually illuminates his form."

    b "You are starting to feel it grow. Creeping its way through your veins."

    "The tense and creeping moment is held until you find yourself face to face. Close enough to see his face illuminated in the moonlight. But something seems a bit… different?"

    define slowWalk = Dissolve(1.5)
    show butler yassified n
    show love:
        alpha 0.4
    with slowWalk

    b "Seeing as this will be amongst your last moments alive, I ha-"

    menu:
        "I have never noticed how stunning you are":
            b "Wha-"
            b "..."
            b "Do you really think flattery will help you in this situation?"
            b "(how did they even talk?)"
            b "And don’t interrupt me again! Or I’ll — I’ll make your last moments even worse."
            b "Ehem."
            b "Before you rudely interrupted me, I was about to reveal something to you."
        "MARRY ME":
            b "WHAT!?"
            b "{cps=20}{b}don’t{/b}{/cps} mess with me"
            b "..."
            b "(how did they speak?)"
            b "I wanted you to know."
        "Say nothing" (didSpeak=False):
            b "-ve one last thing to reveal to you..."
    
    "Before your eyes, you see the butler’s form start to shift and mold into a completely new form. One that stuns you into shock."

    stop music fadeout 1.0
    
    scene black
    with fade
    hide butler

    "Now standing before you is your butler no more. In their place is a menacing,{w} dangerous,{w} stunning beauty."

    play music "inner light.mp3" fadein 1.0 loop

    scene bedroom night
    show love:
        alpha 0.4
    show assassin n
    with fade



    a "Maybe you should do a more thorough check on your closest personal attendants next time."
    a "Or better yet, maybe don’t kill the few loyal servants that you still had. But heavens no, that surely would go against your deepest desires."

    if didSpeak:
        a "Seeing as you are somehow able to speak, I’ll give you the final undeserving honor of granting you some final words."
        menu:
            "In the afterlife, would you be interested in grabbing a bite?":
                a "Butler?: Stop trying to flatter me. It won’t save you."
            "I wish to apologize to all those I’ve wronged.":
                a "I wouldn’t accept it even if you meant it."
            "Say nothing.":
                a "..."
                a "Fine. Be that way."
    
    a "Now let me enjoy your final moments as I watch life slowly fade from your eyes."

    "Your once butler pulls up a chair to watch you die before her."
    "However, something quite bewildering happens. Your eyes look as healthy as before. Even as the night starts to become day, you still seem perfectly fine."
    "As dawn breaks your assassin has a stunned look on their face. A silence falls over you both as you both hear the sounds of the castle starting to wake."
    "Your servants are starting to make their rounds and as you hear footsteps approaching, everything starts to fade to black."

    scene black 
    with fade

    "You’re exhausted, for some odd reason. You feel healthy, yet drained of all energy."

    jump date1_morning