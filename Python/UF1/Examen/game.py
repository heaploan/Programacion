import random
import time
import pygame
table = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
]
formas = {
    "square": [
        ["#", "#"],
        ["#", "#"]
    ],
    "line": [
        [["#"],
         ["#"],
         ["#"],
         ["#"]],
        ["#", "#", "#", "#"]
    ],
    "lr": [
        [["#", "#", "#"],
         ["#", " ", " "]],
        [["#", "#"],
         [" ", "#"],
         [" ", "#"]],
        [[" ", " ", "#"],
         ["#", "#", "#"]],
        [["#", " "],
         ["#", " "],
         ["#", "#"]]
    ],
    "ll": [
        [["#", " ", " "],
         ["#", "#", "#"]],
        [["#", "#"],
         ["#", " "],
         ["#", " "]],
        [["#", "#", "#"],
         [" ", " ", "#"]],
        [[" ", "#"],
         [" ", "#"],
         ["#", "#"]]
    ],
    "t": [
        [[" ", "#", " "],
         ["#", "#", "#"]],
        [["#", " "],
         ["#", "#"],
         ["#", " "]],
        [["#", "#", "#"],
         [" ", "#", " "]],
        [[" ", "#"],
         ["#", "#"],
         [" ", "#"]]
    ],
    "zr": [
        [[" ", "#", "#"],
         ["#", "#", " "]],
        [["#", " "],
         ["#", "#"],
         [" ", "#"]]
    ],
    "zl": [
        [["#", "#", " "],
         [" ", "#", "#"]],
        [[" ", "#"],
         ["#", "#"],
         ["#", " "]]
    ]
}
pygame.init()
def print_table():
    for row in range(len(table)):
        for col in range(len(table[row])):
            x = col * 20
            y = row * 20
            pygame.draw.rect(screen, "black", pygame.Rect(x, y, 20, 20))
            pygame.draw.rect(screen, "white", pygame.Rect(x, y, 20, 20), 1)

def print_piece(piece, x, y):
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if piece[row][col] == "#":
                pygame.draw.rect(screen, "red", pygame.Rect(x + col * 20, y + row * 20, 20, 20))
                pygame.draw.rect(screen, "white", pygame.Rect(x + col * 20, y + row * 20, 20, 20), 1)

def check_collision(piece, x, y):
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if piece[row][col] == "#":
                if x + col < 0 or x + col > 9:
                    return True
                if y + row > 15:
                    return True
                if table[y + row][x + col] != " ":
                    return True
    return False


def move_piece(rotation, x, y):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if rotation == len(formas[form]) - 1:
            rotation = 0
        else:
            rotation += 1
    if keys[pygame.K_DOWN]:
        y += 20
    if keys[pygame.K_LEFT]:
        x -= 20
    if keys[pygame.K_RIGHT]:
        x += 20
    return rotation, x, y


screen = pygame.display.set_mode((200, 320))
running = True
x = random.randint(3, 6) * 20
y = 0
form = random.choice(list(formas.keys()))
rotation = random.randint(0, len(formas[form]) - 1)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    print_table()
    rotation, x, y = move_piece(rotation, x, y)
    keys = pygame.key.get_pressed()
    print_piece(formas[form][rotation], x, y)
    pygame.display.flip()
    time.sleep(0.1)
pygame.quit()
