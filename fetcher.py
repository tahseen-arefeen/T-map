import os
import pandas as pd
import requests
import random

'''
GLOBAL VARIABLES
'''
stop_url = "https://api-v3.mbta.com/stops"
train_url = "https://api-v3.mbta.com/vehicles"

def FetchAPI(url):
    '''
    Goes to API and gets raw data from MBTA creates data frame
    '''
    
    if url == stop_url: # see if accessing stops
        bearer_token = os.environ.get('a2d93c719b8349d0905b19cc9e250e02')
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
    
        response = requests.request("GET", url, headers=headers).json()
    
        #StopFrame
        global sf
        sf = pd.DataFrame(response['data'])
        return sf
    
    elif url == train_url: # see if accessing trains
        bearer_token = os.environ.get('a2d93c719b8349d0905b19cc9e250e02')
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
    
        response = requests.request("GET", url, headers=headers).json()
    
        #TrainFrame
        global tf
        tf = pd.DataFrame(response['data']) 
        return tf
        
def FindStation(train_id):
    tf_index = int((tf[tf["id"]==train_id].index.values))
    relationships = tf.iloc[tf_index,3]
    stop = relationships.get("stop")
    
    data = stop.get("data")
    stop_id = data.get("id")
    
    stop_index = int((sf[sf["id"]==stop_id].index.values))
    attributes = sf.iloc[stop_index,0]

    platform_name = attributes.get('name')
    
    return platform_name

def FindDirectionId(train_id):
    '''
    Find if train is inbound (0) or outbound (1)
    '''
    index = int((tf[tf["id"]==train_id].index.values))
    attributes = tf.iloc[index,0]
    
    id = attributes.get('direction_id')
    return(id)

def FindStatus(train_id):
    index = int((tf[tf["id"]==train_id].index.values))
    attributes = tf.iloc[index,0]
    
    status = attributes.get('current_status')
    return(status)

def FindLat(train_id):
    index = int((tf[tf["id"]==train_id].index.values))
    attributes = tf.iloc[index,0]
    
    lat = attributes.get('latitude')
    return(lat)

def FindLong(train_id):
    index = int((tf[tf["id"]==train_id].index.values))
    attributes = tf.iloc[index,0]
    
    long = attributes.get('longitude')
    return(long)

class trouble_shoot():
    def __init__(self):
        pass
    
    def TestFetchAPI(self):
        try:
            tf = FetchAPI(train_url)
            print(tf)
            print("Train Frame Online")
        except:
            print("Train Frame Fail")
        
        try:
            sf = FetchAPI(stop_url)
            print(sf)
            print("Stop Frame Online")
        
        except:
            print("Stop Frame Fail")

    def TestFindAttribute(self,train_id):
        tf = FetchAPI(train_url)
        sf = FetchAPI(stop_url)
        lines = ["Green","Orange","Red","Blue"]
        condition = True
        
        TOI = []
        
        if train_id == None:
            for i in range(len(lines)):
                while condition is True:
                    index = random.randint(0,len(tf)-1)
                    id = tf.iloc[index,1]
        
                    if lines[i] == "Green" and id[0] == "G":
                        TOI.append(id)
                        break
                    elif lines[i] == "Orange" and id[0] == "O":
                        TOI.append(id)
                        break
                    elif lines[i] == "Red" and id[0] == "R":
                        TOI.append(id)
                        break
                    elif lines[i] == "Blue" and id[0] == "B":
                        TOI.append(id)
                        condition = False
                        break
            
            for i in range(len(TOI)):
                print(TOI[i])
                
                try:
                    print(FindDirectionId(TOI[i]))
                except:
                    print("FindDirectionId Fail")
                
                try:
                    print(FindStatus(TOI[i]))
                except:
                    print("FindStatus Fail")
                    
                try:
                    print(FindStation(TOI[i]))
                except:  
                    print("FindStation Fail")
                
                try:
                    print(FindLat(TOI[i]),FindLong(TOI[i]))
                except:
                    print("FindLat or FindLong Fail")
                
                print()

        else:
            print(train_id)
                
            try:
                print(FindDirectionId(train_id))
            except:
                print("FindDirectionId Fail")
                
            try:
                print(FindStatus(train_id))
            except:
                print("FindStatus Fail")
                    
            try:
                print(FindStation(train_id))
            except:  
                print("FindStation Fail")
                
            try:
                print(FindLat(train_id),FindLong(train_id))
            except:
                print("FindLat or FindLong Fail")
                
            print()
                    
                
            
test = trouble_shoot()
#test.TestFetchAPI()
#test.TestFindAttribute(None)