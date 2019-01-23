import pygame
import sys

class Game():
    #Necesitaremos un atributo: corredores
    corredores = []
    
    
    def __init_(self):
        
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Carrera de bichos')
        #Cargar imagen de fondo de la pantalla
        self.background = pygame.image.load('images/background.png')

    def competir(self):
        
        while True:
            #Comprobación de los eventos
            for event in pygam.event.get():
                if event.type== pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
if __name__ == '__main__':
    pygame.init()
    game = Game()
    