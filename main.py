import os
import tkinter as tk
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
from tkinter import *
from tkinter import messagebox
from functools import partial
from PIL import Image , ImageTk
from openpyxl import Workbook
import pymysql
from tkinter import ttk
from tkinter import filedialog
import pygame
from AudioPlayer import Music

pygame.mixer.init()
master = tk.Tk()
master.title('Railway Announcement System')
master.iconbitmap('train.ico')
master.geometry("600x500+400+30")
master.resizable(width=False,height=False)

file="train1.gif"

info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = master.after(70,lambda :animation(count))

def stop_animation():
    master.after_cancel(anim)

gif_label = tk.Label(master,image="")
gif_label.pack()


animation(count)

class Application:
    def __init__(self,master):
        self.master = master
        self.audiobtn1 = PhotoImage(file='loginb.png')
        self.imgbtn1 = Label(image=self.audiobtn1)
        self.b1 = Button(master, image=self.audiobtn1, command=self.login ,height = 28, width = 215).place(x=170, y=370)
        Frame(master).pack()
        
           

    def login(self):
        self.uname = e1.get()
        self.password = e2.get()
    
        if(self.uname == "" and self.password == "") :
            messagebox.showinfo("", "Blank Not allowed")
    
    
        elif(self.uname == "adee" and self.password == "adee"):
    
            self.newwindow = Toplevel(self.master)
            self.app = window2(self.newwindow)
            

            
    
        else :
            messagebox.showinfo("","Incorrent Username and Password")
            self.uname.set("")
            self.password.set("")


