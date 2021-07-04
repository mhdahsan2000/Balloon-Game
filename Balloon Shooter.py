import turtle
import random
import os 


win = turtle.Screen()
win.title('The BALLOON Shooting Game with edits by mohammed')
win.setup(800,600)
win.bgpic('bkg.gif')
win.tracer(0) 
win.listen() 

cannon = turtle.Turtle()
cannon.shape('square')
cannon.shapesize(2,2) 
cannon.color('black')
cannon.up() 
cannon.goto(-360, -260)

bullet = turtle.Turtle()
bullet.shape('square')
bullet.shapesize(0.2, 0.7)
bullet.color('red')
bullet.lt(50)
bullet.up()
bullet.goto(-340, -240)
bullet.state = 'ready'

pen = turtle.Turtle()
pen.up()
pen.hideturtle()
pen.color('red')
pen.goto(200,-275)
pen.write('POINTS: 0', font=('Century Gothic', 24, 'normal'))


def shoot():
    if bullet.state == 'ready':
            bullet.state = 'fire'
   
    
def bullet_shot():
    bullet.fd(10) 
    if bullet.ycor()<-300 or bullet.ycor()>300 or bullet.xcor()>400: 
        bullet.goto(-340, -240)
        bullet.state = 'ready'
        
    
def turn_right():
    if bullet.state == 'ready':
        bullet.rt(10)
    
    
def turn_left():
    if bullet.state == 'ready':
        bullet.lt(10)
    

win.onkey(shoot, 'space')
win.onkey(turn_left, 'Left')
win.onkey(turn_right, 'Right')

enemy_list = []
colors = ['green']
game_over = False
score = 0

while not game_over:
    win.update()

    
    if bullet.state == 'fire':
        bullet_shot()


    delay = random.random() 
    if len(enemy_list)<10 and delay < 0.05: 
        enemy = turtle.Turtle()
        enemy.shape('circle')
        enemy.shapesize(2,2)
        enemy.color('green')
        enemy.up()
        enemy.goto(420, random.randint(0,280))
        enemy_list.append(enemy)

    for i in enemy_list:
        i.goto(i.xcor()-0.5, i.ycor()) 

        # If the bullet reaches end of the screen the game would be over
        if i.xcor()<-420:
            i.goto(1000,1000) 
            enemy_list.remove(i)
            game_over = True
            pen.goto(0,0)
            pen.clear()
            pen.write(f'!! GAME OVER, GREAT ATTEMPT. TRY AGAIN !!\nScore: {score}',align='center',
                      font=('Century Gothic', 20, 'bold'))
            
        
        if bullet.distance(i) < 30:
            i.goto(1000,1000) 
            enemy_list.remove(i)
            bullet.goto(-340, -240)
            bullet.state = 'ready'
            score += 1
            pen.clear()
            pen.goto(100,100)
            pen.write(f'press space to shoot,left key for left' 
                      ,font=('Century Gothic', 10, 'bold') )
            pen.goto(100,30)
            pen.write(f'and press right key for right' 
                      ,font=('Century Gothic', 10, 'bold') )






