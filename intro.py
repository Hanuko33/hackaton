import pygame
from pygame.locals import QUIT, KEYDOWN
from music import music

t = 0
running = True

background = pygame.image.load("./textures/wizardtower.png")

times_text = {
    100: "In the peaceful realm of Uranex, harmony thrived among its inhabitants.",
    300: "They lived blissfully unaware of the looming shadows that threatened their existence.",
    600: "But then, without warning, disaster struck the very core of their world.",
    800: "Crisis unleashed chaos, shattering their tranquility.",
    1000: "...",
    1200: "The once-vibrant beings were thrown into a reactor...",
    1300: "tainted by a dark energy that warped their essence.",
    1500: "Yet, amidst the corruption, a spark of hope ignited...",
    1600: "One of them dared to resist the encroaching darkness.",
    1700: "...",
    1800: 'This brave soul was known as "Uranek," the beacon of defiance...',
    2000: "Though he stood alone, he carried the weight of a world's fate...",
    2200: "Now, the battle for survival rages on.",
    2400: "Every day, Uranek confronts the chaos within, striving to reclaim what was lost...",
    2600: "He tirelessly works to stabilize the reactor, seeking to restore balance...",
    2700: "...",
    2800: "...",
    2900: "...",
    3000: "Will you join him in this fight for redemption?"
}


def intro(screen, font):
    music.play_intro()
    global running
    global t
    while running:
        (SCREEN_WIDTH, SCREEN_HEIGHT) = screen.get_size()
        background_ = pygame.transform.scale(
            # we don't need performance here =)
            background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(background_, (0, 0))
        t += 1
        if t > 5:
            txt = font.render("press space to skip", True, (50, 50, 50))
            screen.blit(txt, (SCREEN_WIDTH - txt.get_width(),
                        SCREEN_HEIGHT - txt.get_height()))
        i = 0
        for tt in times_text:
            if t > tt * 5:
                txt = font.render(times_text[tt], True, (255, 255, 255))
                screen.blit(txt, (5, txt.get_height() * i + 5))
            i += 1
        if t > 40000:
            running = False
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
        pygame.display.update()
    music.stop()