class window2:
    def __init__(self,master):
        self.master = master

        master.title('RAILWAY ANNOUNCEMENT SYSTEM')
        master.iconbitmap('train.ico')
        master.geometry("600x500+400+30")
        f2 = Frame(master)
        self.photo1 = ImageTk.PhotoImage(Image.open("train1.gif"))
        self.l1 = Label(master,image = self.photo1).pack()
        Frame(master,width=250,height=410,bg='white').place(x=160,y=25)

        #label1
        self.l1=Label(master,text='Train_No :',bg='white',font='Times 10',borderwidth=0)
        self.l1.place(x=180,y=70)

        self.en1=Entry(master,width=20,border=0,font='Times 14',textvariable=t1)
        self.en1.place(x=180,y=90)

        #label2
        self.l2=Label(master,text='Train_Name :',bg='white',font='Times 10')
        self.l2.place(x=180,y=120)

        self.en2=Entry(master,width=20,border=0,font='Times 14',textvariable=t2)
        self.en2.place(x=180,y=140)

        #label3
        self.l3=Label(master,text='From :',bg='white',font='Times 10')
        self.l3.place(x=180,y=170)

        self.e3=Entry(master,width=20,border=0,font='Times 14',textvariable=t3)
        self.e3.place(x=180,y=190)

        #label4
        self.l4=Label(master,text='To :',bg='white',font='Times 10')
        self.l4.place(x=180,y=220)

        self.e4=Entry(master,width=20,border=0,font='Times 14',textvariable=t4)
        self.e4.place(x=180,y=240)

        #label5
        self.l5=Label(master,text='Via :',bg='white',font='Times 10')
        self.l5.place(x=180,y=270)

        self.e5=Entry(master,width=20,border=0,font='Times 14',textvariable=t5)
        self.e5.place(x=180,y=290)

        #label6
        self.l7=Label(master,text='Timing :',bg='white',font='Times 10')
        self.l7.place(x=180,y=320)

        self.e6=Entry(master,width=20,border=0,font='Times 14',textvariable=t6)
        self.e6.place(x=180,y=340)

        #label7
        self.l6=Label(master,text='Platform :',bg='white',font='Times 10')
        self.l6.place(x=180,y=370)

        self.e7=Entry(master,width=20,border=0,font='Times 14',textvariable=t7)
        self.e7.place(x=180,y=390)



        self.announcementbtn = PhotoImage(file='excel.png')
        self.imgbtn = Label(image=self.announcementbtn)
        self.l8=Label(master,text='Enter Train Details',borderwidth=0,font='Times 14',background='white')
        self.l8.place(x=220,y=30)

        Frame(master,width=180,height=1,bg="#141414").place(x=180,y=112)
        Frame(master,width=180,height=1,bg="#141414").place(x=180,y=162)
        Frame(master,width=180,height=1,bg="#141414").place(x=180,y=212)
        Frame(master,width=180,height=1,bg="#141414").place(x=180,y=262)
        Frame(master,width=180,height=1,bg="#141414").place(x=180,y=312)
        Frame(master,width=180,height=1,bg="#141414").place(x=180,y=362)
        Frame(master,width=180,height=1,bg="#141414").place(x=180,y=412)

        submit = Button(master,text='SUBMIT',command=self.insert, height=2,width=8,borderwidth=0)
        submit.place(x=180,y=430)
        Next = Button(master,text='DELAYED',command=self.insert1, height=2,width=8,borderwidth=0)
        Next.place(x=250,y=430)
        Clean = Button(master,text='CLEAR',command=self.clear,height=2,width=8,borderwidth=0)
        Clean.place(x=320,y=430)
        n = Button(master,text='Next',command=self.next)
        n.place(x=550,y=10)
        f2.pack()
        
    def next(self):
        self.newwindow = Toplevel(self.master)
        self.app = window4(self.newwindow)

    def clear(self):
        self.en1.delete(0,END)    
        self.en2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.e5.delete(0,END)
        self.e6.delete(0,END)
        self.e7.delete(0,END)

        
        

    def insert(self):
        if self.en1.get() == "" or self.en2.get() =="" or self.e3.get()=="" or self.e4.get()=="" or self.e5.get()=="" or self.e6.get()=="" or self.e7.get()=="" :
            tk.messagebox.showerror("","Please Enter Correctly")

        else :   
            # Storing in DataBase
            sqlCon = pymysql.connect(host="localhost",user="root",password="admin",database="train_details") 
            cur =sqlCon.cursor()
            cur.execute("insert into train_details values(%s,%s,%s,%s,%s,%s,%s)",(
            t1.get(),
            t2.get(),
            t3.get(),
            t4.get(),
            t5.get(),
            t6.get(),
            t7.get()
            ))
            sqlCon.commit()
            sqlCon.close()
            # Inserting data in excel file
            wb=Workbook()
            wb['Sheet'].title='Train Details'
            sh = wb.active
            sh['A1'].value="train_no"    
            sh['B1'].value="train_name"
            sh['C1'].value="from"
            sh['D1'].value="to"
            sh['E1'].value="via"
            sh['F1'].value="timing"
            sh['G1'].value="platform"
            
         

            sh['A2'].value=self.en1.get()
            sh['B2'].value=self.en2.get() 
            sh['C2'].value=self.e3.get()
            sh['D2'].value=self.e4.get()
            sh['E2'].value=self.e5.get()
            sh['F2'].value=self.e6.get()
            sh['G2'].value=self.e7.get()
            wb.save("name.xlsx")  

            print("Data Submitted")

            self.newwindow = Toplevel(self.master)
            self.app = window4(self.newwindow)  


    def insert1(self):
            if self.en1.get() == "" or self.en2.get() =="" or self.e3.get()=="" or self.e4.get()=="" or self.e5.get()=="" or self.e6.get()=="" or self.e7.get()=="" :
                 tk.messagebox.showerror("","Please Enter Correctly")

            else :   
                # Storing in DataBase
                sqlCon = pymysql.connect(host="localhost",user="root",password="admin",database="train_details") 
                cur =sqlCon.cursor()
                cur.execute("insert into delayed_table values(%s,%s,%s,%s,%s,%s,%s)",(
                t1.get(),
                t2.get(),
                t3.get(),
                t4.get(),
                t5.get(),
                t6.get(),
                t7.get()
                ))
                sqlCon.commit()
                sqlCon.close()
                # Inserting data in excel file
                wb=Workbook()
                wb['Sheet'].title='Train Details'
                sh = wb.active
                sh['A1'].value="train_no"    
                sh['B1'].value="train_name"
                sh['C1'].value="from"
                sh['D1'].value="to"
                sh['E1'].value="via"
                sh['F1'].value="timing"
                sh['G1'].value="platform"
                
            

                sh['A2'].value=self.en1.get()
                sh['B2'].value=self.en2.get() 
                sh['C2'].value=self.e3.get()
                sh['D2'].value=self.e4.get()
                sh['E2'].value=self.e5.get()
                sh['F2'].value=self.e6.get()
                sh['G2'].value=self.e7.get()
                wb.save("name1.xlsx")  

                print("Data Submitted")    

            
            self.newwindow = Toplevel(self.master)
            self.app = window5(self.newwindow) 



