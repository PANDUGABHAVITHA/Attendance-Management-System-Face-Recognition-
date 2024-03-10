from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",25,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1400,height=35)

        img_top=Image.open("college_images/osmania_university.jpg")
        img_top=img_top.resize((1400,325), Image.BILINEAR)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=35,width=1400,height=325)


        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="black",fg="white")
        b1_1.place(x=0,y=325,width=1400,height=100)


        img_bottom=Image.open("college_images/students faces3.jpg")
        img_bottom=img_bottom.resize((1400,325), Image.BILINEAR)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=425,width=1400,height=325)


    #=========Used LBPH algorithm to train the dataset=================
    #LBPH -> Local Binary Pattern Histograms
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]
        #Images of the same person must have the same ID.
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            #the above line converts image to Gray scale image (L)
            #uint8 is a datatype used for array

            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            #C:\Users\HOME\Desktop\face_recognition_system\data\    user.1.1.jpg
            #------------------------Index=0--------------------====--Index=1---


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training the data",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)

        #===============Train the classifier and save===========================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)

        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")





            


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()