from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",25,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1400,height=50)

        img_top=Image.open("college_images/help desk.jpg")
        img_top=img_top.resize((1400,700), Image.BILINEAR)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1400,height=700)

        help_label=Label(f_lbl,text="Email: bhavitha.pandu30@gmail.com",font=("times new roman",18,"bold"),bg="lightgreen")
        help_label.place(x=500,y=0)



if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()