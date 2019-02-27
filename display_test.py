import sys, pygame
from fake_strip import FakeStrip
from text_display import TextDisplayer, init_char_matrix

import time

PIX_WH=5
NUM_STRIPS=8
NUM_PIXELS=100
CHAR_WIDTH=12
init_char_matrix(CHAR_WIDTH)

size = width, height = NUM_PIXELS * PIX_WH, NUM_STRIPS * PIX_WH

pygame.init()
screen = pygame.display.set_mode(size)
screen.fill((0,0,0))

pixels_strips = [FakeStrip(screen, i, NUM_PIXELS, PIX_WH) for i in range(NUM_PIXELS)]

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
text_disp = TextDisplayer(pixels_strips, 0)
text = "abc abc abc abc abc abc abc abc "
texts = [
    "Souvent, pour s'amuser, les hommes d'equipage ",
    "Prennent des albatros, vastes oiseaux des mers, ",
    "Qui suivent, indolents compagnons de voyage, ",
    "Le navire glissant sur les gouffres amers. ",
    "A peine les ont-ils deposes sur les planches, ",
    "Que ces rois de l'azur, maladroits et honteux, ",
    "Laissent piteusement leurs grandes ailes blanches ",
    "Comme des avirons traîner à côte d'eux. ",
    "Ce voyageur aile, comme il est gauche et veule ! ",
    "Lui, naguère si beau, qu'il est comique et laid ! ",
    "L'un agace son bec avec un brûle-gueule, ",
    "L'autre mime, en boitant, l'infirme qui volait ! ",
    "Le Poete est semblable au prince des nuees ",
    "Qui hante la tempête et se rit de l'archer ; ",
    "Exile sur le sol au milieu des huees, ",
    "Ses ailes de geant l'empêchent de marcher. "
]
texts_l = [[x for x in text] for text in texts]
texts_l_ = [[x for x in text] for text in ["abc abc abc ", "def def def "]]
text_l = [x for x in text]
text_offset = 0
texts_idx = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    text_end = text_disp.display_text(texts_l[texts_idx % len(texts_l)], texts_l[(texts_idx + 1) % len(texts_l)], text_offset)
    if text_end:
        print("Text1 fully read")
        texts_idx = (texts_idx + 1) % len(texts_l)
        text_offset = 1
    else:
        text_offset -= 1

    pygame.time.wait(1)
