import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Mixed Betting Game")
icon = pygame.image.load("dice1.png")
pygame.display.set_icon(icon)
background = pygame.image.load("background.png")
dice = [pygame.image.load("dice1.png")]
dices = [pygame.image.load("dice1.png"), pygame.image.load("dice2.png"), pygame.image.load("dice3.png"),
         pygame.image.load("dice4.png"), pygame.image.load("dice5.png"), pygame.image.load("dice6.png")]
x = 0
i = 0
clear = 0
share = 0
deck = [pygame.image.load("2.png"), pygame.image.load("3.png"), pygame.image.load("4.png"), pygame.image.load("5.png"),
        pygame.image.load("6.png"), pygame.image.load("7.png"), pygame.image.load("8.png"), pygame.image.load("9.png"),
        pygame.image.load("10.png"), pygame.image.load("j.png"), pygame.image.load("q.png"), pygame.image.load("k.png"),
        pygame.image.load("ace.png")]
my_deck = []
finally_returns = set()
comp_cards = set()
comp_deck = []
player_wins1 = 0
comp_wins1 = 0
sign = 0
mouse_position = ()
comp_clear_values = []
my_clear_values = []
sign1 = 0
potentials = []
my_new_deck = []
comp_new_deck = []
list_comp_cards = []
mind = 0
mind1 = 0
mind2 = 0
mind3 = 0
mind4 = 0
final_choice = -1
final_choices = [-1]
mind5 = 0
sign2 = 0
# Score
score_value = 0
comp_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
score_value2 = 0
comp_value2 = 0

def show_score(x, y):
    my_score = font.render("My Score : " + str(score_value), True, (255, 255, 255))
    comp_score = font.render("Comp Score : " + str(comp_value), True, (255, 255, 255))
    screen.blit(my_score, (x, y))
    screen.blit(comp_score, (x, y + 40))


def show_score2(x, y):
    my_score = font.render("My Score : " + str(score_value2), True, (255, 255, 255))
    comp_score = font.render("Comp Score : " + str(comp_value2), True, (255, 255, 255))
    screen.blit(my_score, (x, y))
    screen.blit(comp_score, (x, y + 40))


def comp_values():
    for i in range(5):
        value1 = deck.index(comp_deck[i])
        clear_value1 = value1 + 2
        comp_clear_values.append(clear_value1)


def player_values():
    for i in range(len(my_deck)):
        value2 = deck.index(my_deck[i])
        clear_value2 = value2 + 2
        my_clear_values.append(clear_value2)


def mind_pc():
    comp_values()
    player_values()
    global final_choice

    while final_choice in final_choices:
        if card_value == 4:
            for i in range(5):
                if my_clear_values[card_value] < comp_clear_values[i]:
                    potentials.append(i)
                    final_choice = min(potentials)
        else:
            for i in range(card_value + 2):
                if my_clear_values[card_value] < comp_clear_values[i]:
                    potentials.append(i)
                    final_choice = min(potentials)
            if len(potentials) == 0:
                if card_value == 0:
                    final_choice = random.randint(0, 2)
                else:
                    final_choice = random.randint(0, card_value)
        if final_choice in final_choices:
            final_choice = random.randint(0, 4)
    final_choices.append(final_choice)

    my_new_deck.append(my_deck.pop(card_value))
    comp_new_deck.append(comp_deck.pop(final_choice))


running = True

