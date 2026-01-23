#This is chain that continues from start.rpy when the player refuses to drink the tea.

default kills = 0

label drink_refuse:
    scene bedroom night

    "You bid your butler away and go to bed on a cold stomach."
    "Without your bedtime tea, you sleep fitfully."

    scene bedroom day

    $ kills = renpy.random.randint(50,200)
    "The day passes quickly and in your irritated state, you kill [kills] Allarian citizens and palace staff."

    scene teacup

    "When night falls, your butler arrives with tea once more. Chamomile and two scoops of honey. {i}Will you drink it?{/i}"

    menu:
        "No.":
            scene bedroom night

            "You bid your butler away and go to bed on a cold stomach."
            "Without your bedtime tea, you sleep fitfully."

            scene bedroom day

            $ kills = renpy.random.randint(50,200)
            "The day passes quickly and in your irritated state, you kill [kills] Allarian citizens and palace staff."

            scene teacup

        "Yes.":
            jump drink_accept 