class window4:
    def __init__(self,master):
        self.master = master
        
        master.title('RAILWAY ANNOUNCEMENT SYSTEM')
        master.iconbitmap('train.ico')
        master.geometry("600x500+400+30")
        f2 = Frame(master)
        self.photo1 = ImageTk.PhotoImage(Image.open("train1.gif"))
        self.l1 = Label(master,image = self.photo1).pack()
        f2.pack() 
        self.announcementbtn = PhotoImage(file='excel.png')
        self.imgbtn = Label(image=self.announcementbtn)
        self.audiobtn = PhotoImage(file='announcement.png')
        self.imgbtn2 = Label(image=self.audiobtn)
        self.audiobtn2 = PhotoImage(file='audiocut.png')
        self.imgbtn21 = Label(image=self.audiobtn2)

        
        mylabel = Label(master,text="")
        mylabel.pack(pady=5)

        

        self.b2 = Button(master, image=self.audiobtn2,command=partial(self.generateSkeleton), height =90, width = 99,borderwidth=1).place(x=230, y=50)
        self.b3 = Button(master, image=self.audiobtn,command=partial(self.generateAnnouncement,("name.xlsx")), height = 90, width = 99,borderwidth=0).place(x=230, y=150)
        self.b4 = Button(master, image=self.announcementbtn,command= self.open_excel,height = 95, width = 99,borderwidth=0).place(x=230, y=250)
        
        rec = Button(master,text='RECORDS',command=self.records, height=2,width=8,borderwidth=0)
        rec.place(x=250,y=430)
        audio = Button(master,text='Media Player',command=self.joint2,height=2,width=12)
        audio.place(x=130,y=370)
        der = Button(master,text='Delayed Records',command=self.dre, height=2,width=12)
        der.place(x=240,y=370)
   #def open_excel(self):
      #  master.filename = filedialog.askopenfilename(initialdir="D:\project sem5\Railway Annoucement System project",title="Select A File",filetypes=(("mp3 files", "*.mp3"),("all files","*.*")))
       # file = open(self.filename,'r')
       # print(file.read())
      #  file.close()

    def joint2(self):
        self.newwindow = Toplevel(self.master)
        self.app = Music(self.newwindow) 

    def records(self):
        self.newwindow = Toplevel(self.master)
        self.app = window6(self.newwindow) 

    def open_excel(self):
        os.system('name.xlsx')
   
    def dre(self):
        self.newwindow = Toplevel(self.master)
        self.app = window7(self.newwindow) 


    def textToSpeech(self,text, filename):
        self.mytext = str(text)
        self.language ='en'
        self.myobj = gTTS(text = self.mytext, lang = self.language, slow = True)
        self.myobj.save(filename)

    def mergeaudios(self,audios):
        self.combined = AudioSegment.empty()
        for audio in audios:
            self.combined += AudioSegment.from_mp3(audio)
        return self.combined    

    def generateSkeleton(self):
        audio = AudioSegment.from_mp3('Railway.mp3')

        # May I have Your Attention Please
        start = 000
        finish = 2000
        audioProcessed = audio[start:finish]
        audioProcessed.export("1_English.mp3", format="mp3")

        # To
        start = 6000
        finish = 6400
        audioProcessed = audio[start:finish]
        audioProcessed.export("5_English.mp3", format="mp3")

        #via
        start = 7000
        finish = 7400
        audioProcessed = audio[start:finish]
        audioProcessed.export("7_English.mp3", format="mp3")

        #Will Depart At its Sheduled Time
        start = 9000
        finish = 12000
        audioProcessed = audio[start:finish]
        audioProcessed.export("9_English.mp3", format="mp3")
            
        #From Platfrom no 
        start = 15000
        finish = 16850
        audioProcessed = audio[start:finish]
        audioProcessed.export("11_English.mp3", format="mp3")


    def generateAnnouncement(self,filename):
        print("Generating Train_Details")
        df = pd.read_excel(filename)
        print(df)
        for index, item in df.iterrows():
                
                #generate train_no and name
            self.textToSpeech(item['train_no'], '2_English.mp3')

               #Generate from city
            self.textToSpeech(item['train_name'], '3_English.mp3')

               #Generate from city
            self.textToSpeech(item['from'], '4_English.mp3')

                #Generate from city
            self.textToSpeech(item['to'], '6_English.mp3')

                #generate via-city
            self.textToSpeech(item['via'], '8_English.mp3')

                #generate to
            self.textToSpeech(item['timing'], '10_English.mp3')
            
                #generate platform number
            self.textToSpeech(item['platform'], '12_English.mp3')

            audios = [f"{i}_English.mp3" for i in range(1,13)]

            self.announcement = self.mergeaudios(audios)
            self.announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3",format='mp3')        