while running:
    my_deck.clear()
    comp_deck.clear()
    comp_clear_values.clear()
    my_clear_values.clear()
    player_wins1 = 0
    comp_wins1 = 0
    q = -1
    k = -1
    g = -1
    screen.blit(background, (0, 0))
    if len(dice) > 0:
        screen.blit(dice[0], (400 - 32, 800 - 64))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if len(dice) > 0:
            dice.pop()
        number = random.randint(0, 5)
        screen.blit(dices[number], (400 - 32, 400))
        x = 1
        finally_option = dices[number]
        comp_number = random.randint(0, 5)

    if x == 1 and not keys[pygame.K_SPACE]:
        screen.blit(finally_option, (400 - 32, 400))
        font = pygame.font.Font('freesansbold.ttf', 32)
        computer = font.render("Computer's turn", True, (255, 255, 255))
        screen.blit(computer, (500, 50))
        while i < 100:
            pygame.time.delay(10)
            i += 1
        score_value = number + 1
        screen.blit(dices[comp_number], (620 - 32, 400))
        comp_value = comp_number + 1

    if comp_value > score_value:
        show_score(50, 50)
        game_finished = font.render("Comp Wins", True, (255, 255, 255))
        comp_wins1 = 1
        screen.blit(game_finished, (450, 100))
    if score_value != 0 and score_value >= comp_value:
        show_score(50, 50)
        player_wins = font.render("You win", True, (255, 255, 255))
        player_wins1 = 1
        screen.blit(player_wins, (450, 100))
    if keys[pygame.K_KP_ENTER] and x == 1:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        clear = 1
    if clear == 1 and not keys[pygame.K_KP_ENTER]:
        screen.blit(background, (0, 0))
        if comp_wins1 == 1 and sign == 0:
            text = font.render("You should select the first 'obvious' card", True, (255, 255, 255))
            screen.blit(text, (80, 400))
    if comp_wins1 == 1:
        if keys[pygame.K_s] and x == 1 and clear == 1:
            share = 1
        if share == 1 and not keys[pygame.K_s]:
            while len(finally_returns) < 5:
                c1 = random.randint(0, 13)
                c2 = random.randint(0, 13)
                c3 = random.randint(0, 13)
                c4 = random.randint(0, 13)
                c5 = random.randint(0, 13)
                finally_returns = {c1, c2, c3, c4, c5}
            list_finally = list(finally_returns)
            if len(my_deck) == 0:
                for elem in list_finally:
                    my_deck.append(deck[elem])
            for card in my_deck:
                k += 1
                screen.blit(card, (50 + 140 * k, 600))
            if sign == 1:
                for card in my_new_deck:
                    screen.blit(card, (50 + (my_new_deck.index(card)) * 128, 350))

            while len(comp_cards) < 5:
                d1 = random.randint(0, 12)
                d2 = random.randint(0, 12)
                d3 = random.randint(0, 12)
                d4 = random.randint(0, 12)
                d5 = random.randint(0, 12)
                comp_cards = {d1, d2, d3, d4, d5}
                if len(finally_returns | comp_cards) < 10:
                    comp_cards.clear()
            list_comp_cards = list(comp_cards)
            for elem in list_comp_cards:
                comp_deck.append(deck[elem])
            if sign == 1:
                for card in comp_new_deck:
                    screen.blit(card, (50 + comp_new_deck.index(card) * 128, 200))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_position = pygame.mouse.get_pos()
                sign = 1
        if sign == 1 and 50 <= mouse_position[0] <= 178 and 600 <= mouse_position[1] <= 752:
            card_value = 0
            show_score2(50, 50)
            while mind == 0:
                mind_pc()
                mind = 1
                if comp_clear_values[final_choice] > my_clear_values[card_value]:
                    comp_value2 += 1
                else:
                    score_value2 += 1

        if sign == 1 and 190 <= mouse_position[0] <= 190 + 128 and 600 <= mouse_position[1] <= 752:
            card_value = 1
            show_score2(50, 50)
            while mind1 == 0:
                mind_pc()
                mind1 = 1
                if comp_clear_values[final_choice] > my_clear_values[card_value]:
                    comp_value2 += 1
                else:
                    score_value2 += 1

        if sign == 1 and 330 <= mouse_position[0] <= 330 + 128 and 600 <= mouse_position[1] <= 752:
            card_value = 2
            show_score2(50, 50)
            while mind2 == 0:
                mind_pc()
                mind2 = 1
                if comp_clear_values[final_choice] > my_clear_values[card_value]:
                    comp_value2 += 1
                else:
                    score_value2 += 1

        if sign == 1 and 470 <= mouse_position[0] <= 470 + 128 and 600 <= mouse_position[1] <= 752:
            card_value = 3
            show_score2(50, 50)
            while mind3 == 0:
                mind_pc()
                mind3 = 1
                if comp_clear_values[final_choice] > my_clear_values[card_value]:
                    comp_value2 += 1
                else:
                    score_value2 += 1

        if sign == 1 and 610 <= mouse_position[0] <= 610 + 128 and 600 <= mouse_position[1] <= 752:
            card_value = 4
            show_score2(50, 50)
            while mind4 == 0:
                mind_pc()
                mind4 = 1
                if comp_clear_values[final_choice] > my_clear_values[card_value]:
                    comp_value2 += 1
                else:
                    score_value2 += 1
    if player_wins1 == 1:
        sign1 = 1
        if keys[pygame.K_KP_ENTER] and x == 1:
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            clear = 1
        if clear == 1 and not keys[pygame.K_KP_ENTER]:
            screen.blit(background, (0, 0))
        if keys[pygame.K_s] and x == 1 and clear == 1:
            share = 1
        if share == 1 and not keys[pygame.K_s]:
            while len(finally_returns) < 5:
                c1 = random.randint(0, 12)
                c2 = random.randint(0, 12)
                c3 = random.randint(0, 12)
                c4 = random.randint(0, 12)
                c5 = random.randint(0, 12)
                finally_returns = {c1, c2, c3, c4, c5}
            list_finally = list(finally_returns)
            if len(my_deck) == 0:
                for elem in list_finally:
                    my_deck.append(deck[elem])

            for card in my_deck:
                q += 1
                screen.blit(card, (50 + 140 * q, 600))
            if sign1 == 1:
                for card in my_new_deck:
                    screen.blit(card, (50 + (my_new_deck.index(card)) * 128, 350))

            while len(comp_cards) < 5:
                d1 = random.randint(0, 12)
                d2 = random.randint(0, 12)
                d3 = random.randint(0, 12)
                d4 = random.randint(0, 12)
                d5 = random.randint(0, 12)
                comp_cards = {d1, d2, d3, d4, d5}
                if len(finally_returns | comp_cards) < 10:
                    comp_cards.clear()
            list_comp_cards = list(comp_cards)
            for elem in list_comp_cards:
                comp_deck.append(deck[elem])
            if sign1 == 1:
                for card in comp_new_deck:
                    screen.blit(card, (50 + comp_new_deck.index(card) * 128, 200))
            while mind5 == 0:
                final_choice = random.randint(0, 4)
                comp_new_deck.append(comp_deck.pop(final_choice))
                final_choices.append(final_choice)
                comp_first = 1
                mind5 = 1
            if comp_first == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_position = pygame.mouse.get_pos()
                        comp_first += 1
                        sign2 = 1

                if sign2 == 1 and 50 <= mouse_position[0] <= 178 and 600 <= mouse_position[1] <= 752:
                    card_value = 0
                    show_score2(50, 50)
                    while mind == 0:
                        comp_values()
                        player_values()
                        mind = 1
                        my_new_deck.append(my_deck.pop(card_value))
                        if comp_clear_values[final_choice] > my_clear_values[card_value]:
                            comp_value2 += 1
                        else:
                            score_value2 += 1

                if sign2 == 1 and 190 <= mouse_position[0] <= 190 + 128 and 600 <= mouse_position[1] <= 752:
                    card_value = 1
                    show_score2(50, 50)
                    while mind1 == 0:
                        mind1 = 1
                        comp_values()
                        player_values()
                        my_new_deck.append(my_deck.pop(card_value))
                        if comp_clear_values[final_choice] > my_clear_values[card_value]:
                            comp_value2 += 1
                        else:
                            score_value2 += 1

                if sign2 == 1 and 330 <= mouse_position[0] <= 330 + 128 and 600 <= mouse_position[1] <= 752:
                    card_value = 2
                    show_score2(50, 50)
                    while mind2 == 0:
                        mind2 = 1
                        comp_values()
                        player_values()
                        my_new_deck.append(my_deck.pop(card_value))
                        if comp_clear_values[final_choice] > my_clear_values[card_value]:
                            comp_value2 += 1
                        else:
                            score_value2 += 1

                if sign2 == 1 and 470 <= mouse_position[0] <= 470 + 128 and 600 <= mouse_position[1] <= 752:
                    card_value = 3
                    show_score2(50, 50)
                    while mind3 == 0:
                        mind3 = 1
                        comp_values()
                        player_values()
                        my_new_deck.append(my_deck.pop(card_value))
                        if comp_clear_values[final_choice] > my_clear_values[card_value]:
                            comp_value2 += 1
                        else:
                            score_value2 += 1

                if sign2 == 1 and 610 <= mouse_position[0] <= 610 + 128 and 600 <= mouse_position[1] <= 752:
                    card_value = 4
                    show_score2(50, 50)
                    while mind4 == 0:
                        comp_values()
                        player_values()
                        my_new_deck.append(my_deck.pop(card_value))
                        mind4 = 1
                        if comp_clear_values[final_choice] > my_clear_values[card_value]:
                            comp_value2 += 1
                        else:
                            score_value2 += 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_position = pygame.mouse.get_pos()

            if sign2 == 1 and 50 <= mouse_position[0] <= 178 and 600 <= mouse_position[1] <= 752:
                card_value = 0
                show_score2(50, 50)
                while mind == 0:
                    if comp_first > 1:
                        mind_pc()
                    mind = 1
                    if comp_clear_values[final_choice] > my_clear_values[card_value]:
                        comp_value2 += 1
                    else:
                        score_value2 += 1

            if sign2 == 1 and 190 <= mouse_position[0] <= 190 + 128 and 600 <= mouse_position[1] <= 752:
                card_value = 1
                show_score2(50, 50)
                while mind1 == 0:
                    mind_pc()
                    mind1 = 1
                    if comp_clear_values[final_choice] > my_clear_values[card_value]:
                        comp_value2 += 1
                    else:
                        score_value2 += 1

            if sign2 == 1 and 330 <= mouse_position[0] <= 330 + 128 and 600 <= mouse_position[1] <= 752:
                card_value = 2
                show_score2(50, 50)
                while mind2 == 0:
                    mind_pc()
                    mind2 = 1
                    if comp_clear_values[final_choice] > my_clear_values[card_value]:
                        comp_value2 += 1
                    else:
                        score_value2 += 1

            if sign2 == 1 and 470 <= mouse_position[0] <= 470 + 128 and 600 <= mouse_position[1] <= 752:
                card_value = 3
                show_score2(50, 50)
                while mind3 == 0:
                    mind_pc()
                    mind3 = 1
                    if comp_clear_values[final_choice] > my_clear_values[card_value]:
                        comp_value2 += 1
                    else:
                        score_value2 += 1

            if sign2 == 1 and 610 <= mouse_position[0] <= 610 + 128 and 600 <= mouse_position[1] <= 752:
                card_value = 4
                show_score2(50, 50)
                while mind4 == 0:
                    mind_pc()
                    mind4 = 1
                    if comp_clear_values[final_choice] > my_clear_values[card_value]:
                        comp_value2 += 1
                    else:
                        score_value2 += 1

    if score_value2 == 3:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        winning_text = font.render("YOU WIN", True, (255, 255, 255))
        screen.blit(winning_text, (300, 400))

    elif comp_value2 == 3:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        winning_text = font.render("YOU LOST", True, (255, 255, 255))
        screen.blit(winning_text, (300, 400))
    pygame.display.update()
