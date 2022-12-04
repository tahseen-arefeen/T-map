import board 
import adafruit_dotstar as dotstar
import time



#def Brightness
brightness = .5
WHITE = (255,255,255)
GREEN = (0,128,0)
ORANGE = (255,140,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)


'''
    On the issue of transfer stations and forks
    Park Street = rl
    Downtown Crossing = rl
    R10 = rl
    
    North Station = ol
    Haymarket = ol
    
    Government Center = bl
    State = bl
    
    G12 = glb
    G9 = glb
    G5 = glb
      
'''

#### GREEN LINE AND HER DAUGHTERS ####
class GreenLine:
    def __init__(self):
        self.color = 'Green Line'
    
    def type(self):
        return self.color
    
class GL(GreenLine):
    def __init__(self):
        
        self.num_pixels = len(GL.chain(self))
        self.data_pin = board.GP17
        self.clock_pin = board.GP27

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
        self.data_pin = board.GP22
        self.clock_pin = board.GP0

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
        self.data_pin = board.GP5
        self.clock_pin = board.GP6

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
        self.data_pin = board.GP26
        self.clock_pin = board.GP21

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
        self.data_pin = board.GP18
        self.clock_pin = board.GP23

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
    
#### RED LINE AND HER DAUGHTERS ####
class RedLine():
    def __init__(self):
        self.color = 'Red Line'
        
    def type(self):
        return self.color
    
class RL(RedLine):
    def __init__(self):
        
        self.num_pixels = len(RL.chain(self))
        self.data_pin = board.GP24
        self.clock_pin = board.GP25
        self.pixels = dotstar.DotStar(self.data_pin, self.clock_pin, 51, brightness= brightness)
        
    def light_station(self):
        stations = [0, 3, 5, 8, 11, 13, 15, 18, 19, 21, 23, 25, 28, 36, 39, 42, 46, 50]
        
        for i in stations:
            station_index = stations[i]
            self.pixels[station_index] = WHITE
    
    def light_train(self,index):
        self.pixels[index] = RED
    
    def light_clear(self):
        for i in range(len(RL.chain(self))):
            self.pixels[i] = BLACK
    
    def chain(self):
        return ['Alewife',17,16,'Davis',14,'Porter',12,11,'Harvard',9,8,'Central',6,'Kendall/MIT',4,'Charles/MGH',2,1,'Park Street','Downtown Crossing',1,'South Station',3,'Broadway',5,'Andrew',7,8,'JFK/UMass',10,11,12,13,14,15,16,'North Quincy',18,19,'Wollaston',21,22,'Quincy Center',24,25,26,'Quincy Adams',28,29,30,'Braintree']

    def true_index(self,chain_index,direction,status):
        
        chain = RL.chain(self)
        mid_point = 18
        
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
            
    def long_ride(self, station, lat, long, chain_index, direction):
        if station == 'JFK/UMass':
            B = [42.320632,-71.052514] #JFK/UMass
            A = [42.275802,-71.030144] #North Quincy
        else:
            A = [42.320632,-71.052514] #North Quincy
            B = [42.275802,-71.030144] #JFK/UMass
            
        slope_AB = (B[0] - A[0])/(A[1] - B[1])
        intercept_AB = B[0] - B[1] * slope_AB
        
        slope_C = -1/slope_AB
        intercept_C = lat - long * slope_C
        
        long_X = (intercept_C - intercept_AB) / (slope_AB - slope_C)
        lat_X = long_X * slope_C + intercept_C

        d_station = pow(pow((B[0]-A[0]),2) + pow((B[1]-A[1]),2),.5)
        d_X = pow(pow((lat_X-A[0]),2) + pow((long_X-A[1]),2),.5)
        
        progress = d_X / d_station
        
        if direction == 0:
            if progress > 0 and progress <= 1/8:
                chain_index = chain_index - 7
            if progress > 1/8 and progress <= 2/8:
                chain_index = chain_index - 6
            if progress > 2/8 and progress <= 3/8:
                chain_index = chain_index - 5
            if progress > 3/8 and progress <= 4/8:
                chain_index = chain_index - 4
            if progress > 4/8 and progress <= 5/8:
                chain_index = chain_index - 3
            if progress > 5/8 and progress <= 6/8:
                chain_index = chain_index - 2
            if progress > 6/8 and progress <= 7/8:
                chain_index = chain_index - 1
        
        else:
            if progress > 0 and progress <= 1/8:
                chain_index = chain_index + 7
            if progress > 1/8 and progress <= 2/8:
                chain_index = chain_index + 6
            if progress > 2/8 and progress <= 3/8:
                chain_index = chain_index + 5
            if progress > 3/8 and progress <= 4/8:
                chain_index = chain_index + 4
            if progress > 4/8 and progress <= 5/8:
                chain_index = chain_index + 3
            if progress > 5/8 and progress <= 6/8:
                chain_index = chain_index + 2
            if progress > 6/8 and progress <= 7/8:
                chain_index = chain_index + 1
             
class ML(RedLine):
    def __init__(self):
        
        self.num_pixels = len(ML.chain(self))
        self.data_pin = board.GP1
        self.clock_pin = board.GP12

        self.pixels = dotstar.DotStar(self.data_pin, self.clock_pin, 16, brightness= brightness)
        
    def light_station(self):
        stations = [0, 3, 5, 7, 8, 10, 11, 12, 13, 14, 15]
        
        for i in stations:
            station_index = stations[i]
            self.pixels[station_index] = WHITE
    
    def light_train(self,index):
        self.pixels[index] = RED
    
    def light_clear(self):
        for i in range(len(ML.chain(self))):
            self.pixels[i] = BLACK
    
    
    def chain(self):   
        return ['Savin Hill',13,14,'Fields Corner',16,'Shawmut',18,'Ashmount','Cedar Grove',21,'Butler','Milton','Central Avenue','Valley Road','Valley Road','Capen Street']

    def true_index(self,chain_index,direction,status):
        
        chain = ML.chain(self)
        
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

#### ORANGE LINE AND HER DAUGHTERS ####
class OrangeLine():
    
    def __init__(self):
        self.color = 'Orange Line'
    
    def type(self):
        return self.color

class OL(OrangeLine):
    def __init__(self):
        
        self.num_pixels = len(OL.chain(self))
        self.data_pin = board.GP16
        self.clock_pin = board.GP20

        self.pixels = dotstar.DotStar(self.data_pin, self.clock_pin, 32, brightness= brightness)
        
    def light_station(self):
        stations = [0, 2, 5, 8, 10, 12, 13, 15, 16, 18, 20, 22, 23, 25, 27, 29, 31]

        for i in stations:
            station_index = stations[i]
            self.pixels[station_index] = WHITE
    
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

#### BLUE LINE AND HER DAUGHTERS ####
class BlueLine():
    def __init__(self):
        self.color = 'Blue Line'
    
    def type(self):
        return self.color
    
class BL(BlueLine):
    def __init__(self):
        
        self.num_pixels = len(BL.chain(self))
        self.data_pin = board.GP2
        self.clock_pin = board.GP3

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
    
