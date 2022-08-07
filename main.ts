// player controlls
input.onButtonPressed(Button.A, function () {
    player.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function () {
    player.change(LedSpriteProperty.X, 1)
})
let station: game.LedSprite = null
let airlock: game.LedSprite = null
let asteroid: game.LedSprite = null
let player: game.LedSprite = null
let AliveOrnot = 1
// variables
player = game.createSprite(2, 4)
let delay = 350
// asteroid movment
basic.forever(function () {
    while (AliveOrnot) {
        asteroid = game.createSprite(Math.randomRange(4, 0), -1)
        // move asteroid
        while (asteroid.get(LedSpriteProperty.Y) < 4) {
            asteroid.change(LedSpriteProperty.Y, 1)
            basic.pause(delay)
        }
        asteroid.delete()
        game.addScore(1)
        // speed up asteroids
        delay = delay - delay / 70
        // check for player collisions
        if (player.get(LedSpriteProperty.Y) == asteroid.get(LedSpriteProperty.Y) && player.get(LedSpriteProperty.X) == asteroid.get(LedSpriteProperty.X)) {
            AliveOrnot = 0
            game.gameOver()
            break;
        }
        // station
        if (game.score() % 40 == 0) {
            airlock = game.createSprite(2, 0)
            station = game.createSprite(3, 0)
            while (airlock.get(LedSpriteProperty.Y) < 4) {
                airlock.change(LedSpriteProperty.Y, 1)
                station.change(LedSpriteProperty.Y, 1)
                basic.pause(delay)
            }
            // check for succsessful docking
            if (player.get(LedSpriteProperty.Y) == airlock.get(LedSpriteProperty.Y) && player.get(LedSpriteProperty.X) == airlock.get(LedSpriteProperty.X)) {
                basic.showString("+100 POINTS")
                game.addScore(100)
            }
            // delete station
            if (airlock.isTouchingEdge()) {
                airlock.delete()
                station.delete()
            }
        }
    }
})
