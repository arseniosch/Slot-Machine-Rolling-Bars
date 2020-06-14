import numpy as np
import random

paylines = np.array([  [0,0,0,0,0],   
                       [1,1,1,1,1],
                       [2,2,2,2,2],   
                       [0,1,2,1,0],
                       [2,1,0,1,2],   
                       [0,0,1,2,2],
                       [2,1,1,1,0],   
                       [1,2,2,2,1],
                       [1,0,0,0,1],   
                       [2,2,1,0,0] ])
#USER CAN CHANGE IT
paytable = np.array([  [0,2,4,20,40],
                       [0,2,4,20,40],
                       [0,0,5,75,150],
                       [0,0,5,75,150],
                       [0,0,12,120,200],
                       [0,0,12,120,200],
                       [0,2,5,50,500],
                       ])
#EACH KEY OF THIS DICTIONARY IS THE INDEX TO PAYTABLE (THE PAYMENT OF THIS SYMBOL)
symbols = {            0: "symbol_01",
                       1: "symbol_02",
                       2: "symbol_03",
                       3: "symbol_04",
                       4: "symbol_05",
                       5: "symbol_06",
                       6: "sym_scatt"
                       }

def runGame(slot_window,n_rows,n_reels,linebet): 
    totalbet = len(paylines) * linebet
    index = 0
    payment = 0  
    #LINE RULE : FIND PAYMENT
    for i in range(len(paylines)):
        n_comb=0;         			
        if(slot_window[paylines[i][0]][0]!='sym_scatt'):
            #5 OUT OF 5
            if(slot_window[paylines[i][0]][0]==slot_window[paylines[i][1]][1] and slot_window[paylines[i][1]][1]==slot_window[paylines[i][2]][2] and slot_window[paylines[i][2]][2]==slot_window[paylines[i][3]][3] and slot_window[paylines[i][3]][3]==slot_window[paylines[i][4]][4]):		    		
                n_comb = 4
            #4 OUT OF 5
            elif(slot_window[paylines[i][0]][0]==slot_window[paylines[i][1]][1] and slot_window[paylines[i][1]][1]==slot_window[paylines[i][2]][2] and slot_window[paylines[i][2]][2]==slot_window[paylines[i][3]][3]):		    		
                n_comb = 3
            #3 OUT OF 5
            elif(slot_window[paylines[i][0]][0]==slot_window[paylines[i][1]][1] and slot_window[paylines[i][1]][1]==slot_window[paylines[i][2]][2]):		    		
                n_comb = 2
            #2 OUT OF 5    
            elif(slot_window[paylines[i][0]][0]==slot_window[paylines[i][1]][1]):		    		
                n_comb = 1
        if(n_comb>0):    
            index = getKeyGivenValue(slot_window[paylines[i][0]][0])
            payment += linebet*paytable[index][n_comb]

    #EACH INDEX REPRESENTS THE REEL AND THE NUMBER REPRESENTS HOW MANY SCATTER THERE ARE ON THIS REEL
    scatter_counters = [0,0,0,0,0]     
    #SCREEN RULE : FIND PAYMENT (SCATTER SYMBOL)
    #e.g. of an output [3 1 2 3 1]
    scatter_comb = 0
    payment_sc = 0  
    mult_scatter = 1 
    for i in range(n_reels):
        for j in range (n_rows):
            if(slot_window[j][i]=="sym_scatt"):
                scatter_counters[i] += 1
        if(scatter_counters[i]>0):
             mult_scatter *= scatter_counters[i]
             scatter_comb += 1                   
    if(scatter_comb>0):    
        index = getKeyGivenValue("sym_scatt")
        payment_sc += paytable[index][scatter_comb-1]
    multiplier = 1
    #CALLING A MINI GAME THAT CAN DOUBLE YOUR PAYMENT
    #IF YOU WANT TO HAVE THE BONUS GAME REMOVE #
    #ELSE LET IT BE
    #multiplier = miniGame(scatter_comb)
    return (payment + payment_sc*mult_scatter*totalbet),len(paylines),multiplier
                            
def miniGame(scatter_comb):
    mult = 1 
    if(scatter_comb>=2):
        if(isDoubleMoney()):
            mult = 2
    return mult

def getKeyGivenValue(search_symbol_name):
    for index, symbol_name in symbols.items():
        if symbol_name == search_symbol_name:
            return index

def isDoubleMoney():
    if(random.uniform(0, 1)>0.5):
        return True			
    else:
        return False		