class window5:
    def __init__(self,master):
        self.master = master
        
        master.title('RAILWAY ANNOUNCEMENT SYSTEM')
        master.iconbitmap('train.ico')
        master.geometry("600x500+400+30")
        f2 = Frame(master)
        self.photo1 = ImageTk.PhotoImage(Image.open("train1.gif"))
        self.l1 = Label(master,image = self.photo1).pack()
        f2.pack() 
        self.announcementbtn = PhotoImage(file='excel.png')
        self.imgbtn = Label(image=self.announcementbtn)
        self.audiobtn = PhotoImage(file='announcement.png')
        self.imgbtn2 = Label(image=self.audiobtn)
        self.audiobtn2 = PhotoImage(file='audiocut.png')
        self.imgbtn21 = Label(image=self.audiobtn2)

        
        mylabel = Label(master,text="")
        mylabel.pack(pady=5)

        

        self.b2 = Button(master, image=self.audiobtn2,command=partial(self.generateSkeleton), height =90, width = 99,borderwidth=1).place(x=230, y=50)
        self.b3 = Button(master, image=self.audiobtn,command=partial(self.generateAnnouncement,("name1.xlsx")), height = 90, width = 99,borderwidth=0).place(x=230, y=150)
        self.b4 = Button(master, image=self.announcementbtn,command= self.open_excel,height = 95, width = 99,borderwidth=0).place(x=230, y=250)
        audio = Button(master,text='Media Player',command=self.joint2,height=2,width=8)
        audio.place(x=250,y=370)
        rec = Button(master,text='RECORDS',command=self.records, height=2,width=8,borderwidth=0)
        rec.place(x=250,y=430)

   #def open_excel(self):
      #  master.filename = filedialog.askopenfilename(initialdir="D:\project sem5\Railway Annoucement System project",title="Select A File",filetypes=(("mp3 files", "*.mp3"),("all files","*.*")))
       # file = open(self.filename,'r')
       # print(file.read())
      #  file.close()

    def joint2(self):
        self.newwindow = Toplevel(self.master)
        self.app = Music(self.newwindow) 

    def records(self):
        self.newwindow = Toplevel(self.master)
        self.app = window7(self.newwindow) 

    def open_excel(self):
        os.system('name.xlsx')
   


    def textToSpeech(self,text, filename):
        self.mytext = str(text)
        self.language ='en'
        self.myobj = gTTS(text = self.mytext, lang = self.language, slow = True)
        self.myobj.save(filename)

    def mergeaudios(self,audios):
        self.combined = AudioSegment.empty()
        for audio in audios:
            self.combined += AudioSegment.from_mp3(audio)
        return self.combined    

    def generateSkeleton(self):
        audio = AudioSegment.from_mp3('Railway.mp3')

        # May I have Your Attention Please
        start = 000
        finish = 2000
        audioProcessed = audio[start:finish]
        audioProcessed.export("1_late.mp3", format="mp3")

        # To
        start = 6000
        finish = 6400
        audioProcessed = audio[start:finish]
        audioProcessed.export("5_late.mp3", format="mp3")

        #via
        start = 7000
        finish = 7400
        audioProcessed = audio[start:finish]
        audioProcessed.export("7_late.mp3", format="mp3")

        #Will Depart At its Sheduled Time
        start = 109500
        finish = 111000
        audioProcessed = audio[start:finish]
        audioProcessed.export("9_late.mp3", format="mp3")
            
        #From Platfrom no 
        start = 15000
        finish = 16850
        audioProcessed = audio[start:finish]
        audioProcessed.export("11_late.mp3", format="mp3")


    def generateAnnouncement(self,filename):
        print("Generating Train_Details")
        df = pd.read_excel(filename)
        print(df)
        for index, item in df.iterrows():
                
                #generate train_no and name
            self.textToSpeech(item['train_no'], '2_late.mp3')

               #Generate from city
            self.textToSpeech(item['train_name'], '3_late.mp3')

               #Generate from city
            self.textToSpeech(item['from'], '4_late.mp3')

                #Generate from city
            self.textToSpeech(item['to'], '6_late.mp3')

                #generate via-city
            self.textToSpeech(item['via'], '8_late.mp3')

                #generate to
            self.textToSpeech(item['timing'], '10_late.mp3')
            
                #generate platform number
            self.textToSpeech(item['platform'], '12_late.mp3')

            audios = [f"{i}_late.mp3" for i in range(1,13)]

            self.announcement = self.mergeaudios(audios)
            self.announcement.export(f"Late_{item['train_no']}_{index+1}.mp3",format='mp3')        


