# Choose the lottery numbers
# lottery.py by Ronald Adomako July 7, 2016
# edited & modified by A. Alan Browning II April 21, 2025

from itertools import combinations #p, r r-length tuples, in sorted order, no repeated elements
import string
import timeit
start_time = timeit.default_timer()

class lotteryDatabase:
    def __init__(self):       
        self.histBallCount = [0]*69
        self.histPowerballCount = [0]*26
        self.pool = list(combinations(list(range(1,70)),5))
        self.optPool = [] #suggested main draws
        self.optPowerball = [0]*26 #suggested powerballs
        self.played = []#pool of played tickets
         
    def genHistDraw(self, draws):
        
        for line in draws:
            line = line.strip()
            date, *nums = line.split() #python 3
            
            powerball = int(nums[5])#tally powerball 1 through 26
            self.histPowerballCount[powerball-1]+=1
            
            for i in range(5):
                ball = int(nums[i])
                self.histBallCount[ball-1]+=1 #tally balls since 10/07/2015      
        return

    def pickPowerball(self):
            
        tal = self.histPowerballCount
        minPowerball = []
        minPBCount = []
        for index in range(26):       
            ballCount = min(tal)
            minPBCount.append(ballCount)
            minPowerball.append({tal.index(ballCount)+1: ballCount})
            tal[tal.index(ballCount)] = 1000 #place holder assuming each tally <1000
        picks = 3
        self.optPowerball = minPowerball[:picks]
        while (len(self.optPowerball) < 27 and minPBCount[picks-1] == minPBCount[picks]):
            picks+=1
            self.optPowerball = minPowerball[:picks]
        return self.optPowerball

    def pickDrawing(self):#tally of least 5 picked balls
        tal = self.histBallCount
        minDraws = []
        for count in range(69):
            minTal = min(tal)
            ball = tal.index(minTally)+1 #ball draw corresponding to count
            d=dict()
            d[ball]= minTal
            minDraws.append(d)
            tal[ball-1]=1000 #place holder for indices for all tallies <1000
        picks = 5
        self.optPool = minDraws[:picks]
        while minDraws[picks][list(minDraws[picks].keys())[0]] == minDraws[picks-1][list(minDraws[picks-1].keys())[0]]:
            picks+=1
            self.optPool = minDraws[:picks]
            if picks == 70:#in the case that all the balls are uniform
                break
        return self.optPool

def main():
    print('Your calculation for generating wins is running.')
    lot = lotteryDatabase()
    tal = open('powerball.txt','r')
    lot.genHistDraw(tal)
    print ('These are your suggested balls :with tally', lot.pickDrawing())
    print ('These are your suggested power balls: with tally', lot.pickPowerball())
    draws = open('tickets.txt','r')
'''
if __name__ == 'main':
'''
main()#indent when using command line


    #history = input(lottery.txt)
   
   


