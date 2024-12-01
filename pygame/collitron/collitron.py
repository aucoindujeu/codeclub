import random

WIDTH = 800
HEIGHT = 800

BALLES = []
RAYON = 10
MASSE = 1
GRAVITE = 9.81
VITESSE_INITIALE = 100
FAUX_REBOND = 0.1


# On crée un bon paquet de balles
while len(BALLES) < 1000:
    BALLES.append(
        [
            random.randint(0, WIDTH),  # 0: position x
            random.randint(0, HEIGHT),  # 1: position y
            random.random() * VITESSE_INITIALE * 2 - VITESSE_INITIALE,  # 2: vitesse x
            random.random() * VITESSE_INITIALE * 2 - VITESSE_INITIALE,  # 3: vitesse y
            (  # 4: couleur
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            ),
        ]
    )


def draw():
    # On affiche toute les balles
    screen.fill((255, 255, 255))
    for ball in BALLES:
        draw_ball(ball)


def draw_ball(ball):
    # Chaque balle est un cercle
    screen.draw.filled_circle((ball[0], ball[1]), RAYON, ball[4])


def update(dt):
    for ball in BALLES:
        # On met à jour chaque balle une par une
        update_ball(ball, dt)


def update_ball(ball, dt):
    # Rebond bord de gauche
    if ball[0] < RAYON and ball[2] < 0:
        ball[0] = RAYON
        ball[2] *= -1 * (1 + random.random() * FAUX_REBOND * 2 - FAUX_REBOND)

    # Rebond bord de droite
    if ball[0] > WIDTH - RAYON and ball[2] > 0:
        ball[0] = WIDTH - RAYON
        ball[2] *= -1 * (1 + random.random() * FAUX_REBOND * 2 - FAUX_REBOND)

    # Rebond bord du haut
    if ball[1] < RAYON and ball[3] < 3:
        ball[1] = RAYON
        ball[3] *= -1 * (1 + random.random() * FAUX_REBOND * 2 - FAUX_REBOND)

    # Rebond bord du bas
    if ball[1] > HEIGHT - RAYON and ball[3] > 0:
        ball[1] = HEIGHT - RAYON
        ball[3] *= -1 * (1 + random.random() * FAUX_REBOND * 2 - FAUX_REBOND)

    # Déplacement
    ball[0] += ball[2] * dt
    ball[1] += ball[3] * dt
    ball[3] += GRAVITE * MASSE