class window6:
    
    def __init__(self,master):
        self.master = master
        
        self.master.title("Train RECORDS")
        self.master.geometry("600x500+400+30")

        MainFrame = Frame(self.master, bd=10, width=600, height=500,relief=RIDGE, bg='cadet blue')
        
        MainFrame.grid(row=0,column=0)
         
        Frame1 = Frame(self.master, bd=10, width=600, height=214,relief=RIDGE, bg='cadet blue')
        #label1
        self.l1=Label(master,text='Train_No :-',bg='cadet blue',font='Times 11',borderwidth=0)
        self.l1.place(x=12,y=300)

        self.en1=Entry(master,width=20,border=0,font='Times 11',textvariable=t1,bg='cadet blue')
        self.en1.place(x=100,y=300)

        #label2
        self.l2=Label(master,text='Train_Name :-',bg='cadet blue',font='Times 11',borderwidth=0)
        self.l2.place(x=12,y=325)

        self.en2=Entry(master,width=20,border=0,font='Times 11',textvariable=t2,bg='cadet blue')
        self.en2.place(x=100,y=325)

        #label3
        self.l3=Label(master,text='From :-',bg='cadet blue',font='Times 11',borderwidth=0)
        self.l3.place(x=12,y=353)

        self.e3=Entry(master,width=20,border=0,font='Times 11',textvariable=t3,bg='cadet blue')
        self.e3.place(x=100,y=353)

        #label4
        self.l4=Label(master,text='To :-',bg='cadet blue',font='Times 11',borderwidth=0)
        self.l4.place(x=12,y=383)

        self.e4=Entry(master,width=20,border=0,font='Times 11',textvariable=t4,bg='cadet blue')
        self.e4.place(x=100,y=383)

        #label5
        self.l5=Label(master,text='Via :-',bg='cadet blue',font='Times 11',borderwidth=0)
        self.l5.place(x=12,y=413)

        self.e5=Entry(master,width=20,border=0,font='Times 11',textvariable=t5,bg='cadet blue')
        self.e5.place(x=100,y=413)

        #label6
        self.l7=Label(master,text='Timing :-',bg='cadet blue',font='Times 11',borderwidth=0)
        self.l7.place(x=12,y=443)

        self.e6=Entry(master,width=20,border=0,font='Times 11',textvariable=t6,bg='cadet blue')
        self.e6.place(x=100,y=443)

        #label7
        self.l6=Label(master,text='Platform :-',bg='cadet blue',font='Times 11',borderwidth=0)
        self.l6.place(x=12,y=473)

        self.e7=Entry(master,width=20,border=0,font='Times 11',textvariable=t7,bg='cadet blue')
        self.e7.place(x=100,y=473)

        delbtn = Button(master,text="DELETE",command=self.delete)
        delbtn.place(x=300,y=400)

        ubtn = Button(master,text="UPDATE",command=self.update)
        ubtn.place(x=300,y=450)


        Frame(master,width=180,height=1,bg="#141414").place(x=100,y=319)
        Frame(master,width=180,height=1,bg="#141414").place(x=100,y=345)
        Frame(master,width=180,height=1,bg="#141414").place(x=100,y=373)
        Frame(master,width=180,height=1,bg="#141414").place(x=100,y=403)
        Frame(master,width=180,height=1,bg="#141414").place(x=100,y=433)
        Frame(master,width=180,height=1,bg="#141414").place(x=100,y=463)
        Frame(master,width=180,height=1,bg="#141414").place(x=100,y=493)
        Frame1.grid(row=1,column=0)

        scrolly= Scrollbar(MainFrame,orient=VERTICAL)

        self.train1 = ttk.Treeview(MainFrame,height=12,columns=("t1","t2","t3","t4","t5","t6","t7"),yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT , fill=Y)
        self.train1.heading("t1",text="Train_no")
        self.train1.heading("t2",text="Train_name")
        self.train1.heading("t3",text="To")
        self.train1.heading("t4",text="From")
        self.train1.heading("t5",text="Via")
        self.train1.heading("t6",text="Timing")
        self.train1.heading("t7",text="Platform")

        self.train1['show']='headings'

        self.train1.column("t1", width=80)
        self.train1.column("t2", width=100)
        self.train1.column("t3", width=100)
        self.train1.column("t4", width=80)
        self.train1.column("t5", width=80)
        self.train1.column("t6", width=60)
        self.train1.column("t7", width=60)

        self.train1.pack(fill=BOTH,expand=1) 
        
        self.Display()      
              
    def Display(self):
        sqlCon = pymysql.connect(host="localhost",user="root",password="admin",database="train_details")
        cur =sqlCon.cursor()
        cur.execute("select * from train_details")   
        result = cur.fetchall()
        if len(result) !=0:
            self.train1.delete(* self.train1.get_children()) 
            for row in result:
                self.train1.insert('',END,values = row)   
            sqlCon.commit()
        sqlCon.close()       
    
    


    # def update(self):
    #     sqlCon = pymysql.connect(host="localhost",user="root",password="admin",database="train_details") 
    #     cur =sqlCon.cursor()
    #     cur.execute(f"update train_details set Train_no={self.t1.get()},Train_name={self.t2.get()},From={self.t3.get()},To={self.t4.get()},Via={self.t5.get()},Timing={self.t6.get()},Platform={self.t7.get()} Where Train_no = {self.t1.get()} ")
    #     sqlCon.commit()
    #     sqlCon.close()

    def update(self):
        sqlCon = pymysql.connect(host="localhost",user="root",password="admin",database="train_details") 
        cur =sqlCon.cursor()
        cur.execute("DELETE from train_details WHERE Train_no = " + self.en1.get())        
        if self.en1.get() == "" or self.en2.get() =="" or self.e3.get()=="" or self.e4.get()=="" or self.e5.get()=="" or self.e6.get()=="" or self.e7.get()=="" :
                 tk.messagebox.showerror("","Please Enter Correctly")

        else :   
                # Storing in DataBase
            sqlCon = pymysql.connect(host="localhost",user="root",password="admin",database="train_details") 
            cur =sqlCon.cursor()
            cur.execute("insert into train_details values(%s,%s,%s,%s,%s,%s,%s)",(
            t1.get(),
            t2.get(),
            t3.get(),
            t4.get(),
            t5.get(),
            t6.get(),
            t7.get()
                ))
            sqlCon.commit()
            sqlCon.close()
        
        print('Data Updated')

    def delete(self):
        sqlCon = pymysql.connect(host="localhost",user="root",password="admin",database="train_details") 
        cur =sqlCon.cursor()
        cur.execute("DELETE from train_details WHERE Train_no = " + self.en1.get())        
        sqlCon.commit()
        sqlCon.close()
        print('Data Deleted')
        

