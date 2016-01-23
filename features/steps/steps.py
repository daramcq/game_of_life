from behave import *
from game import Game

@given('a game with seed')
def game_with_seed(context):
    dimensions = (5,5)
    cell_set = set([(1,2),(3,3),(2,1),(2,2),(4,5)])    
    context.game = Game(dimensions, cell_set)

@when('I step the game')
def step_the_game(context):
    context.game = context.game.stepGame()

@then('I receive a new game')
def receive_new_game(context):
    assert context.game

