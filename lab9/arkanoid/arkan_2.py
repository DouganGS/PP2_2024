import pygame
import random
import sys

def main():
    pygame.init()

    W, H = 800, 600
    FPS = 60
    ball_speed = 5
    paddle_speed = 10
    brick_w = 60
    brick_h = 20
    paddle_w = 150
    paddle_h = 20
    ball_rad = 10
    score = 0

    screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
    pygame.display.set_caption("Arkanoid")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 30)

    ball_x, ball_y = W // 2, H // 2
    ball_dx, ball_dy = random.choice([-1, 1]) * ball_speed, -ball_speed
    paddle_x = W // 2 - paddle_w // 2
    paddle_y = H - paddle_h - 10
    bricks = []
    unbreakable_bricks = []

    # Create bricks
    for i in range(5):
        for j in range(10):
            brick_x = j * (brick_w + 5) + 5
            if brick_x + brick_w <= W:
                brick = pygame.Rect(brick_x, i * (brick_h + 5) + 50, brick_w, brick_h)
                if random.random() < 0.1:
                    unbreakable_bricks.append(brick)
                else:
                    bricks.append(brick)

    # Bonus brick
    bonus_brick = pygame.Rect(random.randint(0, W - brick_w), random.randint(0, H // 2), brick_w, brick_h)
    bonus_active = False
    bonus_timer = FPS * 5

    # Fonts
    font = pygame.font.SysFont('comicsansms', 40)
    pause_font = pygame.font.SysFont('comicsansms', 60)
    resume_font = pygame.font.SysFont('comicsansms', 30)

    def pause_game():
        screen.fill('White')
        pause_text = pause_font.render('Pause', False, 'Black')
        screen.blit(pause_text, (W//2 - pause_text.get_width()//2, H//2 - pause_text.get_height()//2))
        resume_text = resume_font.render('Press M to resume', False, 'Black')
        screen.blit(resume_text, (W//2 - resume_text.get_width()//2, H//2 + pause_text.get_height()))
        pygame.display.flip()

        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        paused = False

    run = True
    pause = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause_game()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x >= 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x <= W - paddle_w:
            paddle_x += paddle_speed

        ball_x += ball_dx
        ball_y += ball_dy

        if ball_x < ball_rad or ball_x > W - ball_rad:
            ball_dx *= -1
        if ball_y < ball_rad:
            ball_dy *= -1
        if ball_y > H - ball_rad:
            run = False  # Lose

        ball_rect = pygame.Rect(ball_x - ball_rad, ball_y - ball_rad, ball_rad * 2, ball_rad * 2)
        paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_w, paddle_h)

        if ball_rect.colliderect(paddle_rect):
            ball_dy *= -1
        for brick in bricks:
            if ball_rect.colliderect(brick):
                bricks.remove(brick)
                ball_dy *= -1
                score += 1
        for brick in unbreakable_bricks:
            if ball_rect.colliderect(brick):
                ball_dy *= -1

        # Ball speed increase
        ball_speed += 0.01

        # Paddle shrink decrease
        if paddle_w > 50:
            paddle_w -= 0.01
        paddle_rect.width = paddle_w

        # Bonus brick
        if bonus_active:
            bonus_timer -= 1
            if bonus_timer <= 0:
                bonus_active = False

        if ball_rect.colliderect(bonus_brick):
            bonus_active = True
            bonus_timer = FPS * 5
            bonus_brick = pygame.Rect(random.randint(0, W - brick_w), random.randint(0, H // 2),brick_w, brick_h)

        if len(bricks) == 0:
            run = False  # Win

        screen.fill('White')
        for brick in bricks:
            pygame.draw.rect(screen, 'Red', brick)
        for brick in unbreakable_bricks:
            pygame.draw.rect(screen, 'Blue', brick)

        if bonus_active:
            pygame.draw.rect(screen, 'Yellow', bonus_brick)

        pygame.draw.rect(screen, 'Blue', (paddle_x, paddle_y, paddle_w, paddle_h))
        pygame.draw.circle(screen, 'Green', (ball_x, ball_y), ball_rad)

        score_text = font.render(f"Score: {score}", True, pygame.Color('black'))
        screen.blit(score_text, (W//3+50, 0))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

main()
