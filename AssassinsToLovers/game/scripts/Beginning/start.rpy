# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Butler", color="#492828c1")
define p = Character("You", color="#195b13")


# The game starts here.

label start:
    scene bg kingdom

    "In the Kingdom of Allaria, a tyrant rules the land."
    "Their mood shifts with the wind, threatening and bestowing favor to whoever they please."
    "Starting wars require no reason and their spouses are slaughtered as soon as they grow bored of them. No one is safe from their wrath, not even the most hidden."

    scene bg black
    with fade

    "You now find yourself face to face with this vicious monarch, entrapped in the palace walls."
    "Who are you?"
    
    menu:
        "Male":
        "Female":

    scene bedroom night
    with fade

    "You step away from the royal reflection in the mirror, satisfied."
    "Ah, I forgot to mention. You are the tyrant. And you killed me, along with the other twenty-five poison testers this month."
    "If you ask me, eating seems like a lost cause for you. No matter how many chefs you murder, all of your food ends up with a little drop of death in it. Perhaps you could spare all of us the time and finally accept your fate."
    "After all, an assassination is inevitable for someone with so many enemies."

    b "Your Highness? Your bedtime tea is ready."

    p "Bring it in."

    "He enters with a bow, placing the tray of tea on your bedside table. He’s the third butler of the week, but his results have been reliable so far."

    b "Chamomile with two scoops of honey, your Highness."

    menu:
        "Thank you."
            "…You have manners? Since when? That must be a recent development since your entire staff wants to kill-"
        "And only two scoops of honey?"
            b "Nothing more, nothing less."
        "Grunt."
    
    scene teacup

    "You pick up the cup, swirling its warm contents. Relaxation washes over you as you breathe in the steam. {i}Will you drink it?{/i}"

    menu:
        "No."
            jump drink_refuse
        "Yes."
            jump drink_accept

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    player "You've created a new Ren'Py game."

    player "Once you add a story, pictures, and music, you can release it to the world!"

    player "I', by the way."

    # made this as a sample jump to another script file in a different folder

    jump choice_scene