class window7:
    
    def __init__(self,master):
        self.master = master
        
        self.master.title("Train Delayed RECORDS")
        self.master.geometry("600x500+400+30")
        

        MainFrame = Frame(self.master, bd=10, width=600, height=500,relief=RIDGE, bg='cadet blue')
        
        MainFrame.grid(row=0,column=0)
         
        Frame1 = Frame(self.master, bd=10, width=600, height=214,relief=RIDGE, bg='cadet blue')
        #label1
        self.l1=Label(master,text='Train_No :-',bg='cadet blue',font='Times 11',borderwidth=0)
        self.l1.place(x=12,y=300)

        self.en1=Entry(master,width=20,border=0,font='Times 11',textvariable=t1,bg='cadet blue')
        self.en1.place(x=100,y=300)

        #label2
        self.l2=Label(master,text='Train_Name :-',bg='cadet blue',font='Times 11',borderwidth=0)
        self.l2.place(x=12,y=325)

        self.en2=Entry(master,width=20,border=0,font='Times 11',textvariable=t2,bg='cadet blue')
        self.en2.place(x=100,y=325)

        #label3
        self.l3=Label(master,text='From :-',bg='cadet blue',font='Times 11',borderwidth=0)
        self.l3.place(x=12,y=353)

        self.e3=Entry(master,width=20,border=0,font='Times 11',textvariable=t3,bg='cadet blue')
        self.e3.place(x=100,y=353)

        #label4
        self.l4=Label(master,text='To :-',bg='cadet blue',font='Times 11',borderwidth=0)
        self.l4.place(x=12,y=383)

        self.e4=Entry(master,width=20,border=0,font='Times 11',textvariable=t4,bg='cadet blue')
        self.e4.place(x=100,y=383)

        #label5
        self.l5=Label(master,text='Via :-',bg='cadet blue',font='Times 11',borderwidth=0)
        self.l5.place(x=12,y=413)

        self.e5=Entry(master,width=20,border=0,font='Times 11',textvariable=t5,bg='cadet blue')
        self.e5.place(x=100,y=413)

        #label6
        self.l7=Label(master,text='Timing :-',bg='cadet blue',font='Times 11',borderwidth=0)
        self.l7.place(x=12,y=443)

        self.e6=Entry(master,width=20,border=0,font='Times 11',textvariable=t6,bg='cadet blue')
        self.e6.place(x=100,y=443)

        #label7
        self.l6=Label(master,text='Platform :-',bg='cadet blue',font='Times 11',borderwidth=0)
        self.l6.place(x=12,y=473)

        self.e7=Entry(master,width=20,border=0,font='Times 11',textvariable=t7,bg='cadet blue')
        self.e7.place(x=100,y=473)

        delbtn = Button(master,text="DELETE",command=self.delete)
        delbtn.place(x=300,y=400)

        ubtn = Button(master,text="UPDATE",command=self.update)
        ubtn.place(x=300,y=450)

        Frame(master,width=180,height=1,bg="#141414").place(x=100,y=319)
        Frame(master,width=180,height=1,bg="#141414").place(x=100,y=345)
        Frame(master,width=180,height=1,bg="#141414").place(x=100,y=373)
        Frame(master,width=180,height=1,bg="#141414").place(x=100,y=403)
        Frame(master,width=180,height=1,bg="#141414").place(x=100,y=433)
        Frame(master,width=180,height=1,bg="#141414").place(x=100,y=463)
        Frame(master,width=180,height=1,bg="#141414").place(x=100,y=493)
        Frame1.grid(row=1,column=0)

        scrolly= Scrollbar(MainFrame,orient=VERTICAL)

        self.train1 = ttk.Treeview(MainFrame,height=12,columns=("t1","t2","t3","t4","t5","t6","t7"),yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT , fill=Y)
        self.train1.heading("t1",text="Train_no")
        self.train1.heading("t2",text="Train_name")
        self.train1.heading("t3",text="To")
        self.train1.heading("t4",text="From")
        self.train1.heading("t5",text="Via")
        self.train1.heading("t6",text="Timing")
        self.train1.heading("t7",text="Platform")

        self.train1['show']='headings'

        self.train1.column("t1", width=80)
        self.train1.column("t2", width=100)
        self.train1.column("t3", width=100)
        self.train1.column("t4", width=80)
        self.train1.column("t5", width=80)
        self.train1.column("t6", width=60)
        self.train1.column("t7", width=60)

        self.train1.pack(fill=BOTH,expand=1) 
        self.Display()
        
    def Display(self):
        sqlCon = pymysql.connect(host="localhost",user="root",password="admin",database="train_details") 
        cur =sqlCon.cursor()
        cur.execute("select * from delayed_table")   
        result = cur.fetchall()
        if len(result) !=0:
            self.train1.delete(* self.train1.get_children()) 
            for row in result:
                self.train1.insert('',END,values = row)   
            sqlCon.commit()
        sqlCon.close()         

    def delete(self):
        sqlCon = pymysql.connect(host="localhost",user="root",password="admin",database="train_details") 
        cur =sqlCon.cursor()
        cur.execute("DELETE from delayed_table WHERE Train_no = " + self.en1.get())        
        sqlCon.commit()
        sqlCon.close()
        print('Data Deleted')

    def update(self):
        sqlCon = pymysql.connect(host="localhost",user="root",password="admin",database="train_details") 
        cur =sqlCon.cursor()
        cur.execute("DELETE from train_details WHERE Train_no = " + self.en1.get())        
        if self.en1.get() == "" or self.en2.get() =="" or self.e3.get()=="" or self.e4.get()=="" or self.e5.get()=="" or self.e6.get()=="" or self.e7.get()=="" :
                 tk.messagebox.showerror("","Please Enter Correctly")

        else :   
                # Storing in DataBase
            sqlCon = pymysql.connect(host="localhost",user="root",password="admin",database="train_details") 
            cur =sqlCon.cursor()
            cur.execute("insert into train_details values(%s,%s,%s,%s,%s,%s,%s)",(
            t1.get(),
            t2.get(),
            t3.get(),
            t4.get(),
            t5.get(),
            t6.get(),
            t7.get()
                ))
            sqlCon.commit()
            sqlCon.close()    

obj=Application(master)

global e1,e2,t1,t2,t3,t4,t5,t6,t7,en1,en2,e3,e4,e5,e6,e7
t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()
t5=StringVar()
t6=StringVar()
t7=StringVar()

 
Frame(master,width=220,height=330,bg='white',borderwidth=5).place(x=170,y=40)

#label1
l1=Label(master,text='Username',bg='white')
l=('consolas',13) #font,text,size
l1.config(font='Times')
l1.place(x=182,y=200)

e1=Entry(master,width=20,border=0)
e1.config(font='Times')
e1.place(x=182,y=230)

#label2
l2=Label(master,text='Password',bg='white')
l=('consolas',13) #font,text,size
l2.config(font='Times')
l2.place(x=182,y=280)

e2=Entry(master,width=20,border=0)
e2.config(font='Times',show="*")
e2.place(x=182,y=310)

Frame(master,width=181,height=1,bg="#141414").place(x=182,y=252)
Frame(master,width=181,height=1,bg="#141414").place(x=182,y=333)

image1 =Image.open("admin.jpg")
image2 = ImageTk.PhotoImage(image1)

label1=Label(image=image2,borderwidth=0)
label1.place(x=210,y=50)


master.mainloop()