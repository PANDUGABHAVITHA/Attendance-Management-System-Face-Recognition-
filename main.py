from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import os
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import Help
from chatbot import ChatBot



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #second image

        img1=Image.open("C:/Users/HOME/Desktop/face_recognition_system/college_images/osmania_university.jpg")
        img1=img1.resize((1530,130), Image.BILINEAR)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1530,height=130)


        # first image
        img=Image.open("C:/Users/HOME/Desktop/face_recognition_system/college_images/ouce logo.png")
        img=img.resize((200,130), Image.BILINEAR)
        self.photoimg=ImageTk.PhotoImage(img)

        s_lbl=Label(f_lbl,image=self.photoimg)
        s_lbl.place(x=0,y=0,width=200,height=130)


        


        # #third image

        # img2=Image.open("C:/Users/HOME/Desktop/face_recognition_system/college_images/osmania_university.jpg")
        # img2=img2.resize((500,130), Image.BILINEAR)
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # f_lbl=Label(self.root,image=self.photoimg2)
        # f_lbl.place(x=900,y=0,width=500,height=130)


        #background image

        img3=Image.open("C:/Users/HOME/Desktop/face_recognition_system/college_images/peach color background.png")
        img3=img3.resize((1530,710), Image.BILINEAR)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=30)


        #==============================TIME====================================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)#1000 represents 1000ms=1second

        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=30)
        time()


        #student button

        img4=Image.open("college_images/student.jpg")
        img4=img4.resize((180,180), Image.BILINEAR)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=180,height=180)


        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=250,width=180,height=40)


        #Detect face button
        img5=Image.open("college_images/face_detector1.jpg")
        img5=img5.resize((180,180), Image.BILINEAR)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=180,height=180)


        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=250,width=180,height=40)


        #Attendance button
        img6=Image.open("college_images/attendance.jpg")
        img6=img6.resize((180,180), Image.BILINEAR)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=180,height=180)


        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=250,width=180,height=40)


        #help button
        img7=Image.open("college_images/chatIcon.jpg")
        img7=img7.resize((180,180), Image.BILINEAR)
        self.photoimg7=ImageTk.PhotoImage(img7)

        # b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_desk_data)
        # b1.place(x=1100,y=100,width=180,height=180)


        # b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_desk_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        # b1_1.place(x=1100,y=250,width=180,height=40)


        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.chatbot_data)
        b1.place(x=1100,y=100,width=180,height=180)


        b1_1=Button(bg_img,text="ChatBot (Help Desk)",cursor="hand2",command=self.chatbot_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=250,width=180,height=40)


        #Train faces button
        img8=Image.open("college_images/train faces.jpg")
        img8=img8.resize((180,180), Image.BILINEAR)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=320,width=180,height=180)


        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=470,width=180,height=40)



        #photos button
        img9=Image.open("college_images/photos.jpg")
        img9=img9.resize((180,180), Image.BILINEAR)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=320,width=180,height=180)


        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=470,width=180,height=40)


        #Developer button
        img10=Image.open("college_images/developer.jpg")
        img10=img10.resize((180,180), Image.BILINEAR)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=320,width=180,height=180)


        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=470,width=180,height=40)


        #Exit button
        img11=Image.open("college_images/exit.jpg")
        img11=img11.resize((180,180), Image.BILINEAR)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=320,width=180,height=180)


        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=470,width=180,height=40)


    def open_img(self):
        os.startfile("data")


    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Are you sure want to exit?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return



    #===========================Function Buttons=====================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)



    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)


    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)


    
    def help_desk_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    

    def chatbot_data(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)
        
        


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()