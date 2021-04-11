import pygame
  

background_colour = (234, 212, 252)
  

screen = pygame.display.set_mode((900, 600))
  

pygame.display.set_caption('Burger Madness')
  

screen.fill(background_colour)
  

pygame.display.flip()
  

running = True
  
char = pygame.image.load("assets/gui/Main.bmp")
char_rect = char.get_rect()
while running:
    
 
    for event in pygame.event.get():
      
            
        if event.type == pygame.QUIT:
            running = False
    screen.blit(char, char_rect)        
    pygame.display.flip()