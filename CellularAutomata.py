import pygame, random, re, colorsys #, numpy
from tkinter import *
#from Classes.ButtonClass import Button
pygame.init()

width, height = 250, 200
screen1 = pygame.display.set_mode((width, height))
pygame.display.set_caption('Cellular Automata')
clock = pygame.time.Clock()
crashed = False
quitted = False
first = True
customA = False
#fontPath = 'C:/Users/Moist/Desktop/CACA/Fonts/Little Conquest.ttf'
fontPath = 'F:/CACA/Fonts/Little Conquest.ttf'
fontPath2 = 'F:/CACA/Fonts/Nineteen Ninety Three.otf'
small = pygame.font.Font(fontPath, 15)
small2 = pygame.font.Font(fontPath2, 15)
medium = pygame.font.Font(fontPath, 40)
medium2 = pygame.font.Font(fontPath2, 40)
large = pygame.font.Font(fontPath, 60)
buttons = []
sliders = []

mode = "menu"
loggedIn = False

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
light_grey = (240, 240, 240)
light_grey_a = (240, 240, 240, 127)
grey = (127, 127, 127)

#python -m cProfile -o temp.dat F:\CACA\CellularAutomata.py

   ###    ##           ##      ####    ####   ######   ####
 ###  ##  ##          ####    ##   #  ##   #  ##      ##   #
##        ##         ##  ##    ###     ###    #####    ###
##        ##         ######       ##      ##  ##          ##
 ###  ##  ##        ##    ##  #   ##  #   ##  ##      #   ##
   ###    ########  ##    ##   ###     ###    ######   ###

######################## BUTTON ########################

