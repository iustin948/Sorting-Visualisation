import pygame
from random import randint
pygame.init()
WIDTH = 750
WHITE = (255, 255, 255)
RED =   (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
len = 750
SIZE = 750 // len
screen = pygame.display.set_mode((WIDTH, WIDTH))
running = True

#pygame.draw.line(screen, WHITE, (1,1), (20, 20), 1)

def Draw(index, value):
    pygame.draw.line(screen, BLACK, (index, 750), (index, 1), SIZE)
    pygame.draw.line(screen, WHITE, (index, 750), (index, 750 - value), SIZE)

def Make_array():
    Array = []
    for i in range (len):
            Array.append(i)
    return Array

Array = Make_array()

def Shuffle():
    for i in range (2000):
        a = randint(0,len-1)
        b = randint(0,len-1)
        Array[a], Array[b] = Array[b] , Array[a]


def BubbleSort():
    print(1)
    for i in range(len):
        for j in range (len-1):

            if(Array[j] > Array[j+1] ):
                Array[j],  Array[j+1] = Array[j+1] , Array[j]
                Draw(j+1, Array[j+1])
                Draw(j, Array[j])
        pygame.display.update()

def InsertionSort():
    for i in range(0,len):
        x = Array[i]
        j = i - 1
        while(j >= 0 and Array[j] > x):
            Array[j+1]=Array[j]
            Draw(j + 1, Array[j + 1])
            j = j - 1

        Array[j+1] = x
        Draw(j + 1, Array[j + 1])
        pygame.display.update()



def Reset():
    Shuffle()
    for i in range(len):
        Draw(i, Array[i])
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE):
                InsertionSort()
            if (event.key == pygame.K_KP_ENTER):
                BubbleSort()
            if (event.key == pygame.K_r):
                Reset()
            if (event.key == pygame.K_m):
                print(1)
                MergeSort(0,len)
        pygame.display.update()