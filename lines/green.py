import board 
import adafruit_dotstar as dotstar
import time

#def Brightness
brightness = .5
WHITE = (255,255,255)
GREEN = (0,128,0)
BLACK = (0,0,0)

#### GREEN LINE AND HER DAUGHTERS ####
class GreenLine:
    def __init__(self):
        self.color = 'Green Line'
    
    def type(self):
        return self.color
    
class GL(GreenLine):
    def __init__(self):
        
        self.num_pixels = len(GL.chain(self))
        self.data_pin = board.D2
        self.clock_pin = board.D3

        self.pixels = dotstar.DotStar(self.data_pin, self.clock_pin, 8, brightness= brightness)
        
    def light_station(self):
        stations = [0,2,4,6,7]
        
        for i in stations:
            station_index = stations[i]
            self.pixels[station_index] = WHITE
    
    def light_train(self,index):
        self.pixels[index] = GREEN
    
    def light_clear(self):
        for i in range(len(GL.chain(self))):
            self.pixels[i] = BLACK
        
    
    def chain(self):
        return ['Medford/Tufts',16,'Ball Square',14,'Magoun Square',12,'Gilman Square','East Somerville']
    
    def true_index(self,chain_index,direction,status):
        
        chain = GL.chain(self)
        
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
    
class GLB (GreenLine):
    def __init__(self):
        
        self.num_pixels = len(GLB.chain(self))
        self.data_pin = board.D4
        self.clock_pin = board.D17

        self.pixels = dotstar.DotStar(self.data_pin, self.clock_pin, 49, brightness= brightness)
        
    def light_station(self):
        stations = [0, 3, 6, 10, 11, 12, 15, 18, 23, 24, 25, 28, 29, 30, 32, 33, 35, 37, 38, 39, 41, 42, 44, 45, 46, 48]
        
        for i in stations:
            station_index = stations[i]
            self.pixels[station_index] = WHITE
    
    def light_train(self,index):
        self.pixels[index] = GREEN
    
    def light_clear(self):
        for i in range(len(GLB.chain(self))):
            self.pixels[i] = BLACK
    
    def chain(self):   
        return ['Union Square',10,9,'Lechmere',7,6,'Science Park/West End',4,3,1,'Boylston','Arlington','Copely',5,6,'Hynes',8,9,'Kenmore',11,12,13,14,'Blanford Street','BU East','BU Central',18,19,'BU West','Saint Paul Street','Pleasant Street',23,'Babock Street','Packards Corner',26,'Harvard Avenue',28,'Griggs Street','Allston Street','Warren Street',32,'Washington Street','Sutherland Street',35,'Chiswick Road','Chestnut Hill Avenue','South Street',39,'Boston College']

    def true_index(self,chain_index,direction,status):
        
        chain = GLB.chain(self)
        mid_point = 9
        
        condition = (chain_index <= mid_point and direction == 0) or (chain_index > 18 and direction == 1)
        
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
    
class GLC (GreenLine):
    def __init__(self):
        
        self.num_pixels = len(GLC.chain(self))
        self.data_pin = board.D27
        self.clock_pin = board.D22

        self.pixels = dotstar.DotStar(self.data_pin, self.clock_pin, 18, brightness= brightness)
        
    def light_station(self):
        stations = [0, 2, 3, 4, 6, 8, 9, 10, 12, 13, 14, 16, 17]
        
        for i in stations:
            station_index = stations[i]
            self.pixels[station_index] = WHITE
    
    def light_train(self,index):
        self.pixels[index] = GREEN
    
    def light_clear(self):
        for i in range(len(GLC.chain(self))):
            self.pixels[i] = BLACK
    
    def chain(self):   
        return ["Saint Mary's street",14,'Hawes Street','Kent Street','Saint Paul Street',18,'Coolridge Corner',20,'Summit Avenue','Brandon Hall','Fairbanks',24,'Washington Square','Tappan Street','Dean Road',28,'Engelwood Avenue','Cleveland Circle']

    def true_index(self,chain_index,direction,status):
        
        chain = GLC.chain(self)
        
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
    
