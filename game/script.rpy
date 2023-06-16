# character and image definitions
define s = Character("Sariel", color="#f7b0b8")
define l = Character("Lythienne", color="#f37227")
define w = Character("??", color="#f37227")
image sariel = im.Scale("sariel_big.png", 600, 681)
image lyth = im.Scale("lyth_big.png", 627, 681)

default lyth_relationship = 50
default inventory = []
default objects_on_ground = {"potion": True, "sword": True} # "staff": True

screen item_potion:
    showif objects_on_ground["potion"]:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.75
                ypos 0.55
                idle "potion_idle.png"
                hover "potion_hover.png"
                if not objects_on_ground["sword"]:
                    action [SetDict(objects_on_ground, "potion", False), inventory.append("potion"), Jump("meet_lyth")]
                else:
                    action [SetDict(objects_on_ground, "potion", False), inventory.append("potion")]

screen item_sword:
    showif objects_on_ground["sword"]:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.85
                ypos 0.42
                idle "sword_idle.png"
                hover "sword_hover.png"
                if not objects_on_ground["potion"]:
                    action [SetDict(objects_on_ground, "sword", False), inventory.append("sword"), Jump("meet_lyth")]
                else:
                    action [SetDict(objects_on_ground, "sword", False), inventory.append("sword")]

screen lyth_points:
    bar:
        value lyth_relationship
        range(100)
        xysize(200, 25)
        xalign .1
        yalign .9


# The game starts here.

label start:
    scene purple
    show screen item_potion
    show screen item_sword

    show sariel at left

    s "This place is creepy."

    s "I might as well pick up some of this stuff while I'm here."

    # show tooltip: click on stuff to add it to inventory

    window hide dissolve

    $ renpy.notify("Click on an interactable item to add it to your inventory. Interactable items will be highlighted when you mouse over them.")

    $ wait_for_inventory(len(inventory) > 1)

    label meet_lyth:

        # window show

        show lyth at right

        s "??"

        s "Who are you?"

        w "Well, not the nicest introduction from someone entering my domain unannounced."

        w "But since it seems my reputation does not precede me...."

        l "I'm Lythienne."

        show screen lyth_points

        menu: 
            "What do I say?"

            "I'm Sariel. I'm here for the Grimoire.":
                $ lyth_relationship -= 25
                jump grimoire
            
            "Your name sounds familiar...":
                $ lyth_relationship += 25
                jump familiar

    label grimoire:
        l "Great. Another one. What else is new."

        l "Well, you're not going to find it here. Do you see any place I might have something like that hidden?"

        l "Any bookshelves? No?"

        s "This has to be the place. The map led here."

    label familiar:
        l "Hmm. Maybe I have a reputation after all."

        s "..."

    # This ends the game.
    return
