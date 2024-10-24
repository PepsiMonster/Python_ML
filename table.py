import torch
import sklearn 
import sqlalchemy


from turtle import *
def draw_squre(len):
    for i in range(4):
        forward(len)
        right(90)
def draw_grid(rows,coloumns,square_length):
    for i in range(rows):
        for j in range(coloumns):
            draw_squre(square_length)
            forward(square_length)
        penup()
        goto(0, -((i+1)*square_length))
        pendown()

square_length = 50
rows = 5
coloumns  = 5

speed = 0 
penup()
goto(0)
pendown()
