import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y, opponent_score, player_score, timer
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score += 1
        timer = pygame.time.get_ticks()

    if ball.right >= screen_width:
        opponent_score += 1
        timer = pygame.time.get_ticks()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        
def paddles_animation():
    #player
    if player.bottom >= screen_height - 10:
        player.bottom = screen_height -10
    if player.top <= 10:
        player.top = 10
    
def opponentAI():
    if opponent.bottom >= screen_height - 10:
        opponent.bottom = screen_height - 10
    if opponent.top <= 10:
        opponent.top = 10

    if opponent.top >= ball.y:
        opponent.top -= opponent_speed
    if opponent.top <= ball.y:
        opponent.top += opponent_speed

def return_ball():
    global ball_speed_x, ball_speed_y, timer

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)
    
    if current_time - timer < 700:
        number_three = font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width/2 - 9, screen_height/2 - 50))
    if 700 < current_time - timer < 1400:
        number_two = font.render("2", False, light_grey)
        screen.blit(number_two, (screen_width/2 - 9, screen_height/2 - 50))
    if 1400 < current_time - timer < 2100:
        number_one = font.render("1", False, light_grey)
        screen.blit(number_one, (screen_width/2 - 9, screen_height/2 - 50))
    if current_time - timer < 2100:
        ball_speed_x = 0
        ball_speed_y = 0
    else:
        if opponent_score <= player_score:
            ball_speed_x = -7
            ball_speed_y = 7 * random.choice((1, -1))
        if opponent_score >= player_score:
            ball_speed_x = 7
            ball_speed_y = 7 * random.choice((1, -1))
        timer = None
#general setup
pygame.init()
clock = pygame.time.Clock()

#screen
screen_height = 690
screen_width = 1366
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong: Made by B  i  s  h  a  l')

#game rectangles
ball = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10 , 20, 20)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

#colors
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

#variables
ball_speed_x = 10 * random.choice((1, -1))
ball_speed_y = 0 * random.choice((1, -1))
player_speed = 0
opponent_speed = 9
opponent_score = 0
player_score = 0

#game fonts
font = pygame.font.Font("freesansbold.ttf", 32)

# timer
timer = None
#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    player.y += player_speed

    ball_animation()
    paddles_animation()
    opponentAI()
    
    #visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    if timer:
        return_ball()

    player_text = font.render(f"{player_score}", False, light_grey)
    opponent_text = font.render(f"{opponent_score}", False, light_grey)
    screen.blit(player_text, (701, 325))
    screen.blit(opponent_text, (651, 325))
    
    #updating the window
    pygame.display.flip()
    clock.tick(60)
