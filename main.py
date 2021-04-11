import pygame
pygame.init()

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                char_rect.move(-5, 0)     
    screen.blit(char, char_rect)        
    pygame.display.flip()