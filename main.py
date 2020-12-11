def on_button_pressed_a():
    vaisseau.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global pioupiou, score, difficulté
    pioupiou = game.create_sprite(vaisseau.get(LedSpriteProperty.X),
        vaisseau.get(LedSpriteProperty.Y))
    for index in range(4):
        pioupiou.change(LedSpriteProperty.Y, 1)
        basic.pause(20)
        if pioupiou.is_touching(cible):
            score += 1
        else:
            difficulté += 0 - 1
        if pioupiou.get(LedSpriteProperty.Y) == 4:
            pioupiou.delete()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    vaisseau.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

x = 0
pioupiou: game.LedSprite = None
vaisseau: game.LedSprite = None
cible: game.LedSprite = None
score = 0
vie = 5
cible = game.create_sprite(2, 4)
vaisseau = game.create_sprite(2, 0)
difficulté = 1
victoire = 1

def on_forever():
    global x, difficulté
    x = randint(0, 4)
    if victoire == 1:
        cible.set(LedSpriteProperty.X, x)
        if difficulté == 1:
            basic.pause(2000)
        if difficulté == 2:
            basic.pause(1000)
        if difficulté == 3:
            basic.pause(500)
        if difficulté == 4:
            basic.pause(250)
        if game.score() == 10:
            difficulté += 1
    if victoire == 0:
        basic.show_string("Perdu")
basic.forever(on_forever)
