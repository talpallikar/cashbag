#bags.py
import random
import os

#Constants
BAGNUM = 14  #Number of bags 
CASHVAL = 1  #The value of cash in each bag. This is not that important.

HISTORY = [] 

class Bag:
#Bags have an identifying number. They can be empty or full of cash. 

    bagCount = 0
    totalCash = 0

    def __init__(self, num, cash, ):
        self.num = num
        self.cash = cash
        Bag.bagCount += 1

    def displayCount(self):
        print "Total Bags: %d" % Bag.bagCount

    def displayBag(self):
        print "Bag Number: ", self.num,  ", Has Cash?: ", self.cash

    def displayBagPile(self):
        print "Bag Number: ", self.num,  ", Has Cash?: ", self.cash,  ", Cash Pile?: ", self.pile

    def displayCash(self):
        print "Total Cash: %d" % Bag.totalCash   

def populate_bags():
    bagCollection = []
    for x in range (0,BAGNUM):
        k = bool(random.getrandbits(1))
        b = Bag(x,k)
        bagCollection.append(b)
  
    return bagCollection

def process_bag(currentBag,group):
    temp1 = 0
    temp2 = 0
    for x in range(currentBag+1,BAGNUM):
        group[x].displayBag()
        temp2+=1
        if group[x].cash:
            temp1+=1
    print str(temp1) + " out of "+str(temp2)+" checked bags have cash"
        
    while True:
        user_input = raw_input("Does bag: "+str(currentBag)+ " have cash? (Y/N)")
        if user_input in ['Y', 'N']:
            break
        else:
            print('That is not a valid option!')
    if user_input == 'Y':
        group[currentBag].pile = True
    else:
        group[currentBag].pile = False
    #clear screen
    global HISTORY
    HISTORY.append(user_input)
    clear = lambda: os.system('cls')
    clear()
    print "History: "+ str(HISTORY)
    print("")

def score_bags(group):
    yescash = 0 #counts cash bags in cash pile
    nocash = 0  # counts cash bags in empty pile
    yesempty = 0 #counts empty bags in cash pile
    noempty = 0 #counts empty bags in empty pile
    truecash = 0 #counts bags with cash
    trueempty = 0 #counts empty
    for x in range(0,BAGNUM):
        if group[x].cash == True:
            truecash+=1
            if group[x].pile:
                Bag.totalCash += CASHVAL
                yescash+=1
            else:
                nocash+=1
        if group[x].cash == False:
            trueempty+=1
            if group[x].pile:
                yesempty+=1
                Bag.totalCash -= CASHVAL
            else:
                noempty+=1 
    print ("There were " + str(truecash) +" bags with money and " + str(trueempty) +" empty bags")
    print ("Your distribution: ")              
    print ("Money Pile: " + str(yescash) + " Full Bags, " + str(yesempty)+" Empty Bags")
    print ("Empty Pile: " + str(nocash) + " Full Bags, " + str(noempty)+" Empty Bags")
    print ("Game Complete. " + "Money Made: " + str(Bag.totalCash))

def main():
    group = populate_bags()
    for x in range(0,BAGNUM):
        process_bag(x,group)
    for x in range(0,BAGNUM):
        group[x].displayBagPile()
    score_bags(group)

main()