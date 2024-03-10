from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


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



        self.search_by=StringVar()
        self.search_txt=StringVar()


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


        title_lbl=Label(s_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",15,"bold"),fg="darkblue")
        title_lbl.place(x=0,y=100,width=520,height=35)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=0,width=1500,height=600)


        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=0,width=650,height=550)

        img_left=Image.open("C:/Users/HOME/Desktop/face_recognition_system/college_images/students faces3.jpg")
        img_left=img_left.resize((720,130), Image.BILINEAR)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=637,height=130)


        #Current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",fg="green",relief=RIDGE,text="Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=130,width=637,height=120)



        #Department
        dep_label=Label(current_course_frame,text='Department',font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_department,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","CSE","AIML","Civil","ECE","BME","EEE","MECHANICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Course
        course_label=Label(current_course_frame,text='Course',font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=0,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","B.E","M.E")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=2,pady=10)



        #Year
        year_label=Label(current_course_frame,text='Year',font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
        year_combo["values"]=("Select Year","First year","Second year","Third year","Fourth year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester
        semester_label=Label(current_course_frame,text='Semester',font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="read only")
        semester_combo["values"]=("Select Semester","1st sem","2nd sem","3rd sem","4th sem","5th sem","6th sem","7th sem","8th sem")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)



        #Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",fg="green",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=637,height=275)


        #Student ID
        studentId_label=Label(class_student_frame,text='Student ID: ',font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_stdId,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)


        #Student name
        studentName_label=Label(class_student_frame,text='Student Name: ',font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_stdName,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,sticky=W)


        #Class Division
        class_div_label=Label(class_student_frame,text='Class Division: ',font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)


        division_combo=ttk.Combobox(class_student_frame,textvariable=self.var_division,font=("times new roman",12,"bold"),width=18,state="read only")
        division_combo["values"]=("A","B","C")
        division_combo.current(0)
        division_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #Roll No
        roll_no_label=Label(class_student_frame,text='Roll No: ',font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_rollNo,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,sticky=W)



        #Gender
        gender_label=Label(class_student_frame,text='Gender: ',font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Gender,font=("times new roman",12,"bold"),width=18,state="read only")
        gender_combo["values"]=("Female","Male","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)



        #DOB
        dob_label=Label(class_student_frame,text='Date Of Birth: ',font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_DOB,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,sticky=W)



        #Email
        email_label=Label(class_student_frame,text='Email: ',font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,sticky=W)



        #Phone no
        phone_no_label=Label(class_student_frame,text='Phone No: ',font=("times new roman",12,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,sticky=W)



        #Address
        address_label=Label(class_student_frame,text='Address: ',font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,sticky=W)


        #Teacher Name
        teacher_name_label=Label(class_student_frame,text='Teacher Name: ',font=("times new roman",12,"bold"),bg="white")
        teacher_name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_name_entry.grid(row=4,column=3,padx=10,sticky=W)


        #Radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)


        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)



        #Buttons Frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=200,width=620,height=24)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)


        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)



        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=225,width=620,height=24)


        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo",width=43,font=("times new roman",10,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)


        update_photo_btn=Button(btn_frame1,text="Update Photo",width=43,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)





        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=685,y=0,width=650,height=550)


        img_right=Image.open("C:/Users/HOME/Desktop/face_recognition_system/college_images/students faces.jpg")
        img_right=img_right.resize((720,130), Image.BILINEAR)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=637,height=130)



        #===============SEARCH SYSTEM===========================

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",fg="green",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=637,height=60)


        search_label=Label(Search_frame,text='Search By: ',font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=14,state="read only")
        search_combo["values"]=("Select ","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry=ttk.Entry(Search_frame,textvariable=self.search_txt,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,sticky=W)

        # search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold"))
        # search_entry.grid(row=0,column=2,padx=5,sticky=W)


        search_btn=Button(Search_frame,text="Search",command=self.search_data,width=13,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)


        showAll_btn=Button(Search_frame,text="Show All",command=self.fetch_data,width=13,font=("times new roman",10,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)


        #==================Table Frame=============================
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=195,width=637,height=330)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.student_table=ttk.Treeview(table_frame,column=("Department","Course","Year","Semester","ID","Name","Division","Roll No","Gender","DOB","Email","Phone No","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone No",text="Phone No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="Photo Sample Status")
        self.student_table["show"]="headings"


        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Division",width=100)
        self.student_table.column("Roll No",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone No",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #===========================Function declaration===============
    def add_data(self):
        if self.var_department.get()=="Select Department" or self.var_stdName.get()=="" or self.var_stdId.get()=="":
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        
        else:
            # messagebox.showinfo("Success","Welcome")
            try:
                conn=mysql.connector.connect(host="localhost",username="admin",password="panduga@333",database="face_recognizer")

                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_department.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_stdId.get(),
                    self.var_stdName.get(),
                    self.var_division.get(),
                    self.var_rollNo.get(),
                    self.var_Gender.get(),
                    self.var_DOB.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                        ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details Added Successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)




    #=====================fetch data from database===============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="admin",password="panduga@333",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()


        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    
    #=================get cursor==================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_department.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_stdId.set(data[4]),
        self.var_stdName.set(data[5]),
        self.var_division.set(data[6]),
        self.var_rollNo.set(data[7]),
        self.var_Gender.set(data[8]),
        self.var_DOB.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    #==============Update function=============
    def update_data(self):
        if self.var_department.get()=="Select Department" or self.var_stdName.get()=="" or self.var_stdId.get()=="":
            messagebox.showerror("Error", "All Fields are required",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="admin",password="panduga@333",database="face_recognizer")
                    my_cursor=conn.cursor()
                

                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,RollNo=%s,Gender=%s,DOB=%s,Email=%s,PhoneNo=%s,Address=%s,Teacher=%s,PhotoSample=%s where Id=%s",(
                                        self.var_department.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_stdName.get(),
                                        self.var_division.get(),
                                        self.var_rollNo.get(),
                                        self.var_Gender.get(),
                                        self.var_DOB.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get(),
                                        self.var_stdId.get()
                                ))
                else:
                    if not Update:
                        return
                    
                

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Students details updated successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)


    #==================DELETE function==================
    def delete_data(self):
        if self.var_stdId.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
            
        else:
            try:
                delete=messagebox.askyesno("Student Details Delete","Do you want to delete this student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="admin",password="panduga@333",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Id =%s"
                    val=(self.var_stdId.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            

            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)



    #================RESET function=============
    def reset_data(self):
        self.var_department.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_stdId.set("")
        self.var_stdName.set("")
        self.var_division.set("Select Division")
        self.var_rollNo.set("")
        self.var_Gender.set("Female")
        self.var_DOB.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    


    #=================Generate data set and take photo samples============
    def generate_dataset(self):
        if self.var_department.get()=="Select Department" or self.var_stdName.get()=="" or self.var_stdId.get()=="":
            messagebox.showerror("Error", "All Fields are required",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="admin",password="panduga@333",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                my_result=my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,RollNo=%s,Gender=%s,DOB=%s,Email=%s,PhoneNo=%s,Address=%s,Teacher=%s,PhotoSample=%s where Id=%s",(
                                    self.var_department.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.var_stdName.get(),
                                    self.var_division.get(),
                                    self.var_rollNo.get(),
                                    self.var_Gender.get(),
                                    self.var_DOB.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get(),
                                    self.var_teacher.get(),
                                    self.var_radio1.get(),
                                    self.var_stdId.get()==id+1
                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #==================Load pre defined data on face frontals from opencv===========================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #=======scaling factor=1.3
                    #=======minimum neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)


                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed successfully")

            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)




    #=======SEARCH DATA======================

    def search_data(self):
        conn=mysql.connector.connect(host="localhost",username="admin",password="panduga@333",database="face_recognizer")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from student where "+str(self.search_txt.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            conn.commit()
        conn.close()
            
    
    




if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()