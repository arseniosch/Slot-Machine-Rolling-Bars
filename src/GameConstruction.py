from Main import *
import random
import numpy as np
import pandas as pd

def createReels():
    #USE THE PANDAS LIBRARY TO COLLECT THE DATA OF REELS FROM CSV FILE
    data_frame = pd.read_csv("data_slots.csv", header=None) # since you didn't specify header in your question  
    #INSERT THE DATA IN A 2D ARRAY ALL REELS SHOULD HAVE THE SAME NUMBER OF SYMBOLS
    reels = data_frame.iloc[:, :].values # [:, :] => [rows, columns]    
    return reels

def createSlotWindow(n1,n2):
    #INITILIZATION OF WINDOW THAT THE PLAYER PLAYS
    rows, cols = (n1, n2)
    SlotWindow = np.array([['symbol_00' for i in range(cols)] for j in range(rows)]) 
    return SlotWindow
    
def generateStops(reels):
    #STOPS FOR EACH REEL
    #WE GET THE NEXT 2 INDICES VERTICALLY AS ROWS
    #INITIALIZATION
    stops = [0,0,0,0,0]
    for i in range(len(stops)):
        stops[i] = random.randint(0,len(reels[0,:]))        
    return stops

def insertStopsInWindow(reels,stops,slot_window):
    for i in range(3):
        #J IS FOR THE REEL
        for j in range(5):   
            temp_j = (stops[j]+i) % len(reels[j,:])
            slot_window[i][j] = reels[j][temp_j]
    return slot_window