class GLD (GreenLine):
    def __init__(self):
        
        self.num_pixels = len(GLD.chain(self))
        self.data_pin = board.D10
        self.clock_pin = board.D9

        self.pixels = dotstar.DotStar(self.data_pin, self.clock_pin, 18, brightness= brightness)
        
    def light_station(self):
        stations = [3, 4, 6, 7, 9, 11, 13, 16, 17, 18, 22, 25, 27]
        
        for i in stations:
            station_index = stations[i]
            self.pixels[station_index] = WHITE
    
    def light_train(self,index):
        self.pixels[index] = GREEN
    
    def light_clear(self):
        for i in range(len(GLD.chain(self))):
            self.pixels[i] = BLACK
    
    def chain(self):   
        return [13,14,15,'Fenway','Longwood',18,'Brookline Village','Brookline Hills',21,'Beaconsfield',23,'Reservoir',25,'Chestnut Hill',26,27,'Newton Centre','Newton Highlands','Eliot',32,33,34,'Waban',36,37,'Woodland',39,'Riverside']
    
    def true_index(self,chain_index,direction,status):
        
        chain = GLD.chain(self)
        
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
    
class GLE (GreenLine):
    def __init__(self):
        
        self.num_pixels = len(GLE.chain(self))
        self.data_pin = board.D11
        self.clock_pin = board.D5

        self.pixels = dotstar.DotStar(self.data_pin, self.clock_pin, 17, brightness= brightness)
        
    def light_station(self):
        stations = [0, 2, 4, 7, 8, 10, 11, 12, 13, 14, 16]
        
        for i in stations:
            station_index = stations[i]
            self.pixels[station_index] = WHITE
    
    def light_train(self,index):
        self.pixels[index] = GREEN
    
    def light_clear(self):
        for i in range(len(GLE.chain(self))):
            self.pixels[i] = BLACK
    
    
    def chain(self):   
        return ['Prudential',7,'Symphony',9,'Northeastern',11,12,'Museum of Fine Arts','Longwood Medical',15,'Brigham Circle','Fenwood Road','Mission Park','Riverway','Back of the Hill',21,'Heath Street']
    
    def true_index(self,chain_index,direction,status):
        
        chain = GLE.chain(self)
        
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
    
#### GREEN LINE AND HER DAUGHTERS ####
class GreenLine:
    def __init__(self):
        self.color = 'Green Line'
    
    def type(self):
        return self.color
    
class GL(GreenLine):
    def __init__(self):
        
        self.num_pixels = len(GL.chain(self))
        self.data_pin = board.D2
        self.clock_pin = board.D3

        self.pixels = dotstar.DotStar(self.data_pin, self.clock_pin, 8, brightness= brightness)
        
    def light_station(self):
        stations = [0,2,4,6,7]
        
        for i in stations:
            station_index = stations[i]
            self.pixels[station_index] = WHITE
    
    def light_train(self,index):
        self.pixels[index] = GREEN
    
    def light_clear(self):
        for i in range(len(GL.chain(self))):
            self.pixels[i] = BLACK
        
    
    def chain(self):
        return ['Medford/Tufts',16,'Ball Square',14,'Magoun Square',12,'Gilman Square','East Somerville']
    
    def true_index(self,chain_index,direction,status):
        
        chain = GL.chain(self)
        
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
    
class GLB (GreenLine):
    def __init__(self):
        
        self.num_pixels = len(GLB.chain(self))
        self.data_pin = board.D4
        self.clock_pin = board.D17

        self.pixels = dotstar.DotStar(self.data_pin, self.clock_pin, 49, brightness= brightness)
        
    def light_station(self):
        stations = [0, 3, 6, 10, 11, 12, 15, 18, 23, 24, 25, 28, 29, 30, 32, 33, 35, 37, 38, 39, 41, 42, 44, 45, 46, 48]
        
        for i in stations:
            station_index = stations[i]
            self.pixels[station_index] = WHITE
    
    def light_train(self,index):
        self.pixels[index] = GREEN
    
    def light_clear(self):
        for i in range(len(GLB.chain(self))):
            self.pixels[i] = BLACK
    
    def chain(self):   
        return ['Union Square',10,9,'Lechmere',7,6,'Science Park/West End',4,3,1,'Boylston','Arlington','Copely',5,6,'Hynes',8,9,'Kenmore',11,12,13,14,'Blanford Street','BU East','BU Central',18,19,'BU West','Saint Paul Street','Pleasant Street',23,'Babock Street','Packards Corner',26,'Harvard Avenue',28,'Griggs Street','Allston Street','Warren Street',32,'Washington Street','Sutherland Street',35,'Chiswick Road','Chestnut Hill Avenue','South Street',39,'Boston College']

    def true_index(self,chain_index,direction,status):
        
        chain = GLB.chain(self)
        mid_point = 9
        
        condition = (chain_index <= mid_point and direction == 0) or (chain_index > 18 and direction == 1)
        
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
    
