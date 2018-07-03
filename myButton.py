import pygame
pygame.init()
small = pygame.font.Font("./Fonts/Little Conquest.ttf", 15)
black = (0, 0, 0)


class PGButton:
    def __init__(self, x, y, w, h, name, valuet):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, w, h)
        self.value = valuet
        self.text = small.render(name, False, black)
        self.b = False
        
    def display(self, screen):
        #Could have a value to say which screen to draw to
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            col = (210, 210, 210)
        else:
            col = (240, 240, 240)
        pygame.draw.rect(screen, col, self.rect, 0)
        pygame.draw.rect(screen, black, self.rect, 1)
        screen.blit(self.text, (self.x + 3, self.y + 3))

    def pressed(self, event):
        self.b = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.b = True
        return self.b

    def val(self):
        return self.value


class PGSlider:
    def __init__(self, xt, yt, lowt, hight, namet, idt):
        self.x = xt
        self.y = yt
        self.px = xt
        self.low = lowt
        self.high = hight
        self.end = xt + 100
        self.offset = 0
        self.tb = False
        self.name = namet
        self.id = idt
        self.sliding = False
        self.mouseX, self.mouseY = 0, 0
        
    def display(self, screen):
        pygame.draw.line(screen, black, (self.x, self.y), (self.end, self.y), 1)
        self.mouseX, self.mouseY = pygame.mouse.get_pos()
        if self.offset < 0:
            self.offset = 0
        elif self.offset > 100:
            self.offset = 100
        if self.contains(self.mouseX, self.mouseY) or self.sliding:
            col = (210, 210, 210)
        else:
            col = (240, 240, 240)
        pygame.draw.rect(screen, col, (self.x + self.offset - 5, self.y - 10, 10, 20), 0)
        pygame.draw.rect(screen, black, (self.x + self.offset - 5, self.y - 10, 10, 20), 1)
        screen.blit(small.render(self.name + ": " + str(self.offset) + "%", False, black), (self.x, self.y - 30))
        
    def contains(self, x, y):
        return True if x < self.x + self.offset + 5 and x > self.x + self.offset - 5 and y < self.y + 10 and y > y - 10 else False

    def containsAll(self, x, y):
        return True if x < self.end + 5 and x > self.x - 5 and y < self.y + 10 and y > self.y -10 else False

    def slide(self):
        self.offset = self.mouseX - self.x
    
    def update(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.sliding = False
        if event.type == pygame.ACTIVEEVENT:
            self.sliding = False
        if self.containsAll(self.mouseX, self.mouseY):

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sliding = True
        if self.sliding:
            self.slide()
