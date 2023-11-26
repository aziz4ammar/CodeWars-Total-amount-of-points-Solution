def points(games):
    total_points = 0

    for game in games:
        x, y = map(int, game.split(":"))
        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1
        else:
            total_points +=0

    return total_points