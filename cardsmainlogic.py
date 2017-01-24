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
        self.name = str
        self.is_selected = False
        self.attack = int
        self.defense = int

        self.clicked = [0,0]
        self.validmove = True
        self.validslot = None

        self.rect.x = random.randrange(1,GAMEWINDOW_WIDTH)
        self.rect.y = random.randrange(1,GAMEWINDOW_HEIGHT)
    def update(self):
        print self.validmove
        if self.is_selected:
            self.rect.centerx, self.rect.centery = current_mouse_pos[0], current_mouse_pos[1] 
        # Slot hover activate
        for slot in cardslots:
            if card.rect.colliderect(slot[0],slot[1],slot[2], slot[3]):
                slot[4] = (255,50,50)
                self.validmove = True
                self.validslot = slot
                break
            else:
                slot[4] = (50,50,50)
                self.validmove = False
card_list = pygame.sprite.Group()
            
cards = []
with open('cardlist.txt', 'r') as file:
    for line in file:
        cards.append(line.strip())


for card in cards[:3]:
    card_list.add(Card('./Images/'+ card + '.png'))
    
card = Card('./Images/9_of_hearts.png')
card.rect.centerx = GAMEWINDOW_WIDTH/2
card.rect.centery = GAMEWINDOW_HEIGHT-card.rect.height
cardwidth = card.rect.width
cardheight = card.rect.height

card_list.add(card)

# Setting up card slots
cardslots = []
margin = 50
for x in range(3):
    x *= 200
    # cardslot[x, y, width, height]
    cardslots.append([margin+x, 200, cardheight, cardwidth, (50,50,50)])

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
                    if card.validmove == False:
                        card.rect.x, card.rect.y = card.clicked
                    else:
                        card.rect.x, card.rect.y = card.validslot[0], card.validslot[1]
                card.is_selected = False


    for card in card_list:
        if card.rect.collidepoint(current_mouse_pos):
            pass # print "hover over"


    SCREEN.fill((100,100,100))

    for cardslot in cardslots:
        pygame.draw.rect(SCREEN, cardslot[4], [cardslot[0], cardslot[1], cardslot[2], cardslot[3]])

    card_list.update()
    card_list.draw(SCREEN)


  
        

        
    clock.tick(FPS)
    pygame.display.flip()