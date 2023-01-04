GAME_SPEED = 0.1
CAR_FREQUENCY = 3 # Increase number for less frequent cars.


import time
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scores = Scoreboard()
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle.listen()
player_turtle = Player()
car_list = CarManager()
new_car = 1
game_is_on = True
while game_is_on:
    turtle.onkeypress(player_turtle.move_up, "Up")
    if new_car % CAR_FREQUENCY == 0:
        car_list.create_cars()
    car_list.move_cars()
    new_car += 1
    for car in car_list.all_cars:
        car_pos_x = car.position()[0]
        car_pos_y = car.position()[1]
        player_pos_x = player_turtle.position()[0]
        player_pos_y = player_turtle.position()[1]
        if car_pos_x < 40 and car_pos_x > -40 and player_pos_y == car_pos_y:
            scores.game_over()
            game_is_on = False
    if player_turtle.position()[1] > 280:
        scores.update_scoreboard()
        player_turtle.setpos(0,-250)
        car_list.clear_fleet()
        GAME_SPEED *= .9

    time.sleep(GAME_SPEED)
    screen.update()

screen.exitonclick()

