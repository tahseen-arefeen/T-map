import board 
import adafruit_dotstar as dotstar
import time

#def Brightness
brightness = .5
WHITE = (255,255,255)
ORANGE = (255,140,0)
BLACK = (0,0,0)


#### ORANGE LINE AND HER DAUGHTERS ####
class OrangeLine():
    
    def __init__(self):
        self.color = 'Orange Line'
    
    def type(self):
        return self.color

class OL(OrangeLine):
    def __init__(self):
        
        self.num_pixels = len(OL.chain(self))
        self.data_pin = board.D18
        self.clock_pin = board.D23

        self.pixels = dotstar.DotStar(self.data_pin, self.clock_pin, self.num_pixels, brightness= brightness)
        
    def light_station(self):
        stations = [0, 2, 5, 8, 10, 12, 13, 15, 16, 18, 20, 22, 23, 25, 27, 29, 31]

        for i in stations:
            self.pixels[i] = WHITE
    
    def light_train(self,index):
        self.pixels[index] = ORANGE
    
    def light_clear(self):
        for i in range(len(OL.chain(self))):
            self.pixels[i] = BLACK
    

    def chain(self):
        return ['Oak Grove',13,'Malden Center',11,10,'Wellington',8,7,'Sullivan Square',5,'Community College',3,'North Station','Haymarket',1,'Chinatown','Tufts Medical',4,'Back Bay',6,'Massachusetts Avenue',8,'Ruggles','Roxbury Crossing',11,'Jackson Square',13,'Stony Brook',15,'Green Street',17,'Forest Hills']
    
    def true_index(self,chain_index,direction,status):
        
        chain = OL.chain(self)
        
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