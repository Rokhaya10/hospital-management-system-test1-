from tkinter import *
import sqlite3
#import pyttsx3

conn = sqlite3.connect('database.db')
c = conn.cursor()

number = []
patients = []

sql = "SELECT * FROM appointments"
res = c.execute(sql)

for r in res:
    ids = r[0]
    name = r[1]

    number.append(ids)
    patients.append(name)


class Application:
    def __init__(self, master):
        self.master = master


        self.x =0

        self.heading = Label(master, text = "APPOINTMENTS", font =('arial 50 bold'), fg = 'red')
        self.heading.place(x = 300, y = 0)

        self.change = Button(master, text = "New Patient", width = 25, height = 2, bg = 'steelblue', command = self.func)
        self.change.place(x =420, y =600 )

        self.n =Label(master, text = "", font =('arial 75 bold'))
        self.n.place(x =400, y= 150)

        self.pname = Label(master, text = "", font =('arial 80 bold'))
        self.pname.place(x =400, y = 400)

    def func(self):
        self.n.config(text = str(number[self.x]))
        self.pname.config(text = str(patients[self.x]))
        engine = pyttsx3.init()
        voice = engine.getProperty('voices')
        #for voice in voices:
        engine.setProperty('voice', voice[2].id)
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50)
        engine.say("Patient number " + str(number[self.x]) )
        engine.say(str(patients[self.x]) )
        engine.runAndWait()
        self.x = self.x + 1


root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.resizable(False, False)
root.mainloop()
