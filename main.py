import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
dude = Player()
car_manager = CarManager()
my_scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(dude.go_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.spawn_car()
    car_manager.cars_moves()

    # detect collision with cars
    for car in car_manager.all_cars:
        if dude.distance(car) < 25:
            my_scoreboard.game_over()
            game_is_on = False

    # Update level
    if dude.has_won() == True:
        my_scoreboard.increase_score()
        car_manager.update_car_speed()

screen.exitonclick()