import board 
import adafruit_dotstar as dotstar

#def Brightness
brightness = .5
WHITE = (255,255,255)
GREEN = (0,128,0)

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


#### RED LINE AND HER DAUGHTERS ####
class RedLine():
    def __init__(self):
        self.color = 'Red Line'
        
    def type(self):
        return self.color
    
class RL(RedLine):
    def __init__(self):
        
        self.num_pixels = len(RL.chain(self))
        self.data_pin = board.D6
        self.clock_pin = board.D13
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
        self.data_pin = board.D19
        self.clock_pin = board.D26

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