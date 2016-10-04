
import random
import math
def getRandInt(i, j):
    return random.randint(i, j)

class Algorithms(object):
    def __init(self, unSortedlist):
        self.list = unSortedlist


    def activitySchedule(self, start, finish, profit):
        if len(start) != len(finish) != len(profit):
            print "Check the schedule arrays"   
            return [], [], []
        n  = len(start) # total no of events
        activities = [None]*(n)
        activities[0] = 0        
        used = [None]*n #activity used for the problem
        traceBack = [None]*n #js are stored here
        for i in range(1, n):
            activities[i] = activities[i-1]
            used[i] = False
            j = i - 1    
            lower = 0
            upper = j             
            while  lower <= upper:  
                j = int(math.floor((upper + lower)/2))
                if finish[j] < start[i]:
                    lower = j + 1
                elif finish[j] > start[i]:
                    upper = j - 1
                else:
                    break
            if finish[j] > start[i]:
                j = lower - 1
            traceBack[i] = j   #store the comaptible activity wrto i in traceback  [J]                          
            if profit[i] + activities[j] > activities[i]:
                activities[i] = profit[i] + activities[j]
                used[i] = True   
        return activities, used, traceBack

    def activityScheduleSpl(self, start, finish, profit, special):
        if len(start) != len(finish) != len(profit):
            print "Check the schedule arrays"   
            return [], [], []
        n  = len(start) # total no of events
        activities, used, trace = [None]*(n),  [None]*(n),  [None]*(n)      
        activities[0] = 0      
        # used = [None]*n #activity used for the problem
        # traceBack = [None]*n #js are stored here
        for i in range(1, n):
            isSpl = special[i]
            activities[i] = activities[i-1]
            used[i] = False
            j = i - 1    

            ''''Linear Search for j'''
            while finish[j] > start[i]:
                j = j-1     

            trace[i] = k = j
            while used[k]:
                k = trace[k]
            if special[k] & special[i]:     
                k = k-1
            if special[j]:
                k-=1    
        return activities, used, traceBack

    def findSolution(self, activities, used, trace, special, size):
        
        solution = []      
        while size > 0:
            if used[size] == True:
                solution.append(size)
                size = trace[size]
            else: 
                size -= 1
        profit = activities[solution[0]]
        solution.reverse()

        splStatus = []
        for i, x in enumerate(solution):
            splStatus.append(special[x]) 

        return solution, profit, splStatus
    def findLMSequence(self, array):        
        size = len(array)
        aux = [None]*size
        length = [None]*size        
        aux [0]=0
        length[0]=0
        for i in range(1, size):     
            lst = [(0, 0)]*i
            lst[0] = (0, 0)
            for j in range (0, i):                           
                if array[j] <= array[i]:
                    lst.append((j, 1+length[j]))
            # lis,key=itemgetter(1)
            from operator import itemgetter
            index, cnt = max(lst, key=itemgetter(1))
            # index, cnt = max(lst, key=lambda item:item[1])
            length[i] = cnt
            aux[i] = index
        return aux, length

    def findAMSequence(self, array):        
        size = len(array)
        aux = [None]*size
        length = [None]*size        
        aux [0]=0
        length[0]=0
        for i in range(1, size):     
            lst = [(0, 0)]*i
            lst[0] = (0, 0)
            prev = array[i]
            for j in range (i-1, -1, -1):                                         
                if array[j] <= array[i]:
                    a = prev%2 == 0
                    b = array[j]%2 == 0
                    if (a != b):
                        prev = array[j]
                        lst.append((j, 1+length[j]))
            # index, cnt = max(lst, key=lambda item:item[1])
            from operator import itemgetter
            index, cnt = max(lst, key=itemgetter(1))
            length[i] = cnt
            aux[i] = index
        return aux, length
    def findLMSSolution(self, array):   
        
        aux, length = algos.findLMSequence(sequence)    
        # aux, length = algos.findAMSequence(array)   
        size = len(array)-1
        index, cnt = 0, 0
        while size > 0:
            if cnt < length[size]:
                cnt = length[size]                
                index = size      
            size -= 1
        subArray = []
        while index > 0:
            subArray.append(array[index])
            index = aux[index] 
        subArray.reverse()
        return subArray, len(subArray)

        

    def getRevenueArray(self, profit):         
       
        trace, revenue = [None]*len(profit), [None]*len(profit)
        revenue[0] = 0
        trace[0] = 0
        for j in range(1, len(profit)):
            # revenue[j] = -float("inf")
            revenue[j] = revenue[j-1]
            for i in range(1, j+1):# when using range, it doesnot include the last index (start, last)
                if revenue[j] < profit[i] + revenue[j-i]:
                    revenue[j] = profit[i] + revenue[j-i]
                    trace[j] = i                    
        return trace, revenue

    def getCostRevArray(self, profit, cost):            
       
        trace, revenue = [None]*len(profit), [None]*len(profit)
        revenue[0], trace[0] = 0, 0
        #j = 0
        for j in range(1, len(profit)):# when using range, it doesnot include the last index (start, last)
            revenue[j] = -float("inf")
            cutCost = 0
            for i in range(1, j+1):
                if i != j: 
                    cutCost = cost[j]
                if revenue[j] < profit[i] + revenue[j-i] - cutCost:
                    revenue[j] = profit[i] + revenue[j-i] - cutCost
                    trace[j] = i   
        return trace, revenue

    def getLimitRevArray(self, profit, limit):            
       
        trace, revenue = [None]*len(profit), [None]*len(profit)
        revenue[0], trace[0] = 0, 0
        #j = 0

        for j in range(1, len(profit)):# when using range, it doesnot include the last index (start, last)
            # revenue[j] = revenue[j-1]
            iLimit = limit[:j+1]
            revenue[j] = -float("inf")
            for i in range(1, j+1):
                left = iLimit[i]
                if revenue[j] < profit[i] + revenue[j-i]:
                    if left > 0: 
                        revenue[j] = profit[i] + revenue[j-i]
                        trace[j] = i   
                        iLimit[i] -= 1
        return trace, revenue

    def getModRevArray(self, rodSize, profit, sizes):            
       
        trace, revenue = [None]*(rodSize+1), [None]*(rodSize+1)
        revenue[0], trace[0] = 0, 0
        for j in range(1, rodSize+1):            
            revenue[j] = -float("inf")
            for i in range(1, j+1):
                if i in sizes:     
                    index = sizes.index(i)         
                    if revenue[j] < profit[index] + revenue[j-i]:
                        revenue[j] = profit[index] + revenue[j-i]
                        trace[j] = i   
        return trace, revenue
    
    

    def getRCPSolution(self, profit, cost, limit, sizes, rodSize):        
        # trace, revenues = self.getRevenueArray(profit)
        # trace, revenues = self.getCostRevArray(profit, cost)
        # trace, revenues = self.getLimitRevArray(profit, limit)
        trace, revenues = self.getModRevArray(rodSize, profit, sizes)
        size = rodSize
        netProfit = 0
        pieces = []

        while size > 0:
            cut = trace[size]
            pieces.append(cut)
            netProfit += profit[sizes.index(cut)]
            size -= cut
        # netProfit -= 1 # cost[trace[j]]
        # while size > 0:
        #     cut = trace[size]
        #     pieces.append(cut)
        #     netProfit += profit[cut]
        #     size -= cut
        #     # netProfit -= 1 # cost[trace[j]]
        return pieces, netProfit

            
    def quickSort(self, randList, p, r):
        if p >= r: return randList
        q, t, randList = self.randomizedPartition(randList, p, r)
        self.quickSort(randList, p, q-1)
        self.quickSort(randList, t+1, r)
        return randList


    def randomizedPartition(self, randList, p, r):
        i = getRandInt(p, r)
        x = randList[i]
        randList[i], randList[r] =  randList[r], randList[i]
        i = p-1
        t = r
        j = p
        while j < t:
            if randList[j] < x:
                i+=1
                randList[i], randList[j] = randList[j], randList[i]
            elif randList[j] == x:
                t -= 1
                randList[j], randList[t]  = randList[t], randList[j]
                j -= 1
            j += 1
        z = i+1
        k = 0
        while k < r-t+1:
            randList[z+k], randList[t+k] = randList[t+k], randList[z+k]
            k += 1

        #randList[i+1], randList[r] =  randList[r], randList[i+1]
        return [i+1, i+1 + r-t, randList]






