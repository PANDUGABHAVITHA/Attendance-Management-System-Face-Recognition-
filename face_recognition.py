from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",25,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1400,height=35)

        #first image
        img_top=Image.open("college_images/face_detector1.jpg")
        img_top=img_top.resize((800,700), Image.BILINEAR)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=35,width=800,height=700)

        #second image
        img_side=Image.open("college_images/face.jpg")
        img_side=img_side.resize((600,700), Image.BILINEAR)
        self.photoimg_side=ImageTk.PhotoImage(img_side)

        s_lbl=Label(self.root,image=self.photoimg_side)
        s_lbl.place(x=800,y=35,width=600,height=700)

        #button
        b1_1=Button(s_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=190,y=26,width=210,height=80)


    #======================== ATTENDANCE ======================================
        
    def mark_attendance(self,i,r,n,d):
        todays_date=datetime.now()
        temp_date=0
        with open("attendance_sheet.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]

            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
                # name_list.append(todays_date)
                
            
            # if (temp_date not in todays_date and (i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)) :
            
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):

                temp_date=datetime.now()
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")





    #=============FACE RECOGNITION================================
        
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))


                conn=mysql.connector.connect(host="localhost",username="admin",password="panduga@333",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)#concatenate

                my_cursor.execute("select RollNo from student where Id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)#concatenate

                my_cursor.execute("select Department from student where Id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)#concatenate

                my_cursor.execute("select Id from student where Id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)#concatenate


                if confidence>77:
                    cv2.putText(img,f"Student ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    self.mark_attendance(i,r,n,d)
                
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)#for camera
        #video_cap=cv2.VideoCapture(1)-> for other

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()