from tkinter import *
import tkinter.messagebox as t
from plyer import notification
from  covid import  Covid
import matplotlib.pyplot as p
import time
covid=Covid()

root=Tk()

root.geometry("800x500")

root.title("covid-19->Project by :Omkar Lokhande and Viraj Raut ")
def notifyme(title,message):
    notification.notify(
        message=message,
        timeout=25,
        app_icon="D:\PROGRAMMING LANGUAGES\PYTHON\PYTHAN BASIC AND ADVANCE\Python harry tutorial\covid cases\icon.ico"
    )

def showdata():

    a=abc.get()
    if(a==""):
        t.showinfo("info","Please enter country name")

    a=a.lower()


    getdata = covid.get_status_by_country_name(a)



    a=a.title()


    p.title(f"Covid-19: Cases in {a}")
    keys = ["confirmed cases","recovered" ,"active cases", "death"]
    values = [getdata["confirmed"], getdata["recovered"], getdata["active"], getdata["deaths"]]

    p.axis("equal")
    p.pie(values, labels=keys, radius=1, shadow=True, startangle=180,autopct="%0.0f%%")
    p.legend()

    p.text(1.727,-0.212,f"*Confirmed Cases:{values[0]}\n\n"
                        f"*Recovered Cases:{values[1]}\n\n"
                        f"*Active:{values[2]}\n\n"
                        f"*Death:{values[3]}")#to add text on matplotlib



    p.show()
    notifyme("omkar","Stay Home Stay Safe ")









label=Label(root,text="Covid-19:Country Wise Cases",bg="red",font=("comicsansns",25,"bold"))
label.pack()
label=Label(root,text="\nEnter Country Name:",font=("comicsansns",15,"bold"))
label.pack()
abc=StringVar()
screen=Entry(root,textvariable=abc,font="lucida 15 bold")
screen.pack(padx=10,pady=10)
print("\n")
m=Button(root,bg="yellow",text="Show",padx=20,pady=5,font=("comicsansns",10,"bold"),command=showdata)
m.pack()











root.mainloop()