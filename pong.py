import turtle



#Visual do Game
    
window = turtle.Screen()


window.title("Tik Taka")

window.bgcolor("#9400D3")
window.setup(width=800, height=600)

window.tracer(0) # Basicamente faz que o jogo não fica atualizando toda hora
#Visual do Game


## Padlle A

paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("yellow")

paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

## Padlee B

paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("red")

paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

## Ball

ball = turtle.Turtle()
ball.shape("square")
ball.color("blue")

ball.penup()
ball.goto(0, 0) ## Começa do meio por isso o 0 das cordenadas

ball.dx = 0.3 ## Toda Vez que a bola se mover ela se move por 2 pixels
ball.dy = -0.3


## Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()








## Score
score_a = 0
score_b = 0




## Function

            # Up A
def paddle_a_up():
    y = paddle_a.ycor()
    
    y += 20 ## += no python funciona como +
    
    paddle_a.sety(y)

            
            #Down A

def paddle_a_down():
    y = paddle_a.ycor()
    
    y -= 20 ## -= no python funciona como -

    paddle_a.sety(y)
    

          # Up B
def paddle_b_up():
    y = paddle_b.ycor()
    
    y += 20 ## += no python funciona como +
    
    paddle_b.sety(y)

            
            #Down B

def paddle_b_down():
    y = paddle_b.ycor()
    
    y -= 20 ## -= no python funciona como -

    paddle_b.sety(y)


# Keyboard Binding
window.listen() ## Aceitar que o KeyBoard abaixo deixe apertar para funcionar o jogo

window.onkeypress(paddle_a_up, "space") # Apertando no space você pode mover pra cima o retangulo
window.onkeypress(paddle_a_down, "z") # Apertando no space você pode mover pra cima o retangulo

window.onkeypress(paddle_b_up, "m") # Apertando no space você pode mover pra cima o retangulo
window.onkeypress(paddle_b_down, "n") # Apertando no space você pode mover pra cima o retangulo


# Loop Principal do Jogo

while True:
    window.update()


    # Move the ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

 
    
    
    ## Border Checking Top and Bottom Porque o y na cordenada fica cima e baixo

                                    # Y
    if ball.ycor() > 280: ## A lógica aqui é quando a bola bater na borda ela vai voltar
        ball.sety (280)
        ball.dy *= -1
        
       
       




    if ball.ycor() < -280: 
        ball.sety(-280)
        ball.dy *= -1

                             
                                      # X

    if ball.xcor() > 380: 
        ball.goto(0,0)
        ball.dx *= -1

        ## Se a bola for pro plano cartesiano positivo ponto do Player A
        score_a += 1
        pen.clear()
        pen.goto(0, 210)
        pen.write("Player A: {} ".format (score_a), align="center",  font=("bold", 24))




    if ball.xcor() < -380: 
        ball.goto(0,0)
        ball.dx *= -1

        ## Se a bola for pro plano cartesiano negativo ponto do Player B
        score_b += 1
        pen.clear()
        pen.goto(0, -230)
        pen.write("Player B: {} ".format (score_b), align="center", font=("bold", 24))



##CURIOSIDADE: A bola só reverte porque o pixel pra bola andar é de 2 e no ball.dy está fazendo ela vezes -1 assim dando o resultado de -2 fazendo ela rebater



## Paddle and ball colisiont

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):

        ball.setx(340)
    
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):

        ball.setx(-340)
    
        ball.dx *= -1