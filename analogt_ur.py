import math
import pygame
from datetime import datetime


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Analogt ur")
frame_clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

center_x = 320
center_y = 240
radius = 180

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Urskiven og 60 sekundmarkeringer
    pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), radius, 2)

    for second in range(60):
        angle = math.radians(second * 6)
        start_x = center_x + math.sin(angle) * 170
        start_y = center_y - math.cos(angle) * 170
        end_x = center_x + math.sin(angle) * radius
        end_y = center_y - math.cos(angle) * radius
        pygame.draw.line(screen, (0, 0, 0),
                         (int(start_x), int(start_y)),
                         (int(end_x), int(end_y)), 1)

    # 12 timemarkeringer og tallene 1-12
    for number in range(12):
        angle = math.radians(number * 30)
        start_x = center_x + math.sin(angle) * 160
        start_y = center_y - math.cos(angle) * 160
        end_x = center_x + math.sin(angle) * radius
        end_y = center_y - math.cos(angle) * radius
        pygame.draw.line(screen, (0, 0, 0),
                         (int(start_x), int(start_y)),
                         (int(end_x), int(end_y)), 2)

        # Tal markering for hvert timeslag
        if number == 0:
            hour_number = 12
        else:
            hour_number = number
        number_text = font.render(str(hour_number), True, (0, 0, 0))
        text_x = center_x + math.sin(angle) * 135
        text_y = center_y - math.cos(angle) * 135
        text_rect = number_text.get_rect(center=(int(text_x), int(text_y)))
        screen.blit(number_text, text_rect)

    # Henter klokkeslæt fra computeren
    now = datetime.now()
    hour_angle = math.radians((now.hour % 12 + now.minute / 60) * 30)
    minute_angle = math.radians((now.minute + now.second / 60) * 6)
    second_angle = math.radians(now.second * 6)

    # Timeviseren
    hour_x = center_x + math.sin(hour_angle) * 90
    hour_y = center_y - math.cos(hour_angle) * 90
    pygame.draw.line(screen, (0, 0, 0), (center_x, center_y),
                     (int(hour_x), int(hour_y)), 6)

    # Minutviseren
    minute_x = center_x + math.sin(minute_angle) * 135
    minute_y = center_y - math.cos(minute_angle) * 135
    pygame.draw.line(screen, (0, 0, 0), (center_x, center_y),
                     (int(minute_x), int(minute_y)), 4)

    # Sekundviseren
    second_x = center_x + math.sin(second_angle) * 155
    second_y = center_y - math.cos(second_angle) * 155
    pygame.draw.line(screen, (255, 0, 0), (center_x, center_y),
                     (int(second_x), int(second_y)), 2)

    pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), 5)
    pygame.display.flip()
    frame_clock.tick(30)

pygame.quit()
