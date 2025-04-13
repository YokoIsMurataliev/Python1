from snakeApp.classes.point import Point

def food_eating(_inner_data_, snake, all_food):
    for food in all_food:
        if snake.check_collision(food.location):
            _inner_data_['score'] += food.values[food.current]
            snake.body.append(Point(-1, -1))
            food.update()

            #_____Level(SPEED) incresing_____
            if (len(snake.body) % 3 == 0 and len(snake.body) != 0): 
                _inner_data_['speed'] += 1

    return _inner_data_