from tkinter import *
from tkinter import messagebox
import pymysql

window = Tk()
window.title("Insert quiz")
window.geometry('400x400')
#window.configure(background = "grey");

 

serialno=IntVar()
questions=StringVar()
a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
answers=StringVar()

  
def database():
   x=1
   sno=serialno.get()
   question=questions.get()
   aa=a.get()
   bb=b.get()
   cc=c.get()
   dd=d.get()
   answers1=answers.get()

   #print(sno)
   
   # Open database connection
   db = pymysql.connect("localhost","root","root","test" )

   # prepare a cursor object using cursor() method
   cursor = db.cursor()

   # Prepare SQL query to INSERT a record into the database.
   
     #sql=("insert into question  values(%s,%s,%s,%s,%s,%s,%s,%s)",(sno,question,aa,bb,cc,dd,answers1,1))


    
   try:
      # Execute the SQL command
      #print(sql)
      cursor.execute("insert into questions  values(%s,%s,%s,%s,%s,%s,%s,%s)",(sno,question,aa,bb,cc,dd,answers1,1))
      # Commit your changes in the database
      db.commit()
      messagebox.showinfo("Information","Succesfully inserted")
      x=0
      serialno1.delete(0, END)
   except:
      # Rollback in case there is any error
      db.rollback()
      if x==1:
        messagebox.showerror("Error", "some Error. kindly try with other sno")

   # disconnect from server
   db.close()
 
    
    

   



sno = Label(window ,text = "Sno").grid(row = 0,column = 0,padx=10,sticky="W")
question= Label(window ,text = "Question").grid(row = 1,column = 0,padx=10,sticky="W")

AA = Label(window ,text = "A").grid(row = 2,column = 0,padx=10,sticky="W")
BB = Label(window ,text = "B").grid(row = 3,column = 0,padx=10,sticky="W")
CC = Label(window ,text = "C").grid(row = 4,column = 0,padx=10,sticky="W")
DD = Label(window ,text = "D").grid(row = 5,column = 0,padx=10,sticky="W")
answer=Label(window ,text = "Answer").grid(row = 6,column = 0,padx=10,sticky="W")


serialno1 = Entry(window,textvariable=serialno).grid(row = 0,column = 1)
questions1 = Entry(window,textvariable=questions).grid(row = 1,column = 1)
a1 = Entry(window,textvariable=a).grid(row = 2,column = 1)
b1 = Entry(window,textvariable=b).grid(row = 3,column = 1)
c1 = Entry(window,textvariable=c).grid(row = 4,column = 1)
d1 = Entry(window,textvariable=d).grid(row = 5,column = 1)
answers2 = Entry(window,textvariable=answers).grid(row = 6,column = 1)



btn = Button(window ,text="Submit",command=database).grid(row=8,column=0,padx=10,pady=5,sticky="W")
window.mainloop()
