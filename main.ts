input.onButtonPressed(Button.A, function on_button_pressed_a() {
    media.startMediaService()
    basic.showLeds(`
        . . # # .
                . # # # .
                # # # # .
                . # # # .
                . . # # .
    `)
    media.sendCode(media.keys(media._MediaKey.previous))
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    let pause2 = 0
    media.startMediaService()
    basic.showLeds(`
        . # . # .
                . # . # .
                . # . # .
                . # . # .
                . # . # .
    `)
    media.sendCode(pause2)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    media.startMediaService()
    basic.showLeds(`
        . # # . .
                . # # # .
                . # # # #
                . # # # .
                . # # . .
    `)
    media.sendCode(media.keys(media._MediaKey.next))
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    let play = 0
    media.startMediaService()
    basic.showLeds(`
        . . # # .
                . # # # .
                # # # # .
                . # # # .
                . . # # .
    `)
    media.sendCode(play)
})
media.startMediaService()
