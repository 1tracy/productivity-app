import tkinter as tk
import csv
import datetime as dt
from main import *


class MainApplication(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        self._day = 0
        
        self.dateVar = tk.StringVar()
        self.dateLabel = tk.Label(self, textvariable=self.dateVar, font=("Verdana", 10)).grid(row=1, columnspan=3)
        self.getdate()

        self.scheduleVar = tk.StringVar()
        self.scheduleVar.set("Today's Schedule\n")
        self.scheduleMessage = tk.Message(self, textvariable=self.scheduleVar,bg="white", width=100, font=("Verdana", 15)).grid(row=2, rowspan=4, columnspan=3)
        self.nextDayButton = tk.Button(self, text=">>", width=10, command=self.nextDay, font=("Verdana", 10)).grid(row=6, column=2)

        self.addNewTaskButton = tk.Button(self, text="Add New Task", width=20, command=self.addNewTask, font=("Verdana", 10)).grid(row=3, column=3)
        self.editNewTaskButton = tk.Button(self, text="Edit Task", width=20, command=self.editTask, font=("Verdana", 10)).grid(row=4, column=3)
        self.deleteTaskButton = tk.Button(self, text="Delete Task", width=20, command=self.deleteTask, font=("Verdana", 10)).grid(row=5, column=3)
        self.addBusyTimeButton = tk.Button(self, text="Add Busy Time", width=20, command=self.addBusyTime, font=("Verdana", 10)).grid(row=6, column=3)

        #self.printSchedule()
        
        self.pack()

    def printSchedule(self):
        """
        print schedule
        """
        schedule = generateSchedule()
        tempstring = ''
        for i in range(len(schedule[self._day])):
            tempstring = tempstring + schedule[self._day][i][0] + schedule[self._day][i][1] + "\n"
        #print(schedule[self._day])
        #self.scheduleVar.set(tempstring)
        
    def addBusyTime(self):
        """
        add time where events cannot be scheduled
        """
        self.newWindow = tk.Toplevel(self)
        AddBusyTimeFrame(self)
    def addNewTask(self):
        """
        open "add new task" window and update schedule
        """
        self.newWindow = tk.Toplevel(self)
        AddNewTaskFrame(self)

    def editTask(self):
        """
        open "edit existing task" window and update schedule
        """
        self.newWindow = tk.Toplevel(self)
        EditTaskFrame(self)

    def deleteTask(self):
        """
        open "delete task" window, select task from dropdown menu to delete
        """
        print("deleteTask")
        self.newWindow = tk.Toplevel(self)
        DeleteFrame(self)
        
    def nextDay(self):
        """
        updates calendar to next day
        """
        print("nextDay")
        self._day += 1
        self.printSchedule()
        
    def getdate(self):
        """
        get date from datetime function
        format: hours:minutes month date[st/nd/rd/th], year
        """
        f = ''
        months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        day = str(dt.datetime.today().day)
        if len(day)== 1:
            if day == 1:
                f = 'st'
            elif day == 2:
                f = 'nd'
            elif day == 3:
                f = 'rd'
            else:
                f = 'th'
        else:
            if day[1:] == 1:
                f = 'st'
            elif day[1:] == 2:
                f = 'nd'
            elif day[1:] == 3:
                f = 'rd'
            else:
                f = 'th'
        self._time = dt.datetime.today().strftime('%H:%M:%S')
        self._m = int(dt.datetime.today().strftime('%m'))
        self._y = str(dt.datetime.today().year)
        formatted = ("It is "+self._time+", "+months[self._m]+" "+day+f+" "+self._y)

        self.dateVar.set(formatted)
        def _gettime(self):
            return self._time
        def _getm(self):
            return str(self._m)
        def _gety(self):
            return self._y
        
class AddNewTaskFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master.newWindow)
        self.master = master

        self.nameVar = tk.StringVar()
        self.nameLabel = tk.Label(self, text="Name: ", font=("Verdana", 10)).grid(row=1, column=1)
        self.nameEntry = tk.Entry(self, textvariable=self.nameVar, font=("Verdana", 10), width=50).grid(row=1, column=2, columnspan=4)

        self.descVar = tk.StringVar()
        self.descLabel = tk.Label(self, text="Description: ", font=("Verdana", 10)).grid(row=2, column=1)
        self.descEntry = tk.Entry(self, textvariable=self.descVar, font=("Verdana", 10), width=50).grid(row=2, column=2, columnspan=4)

        self.importanceVar = tk.StringVar()
        self.importanceLabel = tk.Label(self, text="Level Of Importance(1-100 (Least to Most)):", font=("Verdana", 10)).grid(row=3, column=1)
        self.importanceEntry = tk.Entry(self, textvariable=self.importanceVar, font=("Verdana", 10), width=50).grid(row=3, column=2, columnspan=4)

        self.lengthVar = tk.StringVar()
        self.lengthLabel = tk.Label(self, text="Task Length (minutes): ", font=("Verdana", 10)).grid(row=4, column=1)
        self.lengthEntry = tk.Entry(self, textvariable=self.lengthVar, font=("Verdana", 10), width=50).grid(row=4, column=2, columnspan=4)

        self.deadlineTimeVar = tk.StringVar()
        self.deadlineDayVar = tk.StringVar()
        self.deadlineMonthVar = tk.StringVar()
        self.deadlineYearVar = tk.StringVar()
        
        self.deadlineLabel = tk.Label(self, text="Deadline: ", font=("Verdana", 10)).grid(row=5, column=1)
        self.deadlineTimeEntry = tk.Entry(self,textvariable=self.deadlineTimeVar, font=("Verdana", 10)).grid(row=5, column=2)
        self.templabel = tk.Label(self, text="24 hour format due date", font=("Verdana", 10)).grid(row=6, column=2)
        self.deadlineDayEntry = tk.Entry(self, width=10,textvariable=self.deadlineDayVar, font=("Verdana", 10)).grid(row=5, column=3)
        self.templabel = tk.Label(self, text="Day", font=("Verdana", 10)).grid(row=6, column=3)
        self.deadlineMonthEntry = tk.Entry(self, width=10,textvariable=self.deadlineMonthVar, font=("Verdana", 10)).grid(row=5, column=4)
        self.templabel = tk.Label(self, text="Month", font=("Verdana", 10)).grid(row=6, column=4)
        self.deadlineYearEntry = tk.Entry(self, width=10, textvariable=self.deadlineYearVar, font=("Verdana", 10)).grid(row=5, column=5)
        self.templabel = tk.Label(self, text="Year", font=("Verdana", 10)).grid(row=6, column=5)

        self.overrideTimeVar = tk.StringVar()
        self.overrideDayVar = tk.StringVar()
        self.overrideMonthVar = tk.StringVar()
        self.overrideYearVar = tk.StringVar()

        self.overrideLabel = tk.Label(self, text="Time Slot Override: ", font=("Verdana", 10)).grid(row=7, column=1)
        self.overrideTimeEntry = tk.Entry(self, textvariable=self.overrideTimeVar, font=("Verdana", 10)).grid(row=7, column=2)
        self.templabel = tk.Label(self, text="24 hour format due date", font=("Verdana", 10)).grid(row=8, column=2)
        self.overrideDayEntry = tk.Entry(self, textvariable=self.overrideDayVar, font=("Verdana", 10), width=10).grid(row=7, column=3)
        self.templabel = tk.Label(self, text="Day", font=("Verdana", 10)).grid(row=8, column=3)
        self.overrideMonthEntry = tk.Entry(self, textvariable=self.overrideMonthVar, font=("Verdana", 10), width=10).grid(row=7, column=4)
        self.templabel = tk.Label(self, text="Month", font=("Verdana", 10)).grid(row=8, column=4)
        self.overrideYearEntry = tk.Entry(self, textvariable=self.overrideYearVar, font=("Verdana", 10), width=10).grid(row=7, column=5)
        self.templabel = tk.Label(self, text="Year", font=("Verdana", 10)).grid(row=8, column=5)

        self.cancelButton = tk.Button(self, text="Cancel", command=self.closeWindow, width=10, font=("Verdana", 10)).grid(row=9, column=1)
        self.saveButton = tk.Button(self, text="Save", command=self.saveChanges, width=10, font=("Verdana", 10)).grid(row=9, column=5)


        self.pack()
    def completed(self):
        """
        if name and task length is filled out
        """
        if self.nameVar.get() != "" and self.lengthVar.get() != "":
            return True
        return False
    def closeWindow(self):
        self.master.newWindow.destroy()
    def saveChanges(self):
        """
        send data from get_data to write csv fcn in main py file
        """
        print("savechanges")
        if self.completed():
            print("Ee")
            main(self.get_data())
            self.master.printSchedule()
            self.closeWindow()
        
        
    #getter functions
    def get_data(self):
        temp = []
        temp.append(self.nameVar.get())
        temp.append(self.descVar.get())
        temp.append(self.importanceVar.get())
        temp.append(self.lengthVar.get())
        temp2 = [self.deadlineTimeVar.get(), self.deadlineDayVar.get(), self.deadlineMonthVar.get(), self.deadlineYearVar.get()]
        temp.append(temp2)
        temp3 = [self.overrideTimeVar.get(), self.overrideDayVar.get(), self.overrideMonthVar.get(), self.overrideYearVar.get()]
        temp.append(temp3)
        return temp

class EditTaskFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master.newWindow)
        self.master = master

        self.anameVar = tk.StringVar()
        self.anameLabel = tk.Label(self, text="Name: ", font=("Verdana", 10)).grid(row=1, column=1)
        #self.tasklist = getTaskNames()
        self.tasklist = ['task 1', 'task 2', 'task 3', 'task 4']
        self.anameEntry = tk.OptionMenu(self, self.anameVar, font=("Verdana", 10), width=50, *self.tasklist).grid(row=1, column=2, columnspan=4)

        if self.anameVar in self.tasklist:
            self.updateWithSaved()
        
        self.adescVar = tk.StringVar()
        self.adescLabel = tk.Label(self, text="Description: ", font=("Verdana", 10)).grid(row=2, column=1)
        self.adescEntry = tk.Entry(self, textvariable=self.adescVar, font=("Verdana", 10), width=50).grid(row=2, column=2, columnspan=4)

        self.aimportanceVar = tk.StringVar()
        self.aimportanceLabel = tk.Label(self, text="Level Of Importance(1-100 (Least to Most)):", font=("Verdana", 10)).grid(row=3, column=1)
        self.aimportanceEntry = tk.Entry(self, textvariable=self.aimportanceVar, font=("Verdana", 10), width=50).grid(row=3, column=2, columnspan=4)

        self.alengthVar = tk.StringVar()
        self.alengthLabel = tk.Label(self, text="Task Length (minutes): ", font=("Verdana", 10)).grid(row=4, column=1)
        self.alengthEntry = tk.Entry(self, textvariable=self.alengthVar, font=("Verdana", 10), width=50).grid(row=4, column=2, columnspan=4)

        self.adeadlineTimeVar = tk.StringVar()
        self.adeadlineDayVar = tk.StringVar()
        self.adeadlineMonthVar = tk.StringVar()
        self.adeadlineYearVar = tk.StringVar()
        
        self.adeadlineLabel = tk.Label(self, text="Deadline: ", font=("Verdana", 10)).grid(row=5, column=1)
        self.adeadlineTimeEntry = tk.Entry(self,textvariable=self.adeadlineTimeVar, font=("Verdana", 10)).grid(row=5, column=2)
        self.atemplabel = tk.Label(self, text="24 hour format due date", font=("Verdana", 10)).grid(row=6, column=2)
        self.adeadlineDayEntry = tk.Entry(self, width=10,textvariable=self.adeadlineDayVar, font=("Verdana", 10)).grid(row=5, column=3)
        self.atemplabel = tk.Label(self, text="Day", font=("Verdana", 10)).grid(row=6, column=3)
        self.adeadlineMonthEntry = tk.Entry(self, width=10,textvariable=self.adeadlineMonthVar, font=("Verdana", 10)).grid(row=5, column=4)
        self.atemplabel = tk.Label(self, text="Month", font=("Verdana", 10)).grid(row=6, column=4)
        self.adeadlineYearEntry = tk.Entry(self, width=10, textvariable=self.adeadlineYearVar, font=("Verdana", 10)).grid(row=5, column=5)
        self.atemplabel = tk.Label(self, text="Year", font=("Verdana", 10)).grid(row=6, column=5)

        self.aoverrideTimeVar = tk.StringVar()
        self.aoverrideDayVar = tk.StringVar()
        self.aoverrideMonthVar = tk.StringVar()
        self.aoverrideYearVar = tk.StringVar()

        self.aoverrideLabel = tk.Label(self, text="Time Slot Override: ", font=("Verdana", 10)).grid(row=7, column=1)
        self.aoverrideTimeEntry = tk.Entry(self, textvariable=self.aoverrideTimeVar, font=("Verdana", 10)).grid(row=7, column=2)
        self.atemplabel = tk.Label(self, text="24 hour format due date", font=("Verdana", 10)).grid(row=8, column=2)
        self.aoverrideDayEntry = tk.Entry(self, textvariable=self.aoverrideDayVar, font=("Verdana", 10), width=10).grid(row=7, column=3)
        self.atemplabel = tk.Label(self, text="Day", font=("Verdana", 10)).grid(row=8, column=3)
        self.aoverrideMonthEntry = tk.Entry(self, textvariable=self.aoverrideMonthVar, font=("Verdana", 10), width=10).grid(row=7, column=4)
        self.atemplabel = tk.Label(self, text="Month", font=("Verdana", 10)).grid(row=8, column=4)
        self.aoverrideYearEntry = tk.Entry(self, textvariable=self.aoverrideYearVar, font=("Verdana", 10), width=10).grid(row=7, column=5)
        self.atemplabel = tk.Label(self, text="Year", font=("Verdana", 10)).grid(row=8, column=5)

        self.acancelButton = tk.Button(self, text="Cancel", command=self.closeWindow, width=10, font=("Verdana", 10)).grid(row=9, column=1)
        self.asaveButton = tk.Button(self, text="Save", command=self.saveChanges, width=10, font=("Verdana", 10)).grid(row=9, column=5)
        
        self.updateWithSaved()
        self.pack()
        
    def closeWindow(self):
        self.master.newWindow.destroy()
    def saveChanges(self):
        """
        call function in other file with write to csv
        """
        print("savechanges")
        if self.completed():
           main(self.get_data())
           self.master.printSchedule()
           self.closeWindow()
    def completed(self):
        """
        if name and task length is filled out
        """
        print("completed " + self.anameVar.get() + self.alengthVar.get())
        if self.anameVar.get() != "" and self.alengthVar.get() != "":
            return True 
        return False
    def updateWithSaved(self):
        """
        call function in other file with task name receive csv information
        """
        print("update with saved")
        if self.completed:
            #biglist = getDataFromCSV(self.anameVar.get())
            #set variables to biglist indexes
            #self.anameVar.set(#)
            #self.adescVar.set(#)
            #self.aimportanceVar.set(#)
            #self.alengthVar.set(#)
            #self.adeadlineTimeVar.set(#)
            #self.adeadlineDayVar.set(#)
            #self.adeadlineMonthVar.set(#)
            #self.adeadlineYearVar.set(#)
            self.aoverrideYearVar.set("edited")

    def get_data(self):
        temp = []
        temp.append(self.nameVar.get())
        temp.append(self.descVar.get())
        temp.append(self.importanceVar.get())
        temp.append(self.lengthVar.get())
        temp2 = [self.deadlineTimeVar.get(), self.deadlineDayVar.get(), self.deadlineMonthVar.get(), self.deadlineYearVar.get()]
        temp.append(temp2)
        temp3 = [self.overrideTimeVar.get(), self.overrideDayVar.get(), self.overrideMonthVar.get(), self.overrideYearVar.get()]
        temp.append(temp3)
        return temp

class DeleteFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master.newWindow)
        self.master = master

        self.deleteLabel = tk.Label(self, text="Select Task To Delete", font=("Verdana", 10)).grid(row=1, column=1, columnspan=2)
        self.tasklist = self.getTasks()

        self.taskOptionVar = tk.StringVar()
        self.taskOptionVar.set(self.tasklist[0])
        self.taskOptionMenu = tk.OptionMenu(self, self.taskOptionVar, *self.tasklist).grid(row=2, column=1, columnspan=2)
        
        self.cancelButton = tk.Button(self, text="Cancel", command= self.closeWindow, font=("Verdana", 10)).grid(row=3, column=1)
        self.saveButton = tk.Button(self, text="Save", command=self.saveChanges, font=("Verdana", 10)).grid(row=3, column=2)
        self.pack()
    def getTasks(self):
        """
        parse csv to extract task names
        """
        #temp = main.getTaskNames() <- list format
        return (['Option1', 'Option2', 'Option3'])
    def closeWindow(self):
        self.master.newWindow.destroy()
    def saveChanges(self):
        print("savechanges")
        #deleteTask(self.taskOptionVar())
        self.master.printSchedule()
        self.closeWindow()

class AddBusyTimeFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master.newWindow)
        self.master = master

        self.wakeUpVar = tk.StringVar()
        self.wakeUpVar.set("0000")
        self.sleepVar = tk.StringVar()
        self.sleepVar.set("0000")
        self.breakfastStartVar = tk.StringVar()
        self.breakfastStartVar.set("0000")
        self.breakfastEndVar = tk.StringVar()
        self.breakfastEndVar.set("0000")
        self.lunchStartVar = tk.StringVar()
        self.lunchStartVar.set("0000")
        self.lunchEndVar = tk.StringVar()
        self.lunchEndVar.set("0000")
        self.dinnerStartVar = tk.StringVar()
        self.dinnerStartVar.set("0000")
        self.dinnerEndVar = tk.StringVar()
        self.dinnerEndVar.set("0000")
        self.breakStartVar = tk.StringVar()
        self.breakStartVar.set("0000")
        self.breakEndVar = tk.StringVar()
        self.breakEndVar.set("0000")

        self.wakeUpLabel = tk.Label(self, text="Wakeup Time", font=("Verdana", 10)).grid(row=1, column=1)
        self.wakeUpEntry = tk.Entry(self, textvariable=self.wakeUpVar, font=("Verdana", 10)).grid(row=1, column=2)
        
        self.sleepLabel = tk.Label(self, text="Sleep Time", font=("Verdana", 10)).grid(row=2, column=1)
        self.sleepEntry = tk.Entry(self, textvariable=self.sleepVar, font=("Verdana", 10)).grid(row=2, column=2)
        
        self.breakfastLabel = tk.Label(self, text="Breakfast Time", font=("Verdana", 10)).grid(row=3, column=1)
        self.breakfastStartEntry = tk.Entry(self, textvariable=self.breakfastStartVar, font=("Verdana", 10)).grid(row=3, column=2)
        self.dashLabel = tk.Label(self, text="~", font=("Verdana", 10)).grid(row=3, column=3)
        self.breakfastEndEntry = tk.Entry(self, textvariable=self.breakfastEndVar, font=("Verdana", 10)).grid(row=3, column=4)
        
        self.lunchLabel = tk.Label(self, text="Lunch Time", font=("Verdana", 10)).grid(row=4, column=1)
        self.lunchStartEntry = tk.Entry(self, textvariable=self.lunchStartVar, font=("Verdana", 10)).grid(row=4, column=2)
        self.dashLabel = tk.Label(self, text="~", font=("Verdana", 10)).grid(row=4, column=3)
        self.lunchEndEntry = tk.Entry(self, textvariable=self.lunchEndVar, font=("Verdana", 10)).grid(row=4, column=4)

        self.dinnerLabel = tk.Label(self, text="Dinner Time", font=("Verdana", 10)).grid(row=5, column=1)
        self.dinnerStartEntry = tk.Entry(self, textvariable=self.dinnerStartVar, font=("Verdana", 10)).grid(row=5, column=2)
        self.dashLabel = tk.Label(self, text="~", font=("Verdana", 10)).grid(row=5, column=3)
        self.dinnerEndEntry = tk.Entry(self, textvariable=self.dinnerEndVar, font=("Verdana", 10)).grid(row=5, column=4)

        self.breakLabel = tk.Label(self, text="Break Time", font=("Verdana", 10)).grid(row=6, column=1)
        self.breakStartEntry = tk.Entry(self, textvariable=self.breakStartVar, font=("Verdana", 10)).grid(row=6, column=2)
        self.dashLabel = tk.Label(self, text="~", font=("Verdana", 10)).grid(row=6, column=3)
        self.breakEndEntry = tk.Entry(self, textvariable=self.breakEndVar, font=("Verdana", 10)).grid(row=6, column=4)

        self.cancelButton = tk.Button(self, command=self.closeWindow, text="Cancel", font=("Verdana", 10)).grid(row=7, column=1)
        self.saveButton = tk.Button(self, command=self.saveChanges, text="Save", font=("Verdana", 10)).grid(row=7, column=4)
        self.pack()
        ##
        
    def closeWindow(self):
        self.master.newWindow.destroy()
    def saveChanges(self):
        print("savechanges")
        userInputSetAllocation(self.get_data())
        self.master.printSchedule()
        self.closeWindow()
    def get_data(self):
        t = [self.wakeUpVar.get(),
             self.sleepVar.get(),
             [self.breakfastStartVar.get(), self.breakfastEndVar.get()],
             [self.lunchStartVar.get(), self.lunchEndVar.get()],
             [self.dinnerStartVar.get(), self.dinnerEndVar.get()],
             [self.breakStartVar.get(), self.breakEndVar.get()]
             ]
        return t
    
def maine():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == '__main__':
    maine()
