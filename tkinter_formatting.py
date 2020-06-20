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
        print("addNewTask")

    def editTask(self):
        """
        open "edit existing task" window and update schedule
        """
        print("editTask")

    def deleteTask(self):
        """
        open "delete task" window, select task from dropdown menu to delete
        """
        print("deleteTask")
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
        time = dt.datetime.today().strftime('%H:%M:%S')
        m = int(dt.datetime.today().strftime('%m'))
        y = str(dt.datetime.today().year)
        formatted = ("It is "+time+", "+months[m]+" "+day+f+" "+y)

        self.dateVar.set(formatted)


def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()

            
