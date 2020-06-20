

#user input
#-Name & Description
#-Length of task
#-Importance of task
#-Time slots for eating, waking up 
#-Time slots for liesure 
#-Deadline
#-Time slot override (time & date)

#check if it is interger
def checkInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
def userInputLength(length):
    #length recived as a string, convert to int
    #in minutes
    if checkInt(length) == True:
        return int (length)
    else:
        return "enter a valid task length"

def userInputImportance(importance):
    #this is a string, convert to int
    #from 1-100 
    if checkInt (importance) == True:
        if int(importance) <= 100:
            return int(importance)
    else:
        return "enter a valid importance between 1-100"

def getTimeInMin(item):
    hoursToMin = int((item[:2])) * 60
    extraMin = int((item[2:]))
    totalTimeInMin = hoursToMin + extraMin
    return (totalTimeInMin)
            
def userInputSetAllocation(alloTimeList):
    #this is a list of times already allocated in string
    #[wakeup,sleep,[breakfastStart, breakfastEnd],[lunchStart, lunchEnd],[dinnerStart, dinnerEnd],[extraBreakStart, extraBreakEnd]]
    #returns a 4 digit interger
    parsedAlloTimeList = []
    for i in range (0,2): 
        if checkInt(alloTimeList[i]) == True:
            parsedAlloTimeList.append(getTimeInMin(alloTimeList[i]))
    for i in range(2, len(alloTimeList)):
        smallList = []
        #going to convert into [startMin, length]
        smallList.append(getTimeInMin(alloTimeList[i][0]))
        #calculate length of time
        length = getTimeInMin(alloTimeList[i][1]) - getTimeInMin(alloTimeList[i][0])
        smallList.append(length)
        parsedAlloTimeList.append(smallList)

    return parsedAlloTimeList
    
test =['0800','2100',['0830', '0900'],['1130', '1230'],['1845', '1930'],['1520', '1630']]

print(userInputSetAllocation(test))
            

    
