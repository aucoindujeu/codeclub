#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import pgzero
import math
import random

# Constantes - taille de la fenêtre
WIDTH = 800
HEIGHT = 600

# on va avoir besoin de calculer la distance euclidienne
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


class Boid():

    # Variables de classe : ces valeurs seronts partagées 
    # par toutes les instances de la classe
    n_boids = 80 # nombre total de boids
    w_limit = 40 # distance au bord de la fenêtre
    v_range = 60 # champ visuel / rayon zone d’attraction des boids
    min_distance = 20 # rayon de la zone de répulsion des boids
    max_speed = 3 # vitesse maximum d’un boid

    # pondération des différentes forces pour l’update des vitesses 
    REPULSION = .3
    ALIGNMENT = 0.001
    COHESION = 0.00001 
    CENTERING = 0.9

    boid_pix = pygame.image.load('images/boid.png')

    
    def __init__(self, position: tuple, speed: tuple) -> None:
        
        self.x, self.y = position
        self.vx, self.vy = speed

    
    def centering_force(self) -> tuple:
        # Cette force ne fait pas vraiment partie du modèle 
        # elle sert surtout à empêcher les boids de sortir
        # de la fenêtre et à les maintenir à l’intérieur

        if self.x < Boid.w_limit:
            turn_x = 1 
        elif self.x > WIDTH - Boid.w_limit:
            turn_x = -1
        else:
            turn_x = 0

        if self.y < Boid.w_limit:
            turn_y = 1
        elif self.y > HEIGHT - Boid.w_limit:
            turn_y = -1
        else:
            turn_y = 0

        return (turn_x, turn_y)

        
    def repulsion_force(self, lst_boids: list) -> tuple:

        repulsion_x= 0
        repulsion_y = 0
        for other_boid in lst_boids:
            if other_boid is not self and distance(self.x, self.y, other_boid.x, other_boid.y)  < Boid.min_distance:
                repulsion_x += (self.x - other_boid.x)  
                repulsion_y += (self.y - other_boid.y)

        if repulsion_x != 0:
            repulsion_x = repulsion_x/abs(repulsion_x)
        if repulsion_y != 0:
            repulsion_y = repulsion_y/abs(repulsion_y)

        return (repulsion_x, repulsion_y)


    def cohesion_force(self, lst_boids: list) -> tuple:

        cohesion_x = 0
        cohesion_y = 0
        count = 0
        for other_boid in lst_boids:
            dist = distance(self.x, self.y, other_boid.x, other_boid.y)
            if dist > Boid.min_distance and dist < Boid.v_range:
                count += 1
                cohesion_x += other_boid.x
                cohesion_y += other_boid.y

        if count > 0:
            cohesion_x = cohesion_x/count - self.x
            cohesion_y = cohesion_y/count - self.y

        return(cohesion_x, cohesion_y)


    def alignment_force(self,lst_boids: list) -> tuple:
        
        alignement_x = 0
        alignement_y = 0
        count = 0
        for other_boid in lst_boids:
            dist = distance(self.x, self.y, other_boid.x, other_boid.y)
            if dist > Boid.min_distance and dist < Boid.v_range:
                count += 1
                alignement_x += other_boid.vx
                alignement_y += other_boid.vy

        if count > 0:
            alignement_x = alignement_x/count - self.vx
            alignement_y = alignement_y/count - self.vy

        return(alignement_x, alignement_y)


    def speed_update(self, lst_boids: list) -> None:
        
        center = self.centering_force()
        repulsion = self.repulsion_force(lst_boids)
        cohesion = self.cohesion_force(lst_boids)
        alignment = self.alignment_force(lst_boids)

        self.vx = self.vx  \
                        + center[0] * Boid.CENTERING \
                        + repulsion[0] * Boid.REPULSION \
                        + cohesion[0] * Boid.COHESION \
                        + alignment[0] * Boid.ALIGNMENT

        self.vy = self.vy \
                    + center[1] * Boid.CENTERING \
                    + repulsion[1] * Boid.REPULSION \
                    + cohesion[1] * Boid.COHESION \
                    + alignment[1] + Boid.ALIGNMENT

        # speed limitation

        if abs(self.vx) > Boid.max_speed:
            self.vx = self.vx/abs(self.vx) * Boid.max_speed
        
        if abs(self.vy) > Boid.max_speed:
            self.vy = self.vy/abs(self.vy) * Boid.max_speed

    
    def position_update(self) -> None:
        
        self.x += self.vx
        self.y += self.vy


    def draw(self) -> None:
        
        rotated_boid = pygame.transform.rotate(self.boid_pix, -math.degrees(math.atan2(self.vy, self.vx)))
        screen.blit(rotated_boid, (self.x, self.y))


def init_demo():

    lst_boids = []
    for n in range(Boid.n_boids):
        lst_boids.append(Boid((random.randint(0,WIDTH), 
                                random.randint(0,HEIGHT)), 
                                (random.randint(-Boid.max_speed, Boid.max_speed), 
                                random.randint(-Boid.max_speed, Boid.max_speed))))
    
    return lst_boids

BOIDS = init_demo()

#
# UPDATE
#
def update():

    for b in BOIDS:
        b.speed_update(BOIDS)
        b.position_update()
        
#
# AFFICHAGE
#
def draw():
    
    screen.fill((0, 0, 0))
    for b in BOIDS:
        b.draw()