class PGButton:
    def __init__(self, xt, yt, wt, ht, name, valuet):
        self.x = xt
        self.y = yt
        self.w = wt
        self.h = ht
        self.rect = pygame.Rect(xt, yt, wt, ht)
        self.value = valuet
        self.text = small.render(name, False, black)
        
    def display(self):
        #Could have a value to say which screen to draw to
        if self.rect.collidepoint((mouseX, mouseY)):
            col = (210, 210, 210)
        else:
            col = light_grey
            
        pygame.draw.rect(screen1, col, self.rect, 0)
            
        pygame.draw.line(screen1, black, (self.x, self.y), (self.x + self.w, self.y), 1)
        pygame.draw.line(screen1, black, (self.x + self.w, self.y), (self.x + self.w, self.y + self.h), 1)
        pygame.draw.line(screen1, black, (self.x + self.w, self.y + self.h), (self.x, self.y + self.h), 1)
        pygame.draw.line(screen1, black, (self.x, self.y + self.h), (self.x, self.y), 1)
        
        screen1.blit(self.text, (self.x + 3, self.y + 3))
    def pressed(self):
        self.b = False
        if self.rect.collidepoint((mouseX, mouseY)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.b = True
        return self.b

    def val(self):
        return self.value

######################## Log In Class ########################

class PGSlider:
    def __init__(self, xt, yt, lowt, hight, namet, idt):
        self.x = xt
        self.y = yt
        self.px = xt;
        self.low = lowt
        self.high = hight
        self.end = xt + 100
        self.offset = 0
        self.tb = False
        self.name = namet
        self.id = idt
        self.sliding = False
        
    def display(self):
        pygame.draw.line(screen1, black, (self.x, self.y), (self.end, self.y), 1)
        if self.offset < 0:
            self.offset = 0
        elif self.offset > 100:
            self.offset = 100
        if self.contains(mouseX, mouseY) or self.sliding:
            col = (210, 210, 210)
        else:
            col = light_grey
        pygame.draw.rect(screen1, col, (self.x + self.offset - 5, self.y - 10, 10, 20), 0)
        pygame.draw.line(screen1, black, (self.x + self.offset - 5, self.y - 10), (self.x + self.offset + 5, self.y - 10), 1)
        pygame.draw.line(screen1, black, (self.x + self.offset + 5, self.y - 10), (self.x + self.offset + 5, self.y + 10), 1)
        pygame.draw.line(screen1, black, (self.x + self.offset + 5, self.y + 10), (self.x + self.offset - 5, self.y + 10), 1)
        pygame.draw.line(screen1, black, (self.x + self.offset - 5, self.y + 10), (self.x + self.offset - 5, self.y - 10), 1)
        screen1.blit(small2.render(self.name + ": " + str(self.offset) + "%", False, black), (self.x, self.y - 30))
        
    def contains(self, x, y):
        return True if x < self.x + self.offset + 5 and x > self.x + self.offset - 5 and y < self.y + 10 and y > y - 10 else False

    def containsAll(self, x, y):
        return True if x < self.end + 5 and x > self.x - 5 and y < self.y + 10 and y > self.y -10 else False

    def slide(self):
        self.offset = mouseX - self.x
    
    def update(self):
        if event.type == pygame.MOUSEBUTTONUP:
            self.sliding = False
        if event.type == pygame.ACTIVEEVENT:
            self.sliding = False
        if self.containsAll(mouseX, mouseY):

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sliding = True
        if self.sliding:
            self.slide()

######################## Log In Class ########################

class login:
    def __init__(self, master, errorMsg):
        self.submitted = False
        
        self.master = master
        master.title("Log In")
        
        self.label = Label(master, text = "Enter log in details.")
        self.label.pack()

        if errorMsg != "":
            self.errorMsgLab = Label(master, text = errorMsg, fg = "red")
            self.errorMsgLab.pack()
            
        self.uNameB = Entry(master)
        self.labelU = Label(master, text = "Username:")
        self.labelU.pack()
        self.uNameB.pack(padx = 10)
        
        self.pWordB = Entry(master)
        self.labelP = Label(master, text = "Password:")
        self.labelP.pack()
        self.pWordB.pack(padx = 10)

        self.submitButt = Button(master, text = "Submit", command = self.submit)
        self.submitButt.pack(pady = 5)
    
    def submit(self):
        self.submitted = True
        info = [self.uNameB.get(), self.pWordB.get()]
        self.master.destroy()
        logIn(True, info)
        
    def getInfo(self):
        if self.submitted:
            return info

######################## Sign Up Class ########################

class signup:
    def __init__(self, master, errorMsg):
        self.submitted = False
        
        self.master = master
        master.title("Sign Up")
        self.label = Label(master, text = "Fill out this form to sign up.")
        self.label.pack()

        if errorMsg != "":
            self.errorMsgLab = Label(master, text = errorMsg, fg = "red")
            self.errorMsgLab.pack()
            
        self.uNameB = Entry(master)
        self.labelU = Label(master, text = "Username:")
        self.labelU.pack()
        self.uNameB.pack(padx = 10)
        
        self.pWordB = Entry(master)
        self.labelP = Label(master, text = "Password:")
        self.labelP.pack()
        self.pWordB.pack(padx = 10)

        self.submitButt = Button(master, text = "Submit", command = self.submit)
        self.submitButt.pack(pady = 5)
    
    def submit(self):
        self.submitted = True
        info = [self.uNameB.get(), self.pWordB.get()]
        self.master.destroy()
        signUp(True, info)
        
    def getInfo(self):
        if self.submitted:
            return info
        
######################## Name Class ########################

class nameC:
    def __init__(self, master):
        self.submitted = False
        
        self.master = master
        master.title("Name")
        
        self.label = Label(master, text = "Enter your CA's name: ")
        self.label.pack()
        
        self.nameB = Entry(master)
        self.labelN = Label(master, text = "Name:")
        self.labelN.pack()
        self.nameB.pack(padx = 10)

        self.submitButt = Button(master, text = "Submit", command = self.submit)
        self.submitButt.pack(pady = 5)
    
    def submit(self):
        self.submitted = True
        info = self.nameB.get()
        self.master.destroy()
        name(True, info)
        
    def getInfo(self):
        if self.submitted:
            return info

######################## Pixel Class ########################

class pixel():
    def __init__(self, idt, reprodt, strengtht, xt, yt, indext):
        self.x = xt
        self.y = yt
        self.px = self.x #% width
        self.py = self.y #% height
        self.index = indext
        #print(self.x, self.y, self.px, self.py)
        self.id = idt
        self.reprod = reprodt
        self.strength = strengtht
        self.first = True
        self.surr = [None, None, None, None, None, None, None, None]
        self.pos = int(self.y * width + self.x)

        r, g, b = colorsys.hsv_to_rgb(self.id / 255, 1, 1)
        self.col = (r * 255, g * 255, b * 255)
    
        
        changes_1d = [-1, 0, 1]
        changes_2d = [[i, j] for j in changes_1d for i in changes_1d]
        del changes_2d[5]
        self.movements = changes_2d
        
    def move(self, ret):
        if self.first:
            self.first = False
            self.surr = [allPixels[(self.x + self.movements[i][0]) % width][(self.y + self.movements[i][1]) % height] for i in range(8)]
        
            #self.surrounding() #as self.surrounding() is slow, i only want to call it once
        
        #surroundingBool = [False if i == None else True for i in self.surr]
        #print(surroundingBool)
        surroundingBool = [i is not None for i in self.surr]
        
        #for i in surroundingBool:
            #if i:
                #print("A")
        
        pixel = int(random.random() * 8)
        movement = self.movements[pixel]
        if not ret:
            if not surroundingBool[pixel]:
                self.x += movement[0]
                self.y += movement[1]
                
            self.x %= width
            self.y %= height
            self.pos = self.y * width + self.x
        else:
            if not surroundingBool[pixel]:
                return movement
            else:
                return False
            
        #r1 = random.random()
        #r2 = random.random()
        #r3 = random.random()
        
        #if r1 <= 0.333:
            #if r3 < 0.5 and not surroundingBool[4]: self.x += 1
            #elif not surroundingBool[3]: self.x -= 1
        #elif r1 <= 0.666:
            #if r3 < 0.5 and not surroundingBool[6]: self.y += 1
            #elif not surroundingBool[1]: self.y -= 1
        #else:
            #if r2 < 0.25 and not surroundingBool[7]:
                #self.x += 1
                #self.y += 1
            #elif r2 < 0.5 and not surroundingBool[2]:
                    #self.x += 1
                    #self.y -= 1
            #elif r2 < 0.75 and not surroundingBool[5]:
                    #self.x -= 1
                    #self.y += 1
            #elif not surroundingBool[0]:
                    #self.x -= 1
                    #self.y -= 1

    def reproduction(self):
        if random.random() <= self.reprod:
            where = self.move(True)
            if where != False:
                CAs[self.index].addPix(self.reprod, self.strength, self.x + where[0], self.y + where[1], True)

    def mutation(self):
        if random.random <= 0.1:
            pass #mutate
        
    #def surrounding(self):
        #for i in range(9):
            #x = i % 3 - 2
            #y = int((i % 3) / 3) - 1
            #if x == 0 and y == 0:
                #pass
            #else:
                #PAI = allPixels[(self.x + x) % width][(self.y + y) % height]
                #self.surr[(y * 3) + x] = (PAI)
        
        #for i in allPixels:
            #for j in i:
                #if j != None:
                    #print(j)

        
        #for i in range(8):
            #print(allPixels[(self.x + self.movements[i][0]) % width][(self.y + self.movements[i][1]) % height])
            #self.surr[i] = allPixels[(self.x + self.movements[i][0]) % width][(self.y + self.movements[i][1]) % height]
        #return self.surr
    
    def fight(self):
        pass
    
######################## Cellular Automata Class ########################

class CellularAuto:
    def __init__(self, idt, indext):
        global customA
        self.pixels = []
        self.id = idt
        self.index = indext
        if customA:
            self.addPix(CUSTOMREPROD, CUSTOMSTRENGTH, CUSTOMX, CUSTOMY, False)
            customA = False
        else:
            self.addPix(None, None, None, None, False)
            

    def display(self):
        for pix in self.pixels:
            screen2.set_at((pix.x, pix.y), pix.col)
        
    def update(self):
        for pix in self.pixels:
            pix.px = pix.x % width
            pix.py = pix.y % height
            pix.reproduction()
            pix.move(False)
            pix.fight()

    def addPix(self, reprod, strength, x, y, child):
        #global customA
        if child or customA:
            self.pixels.append(pixel(self.id, reprod, strength, x, y, self.index))
        else:
            x = random.randrange(width)
            y = random.randrange(height)
            reprod = random.random() * 0.2
            strength = random.random()
            self.pixels.append(pixel(self.id, reprod, strength, x, y, self.index))
            
######  ##     ##  ##    ##     ###    ##########  ##   #####   ##    ##   ####
##      ##     ##  ####  ##   ###  ##      ##      ##  ##   ##  ####  ##  ##   #
#####   ##     ##  ## ## ##  ##            ##      ##  ##   ##  ## ## ##   ###
##      ##     ##  ##  ####  ##            ##      ##  ##   ##  ##  ####      ##
##       ##   ##   ##   ###   ###  ##      ##      ##  ##   ##  ##   ###  #   ##
##        #####    ##    ##     ###        ##      ##   #####   ##    ##   ###

######################## LOG OUT ########################

def logout():
    global first, loggedIn, USERNAME
    loggedIn = False
    USERNAME = ""
    first = True
    
######################## MENU ########################

def menu():
    global first, screen1, buttons, sliders, mode
    screen1.fill((white));
    if first:
        first = False
        buttons = []
        sliders = []
        mode = "menu"
        but = ""
        if not loggedIn:
            width, height = 250, 230
            buttons.append(PGButton(10, 80, 40, 20, "Start", "start"))
            buttons.append(PGButton(10, 110, 135, 20, "Custom Automaton", "custom"))
            buttons.append(PGButton(10, 140, 55, 20, "Log In", "login"))
            buttons.append(PGButton(10, 170, 115, 20, "Create Account", "signup"))
            buttons.append(PGButton(10, 200, 45, 20, "Quit", "quit"))
        else:
            sw, sh = large.size(USERNAME)
            if sw > 250:
                w = sw + 10
            else:
                w = 250
            width, height = w, 280
            buttons.append(PGButton(10, 130, 40, 20, "Start", "start"))
            buttons.append(PGButton(10, 160, 135, 20, "Custom Automaton", "custom"))
            buttons.append(PGButton(10, 190, 110, 20, "Your Automata", "yours"))
            buttons.append(PGButton(10, 220, 60, 20, "Log Out", "logout"))
            buttons.append(PGButton(10, 250, 45, 20, "Quit", "quit"))

        screen1 = pygame.display.set_mode((width, height))
    else:
        but = doButtons()
    if not loggedIn:
        screen1.blit(large.render("Welcome", False, black), (10, 10))
    else:
        screen1.blit(large.render("Welcome", False, black), (10, 10))
        screen1.blit(large.render(USERNAME, False, black), (10, 60))
    if but != "":
        if but == "start":
            mode = "startmenu"
            first = True
            startMenu()
        elif but == "custom":
            mode = "custom"
            first = True
            custom()
        elif but == "login":
            mode = "login"
            first = True
            logIn(False, "")
        elif but == "signup":
            mode = "signup"
            first = True
            signUp(False, "")
        elif but == "quit":
            global quitted
            quitted = True
        elif but == "yours":
            mode = "YA"
            first = True
            YA()
        elif but == "logout":
            mode = "menu"
            logout()

######################## Quit Tkinter Function ########################

def quitTK():
    global mode, first, root
    root.destroy()
    first = True
    mode = "menu"
    menu()
    

######################## Log In Function ########################

def logIn(parsed, loginDetails):
    global first, loggedIn, running, root
    if not loggedIn:
        if first:
            first = False
            running = True
            root = Tk()
            if parsed == False and loginDetails != "":
                gui = login(root, loginDetails)
            else:
                gui = login(root, "")
                
            root.protocol("WM_DELETE_WINDOW", quitTK)
            root.mainloop()
        if parsed:
            if loginDetails[0] == "" or loginDetails[1] == "":
                first = True
                logIn(False, "Please fill both fields.")
            elif len(loginDetails[1]) < 8:
                first = True
                logIn(False, "Password is too short")
            else:
                users = eval(open("F:/FCACA/Users.txt").read()) #Opens the text file and evaluates it and users becomes a dictionary made from the items in the text file.
                uNameTrue = False
                for uName in users:
                    if not loggedIn:
                        if loginDetails[0] == uName and loginDetails[1] == users[uName]:
                            loggedIn = True
                            global USERNAME
                            USERNAME = uName
                            first = True
                        elif loginDetails[0] == uName:
                            uNameTrue == True
                        
                if not loggedIn:
                    if uNameTrue:
                        first = True
                        logIn(False, "Incorrect Password")
                    else:
                        first = True
                        logIn(False, "Incorrect Username")
    else:
        mode = "menu"
        menu()
        
######################## Sign Up Function ######################## 

def signUp(parsed, signUpDetails):
    global first, loggedIn, root
    if not loggedIn:
        problem = False
        if first:
            first = False
            root = Tk()
            if parsed == False and signUpDetails != "":
                gui = signup(root, signUpDetails)
            else:
                gui = signup(root, "")
            root.protocol("WM_DELETE_WINDOW", quitTK)
            root.mainloop()
        if parsed:
            if len(signUpDetails[1]) < 8:
                first = True
                signUp(False, "Your password is too short.")
            else:
                users = eval(open("F:/CACA/Users.txt").read())
                for uName in users:
                    if not problem:
                        if signUpDetails[0] == uName:
                            problem = True
                            first = True
                            signUp(False, "Existing username")
                if not problem:
                    if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', signUpDetails[1]):
                        usersfile = open("F:/CACA/Users.txt", "w")
                        usersfile.seek(0)
                        usersfile.truncate()
                        usersfile.write("{")
                        for uName in users:
                            usersfile.write("\"" + uName + "\":\"" + users[uName] + "\", ")
                        users[signUpDetails[0]] = signUpDetails[1]
                        usersfile.write("\"" + signUpDetails[0] + "\":\"" + signUpDetails[1] + "\"}")
                        loggedIn = True
                        global USERNAME
                        USERNAME = signUpDetails[0]
                        first = True
                    else:
                        first = True
                        signUp(False, "Invalid characters in password")
    else:
        mode = "menu"
        menu()

######################## Start Menu Function ########################
        
def startMenu():
    global first, screen1, buttons, sliders,  mode
    if first:
        first = False
        buttons = []
        sliders = []
        buttons.append(PGButton(10, 220, 60, 20, "Go Back", "back"))
        buttons.append(PGButton(75, 220, 120, 20, "Start simulation", "startSim"))
        width, height = 205, 250

        screen1 = pygame.display.set_mode((width, height))

    screen1.fill((white))

    screen1.blit(small2.render("This will say stuff yanno", False, black), (15, 10))
    screen1.blit(small2.render("More damned lines", False, black), (15, 26))
    screen1.blit(small2.render("More linezzzzzzzzzzz", False, black), (15, 42))
    screen1.blit(small2.render("Line number four", False, black), (15, 58))
    screen1.blit(small2.render("This will have more ", False, black), (15, 74))
    screen1.blit(small2.render("informative stuff in", False, black), (15, 90))
    screen1.blit(small2.render("the end i promise lol", False, black), (15, 106))

    but = doButtons()
    
    if but == "back":
        mode = "menu"
        first = True
        menu()
    elif but == "startSim":
        mode = "CA"
        first = True
        CA()

######################## Cellular Automata Function ########################

def CA():
    global first, buttons, sliders, allPixels, CAs, screen2, width, height, customA, CUSTOMCOLOR, CUSTOMID
    if first:
        first = False
        width, height = 1200, 600
        buttons = []
        sliders = []
        CAs = []
        allPixels = []
        buttons.append(PGButton(10, 10, 60, 20, "Go Back", "back"))
        for i in range(5):
            CAs.append(CellularAuto(int(random.random() * 255), i))
        for i in CAs:
            print(i.pixels[0].x, i.pixels[0].y)

        for x in range(width):
            allPixels.append([])
            for y in range(height):
                allPixels[x].append(None)
        screen2 = pygame.display.set_mode((width, height))

    screen2.fill(white)
    
    for CellularAutomata in CAs:
        for pix in CellularAutomata.pixels:
            allPixels[pix.px][pix.py] = None
            pix.first = True
            
    for CellularAutomata in CAs:
        for pix in CellularAutomata.pixels:
            allPixels[pix.x][pix.y] = pix
        CellularAutomata.update()
        CellularAutomata.display()

    but = doButtons()

    if but == "back":
        global mode
        mode = "menu"
        first = True
        menu()

def CACustom():
    global first, buttons, sliders, allPixels, CAs, screen2, width, height, customA, CUSTOMCOLOR, CUSTOMID
    if first:
        first = False
        width, height = 1200, 600
        buttons = []
        sliders = []
        CAs = []
        allPixels = []
        buttons.append(PGButton(10, 10, 60, 20, "Go Back", "back"))
        CAs.append(CellularAuto(CUSTOMCOLOR, 4))
        for i in range(4):
            CAs.append(CellularAuto(int(random.random() * 255), i))
        for i in CAs:
            print(i.pixels[0].x, i.pixels[0].y)

        for x in range(width):
            allPixels.append([])
            for y in range(height):
                allPixels[x].append(None)
        screen2 = pygame.display.set_mode((width, height))

    screen2.fill(white)
    
    for CellularAutomata in CAs:
        for pix in CellularAutomata.pixels:
            allPixels[pix.px][pix.py] = None
            pix.first = True
            
    for CellularAutomata in CAs:
        for pix in CellularAutomata.pixels:
            allPixels[pix.x][pix.y] = pix
        CellularAutomata.update()
        CellularAutomata.display()

    but = doButtons()

    if but == "back":
        global mode
        mode = "menu"
        first = True
        menu()
            
    

######################## Custom Automaton Function ########################

def custom():
    global first, buttons, sliders, screen1, width, height, mode, nameG, customA, CUSTOMID, CUSTOMCOLOR, CUSTOMSTRENGTH, CUSTOMREPROD, CUSTOMX, CUSTOMY
    if first:
        first = False
        buttons = []
        sliders = []
        width, height = 350, 350
        w, h = small.size("Set Automaton Name")
        nameG = "Custom Automata"
        buttons.append(PGButton(10, 320, 60, 20, "Go Back", "back"))
        buttons.append(PGButton(225, 320, 115, 20, "Start Simulation", "start"))
        buttons.append(PGButton((width / 2) - (w / 2), 260, w + 5, 20, "Set Automaton Name", "name"))
        sliders.append(PGSlider(40, 140, 0, 100, "Strength", "strength"))
        sliders.append(PGSlider(210, 140, 0, 100, "Reprod Value", "reprod"))
        sliders.append(PGSlider(40, 190, 0, 100, "X position", "strength"))
        sliders.append(PGSlider(210, 190, 0, 100, "Y position", "reprod"))
        sliders.append(PGSlider(125, 230, 0, 100, "Colour", "color"))
        screen1 = pygame.display.set_mode((width, height))
        
    screen1.fill(white)
    screen1.blit(medium.render("Create Your", False, black), (70, 10))
    screen1.blit(medium.render("Custom Automaton", False, black), (15, 50))
    but = doButtons()
    sli = doSliders()

    r, g, b = colorsys.hsv_to_rgb(sli[4]/100, 1, 1)
    r *= 255
    g *= 255
    b *= 255
    try:
        pygame.draw.rect(screen1, (r, g, b), (250, 220, 20, 20) , 0)
    except(TypeError):
        pygame.draw.rect(screen1, (255, 0, 0), (250, 220, 20, 20) , 0)
            
    pygame.draw.line(screen1, black, (250, 220), (270, 220), 1)
    pygame.draw.line(screen1, black, (270, 220), (270, 240), 1)
    pygame.draw.line(screen1, black, (270, 240), (250, 240), 1)
    pygame.draw.line(screen1, black, (250, 240), (250, 220), 1)
    

    if but == "start":
        customA = True
        CUSTOMID = nameG
        if sli[0] < 1:
            sli[0] = 1
        if sli[1] < 1:
            sli[1] = 1
        CUSTOMSTRENGTH = sli[0] * 0.002
        CUSTOMREPROD = sli[1] * 0.002
        CUSTOMX = int(sli[2] * width / 100)
        CUSTOMY = int(sli[3] * height / 100)
        CUSTOMCOLOR = sli[4] * 2.55
        mode = "CACustom"
        first = True
        CACustom()
        
    elif but == "name":
        first = True
        name(False, "")
        buttons.pop()
        w, h = small.size(nameG)
        buttons.append(PGButton((width / 2) - (w / 2), 230, w + 5, 20, nameG, "name"))
    elif but == "back":
        mode = "menu"
        first = True
        menu()

######################## Get Name Function ########################

def name(parsed, Name):
    global first, nameG
    if first:
        first = False
        root = Tk()
        if parsed == False and Name != "":
            gui = nameC(root)
        else:
            gui = nameC(root)
        root.protocol("WM_DELETE_WINDOW", root.destroy)
        root.mainloop()
    if parsed:
        problem = False
        if len(Name) == 0:
            problem = True
            first = True
            name(False, "")
        if not problem:
            nameG = Name

######################## Do Buttons Function ########################
    
def doButtons():
    but = ""
    for b in buttons:
        b.display()
        if b.pressed():
            but = b.val()
    return but

######################## So Sliders Function ########################

def doSliders():
    sli = []
    for slider in sliders:
        slider.display()
        slider.update()
        sli.append(slider.offset)
    return sli
    
######################## Main Loop ######################## 

while not quitted:
    #print(mode)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitted = True
        mouseX, mouseY = pygame.mouse.get_pos()
        #print(event)
    pygame.display.update()
    if mode == "menu":
        menu()
    elif mode == "startmenu":
        startMenu()
    elif mode == "custom":
        custom()
    elif mode == "CA":
        CA()
    elif mode == "CACustom":
        CACustom()
    elif mode == "login":
        logIn(False, "")
    elif mode == "signup":
        signUp(False, "")
    elif mode == "run":
        run()
        
    clock.tick(60)

pygame.quit()
quit()
