from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect('database.db')
c = conn.cursor()

ids =[]
class Application:
    def __init__(self, master):
        self.master = master

        self.left = Frame(master, width = 800, height =720, bg = 'steelblue')
        self.left.pack(side = LEFT)

        self.right = Frame(master, width = 400, height = 720, bg ='steelblue')
        self.right.pack(side = RIGHT)

        self.heading = Label(self.left, text = "HOSPITAL APPOINTMENTS", font = ('arial 40 bold'), fg ='steelblue', bg = 'white')
        self.heading.place(x=0, y=0)


        self.name = Label(self.left, text = "Patient's Name", font =('arial 15 bold'), fg = 'black', bg = 'steelblue')
        self.name.place(x =0, y = 100)

        self.age =Label(self.left, text = "Age", font =('arial 15 bold'), fg = 'black', bg = 'steelblue')
        self.age.place(x = 0, y =140)


        self.gender = Label(self.left, text="Gender", font=('arial 15 bold'), fg='black', bg='steelblue')
        self.gender.place(x=0, y=180)

        self.location = Label(self.left, text="Address", font=('arial 15 bold'), fg='black', bg='steelblue')
        self.location.place(x=0, y=220)

        self.time = Label(self.left, text="Appointment time and date ", font=('arial 15 bold'), fg='black', bg='steelblue')
        self.time.place(x=0, y=260)

        self.phone =Label(self.left, text ="Phone number", font =('arial 15 bold'), fg ='black', bg ='steelblue')
        self.phone.place(x =0, y= 300)

        self.name_ent = Entry(self.left, width =30)
        self.name_ent.place(x = 250, y =100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=260)

        self.phone_ent =Entry(self.left, width =30)
        self.phone_ent.place(x =250, y = 300)

        self.submit = Button(self.left, text = "Book Appointment", width = 20, height = 2, bg = 'steelblue', command = self.add_appointment)
        self.submit.place(x = 280, y = 340)

        sql2 = "SELECT ID FROM appointments"
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]

        self.logs = Label(self.right, text = "Appointments", font = ('arial 20 bold'), fg ='white', bg = 'steelblue')
        self.logs.place(x =0, y =0)

        self.box = Text(self.right, width =60, height =40)
        self.box.place(x =0, y =40)
        self.box.insert(END, "Total appointments till now: " + str(self.final_id))

    def add_appointment(self):
      #  print("This is working")
         self.val1 = self.name_ent.get()
         self.val2 = self.age_ent.get()
         self.val3 = self.gender_ent.get()
         self.val4 = self.location_ent.get()
         self.val5 = self.time_ent.get()
         self.val6 = self.phone_ent.get()

         #print(self.val1)
         if(self.val1== '' or self.val2 =='' or self.val3=='' or self.val4=='' or self.val5 =='' or self.val6 ==''):
             tkinter.messagebox.showinfo("Warning", "Please fill up all boxes")
         else:

             sql = "INSERT INTO 'appointments' (name, age, gender , location , scheduled_time, phone number) VALUES(?,?,?,?,?,?)"
             c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
             conn.commit()
             tkinter.messagebox.showinfo("Success","Appointment for " +str(self.val1) + " has been created!")



             self.box.insert(END, '\nAppointment fixed for  ' + str(self.val1) + ' at ' + str(self.val5))


root = Tk()
root.title('HOSPITAL MANAGEMENT SYSTEM by Rokhaya and Moustapha ')
b = Application(root)
root.geometry("1200x720+0+0")


root.resizable(False, False)
root.mainloop()
