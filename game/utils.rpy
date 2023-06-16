init python:
    def wait_for_inventory(is_on_ground):
        while(is_on_ground):
            renpy.pause(1)
        return