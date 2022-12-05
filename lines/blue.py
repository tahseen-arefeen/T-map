import board 
import adafruit_dotstar as dotstar
import time



#def Brightness
brightness = .5
WHITE = (255,255,255)
BLUE = (0,0,255)
BLACK = (0,0,0)

#### BLUE LINE AND HER DAUGHTERS ####
class BlueLine():
    def __init__(self):
        self.color = 'Blue Line'
    
    def type(self):
        return self.color
    
class BL(BlueLine):
    def __init__(self):
        
        self.num_pixels = len(BL.chain(self))
        self.data_pin = board.D24
        self.clock_pin = board.D25

        self.pixels = dotstar.DotStar(self.data_pin, self.clock_pin, 21, brightness= brightness)
        
    def light_station(self):
        stations = [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 18, 20]
        
        for i in stations:
            station_index = stations[i]
            self.pixels[station_index] = WHITE
    
    def light_train(self,index):
        self.pixels[index] = BLUE
    
    def light_clear(self):
        for i in range(len(BL.chain(self))):
            self.pixels[i] = BLACK
    
    def chain(self):
        return ['Wonderland','Revere Beach',15,'Beachmont',13,'Suffolk Downs',11,'Orient Heights',9,'Wood Island',7,'Airport',5,'Maverick',3,'Aquarium',1,'State','Governement Center',1,'Bowdin']
    
    def true_index(self,chain_index,direction,status):
        
        chain = BL.chain(self)
        
        condition =  direction == 0
        
        if condition == True:
            if status == 'IN_TRANSIT_TO' and type(chain[chain_index]+2) == int:
                chain_index = chain_index + 2
            if status == 'INCOMING_AT' and type(chain[chain_index]+1) == int:
                chain_index = chain_index + 1
        else:
            if status == 'IN_TRANSIT_TO' and type(chain[chain_index]-2) == int:
                chain_index = chain_index - 2
            if status == 'INCOMING_AT' and type(chain[chain_index]-1) == int:
                chain_index = chain_index - 1
        
        return chain_index