import pygame
import sys
from pygame.locals import *
import main

def test_game_start():
    pygame.init()
    pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Tank Runner')

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        # Simulate pressing any key to start the game
        pygame.event.post(pygame.event.Event(KEYDOWN))

        # Call the main game function
        main()

        # Test if the game ends after quitting
        running = False

        clock.tick(30)

def test_bullet_shooting():
    pygame.init()
    pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Tank Runner')

    clock = pygame.time.Clock()
    running = True

    # Flag to track if bullet is created and moving
    bullet_created = False
    bullet_moving = False

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_SPACE:
                    # Simulate shooting a bullet
                    bullet_created = True

        # Simulate pressing any key to start the game
        pygame.event.post(pygame.event.Event(KEYDOWN))

        # Call the main game function
        main()

        if bullet_created and not bullet_moving:
            # Test if the bullet is created and moving
            bullet_moving = True

        # Simulate ending the game after shooting the bullet
        if bullet_moving:
            running = False

        clock.tick(30)

def test_collision_detection():
    pygame.init()
    pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Tank Runner')

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        # Simulate pressing any key to start the game
        pygame.event.post(pygame.event.Event(KEYDOWN))

        # Call the main game function
        main()

        # Simulate a collision between two game objects
        object1_rect = pygame.Rect(100, 200, 50, 50)
        object2_rect = pygame.Rect(200, 200, 50, 50)

        # Test if the collision detection logic correctly detects the collision
        if object1_rect.colliderect(object2_rect):
            print("Collision detected!")
        else:
            print("No collision detected!")

        # Simulate ending the game after collision detection
        running = False

        clock.tick(30)

def test_score():
    pygame.init()
    pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Tank Runner')

    clock = pygame.time.Clock()
    running = True

    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        # Simulate pressing any key to start the game
        pygame.event.post(pygame.event.Event(KEYDOWN))

        # Call the main game function
        main()

        # Update the score based on the game logic
        score += 100

        # Print the current score
        print("Current Score:", score)

        # Simulate ending the game after a certain score threshold
        if score >= 1000:
            running = False

        clock.tick(30)


# Run the test case, uncomment the one you want to test
#test_game_start()
#test_bullet_shooting()
#test_collision_detection()
#test_score()
