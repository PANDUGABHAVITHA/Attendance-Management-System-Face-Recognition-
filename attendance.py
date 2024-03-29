from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]#=====Global variable

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #=================variables====================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        #============Variables===============
        self.var_department=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_stdId=StringVar()
        self.var_stdName=StringVar()
        self.var_division=StringVar()
        self.var_rollNo=StringVar()
        self.var_Gender=StringVar()
        self.var_DOB=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        # first image
        img=Image.open("C:/Users/HOME/Desktop/face_recognition_system/college_images/students faces.jpg")
        img=img.resize((500,130), Image.BILINEAR)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        #second image

        img1=Image.open("college_images/student faces left frame.jpg")
        img1=img1.resize((500,130), Image.BILINEAR)
        self.photoimg1=ImageTk.PhotoImage(img1)

        s_lbl=Label(self.root,image=self.photoimg1)
        s_lbl.place(x=500,y=0,width=500,height=130)


        #third image

        img2=Image.open("college_images/students faces1.jpg")
        img2=img2.resize((500,130), Image.BILINEAR)
        self.photoimg2=ImageTk.PhotoImage(img2)

        t_lbl=Label(self.root,image=self.photoimg2)
        t_lbl.place(x=1000,y=0,width=500,height=130)


        #background image

        img3=Image.open("C:/Users/HOME/Desktop/face_recognition_system/college_images/peach color background.png")
        img3=img3.resize((1530,710), Image.BILINEAR)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(s_lbl,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",15,"bold"),fg="darkblue")
        title_lbl.place(x=0,y=100,width=520,height=35)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=0,width=1500,height=600)


        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=0,width=650,height=550)

        img_left=Image.open("college_images/students faces3.jpg")
        img_left=img_left.resize((720,130), Image.BILINEAR)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=637,height=130)


        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=132,width=638,height=390)

        #Label and entry

        #Attendance ID
        AttendanceId_label=Label(left_inside_frame,text='Attendance ID: ',font=("times new roman",12,"bold"),bg="white")
        AttendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        AttendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        AttendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #Roll No
        roll_label=Label(left_inside_frame,text='Roll No: ',font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #Name
        name_label=Label(left_inside_frame,text='Name: ',font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #Department
        department_label=Label(left_inside_frame,text='Department: ',font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        department_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #Time
        time_label=Label(left_inside_frame,text='Time: ',font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #Date
        date_label=Label(left_inside_frame,text='Date: ',font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        atten_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #Attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance Status",bg="white",font=("times new roman",12,"bold"))
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=18,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=5)
        self.atten_status.current(0)


        #Buttons Frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=325,width=620,height=60)

        importcsv_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=15,height=2,font=("times new roman",13,"bold"),bg="blue",fg="white")
        importcsv_btn.grid(row=0,column=0)


        exportcsv_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=15,height=2,font=("times new roman",13,"bold"),bg="blue",fg="white")
        exportcsv_btn.grid(row=0,column=1)


        update_btn=Button(btn_frame,text="Update",width=15,height=2,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,height=2,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)



        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=685,y=0,width=650,height=550)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=3,width=638,height=518)



        #======================SCROLL BAR TABLE===============================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)



        self.AttendanceReportTable.pack(fill=BOTH,expand=1)


        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    #=======================FETCH DATA===================================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    #========Import csv==============
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)




    #========Export csv==============
    def exportCsv(self):
        try:
            #if no data
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")

        except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])



    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()