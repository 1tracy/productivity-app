dateDict = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
setTimeList = []
import datetime as dt
import csv
import random

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
def countingSort(aList):
    #find max importance/time
    temp = []
    for item in aList:
        temp.append(aList[5])

    #create the key or counting array based on max value in list
    key = []
    for i in range(0, max(temp) + 1):
        key.append(0)

    #iterate through given list and increase counters of key
    #for each element in list
    for num in aList:
        #increase the respective counter by 1
        key[num[5]] += 1


    #create a new list with values in sorted order based on couters of key
    sortedList = []
    #for each counter, starting from smallest key
    for i in range(0, len(key)):
        counter = key[i]

        #while counter is non-zero
        while(counter > 0):
            #restore element to list
            sortedList.append(i)
            #decrease counter by 1
            counter -= 1

    return sortedList

def getNextDay():
    pass
def getTaskNames():
    """
    return a list of task names from CSV
    """
    with open ("csvOfTasks.csv", "r") as csvFile:
        readCSV = csv.reader(csvFile, delimiter=',')
        taskNames = []
        for row in readCSV:
            taskNames.append(row[0][0])
        return taskNames

def getDataFromCSV(task_name):
    """
    return list from CSV for task name specifically
    """
    with open ("csvOfTasks.csv", "r") as csvFile:
        readCSV = csv.reader(csvFile, delimiter=',')
        for row in readCSV:
            if row[0][0] == task_name:
                return row
            else:
                return "task not found"
    


def deleteTask(task_name):
    """
    delete task from CSV given task name
    """
    with open ("csvOfTasks.csv") as csvFile:
        readCSV = csv.reader(csvFile, delimiter=',')
        writer = csv.writer(csvFile)
        for row in readCSV:
            if row[0][0] == task_name:
                writer.writerow(row)
            else:
                return "task name not found"


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
    print(item)
    #gets time like '1230' and converts to min relative to 00:00
    hoursToMin = int((item[:2])) * 60
    extraMin = int((item[2:]))
    totalTimeInMin = hoursToMin + extraMin
    print(totalTimeInMin)
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
    for i in range (0,1): 
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

    setTimeList = parsedAlloTimeList #[startmin, endmin....]

def userInputOverride(override):
    if override == ['','','','']:
        return False
    else:
        return override
    
def organizedTaskInfo(data):
    print(data)
    organizedList = [
        userInputNameAndDesc(data[0], data[1]),
        userInputImportance(data[2]),
        userInputLength(data[3]),
        userInputTaskDeadline(data[4],getTotalTimeInMin(time,day,m),y),
        userInputOverride(data[5]),
        int(round(userInputImportance(data[2])/userInputLength(data[3])))
        ]
    print(organizedList)
    return organizedList


def writeToCsv(taskInfo):
    print(taskInfo)
    with open ("csvOfTasks.csv", "a") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(taskInfo)


def countingSort(aList):
    #find max importance/time
    print(aList)
    temp = []
    for item in aList:
        print("printing item")
        print(item)
        temp.append(int(item[5]))
        
    #create the key or counting array based on max value in list
    key = []
    for i in range(0, max(temp) + 1):
        key.append(0)

    #iterate through given list and increase counters of key
    #for each element in list
    for num in aList:
        #increase the respective counter by 1
        key[int(num[5])] += 1


    #create a new list with values in sorted order based on couters of key
    sortedList = []
    #for each counter, starting from smallest key
    for i in range(0, len(key)):
        counter = key[i]

        #while counter is non-zero
        while(counter > 0):
            #restore element to list
            sortedList.append(i)
            #decrease counter by 1
            counter -= 1

    return sortedList

def convertMinIntoTime(mins):
    hour = mins//60
    minute = mins%60
    return f'{hour}:{minute}'
        
def gatherAllTasks():
    """
    Gathers all the tasks into a big list
    """
    bigList = []

    with open ("csvOfTasks.csv") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            bigList.append(row)
    return bigList
    
    
def generateSchedule():
    """
    Generates the weekly schedule
    """
    minutesInDayCount = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    allTasksList = gatherAllTasks()
    organizedListRatioBased = countingSort(allTasksList)
    weeklySchedule = []
    if len(setTimeList) == 0:
        for i in range (0,6):
            weeklySchedule.append([])
            
        for item in allTasksList:
            if item[4] != False:
                weeklySchedule[int(item[4][1]) - day -1].append([item[0],item[4]]) #[walk dog,["1230","3","10,"2020"]
            else:
                pass

        totalSetTime = 0
        count = 0        
        for item in allTasksList:
            if item[4] == False:
                if count <=6:
                    if (minutesInDayCount[count] + item[2] + totalSetTime) <=(endTime-startTime):
                        weeklySchedule[count].append([item[0],item[2]])
                        minutesInDayCount[count] += item[2]
                    else:
                        count += 1
        for item in weeklySchedule:
            item.append(["Breakfast", setTimeList[2]],
                        ["Lunch",setTimeList[3]],
                        ["Dinner", setTimeList[4]],
                        ["Extra Break", setTimeList[5]]
                        )
            
        return weeklySchedule
    
    else:
        startTime = setTimeList[0]
        endTime = setTimeList[1]
        
        for i in range (0,6):
            weeklySchedule.append([])
            
        for item in allTasksList:
            if item[4] != False:
                weeklySchedule[int(item[4][1]) - day -1].append([item[0],item[4]]) #[walk dog,["1230","3","10,"2020"]

        totalSetTime = setTimeList[2][1] + setTimeList[3][1] + setTimeList[4][1] + setTimeList[5][1]
        count = 0        
        for item in allTasksList:
            if item[4] == False:
                if count <=6:
                    if (minutesInDayCount[count] + item[2] + totalSetTime) <=(endTime-startTime):
                        weeklySchedule[count].append([item[0],item[2]])
                        minutesInDayCount[count] += item[2]
                    else:
                        count += 1
        for item in weeklySchedule:
            item.append(["Breakfast", setTimeList[2]],
                        ["Lunch",setTimeList[3]],
                        ["Dinner", setTimeList[4]],
                        ["Extra Break", setTimeList[5]]
                        )
            
        return weeklySchedule
                    
                                
    
    
def main(data):
    print("s")
    writeToCsv(organizedTaskInfo(data))