class GLC (GreenLine):
    def __init__(self):
        
        self.num_pixels = len(GLC.chain(self))
        self.data_pin = board.D27
        self.clock_pin = board.D22

        self.pixels = dotstar.DotStar(self.data_pin, self.clock_pin, 18, brightness= brightness)
        
    def light_station(self):
        stations = [0, 2, 3, 4, 6, 8, 9, 10, 12, 13, 14, 16, 17]
        
        for i in stations:
            station_index = stations[i]
            self.pixels[station_index] = WHITE
    
    def light_train(self,index):
        self.pixels[index] = GREEN
    
    def light_clear(self):
        for i in range(len(GLC.chain(self))):
            self.pixels[i] = BLACK
    
    def chain(self):   
        return ["Saint Mary's street",14,'Hawes Street','Kent Street','Saint Paul Street',18,'Coolridge Corner',20,'Summit Avenue','Brandon Hall','Fairbanks',24,'Washington Square','Tappan Street','Dean Road',28,'Engelwood Avenue','Cleveland Circle']

    def true_index(self,chain_index,direction,status):
        
        chain = GLC.chain(self)
        
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
    
class GLD (GreenLine):
    def __init__(self):
        
        self.num_pixels = len(GLD.chain(self))
        self.data_pin = board.D10
        self.clock_pin = board.D9

        self.pixels = dotstar.DotStar(self.data_pin, self.clock_pin, 18, brightness= brightness)
        
    def light_station(self):
        stations = [3, 4, 6, 7, 9, 11, 13, 16, 17, 18, 22, 25, 27]
        
        for i in stations:
            station_index = stations[i]
            self.pixels[station_index] = WHITE
    
    def light_train(self,index):
        self.pixels[index] = GREEN
    
    def light_clear(self):
        for i in range(len(GLD.chain(self))):
            self.pixels[i] = BLACK
    
    def chain(self):   
        return [13,14,15,'Fenway','Longwood',18,'Brookline Village','Brookline Hills',21,'Beaconsfield',23,'Reservoir',25,'Chestnut Hill',26,27,'Newton Centre','Newton Highlands','Eliot',32,33,34,'Waban',36,37,'Woodland',39,'Riverside']
    
    def true_index(self,chain_index,direction,status):
        
        chain = GLD.chain(self)
        
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
    
class GLE (GreenLine):
    def __init__(self):
        
        self.num_pixels = len(GLE.chain(self))
        self.data_pin = board.D11
        self.clock_pin = board.D5

        self.pixels = dotstar.DotStar(self.data_pin, self.clock_pin, 17, brightness= brightness)
        
    def light_station(self):
        stations = [0, 2, 4, 7, 8, 10, 11, 12, 13, 14, 16]
        
        for i in stations:
            station_index = stations[i]
            self.pixels[station_index] = WHITE
    
    def light_train(self,index):
        self.pixels[index] = GREEN
    
    def light_clear(self):
        for i in range(len(GLE.chain(self))):
            self.pixels[i] = BLACK
    
    
    def chain(self):   
        return ['Prudential',7,'Symphony',9,'Northeastern',11,12,'Museum of Fine Arts','Longwood Medical',15,'Brigham Circle','Fenwood Road','Mission Park','Riverway','Back of the Hill',21,'Heath Street']
    
    def true_index(self,chain_index,direction,status):
        
        chain = GLE.chain(self)
        
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
    