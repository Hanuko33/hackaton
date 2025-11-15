import pygame
from pygame.locals import QUIT, KEYDOWN, MOUSEBUTTONDOWN
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
    1600: "Yet, amidst the corruption, a spark of hope ignited...",
    1700: "One of them dared to resist the encroaching darkness.",
    1800: "...",
    1900: 'This brave soul was known as "Uranek," the beacon of defiance...',
    2100: "Though he stood alone, he carried the weight of a world's fate...",
    2300: "Now, the battle for survival rages on.",
    2500: "Every day, Uranek confronts the chaos, striving to reclaim what was lost...",
    2700: "He tirelessly works to stabilize the reactor, seeking to restore balance...",
    2800: "...",
    2900: "...",
    3000: "...",
    3100: "Will you join him in this fight for redemption?"
}

times_text_pl = {
    100: "W łagodnej krainie Uranex, harmonia wspaniale kwitła wśród jej mieszkańców.",
    300: "Żyli w błogiej nieświadomości nadciągających cieni, które zagrażały ich egzystencji.",
    600: "Lecz nagle, bez ostrzeżenia, katastrofa uderzyła w samą istotę ich świata.",
    800: "Kryzys uwolnił chaos, rozdzierając ich spokój na strzępy.",
    1000: "...",
    1200: "Niegdyś tętniące życiem istoty zostały wrzucone do reaktora",
    1300: "zatrutego ciemną energią, która zniekształcała ich esencję.",
    1600: "Jednak w obliczu zepsucia, iskra nadziei zapłonęła...",
    1700: "Jeden z nich odważył się stanąć przeciw narastającej ciemności.",
    1800: "...",
    1900: 'Ten odważny duch był znany jako "Uranek", latarnia oporu...',
    2100: "Choć stał sam, dźwigał ciężar losu całego świata...",
    2300: "A teraz walka o przetrwanie trwa w nieustannym zrywie.",
    2500: "Każdego dnia Uranek stawia czoła chaosowi, usiłując odzyskać to, co utracone...",
    2700: "Niezłomnie pracuje nad stabilizacją reaktora, pragnąc przywrócić równowagę...",
    2800: "...",
    2900: "...",
    3000: "...",
    3100: "Czy dołączysz do niego w tej bohaterskiej walce o odkupienie?"
}


clock = pygame.time.Clock()


def intro(screen, font):
    music.play_intro()
    global running
    global t
    polish = False
    while running:
        (SCREEN_WIDTH, SCREEN_HEIGHT) = screen.get_size()
        background_ = pygame.transform.scale(
            # we don't need performance here =)
            background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(background_, (0, 0))
        t += clock.tick(120) / 15
        if t > 5:
            txt = font.render(
                "press space or any mouse button to skip", True, (50, 50, 50))
            screen.blit(txt, (SCREEN_WIDTH - txt.get_width(),
                        SCREEN_HEIGHT - txt.get_height()))
            txt = font.render(
                "press p for polish version", True, (50, 50, 50))
            screen.blit(txt, (SCREEN_WIDTH - txt.get_width(),
                        SCREEN_HEIGHT - txt.get_height() * 2))
        i = 0
        operating = times_text_pl if polish else times_text
        for tt in operating:
            if t > tt:
                txt = font.render(operating[tt], True, (255, 255, 255))
                screen.blit(txt, (5, txt.get_height() * i + 5))
            i += 1
        if t > 4000:
            running = False
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                if event.key == pygame.K_p:
                    polish ^= 1
                    polish = bool(polish)
            if event.type == MOUSEBUTTONDOWN:
                running = False
        pygame.display.update()
    music.stop()
