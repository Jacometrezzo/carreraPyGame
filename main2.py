import pygame, sys
import random


class Runner():
    __customes = ('turtle', 'fish', 'prawn', 'moray', 'octopus')
    
    
    def __init__(self, x=0, y=0, custome = 'turtle'):
        
        self.custome = pygame.image.load('images/turtle.png'.format(custome))
        self.position = [x, y]
        self.name = custome
        
    def avanzar(self):
        self.position[0] += random.randint(1,12)
        
    

class Game():
    runners = []
    __posY = (160, 200, 240, 280)
    __names = ('Speedy', 'Lucera', 'Alonso', 'Torcuata')
    __startLine = 20
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load('images/background.png')
        #titulo de la pantalla
        pygame.display.set_caption('carrera de bichos')
        
        for i in range (4):
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
        
        '''
        #Esto es lo mismo que las 3 lineas de arriba(crea al primer corredor, lo situa en la linea de salida, le pone nombre
        y lo añade a la lista de corredores)
        
        runners.append(Runner(self.__StarLine, 240)) 
        '''
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
            for activeRunner in self.runners:       
                activeRunner.avanzar()
            
            if self.runners[0].position[0] >= self.__finishLine:
                print('{} ha ganado la carrera'.format(self.runners[0].name))
                gameOver = True
                
                    
            self.__screen.blit(self.__background, (0, 0))
            
            '''
            self.__screen.blit(self.runners[0].custome, self.runners[0].position)
            self.__screen.blit(self.runners[1].custome, self.runners[1].position)
            self.__screen.blit(self.runners[2].custome, self.runners[2].position)
            self.__screen.blit(self.runners[3].custome, self.runners[3].position)
            estas cuatro lineas de arriba es exactamente lo mismo que el bloque if de abajo pero repitiendonos menos
            ''' 
            
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
            pygame.display.flip()
            
        pygame.quit()
        sys.exit()
            


if __name__ == '__main__':
    game = Game()
    pygame.font.init()
    game.competir()
    