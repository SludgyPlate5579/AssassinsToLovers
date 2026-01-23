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
            "Without your bedtime tea, you are restless."

            scene bedroom day

            $ kills = renpy.random.randint(200,1000)
            "The day passes quickly and in your agitation, you kill [kills] Allarian citizens and palace staff."

            scene teacup

            "When night falls, your butler arrives with tea {i}yet again{/i}. I already told you, tyrant, accept your fate. Wasting our time… {i}Will you drink it?{/i}"

            menu:
                "No.":
                    "I warned you, you know."

                    scene bedroom night

                    "You bid your butler away and go to bed on a cold stomach."

                    scene bedroom day
                    show blood onlayer overlay

                    "Today, your rampage does not go over so peacefully. The assassins have given up on your meals and resorted to direct violence. With so many citizens and staff gone, there is no one to shield you. Your throat is slit and your reign of evil finally comes to an end."
                    "{i}THE END{/i}"

                    $ renpy.full_restart()
                "Yes":
                    jump drink_accept

        "Yes.":
            jump drink_accept 