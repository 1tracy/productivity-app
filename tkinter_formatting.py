""" tkinter interface for productivity app """

import tkinter as tk
import csv
import datetime as dt

class MainApplication(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        #self.dateLabel = tk.Label(self, textvariable=self.getdate(), font=("Verdana", 10)).grid(row=1)

    def getdate(self):
        """
        get date from datetime function
        format: hours:minutes month date[st/nd/rd/th], year
        """
        f = ''
        months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        day = str(dt.datetime.today().day)
        #print(datetime.datetime.today().strftime("%m/%d/%Y, %H:%M:%S"))
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
        print(dt.datetime.today().strftime(f"It is %H:%M:%S,{months[%m]} %d{f} %Y"))

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()

            
