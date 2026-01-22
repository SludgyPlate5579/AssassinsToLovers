# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define player = Character("Player")


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

    if player.name == "":
        $ player.name = "No Name"
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

    player "I'm %(player)s, by the way."

    # made this as a sample jump to another script file in a different folder

    jump choice_scene
