# usr/bin/env

# Created by Ben Lapuhapo
# Created on Oct 2019
# Pibadge

import ugame
import stage

# an image bank for CircuitPython
image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
# A list of sprites that will be updated every frame
sprites = []


def main():
    # this function is a scene

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 10, 8)

    # Create a sprite
    # parameters (image_bank, image # in bank, x, y)
    alien = stage.Sprite(image_bank_1, 9, 64, 56)
    sprites.append(alien)
    ship = stage.Sprite(image_bank_1, 5, 74, 56)
    sprites.insert(0, ship)  # insert at the top of the sprite list

    # create a stage for the background to show up on
    # and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = sprites + [background]
    # render the background and initial location of sprites list
    # most likely you will render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # print (keys)

        if keys & ugame.K_X:
            # print ("A")
            pass
        if keys & ugame.K_O:
            # print ("B")
            pass
        if keys & ugame.K_START:
            # print ("K_START")
            pass
        if keys & ugame.K_SELECT:
            # print ("K_SELECT")
            pass
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
            pass
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
            pass
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
            pass
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
            pass

        # update game logic

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    main()
