from pygame import *   #подключаем библиотеку pygame

back_color = (200, 255, 255) #цвет фона
win_wigth = 600  #длина экрана
win_height = 500  #ширина экрана
window = display.set_mode((win_wigth, win_height)) #создание окна игры
window.fill(back_color)  #заливка фона

clock = time.Clock()  #создаём обЪект часы
fps = 60  #ограничение частоты кадров
game = True  #переменная флаг, используется как условие для игрового цикла
finish = False  #переменная флаг, используется как условие для завершения цикла

class GameSprite(sprite.Sprite):  #создание класса
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):  #конструктор класса  
        super().__init__()  #вызов конструктора класса Sprite
        self.image = transform.scale(image.load(player_image), (size_x, size_y))  #загрузка изображения спрайта
        self.rect = self.image.get_rect()  #получение прямоугольника ограничивающего спрайт
        self.rect.x = player_x  #установление начальных координат спрайта
        self.rect.y = player_y  #установление начальных координат спрайта
        self.speed = player_speed  #установка скорости спрайта
        self.size_x = size_x  #установление размеров спрайта
        self.size_y = size_y  #установление размеров спрайта
    def reset(self):  #метод для отрисовки спрайта
        window.blit(self.image, (self.rect.x, self.rect.y))  #отрисовка спрайта

class Player(GameSprite):  #создание класса наследника GameSprite
    def update_l(self):  #метод для управления первой ракеткой
        keys = key.get_pressed()  #получение состояния всех клавиш
        if keys[K_w] and self.rect.y > 5:  #движение вверх при нажатии w
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 345:  #движение вниз при нажатии s
            self.rect.y += self.speed
    
    def update_r(self):  #метод для управления второй ракеткой
        keys = key.get_pressed()  #получение состояния всех клавиш
        if keys[K_UP] and self.rect.y > 5:  #движение вверх при нажатии стрелка вверх
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 345: #движение вверх при нажатии стрелка вниз
            self.rect.y += self.speed

racket1 = Player('platform.jpg', 20, 250, 2, 20, 150)  #создание левой ракетки
racket2 = Player('platform.jpg', 560, 250, 2, 20, 150)  #создание правой ракетки
ball = GameSprite('ball.png', 300, 250, 2, 50, 50)  #создание мяча

font.init()  #подключаем модуль font
font1 = font.Font(None, 35)  #создание обЪекта шрифта
lose1 = font1.render('Player 1 lose!', True, (180, 0, 0))  #создание текстового сообщения о поражении для левой ракетки
lose2 = font1.render('Player 2 lose!', True, (180, 0, 0))  #создание текстового сообщения о поражении для правой ракетки

speed_x = 3  #установка начальной скорости мяча по оси x
speed_y = 3  #установка начальной скорости мяча по оси y

while game:  #создание игрового цикла
    for e in event.get():  #получение всех событий из очереди событий pygame
        if e.type == QUIT:  #условие для завершения цикла
            game = False
 
    if finish != True:  #проверка не завершена ли игра
        ball.rect.x += speed_x  #перемещение мяча по осям x согласно текущей скорости
        ball.rect.y += speed_y  #перемещение мяча по осям y согласно текущей скорости

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:  #если мяч достигает верхней или нижней границы, меняем направление по y
            speed_y *= -1

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):  #если мяч сталкивается с ракеткой, меняем направление по x
            speed_x *= -1
            speed_y *= -1
        
        if ball.rect.x < 0:  #если мяч уходит за левую границу - игрок 2 выиграл
            finish = True  #остановка цикла
            window.blit(lose1, (200, 200))  #появление сообщения о поражении игрока 1
            game = False
            
        if ball.rect.x > 600:  #если мяч уходит за правую границу - игрок 1 выиграл
            finish = True  #остановка цикла
            window.blit(lose2, (200, 200))  #появление сообщения о поражении игрока 2
            game = False

        window.fill(back_color)
        racket1.reset()  #отрисовка левой ракетки
        racket2.reset()  #отрисовка правой ракетки
        ball.reset()  #отрисовка мяча
        racket1.update_l()  #передвижение левой ракетки
        racket2.update_r()  #передвижение правой ракетки

    clock.tick(fps)  #ограничение частоты кадров до значения fps
    display.update()  #обновление всего экрана
