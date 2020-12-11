input.onButtonPressed(Button.A, function () {
    vaisseau.move(-1)
})
input.onButtonPressed(Button.AB, function () {
    pioupiou = game.createSprite(vaisseau.get(LedSpriteProperty.X), vaisseau.get(LedSpriteProperty.Y))
    for (let index = 0; index < 4; index++) {
        pioupiou.change(LedSpriteProperty.Y, 1)
        basic.pause(20)
        if (pioupiou.isTouching(cible)) {
            score += 1
        } else {
            difficulté += 0 - 1
        }
        if (pioupiou.get(LedSpriteProperty.Y) == 4) {
            pioupiou.delete()
        }
    }
})
input.onButtonPressed(Button.B, function () {
    vaisseau.move(1)
})
let x = 0
let score = 0
let pioupiou: game.LedSprite = null
let vaisseau: game.LedSprite = null
let cible: game.LedSprite = null
let vie = 5
cible = game.createSprite(2, 4)
vaisseau = game.createSprite(2, 0)
let difficulté = 1
let victoire = 1
basic.forever(function () {
    x = randint(0, 4)
    if (vie < 1) {
        cible.set(LedSpriteProperty.X, x)
        if (difficulté == 1) {
            basic.pause(2000)
        }
        if (difficulté == 2) {
            basic.pause(1000)
        }
        if (difficulté == 3) {
            basic.pause(500)
        }
        if (difficulté == 4) {
            basic.pause(250)
        }
        if (game.score() == 10) {
            difficulté += 1
        }
    }
    if (vie == 0) {
        basic.showString("Perdu")
    }
})
