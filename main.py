import pygame
from pygame.locals import QUIT
from classes import Ball, Player, win_width, win_height
import Functions

pygame.init()

fps = 60

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


my_ball = Ball()


p1 = Player()
p2 = Player()

def main():
    play = True

    font = pygame.font.Font(None, 60)

    p1.x = 60
    p2.x = win_width - 60 - p2.width

    while play:
        window.fill(BLACK)
        
        my_ball.move()
        my_ball.bounce()

        p1.move()
        p1.hit(my_ball)
        p2.move2(my_ball)
        p2.hit2(my_ball)


        
        pygame.draw.rect(window, WHITE, (my_ball.x, my_ball.y, my_ball.width, my_ball.height))
        pygame.draw.rect(window, WHITE, (p1.x, p1.y, p1.width, p1.height))
        pygame.draw.rect(window, WHITE, (p2.x, p2.y, p2.width, p2.height))

        text = f"{my_ball.points} : {my_ball.points2}"
        letrero = font.render(text, False, WHITE)
        window.blit(letrero, (win_width / 2 - font.size(text)[0] / 2, 50))

        for event in pygame.event.get():
            if event.type == QUIT:
                play = False
            
                        # Detecta que se ha pulsado una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    p1.dir_y = -5
                if event.key == pygame.K_s:
                    p1.dir_y = 5

            # Detecta que se ha soltado la tecla
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    p1.dir_y = 0
                if event.key == pygame.K_s:
                    p1.dir_y = 0

        pygame.display.flip()
        pygame.time.Clock().tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()



#WEIGHTS


w = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


#BIAS
b = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

#NEURONES

#input:
n1 = my_ball.x #Ball x
n2 = my_ball.y #Ball y
n3 = Functions.CalcA(my_ball.dir_x, my_ball.dir_y) #Ball direction
n4 = fps #Ball Velocity
n5 = p2.x #Player x
n6 = p2.y #Player y 
n7 = p2.height #Player Height




Input = [n1, n2, n3, n4, n5, n6, n7]



#hiddenLayer


n9 = Functions.CalcNeurone(n1, w[1], n2, w[2], n3, w[3], b[1])
n10 = Functions.CalcNeurone(n2, w[2], n3, w[3], n4, w[4], b[2])
n11 = Functions.CalcNeurone(n3, w[3], n4, w[4], n5, w[5], b[3])
n12 = Functions.CalcNeurone(n4, w[4], n5, w[5], n6, w[6], b[4])
n13 = Functions.CalcNeurone(n5, w[5], n6, w[6], n7, w[7], b[5])
n14 = Functions.CalcNeurone(n6, w[6], n7, w[7], n1, w[8], b[6])
n15 = Functions.CalcNeurone(n7, w[7], n1, w[8], n2, w[9], b[7])
n16 = Functions.CalcNeurone(n1, w[8], n2, w[9], n3, w[10], b[8])
n17 = Functions.CalcNeurone(n2, w[9], n3, w[10], n4, w[11], b[9])


HiddenLayer = [n9, n10, n11, n12, n13, n14, n15, n16, n17]


#OutPut

Up
Down
stay

OutPut = [Up, Down ,stay]