#crudeList = [2, 3, 36, 4, 12, 5, 44, 7, 66, 8, 10, 9, 1, 30]
crudeList = [2, 3, 4, 6,3, 6,4, 3]
#crudeList = [2, 3, 4, 6,3, 6,4, 3, 7, 8,2,1 ,7, 9, 3, 4, 6,6, 7, 8, 9, 10,3,5,11,4,5] # for QuickSort
algos = Algorithms()

""" rod cutting problem"""
profit = [0, 1, 6, 9, 10, 13, 17, 17, 20, 24, 28]
cost   = [0, 0, 1, 1, 2,  2,  2,  3,  3,  3,  4]
limit =  [0, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
testProfit = [0, 1, 5, 8, 10, 14, 17, 17, 20, 24, 26]#[(2, 2, 6) - 27]


sizes = [0, 2, 3, 5, 7, 10]
modProfit = [0, 5, 8, 10, 17, 23]#[(3, 7) 10]


print algos.getRCPSolution(modProfit, cost, limit, sizes, 10)
# sequence = [0, 7, 9, 12, 3, 5, 6, 8, 4, 15, 9]
# testSequence = [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# t2Seq = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print algos.findLMSSolution(sequence)


# start = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
# finish = [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# profit = [0, 3, 2, 6, 2, 5, 4, 4, 3, 4, 11, 2]
# special = [False, True, False, False, True, False, True, True, False, False, True,  True]
# dummy  =  [ 0,     1,      2,     3,    4,    5,     6,    7,     8,     9,     10,   11]
# a, use, j = algos.activitySchedule(start, finish, profit)
# a, use, j = algos.activityScheduleSpl(start, finish, profit, special)

# print algos.findSolution(a, use, j, special, len(start)-1)
# print algos.findSolution(a, use, j, len(start)-1)