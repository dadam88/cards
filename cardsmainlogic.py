import pygame
import random
#Initialize for pygame...
pygame.font.init() #without this I can't use font class
clock =  pygame.time.Clock()

#CONSTANTS
BACGKROUND_COLOR = (255,255,255) #White

#Main window game is stored in
GAMEWINDOW_WIDTH = 600
GAMEWINDOW_HEIGHT = 600

SCREEN = pygame.display.set_mode((GAMEWINDOW_WIDTH, GAMEWINDOW_HEIGHT))
#Frames per second, using in conjunction with pygame.clock.tick
FPS = 60

class Hand():
    def __init__(self):
        cards = []

class Card(pygame.sprite.Sprite):
    def __init__(self, filename):
        # Pygame engine to initialize sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.scale(self.image, (GAMEWINDOW_WIDTH/5, GAMEWINDOW_HEIGHT/5))
        self.rect = self.image.get_rect()
        ##################################
        self.is_highlighted = bool
        self.name = filename
        self.is_selected = False
        self.attack = int
        self.defense = int

        self.clicked = [0,0]
        self.validmove = True
        self.validslot = None

        self.rect.x = random.randrange(1,GAMEWINDOW_WIDTH-self.rect.width)
        self.rect.y = random.randrange(1,GAMEWINDOW_HEIGHT-self.rect.height)

    def update(self):
       
        if self.is_selected:
            print self.name
            self.rect.centerx, self.rect.centery = current_mouse_pos[0], current_mouse_pos[1] 
        # Slot hover activate
            for slot in cardslots:
                if self.rect.colliderect(slot[0][0],slot[0][1],slot[0][2], slot[0][3]):
                    slot[1] = True
                    self.validmove = True
                    self.validslot = slot
                    
                else:
                    slot[1] = False
                    self.validmove = False
                    
card_list = pygame.sprite.Group()
            
cards = []
with open('cardlist.txt', 'r') as file:
    for line in file:
        cards.append(line.strip())

hand = Hand()
for card in cards[:10]:
    card_list.add(Card('./Images/'+ card + '.png'))
    
card = Card('./Images/9_of_hearts.png')
card.rect.centerx = GAMEWINDOW_WIDTH/2
card.rect.centery = GAMEWINDOW_HEIGHT-card.rect.height
cardwidth = card.rect.width
cardheight = card.rect.height



# Setting up card slots
cardslots = []
margin = 50
for x in range(3):
    x *= 200
    # cardslot[x, y, width, height]
    cardslots.append([[margin+x, 200, cardheight, cardwidth, (50,50,50)],[False]])

#Main game loop
while True:
    for event in pygame.event.get():
        #Mouse position variable...
        current_mouse_pos = pygame.mouse.get_pos()

        #If user clicks the X in window
        if event.type == pygame.QUIT:
            pygame.QUIT()
            break

        # Handling User Input
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #event.button 1, Left : 2, Middle : 3, Right
            for card in card_list:
                if card.rect.collidepoint(current_mouse_pos) and event.button == 1:
                    card.clicked = card.rect.x, card.rect.y
                    card.is_selected = True


        elif event.type == pygame.MOUSEBUTTONUP:
            for card in card_list:
                if card.is_selected:
                    # returns to original position
                    if card.validslot[1] == True:
                        card.rect.x, card.rect.y = card.validslot[0][0], card.validslot[0][1]
                    else:
                        card.rect.x, card.rect.y = card.clicked
                        
                card.is_selected = False


    for card in card_list:
        if card.rect.collidepoint(current_mouse_pos):
            pass # print "hover over"


    SCREEN.fill((100,100,100))

    for cardslot in cardslots:
        if cardslot[1] == True:
            pygame.draw.rect(SCREEN, (200,50,50), [cardslot[0][0], cardslot[0][1], cardslot[0][2], cardslot[0][3]])
        else:
            pygame.draw.rect(SCREEN, cardslot[0][4], [cardslot[0][0], cardslot[0][1], cardslot[0][2], cardslot[0][3]])
            

    card_list.update()
    card_list.draw(SCREEN)


  
        

        
    clock.tick(FPS)
    pygame.display.flip()