import time
import lines
import fetcher as f

'''
GLOBAL VARIABLES
'''

stop_url = "https://api-v3.mbta.com/stops"
train_url = "https://api-v3.mbta.com/vehicles"

rl = lines.RL()
ml = lines.ML()
gl = lines.GL()
glb = lines.GLB()
glc = lines.GLC()
gld = lines.GLD()
gle = lines.GLE()
ol = lines.OL()
bl = lines.BL()

def LocateChain(train_id,station):
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
        condition = 'pass'
        
        try:
            direction = f.FindDirectionId(train_id)
            status = f.FindStatus(train_id)
            station = f.FindStation(train_id)
            chain_index, chain_id = LocateChain(train_id,station)
            lat = f.FindLat(train_id)
            long = f.FindLong(train_id)
            
            line = getattr(lines,chain_id)
            
            result = ChainAdjuster(train_id, chain_index, chain_id, direction, status,lat,long)
            
            line.light_train(result)
            
            if result != None:
                chain_index = result[0]
                chain_id = result[1]
                
                line = getattr(lines,chain_id)
                
                line.light_train(chain_index)
            
        except:
            pass
        
    time.sleep(1)
    
    gl.light_clear()
        
def RAVE():
    pass         
               

while True:
    try:
        tf = f.FetchAPI(train_url)
        sf = f.FetchAPI(stop_url)
        #MainLoop()
        print(len(rl.chain()))
    except:
        print('connection error')
        break