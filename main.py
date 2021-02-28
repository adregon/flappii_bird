import pygame
import play
from random import randint
from time import sleep

catolog=0
play.set_backdrop((215, 196, 164))




bird=play.new_image(image='sprite_23.png',x=-200,y=0,size=300)
bird.start_physics(can_move=True,stable=False,bounciness=0)




def draw_truba(y,delta):
    size = 100
    trub=play.new_image(image="sprite_1.png",x=0,y=y,size=size)
    trub2=play.new_image(image="sprite_22.png",x=0,y=y+700+delta,size=size)
    return trub, trub2




truba_list =[]

@play.repeat_forever
async def do():
    truba_list.append(draw_truba(randint(-500,-100),0))
    await play.timer(2)


@play.repeat_forever
async def do():
    if play.key_is_pressed('space'):
        bird.physics.y_speed=30         
        await play.timer(0.1)


play.start_program()
