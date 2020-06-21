import tkinter as tk
import csv
import datetime as dt

class MainApplication(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        
        self.dateVar = tk.StringVar()
        self.dateLabel = tk.Label(self, textvariable=self.dateVar, font=("Verdana", 10)).grid(row=1, columnspan=3)
        self.getdate()

        self.scheduleVar = tk.StringVar()
        self.scheduleVar.set("Today's Schedule\n")
        self.scheduleMessage = tk.Message(self, textvariable=self.scheduleVar,bg="white", width=100, font=("Verdana", 15)).grid(row=2, rowspan=4, columnspan=3)

        self.prevDayButton = tk.Button(self, text="<<", width=10, command=self.prevDay, font=("Verdana", 10)).grid(row=6, column=1)
        self.nextDayButton = tk.Button(self, text=">>", width=10, command=self.nextDay, font=("Verdana", 10)).grid(row=6, column=2)

        self.addNewTaskButton = tk.Button(self, text="Add New Task", width=20, command=self.addNewTask, font=("Verdana", 10)).grid(row=3, column=3)
        self.editNewTaskButton = tk.Button(self, text="Edit Task", width=20, command=self.editTask, font=("Verdana", 10)).grid(row=4, column=3)
        self.deleteTaskButton = tk.Button(self, text="Delete Task", width=20, command=self.deleteTask, font=("Verdana", 10)).grid(row=5, column=3)
        self.addBusyTimeButton = tk.Button(self, text="Add Busy Time", width=20, command=self.addBusyTime, font=("Verdana", 10)).grid(row=6, column=3)
        
        self.pack()

    def addBusyTime(self):
        """
        add time where events cannot be scheduled
        """
        print("addBusyTime")
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
        
    def prevDay(self):
        """
        updates calendar to previous day
        """
        print("prevDay")
        
    def nextDay(self):
        """
        updates calendar to next day
        """
        print("nextDay")
        
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
        self.importanceVar.set("100 is most important")
        self.importanceLabel = tk.Label(self, text="Level Of Importance(1-100):", font=("Verdana", 10)).grid(row=3, column=1)
        self.importanceEntry = tk.Entry(self, textvariable=self.importanceVar, font=("Verdana", 10), width=50).grid(row=3, column=2, columnspan=4)

        self.lengthVar = tk.StringVar()
        self.lengthLabel = tk.Label(self, text="Task Length (minutes): ", font=("Verdana", 10)).grid(row=4, column=1)
        self.lengthEntry = tk.Entry(self, textvariable=self.lengthVar, font=("Verdana", 10), width=50).grid(row=4, column=2, columnspan=4)

        self.deadlineTimeVar = tk.StringVar()
        self.deadlineTimeVar.set("24hr format due date")
        self.deadlineDayVar = tk.StringVar()
        self.deadlineDayVar.set("Day")
        self.deadlineMonthVar = tk.StringVar()
        self.deadlineMonthVar.set("Month")
        self.deadlineYearVar = tk.StringVar()
        self.deadlineYearVar.set("Year")
        
        self.deadlineLabel = tk.Label(self, text="Deadline: ", font=("Verdana", 10)).grid(row=5, column=1)
        self.deadlineTimeEntry = tk.Entry(self,textvariable=self.deadlineTimeVar, font=("Verdana", 10)).grid(row=5, column=2)
        self.deadlineDayEntry = tk.Entry(self, width=10,textvariable=self.deadlineDayVar, font=("Verdana", 10)).grid(row=5, column=3)
        self.deadlineMonthEntry = tk.Entry(self, width=10,textvariable=self.deadlineMonthVar, font=("Verdana", 10)).grid(row=5, column=4)
        self.deadlineYearEntry = tk.Entry(self, width=10, textvariable=self.deadlineYearVar, font=("Verdana", 10)).grid(row=5, column=5)

        self.overrideTimeVar = tk.StringVar()
        self.overrideTimeVar.set("start time (ex. 2210)")
        self.overrideDayVar = tk.StringVar()
        self.overrideDayVar.set("Day")
        self.overrideMonthVar = tk.StringVar()
        self.overrideMonthVar.set("Month")
        self.overrideYearVar = tk.StringVar()
        self.overrideYearVar.set("Year")

        self.overrideLabel = tk.Label(self, text="Time Slot Override: ", font=("Verdana", 10)).grid(row=6, column=1)
        self.overrideTimeEntry = tk.Entry(self, textvariable=self.overrideTimeVar, font=("Verdana", 10)).grid(row=6, column=2)
        self.overrideDayEntry = tk.Entry(self, textvariable=self.overrideDayVar, font=("Verdana", 10), width=10).grid(row=6, column=3)
        self.overrideMonthEntry = tk.Entry(self, textvariable=self.overrideMonthVar, font=("Verdana", 10), width=10).grid(row=6, column=4)
        self.overrideYearEntry = tk.Entry(self, textvariable=self.overrideYearVar, font=("Verdana", 10), width=10).grid(row=6, column=5)

        self.cancelButton = tk.Button(self, text="Cancel", command=self.closeWindow, width=10, font=("Verdana", 10)).grid(row=7, column=1)
        self.saveButton = tk.Button(self, text="Save", command=self.saveChanges, width=10, font=("Verdana", 10)).grid(row=7, column=5)
        self.pack()
    def closeWindow(self):
        self.master.newWindow.destroy()
    def saveChanges(self):
        print("savechanges")

class EditTaskFrame(tk.Frame):
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
        self.importanceVar.set("100 is most important")
        self.importanceLabel = tk.Label(self, text="Level Of Importance(1-100):", font=("Verdana", 10)).grid(row=3, column=1)
        self.importanceEntry = tk.Entry(self, textvariable=self.importanceVar, font=("Verdana", 10), width=50).grid(row=3, column=2, columnspan=4)

        self.lengthVar = tk.StringVar()
        self.lengthLabel = tk.Label(self, text="Task Length (minutes): ", font=("Verdana", 10)).grid(row=4, column=1)
        self.lengthEntry = tk.Entry(self, textvariable=self.lengthVar, font=("Verdana", 10), width=50).grid(row=4, column=2, columnspan=4)

        self.deadlineTimeVar = tk.StringVar()
        self.deadlineTimeVar.set("24hr format due date")
        self.deadlineDayVar = tk.StringVar()
        self.deadlineDayVar.set("Day")
        self.deadlineMonthVar = tk.StringVar()
        self.deadlineMonthVar.set("Month")
        self.deadlineYearVar = tk.StringVar()
        self.deadlineYearVar.set("Year")
        
        self.deadlineLabel = tk.Label(self, text="Deadline: ", font=("Verdana", 10)).grid(row=5, column=1)
        self.deadlineTimeEntry = tk.Entry(self,textvariable=self.deadlineTimeVar, font=("Verdana", 10)).grid(row=5, column=2)
        self.deadlineDayEntry = tk.Entry(self, width=10,textvariable=self.deadlineDayVar, font=("Verdana", 10)).grid(row=5, column=3)
        self.deadlineMonthEntry = tk.Entry(self, width=10,textvariable=self.deadlineMonthVar, font=("Verdana", 10)).grid(row=5, column=4)
        self.deadlineYearEntry = tk.Entry(self, width=10, textvariable=self.deadlineYearVar, font=("Verdana", 10)).grid(row=5, column=5)

        self.overrideTimeVar = tk.StringVar()
        self.overrideTimeVar.set("start time (ex. 2210)")
        self.overrideDayVar = tk.StringVar()
        self.overrideDayVar.set("Day")
        self.overrideMonthVar = tk.StringVar()
        self.overrideMonthVar.set("Month")
        self.overrideYearVar = tk.StringVar()
        self.overrideYearVar.set("Year")

        self.overrideLabel = tk.Label(self, text="Time Slot Override: ", font=("Verdana", 10)).grid(row=6, column=1)
        self.overrideTimeEntry = tk.Entry(self, textvariable=self.overrideTimeVar, font=("Verdana", 10)).grid(row=6, column=2)
        self.overrideDayEntry = tk.Entry(self, textvariable=self.overrideDayVar, font=("Verdana", 10), width=10).grid(row=6, column=3)
        self.overrideMonthEntry = tk.Entry(self, textvariable=self.overrideMonthVar, font=("Verdana", 10), width=10).grid(row=6, column=4)
        self.overrideYearEntry = tk.Entry(self, textvariable=self.overrideYearVar, font=("Verdana", 10), width=10).grid(row=6, column=5)

        self.cancelButton = tk.Button(self, text="Cancel", command=self.closeWindow, width=10, font=("Verdana", 10)).grid(row=7, column=1)
        self.saveButton = tk.Button(self, text="Save", command=self.saveChanges, width=10, font=("Verdana", 10)).grid(row=7, column=5)

        self.updateWithSaved()
        self.pack()
        
    def closeWindow(self):
        self.master.newWindow.destroy()
    def saveChanges(self):
        print("savechanges")
    def updateWithSaved(self):
        print("update with saved")
        self.overrideYearVar.set("edited")

class DeleteFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master.newWindow)
        self.master = master

        self.deleteLabel = tk.Label(self, text="Select Task To Delete", font=("Verdana", 10)).grid(row=1, column=1, columnspan=2)
        self.tasklist = self.getTasks()

        self.taskOptionVar = tk.StringVar()
        self.taskOptionVar.set(self.tasklist[0])
        self.taskOptionMenu = tk.OptionMenu(self, self.taskOptionVar, *self.tasklist).grid(row=2, column=1, columnspan=2)

        self.pack()
    def getTasks(self):
        """
        parse csv to extract task names
        """
        return (['a', 'b', 'c'])
    def closeWindow(self):
        self.master.newWindow.destroy()
    def saveChanges(self):
        print("savechanges")
def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()

            
