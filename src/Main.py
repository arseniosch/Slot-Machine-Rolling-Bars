from GameConstruction import *
from GameRun import *
from Printer import *
import progressbar

#WIDGETS FOR PROGRESSBAR
widgets=[
    ' [', progressbar.Timer(), '] ',
    progressbar.Bar(),
    ' (', progressbar.ETA(), ') ',
]

if __name__== "__main__":       
    #REWARD HOLDS THE TEMPORARY REWARD FOR THE SPIN
    reward = 0   
    #ONLY FOR SPINS NOT FOR SIMULATIONS (USER CAN CHANGE IT)
    coins = 100000   
    #THE TOTALBET OF PLAYER WHERE LINEBET REPRESENTS THE THE BET FOR EACH PAYLINE OF THE GAME
    linebet = 1  
    #IT IS USED FOR THE MENU (USER CAN CHANGE IT)
    choice=True       
    #REEL CREATION, IMPORT FROM CSV ALL THE REELS
    Reels = createReels()      
    #SLOT WINDOW CREATION (3X5) - INITIALIZATION
    SlotWindow = createSlotWindow(3,5)   
    while choice:
        print("=================================")
        print("||Menu || Rolling Sevens Slots ||")
        print("=================================")
        print ("1.Spin & Win!")
        print ("2.Monte Carlo Simulation")
        print ("3.Exit/Quit")
        choice=input("What would you like to do? ")             
        if choice=="1":             
            #GENERATE THE STOPS
            Stops = generateStops(Reels)         
            #GET THE RANDOM STOPS-INDICES AND INSERT THE SYMBOLS IN (3X5) SLOT WINDOW
            #THE FUNCTION RETURNS THE (3X5) SLOT WINDOW WITH THE RANDOM GENERATED STOPS
            SlotWindow = insertStopsInWindow(Reels,Stops,SlotWindow)          
            #GET THE REWARD
            reward,paylines,multiplier = runGame(SlotWindow,3,5,linebet)
            totalbet = paylines * linebet
            #EACH TIME THE PLAYER PRESS THE SPIN BUTTON HE BETS AND IT IS SUBSTRACTED FROM HIS TOTAL COINS
            coins -= totalbet        
            #ADD THE REWARD IN COINS OF PLAYER
            coins += reward*multiplier         
            #PRINT "SLOT MACHINE" WITH CURRENT STOPS
            printAll(SlotWindow,reward,coins,totalbet)
            if(multiplier==2):
                print("You won a Double Up!")  
            print("\n")             
        elif choice=="2":
            #THE NUMBER OF SPINS THAT THE SIMULATION RUNS TO GET RTP (AVG THAT PAYS BACK THE PLAYER)
            #USAGE --> ONLY FOR CHOICE 2, MONTE CARLO SIMULATION (USER CAN CHANGE IT)
            #THE MORE THE STEPS, THE MORE EXACT RTP THAT COINCIDES WITH THAT IN .XLSX FILE WHICH IS THE THEORETICAL AND EXACT
            steps = int(input("Give the number of steps (use 100k as default, but 10m => close to theoretical): "))  
            bar = progressbar.ProgressBar(max_value=steps,widgets=widgets)     
            #SUM IS USED TO CALCULATE RTP
            sum = 0       
            #CALLS MONTE CARLO SIMULATION
            for i in range(steps): 
                Stops = generateStops(Reels)       
                SlotWindow = insertStopsInWindow(Reels,Stops,SlotWindow)           
                reward,number_of_paylines,multiplier = runGame(SlotWindow,3,5,linebet)
                sum += reward*multiplier     
                bar.update(i)                                         
            print("\nRTP:",(float) (sum/(steps*number_of_paylines))*100,"%")                
        elif choice=="3":
          print("\nSee ya!") 
          choice=False          
        elif choice !="":
          print("\nNot a valid choice, please try again!") 