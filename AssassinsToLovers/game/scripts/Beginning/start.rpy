# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Butler", color="#476fd3c1")
define p = Character("You", color="#195b13")
define a = Character("Assassin", color="#6f47d3c1")


# The game starts here.

label start:
    scene kingdom

    "In the Kingdom of Allaria, a tyrant rules the land."
    "Their mood shifts with the wind, threatening and bestowing favor to whoever they please."
    "Starting wars require no reason and their spouses are slaughtered as soon as they grow bored of them. No one is safe from their wrath, not even the most hidden."

    scene black
    with fade

    "You now find yourself face to face with this vicious monarch, entrapped in the palace walls."
    "Who are you?"
    
    menu:
        # apply player sprites here and pronouns if needed.
        "Male":
            pass
        "Female":
            pass

    scene bedroom night
    with fade

    "You step away from the royal reflection in the mirror, satisfied."
    "Ah, I forgot to mention. You are the tyrant. And you killed me, along with the other twenty-five poison testers this month."
    "If you ask me, eating seems like a lost cause for you. No matter how many chefs you murder, all of your food ends up with a little drop of death in it. Perhaps you could spare all of us the time and finally accept your fate."
    "After all, an assassination is inevitable for someone with so many enemies."

    show butler

    b "Your Highness? Your bedtime tea is ready."

    p "Bring it in."

    "He enters with a bow, placing the tray of tea on your bedside table. He’s the third butler of the week, but his results have been reliable so far."

    b "Chamomile with two scoops of honey, your Highness."

    menu:
        "Thank you.":
            "…You have manners? Since when? That must be a recent development since your entire staff wants to kill-"
        "And only two scoops of honey?":
            b "Nothing more, nothing less."
        "Grunt.":
            pass
    
    scene teacup

    "You pick up the cup, swirling its warm contents. Relaxation washes over you as you breathe in the steam. {i}Will you drink it?{/i}"

    menu:
        "No.":
            jump drink_refuse
        "Yes.":
            jump drink_accept
