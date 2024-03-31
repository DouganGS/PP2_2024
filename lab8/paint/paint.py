import pygame

"""
Key Q - lines of rectangles
Key C - lines of circles
key R, G, B - change color
Key E - eraser
E + Mouse3 - clear all shapes
"""

CIRCLE = 'circle'
RECTANGLE = 'rectangle'
ERASER = 'eraser'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = WHITE
    points = []
    drawing_shape = CIRCLE  
    shapes = [] 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mode = RED
                elif event.key == pygame.K_g:
                    mode = GREEN
                elif event.key == pygame.K_b:
                    mode = BLUE
                elif event.key == pygame.K_c:  #draw a circle
                    mode = WHITE
                    drawing_shape = CIRCLE
                elif event.key == pygame.K_q:  #draw a rectangle
                    mode = WHITE
                    drawing_shape = RECTANGLE
                elif event.key == pygame.K_e:  # eraser
                    mode = BLACK
                    drawing_shape = None
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and mode != BLACK: # grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # shrinks radius
                    radius = max(1, radius - 1)
                elif event.button == 1 and mode == BLACK:
                    eraseShapes(event.pos, shapes)
                    erasePoints(event.pos, points)
                elif event.button == 2 and mode == BLACK:
                    shapes.clear()
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points = points + [position]
                points = points[-256:]
        
        if drawing_shape:
            # saving the points 
            if pygame.mouse.get_pressed()[0]:
                if drawing_shape == CIRCLE:
                    center = pygame.mouse.get_pos()
                    shapes.append((CIRCLE, center, radius, mode, points[:])) 
                elif drawing_shape == RECTANGLE:
                    if len(points) >= 2:
                        start = points[-2]
                        end = points[-1]
                        shapes.append((RECTANGLE, start, end, mode, points[:]))
        
        screen.fill(BLACK)
        
        for shape in shapes:
            if shape[0] == CIRCLE:
                drawCircle(screen, shape[1], shape[2], shape[3])
            elif shape[0] == RECTANGLE:
                drawRectangle(screen, shape[1], shape[2], shape[3])
        
        pygame.display.flip()
        
        clock.tick(60)

def eraseShapes(pos, shapes):
    for shape in shapes:
        if shape[0] == CIRCLE:
            if pointInCircle(pos, shape[1], shape[2]):
                shapes.remove(shape)
        elif shape[0] == RECTANGLE:
            if pointInRectangle(pos, shape[1], shape[2]):
                shapes.remove(shape)

def erasePoints(pos, points):
    for point in points[:]:  
        if pointDistance(pos, point) < 15:  
            points.remove(point)

def drawCircle(screen, center, radius, color_mode):
    pygame.draw.circle(screen, color_mode, center, radius)

def drawRectangle(screen, start, end, color_mode):
    x1 = min(start[0], end[0])
    y1 = min(start[1], end[1])
    width = abs(start[0] - end[0])
    height = abs(start[1] - end[1])
    pygame.draw.rect(screen, color_mode, (x1, y1, width, height))

def pointDistance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def pointInCircle(point, center, radius):
    return pointDistance(point, center) <= radius

def pointInRectangle(point, start, end):
    x, y = point
    x1, y1 = start
    x2, y2 = end
    return x1 <= x <= x2 and y1 <= y <= y2

main()
    