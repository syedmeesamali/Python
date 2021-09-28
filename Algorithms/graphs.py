import pygame
import math
import time
from queue import PriorityQueue

WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* path finding algorithm")

red = (255, 0, 0)
green = (0, 255, 0)
green = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
purple = (128, 0, 128)
orange = (255, 165, 0)
grey = (128, 128, 128)
turq = (64, 224, 208)

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = white
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == red        #Square already visited

    def is_open(self):
        return self.color == green

    def is_barrier(self):
        return self.color == black
    
    def is_start(self):                 #Starting point for algorithm
        return self.color == orange
    
    def is_end(self):
        return self.color == purple
    
    def reset(self):                    #Reset all back to white
        self.color = white
    
    #Below are all to make the functions into particular categories
    def make_start(self):
        self.color = orange
    
    def make_closed(self):
        self.color = red        #Make it visited

    def make_open(self):
        self.color = green

    def make_barrier(self):
        self.color = black
    
    def make_end(self):
        self.color = turq
    
    def make_path(self):                    #Reset all back to white
        self.color == purple
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False

#Heuristic function for point p1 and point p2 using manhattan distance
def h(p1, p2):              
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)      #Distance function

#Make the logical grid
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid

#ACtually draw the grid on screen
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, grey, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, grey, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill(white)
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap
    return row, col

#Main function to draw the game and start the processing
def main(win, width):
    ROWS = 40
    grid = make_grid(ROWS, width)
    start = None
    end = None
    run = True
    started = False
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
            if pygame.mouse.get_pressed()[0]:           #left button pressed
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()
            
            elif pygame.mouse.get_pressed()[2]:         #right button pressed
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    pass

    pygame.quit()       #If cross is clicked

#Run the main function
main(WIN, WIDTH)
