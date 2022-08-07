station: game.LedSprite = None
airlock: game.LedSprite = None
asteroid: game.LedSprite = None
X_Acceleration = 0
AliveOrnot = 1
# variables
player = game.create_sprite(2, 4)
delay = 500
# player controlls

def on_forever():
    global X_Acceleration
    X_Acceleration = input.acceleration(Dimension.X)
    # move player
    if X_Acceleration < 150 and player.get(LedSpriteProperty.X) > 0:
        player.change(LedSpriteProperty.X, -1)
    elif X_Acceleration > 150 and player.get(LedSpriteProperty.X) < 4:
        player.change(LedSpriteProperty.X, 1)
    basic.pause(600)
basic.forever(on_forever)

# asteroid movment

def on_forever2():
    global asteroid, delay, AliveOrnot, airlock, station
    while AliveOrnot:
        asteroid = game.create_sprite(Math.random_range(4, 0), 0)
        # move asteroid
        while asteroid.get(LedSpriteProperty.Y) < 4:
            asteroid.change(LedSpriteProperty.Y, 1)
            basic.pause(delay)
        asteroid.delete()
        game.add_score(1)
        # speed up asteroids
        delay = delay - delay / 350
        if delay < 0:
            delay = 0.25
        # check for player collisions
        if player.get(LedSpriteProperty.Y) == asteroid.get(LedSpriteProperty.Y) and player.get(LedSpriteProperty.X) == asteroid.get(LedSpriteProperty.X):
            AliveOrnot = 0
            game.game_over()
            break
        # station
        if game.score() == 4:
            airlock = game.create_sprite(2, 0)
            station = game.create_sprite(3, 0)
            while airlock.get(LedSpriteProperty.Y) < 4:
                airlock.change(LedSpriteProperty.Y, 1)
                station.change(LedSpriteProperty.Y, 1)
                basic.pause(delay)
            # check for succsessful docking
            if player.get(LedSpriteProperty.Y) == airlock.get(LedSpriteProperty.Y) and player.get(LedSpriteProperty.X) == airlock.get(LedSpriteProperty.X):
                game.add_score(100)
                basic.show_string("+100 POINTS")
                # delete station
                if airlock.is_touching_edge():
                    airlock.delete()
                    station.delete()
basic.forever(on_forever2)
