from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",25,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1400,height=50)

        img_top=Image.open("college_images/developer.jpg")
        img_top=img_top.resize((1400,700), Image.BILINEAR)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1400,height=700)

        #=========FRAME==============
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=800,y=0,width=500,height=600)

        img_top1=Image.open("college_images/osmania_university.jpg")
        img_top1=img_top1.resize((200,200), Image.BILINEAR)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        s_lbl=Label(main_frame,image=self.photoimg_top1)
        s_lbl.place(x=300,y=0,width=200,height=200)


        #Developer Information
        dev_label=Label(main_frame,text="Hello!! My name is Bhavitha",font=("times new roman",18,"bold"),bg="white")
        dev_label.place(x=0,y=5)


        dev_label=Label(main_frame,text="I am full Stack developer",font=("times new roman",18,"bold"),bg="white")
        dev_label.place(x=0,y=40)


        img2=Image.open("college_images/developer_image.jpg")
        img2=img2.resize((500,300), Image.BILINEAR)
        self.photoimg2=ImageTk.PhotoImage(img2)

        t_lbl=Label(main_frame,image=self.photoimg2)
        t_lbl.place(x=0,y=200,width=500,height=300)



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()