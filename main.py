import time
from lines import green, orange, red, blue
import fetcher as f

'''
GLOBAL VARIABLES
'''

stop_url = "https://api-v3.mbta.com/stops"
train_url = "https://api-v3.mbta.com/vehicles"

rl = red.RL()
ml = red.ML()
gl = green.GL()
glb = green.GLB()
glc = green.GLC()
gld = green.GLD()
gle = green.GLE()
ol = orange.OL()
bl = blue.BL()

def LocateChain(train_id,station):
    """identifies which led chain train belongs to and identifies exceptions 

    Args:
        train_id (str): train identification string
        station (str): station name 

    Returns:
        chain_index: location of train within led chain 
        chain_id: led chain identity
    """
    chain_index = 0
    chain = 'null'
    chain_id = 'null'
    if train_id[0] in ['G', 'O', 'R', 'B']: 
        ######################################################
        
        if train_id[0] == 'R' and station in rl.chain():
            chain = rl.chain()
            chain_index = chain.index(station)
            chain_id = 'rl'
                
        elif train_id[0] == 'R' and station in ml.chain():
            chain = ml.chain()
            chain_index = chain.index(station)
            chain_id = 'ml'
            
        elif train_id[0] == 'R' and station in ['JFK/UMass','North Quincy']:
            chain = rl.chain()
            chain_index = chain.index(station)
            chain_id = 'Lrl'
            
        ######################################################
            
        elif train_id[0] == 'G' and station in ['Government Center','Park Street']: 
            if station == 'Government Center':
                chain = bl.chain()
                chain_index = chain.index(station)
                chain_id = 'Gbl'
            elif station == 'Park Street':
                chain = rl.chain()
                chain_index = chain.index(station)
                chain_id = 'Grl'
            else:
                chain = ol.chain()
                chain_index = chain.index(station)
                chain_id = 'Gol'
            
        elif train_id[0] == 'G' and station in gl.chain():
            chain = gl.chain()
            chain_index = chain.index(station)
            chain_id = 'gl'
            
        elif train_id[0] == 'G' and station in glb.chain():
            chain = glb.chain()
            chain_index = chain.index(station)
            chain_id = 'glb'
            
        elif train_id[0] == 'G' and station in glc.chain():
            chain = glc.chain()
            chain_index = chain.index(station)
            chain_id = 'glc'
            
        elif train_id[0] == 'G' and station in gld.chain():
            chain = gld.chain()
            chain_index = chain.index(station)
            chain_id = 'gld'
            
        elif train_id[0] == 'G' and station in gle.chain():
            chain = gle.chain()
            chain_index = chain.index(station)
            chain_id = 'gle'
            
        ######################################################
            
        elif train_id[0] == 'O' and station in ['State','Downtown Crossing']:
            if station == 'State':
                chain = bl.chain()
                chain_index = chain.index(station)
                chain_id = 'Obl'
            else:
                chain = rl.chain()
                chain_index = chain.index(station)
                chain_id = 'Orl'
                
        elif train_id[0] == 'O' and station in ol.chain():
            chain = ol.chain()
            chain_index = chain.index(station)
            chain_id = 'ol'
            
        ######################################################
            
        elif train_id[0] == 'B' and station in bl.chain():
            chain = bl.chain()
            chain_index = chain.index(station)
            chain_id = 'bl'
          
    return chain_index, chain_id
    
def ChainAdjuster(station,chain_index, chain_id, direction, status,lat,long):
    """Adjusts chain index to account for train status

    Args:
        station (str): station name
        chain_index (int): unadjusted index in chain
        chain_id (str): identity of chain
        direction (int): inbound or outbound status
        status (str): status of train of intrest
        lat (float): latitude of train of interest
        long (float): longitude of train of interest

    Returns:
        true_index: adjusted index within chain
    """

    if chain_id == 'Gbl':
        return chain_index, 'bl'
    
    elif chain_id == 'Grl':
        return chain_index, 'rl'
    
    elif chain_id == 'Gol':
        return chain_index, 'ol'
    
    elif chain_id == 'Obl':
        return chain_index, 'bl'
    
    elif chain_id == 'Orl':
        return chain_index, 'rl'
    
    elif chain_id == 'Lrl':
        return rl.long_ride(station, lat, long, chain_index, direction)

    
    elif chain_id == 'rl':
        return rl.true_index(chain_index,direction,status), 'rl'

    elif chain_id == 'ml':
        return ml.true_index(chain_index,direction,status), 'ml'     
    
    elif chain_id == 'gl':
        return gl.true_index(chain_index,direction,status), 'gl' 
    
    elif chain_id == 'glb':
        return glb.true_index(chain_index,direction,status), 'glb'
    
    elif chain_id == 'glc':
        return glc.true_index(chain_index,direction,status), 'glc'
    
    elif chain_id == 'gld':
        return gld.true_index(chain_index,direction,status), 'gld'
    
    elif chain_id == 'gle':
        return gle.true_index(chain_index,direction,status), 'gle'

    elif chain_id == 'ol':
        return ol.true_index(chain_index,direction,status), 'ol'
            
    elif chain_id == 'bl':
        return ml.true_index(chain_index,direction,status), 'bl'
                    
def MainLoop():
    for i in range(len(tf)):
        train_id = tf.iloc[i,1]
        
        try:
            direction = f.FindDirectionId(train_id)
            status = f.FindStatus(train_id)
            station = f.FindStation(train_id)
            chain_index, chain_id = LocateChain(train_id,station)
            lat = f.FindLat(train_id)
            long = f.FindLong(train_id)

            result = ChainAdjuster(train_id, chain_index, chain_id, direction, status,lat,long)
           
            
            if result != None:
                chain_index = result[0]
                chain_id = result[1]
                print(chain_index,chain_id)
                
                chain_id.light_train(chain_index)
            
        except:
            pass
        
    time.sleep(1)
    
    gl.light_clear()
    glb.light_clear()
    glc.light_clear()
    gld.light_clear()
    gle.light_clear()
    ol.light_clear()
    rl.light_clear()
    ml.light_clear()
    bl.light_clear()
        
def RAVE():
    pass         
               
sf = f.FetchAPI(stop_url)

rl.light_station()
ml.light_station()
gl.light_station()
glb.light_station()
glc.light_station()
gld.light_station()
gle.light_station()
ol.light_station()
bl.light_station()

while True:
    try:
        tf = f.FetchAPI(train_url)
        
        MainLoop()
        
    except:
        pass
        