import random
win_width = 960
win_height = 540


class Ball:
    def __init__(self):
        self.width = 25
        self.height = 25
        self.x = win_width / 2 - self.width / 2
        self.y = win_height / 2 - self.height / 2
        self.velocity = 1
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])
        self.points = 0
        self.points2 = 0

    def move(self):
        self.x += self.dir_x
        self.y += self.dir_y

    
    def restart(self):
        self.x = win_width / 2 - self.width / 2
        self.y = win_height / 2 - self.height / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])

    def bounce(self):
        if self.x <= -self.width:
            self.restart()
            self.points2 += 1
        if self.x >= win_width:
            self.restart()
            self.points += 1
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.height >= win_height:
            self.dir_y = -self.dir_y

class Player:
    def __init__(self):
        self.width = 25
        self.height = 100
        self.x = 0
        self.y = win_height / 2 - self.height / 2
        self.dir_y = 0

    def move(self):
        self.y += self.dir_y
        if self.y <= 0:
            self.y = 0
        if self.y + self.height >= win_height:
            self.y = win_height - self.height

    def move2(self, ball):
        if self.y > ball.y:
            self.dir_y = -3
        elif self.y < ball.y:
            self.dir_y = 3
        else:
            self.dir_y = 0

        self.y += self.dir_y
    
    def hit(self, ball):
        if (
            ball.x < self.x + self.width
            and ball.x > self.x
            and ball.y + ball.height > self.y
            and ball.y < self.y + self.height
        ):
            ball.dir_x = -ball.dir_x
            ball.x = self.x + self.width  

    def hit2(self, ball):
        if (
            ball.x + ball.width > self.x
            and ball.x < self.x + self.width
            and ball.y + ball.height > self.y
            and ball.y < self.y + self.height
        ):
            ball.dir_x = -ball.dir_x
            ball.x = self.x - ball.width