def on_button_pressed_a():
    media.start_media_service()
    basic.show_leds("""
        . . # # .
                . # # # .
                # # # # .
                . # # # .
                . . # # .
    """)
    media.send_code(media.keys(media._MediaKey.PREVIOUS))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    pause2 = 0
    media.start_media_service()
    basic.show_leds("""
        . # . # .
                . # . # .
                . # . # .
                . # . # .
                . # . # .
    """)
    media.send_code(pause2)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    media.start_media_service()
    basic.show_leds("""
        . # # . .
                . # # # .
                . # # # #
                . # # # .
                . # # . .
    """)
    media.send_code(media.keys(media._MediaKey.NEXT))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    play = 0
    media.start_media_service()
    basic.show_leds("""
        . . # # .
                . # # # .
                # # # # .
                . # # # .
                . . # # .
    """)
    media.send_code(play)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

media.start_media_service()