dateDict = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
import datetime as dt
import csv
time = dt.datetime.today().strftime('%H:%M:%S')
m = int(dt.datetime.today().strftime('%m'))
y = int(dt.datetime.today().year)
day = int(dt.datetime.today().day)
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
    
def userInputNameAndDesc(name, desc):
    #nameAndDesc is a list of 2 items
    return [name, desc]



def userInputImportance(importance):
    #this is a string, convert to int
    #from 1-100 
    if checkInt (importance) == True:
        if int(importance) <= 100:
            return int(importance)
    elif importance == '':
        return -1
    else:
        return "enter a valid importance between 1-100"
    
def userInputLength(length):
    #length recived as a string, convert to int
    #in minutes
    if checkInt(length) == True:
        return int (length)
    else:
        return "enter a valid task length"
    
def userInputTaskDeadline(taskDeadline, currentDateInMin,y):
    #given ['time', 'date', 'month', 'year']
    #time is formatted like hr:min:sec
    #convert into minutes assume not leapyear
    #find relative minutes to the current time
    time = taskDeadline[0][:2] + ":" + taskDeadline[0][2:] +":00"
    if int(taskDeadline[3]) >  y:
        deltaTime = (525600 - currentDateInMin) + getTotalTimeInMin(time,int(taskDeadline[1]), int(taskDeadline[2]))
        return deltaTime
    else:
        deltaTime = getTotalTimeInMin(time,int(taskDeadline[1]), int(taskDeadline[2])) - currentDateInMin
        return deltaTime
    
def getTimeInMin(item):
    #gets time like '1230' and converts to min relative to 00:00
    hoursToMin = int((item[:2])) * 60
    extraMin = int((item[2:]))
    totalTimeInMin = hoursToMin + extraMin
    return (totalTimeInMin)

def getTotalTimeInMin(time,day,m):
    #gets current date in mins relative to beginging of year
    totalMinsInDay = int(time[:2])*60 + int(time[3:5]) 
    totalDays = day
    for i in range (1,m):
        totalDays+= dateDict[i]

    totalMinCurrent = totalMinsInDay + totalDays*24*60

    return totalMinCurrent
    
def userInputSetAllocation(alloTimeList):
    #this is a list of times already allocated in string
    #[wakeup,sleep,[breakfastStart, breakfastEnd],[lunchStart, lunchEnd],[dinnerStart, dinnerEnd],[extraBreakStart, extraBreakEnd]]
    #returns a 4 digit string
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

def userInputOverride(override):
    if override == ['','','','']:
        return False
    else:
        return override
    
def organizedTaskInfo(data):
    organizedList = [
        userInputNameAndDesc(data[0], data[1]),
        userInputImportance(data[2]),
        userInputLength(data[3]),
        userInputTaskDeadline(data[4],getTotalTimeInMin(time,day,m),y),
        userInputOverride(data[5])
        ]
    

def writeToCsv(taskInfo):
    with open ("csvOfTasks.csv", "a") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(taskInfo)

def main(data):
    print("s")
    writeToCsv(organizedTaskInfo(data))
    print("ss")


            

    
