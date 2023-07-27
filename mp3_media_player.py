
import tkinter as Tk
from tkinter import *
import mysql.connector
from tkinter import messagebox
import pygame
from tkinter import filedialog
from tkinter import ttk

root1=Tk()       
root1.title("Welcome Page")
root1.geometry("1000x600+50+50")
root1.configure(background = "light blue")
Label(root1,text="LOOPMIX Mp3 Player",font=("Helvetica",50),fg="Red",width=46,bg="White",compound="center").pack(pady=50)
Label(root1,text="Bring Music to Life",font=("Helvetica",20),fg="White",width=100,bg="red",compound="center").pack(pady=100)

#Sign up
def signup():    
    def email_check_1(x,y):
                    val=False
                    for i in x:
                        if i in y:
                            val=True
                    return val
    def email_check_2(x,y):
                    val=False
                    for i in x:
                        if i in y:
                            val=True
                    return val
    def display(label):
                    label.pack()
                    root3.after(2000, destroy_widget, label)
    def destroy_widget(widget):
                    widget.destroy()
    def onclick_signup():
                
                    em_chk_1 = ["@"]
                    em_chk_2 = [".com"]

                    if name.get()!="":
                        if Gender.get()!="":
                            if email.get()!="":
                                if user_name.get()!="":
                                    if passw.get()!="":
                                        if name.get().isalpha() == True:
                                            if Gender.get() in ["M","F","NB"]:
                                                if email_check_1(em_chk_1,email.get()) and email_check_2(em_chk_2,email.get()):
                                                    if len(user_name.get()) > 4:
                                                        if (user_name.get().isalpha() == False) and (user_name.get().isdigit() == False):
                                                            if len(user_name.get().split())==1:
                                                                if len(passw.get()) > 4:
                                                                    if len(passw.get().split())==1:
                                                                        conn = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                                                                        cursor=conn.cursor()
                                                                        username = user_name.get()
                                                                        cursor.execute('SELECT username FROM users WHERE username = %(username)s', { 'username' : username })
                                                                        checkUsername = cursor.fetchone()
                                                                        print(checkUsername)
                                                                        conn.close()
                                                                        if checkUsername == None:
                                                                            conn = mysql.connector.connect(user="root", password="root", host='localhost', database='mp3player')
                                                                            cursor = conn.cursor()
                                                                            p = passw.get()
                                                                            cursor.execute('SELECT password FROM users WHERE password = %(password)s', { 'password' : p })
                                                                            checkpassword = cursor.fetchone()
                                                                            print(checkpassword)
                                                                            conn.close()
                                                                            if checkpassword == None:
                                                                                conn = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                                                                                cursor=conn.cursor()
                                                                                name_stored = name.get()
                                                                                gender_stored = Gender.get()
                                                                                email_stored = email.get()
                                                                                username_stored = user_name.get()
                                                                                passw_stored = passw.get()
                                                                                cursor.execute("insert into users values('"+str(name_stored)+"','"+str(gender_stored)+"','"+str(email_stored)+"','"+str(username_stored)+"','"+str(passw_stored)+"');")
                                                                                cursor.execute("insert into logininfo values('"+str(username_stored)+"','"+str(passw_stored)+"');")
                                                                                conn.commit()
                                                                                conn.close()
                                                                                messagebox.showinfo("DONE","sign up successful!")
                                                                                name.delete(0,END)
                                                                                Gender.delete(0,END)
                                                                                email.delete(0,END)
                                                                                user_name.delete(0,END)
                                                                                passw.delete(0,END)
                                                                                                                                                                
                                                                            else:
                                                                                a14 = Label(root3,text = "change password!(already taken)")
                                                                                display(a14)                                                                        
                                                                                
                                                                        else:
                                                                            a1 = Label(root3,text = "change username!(already taken)")
                                                                            display(a1)
                                                                            #user_name.delete(0,END)
                                                                    else:
                                                                        a13 = Label(root3,text = "no space in password!")
                                                                        display(a13)
                                                                else:
                                                                    a2 = Label(root3,text = "password: atleast 5 digits")
                                                                    display(a2)
                                                            else:
                                                                a15 = Label(root3,text = "no space in username!")
                                                                display(a15)
                                                        else:
                                                            a3 = Label(root3,text = "username should be alpha numeric")
                                                            display(a3)
                                                    else:
                                                        a4 = Label(root3,text = "username: atleast 5 digits")
                                                        display(a4)
                                                else:
                                                    a5 = Label(root3,text = "please check your email id")
                                                    display(a5)
                                            else:
                                                a6 = Label(root3,text = "please enter gender in the specified format")
                                                display(a6)
                                                Gender.delete(0,END)
                                        else:
                                            a7 = Label(root3,text = "name should be char only")
                                            display(a7)
                                    else:
                                        a8 = Label(root3,text = "please enter all values")
                                        display(a8)
                                else:
                                    a9 = Label(root3,text = "please enter all values")
                                    display(a9)
                            else:
                                a10 = Label(root3,text = "please enter all values")
                                display(a10)
                        else:
                            a11 = Label(root3,text = "please enter all values")
                            display(a11)
                    else:
                        a12 = Label(root3,text = "please enter all values")
                        display(a12)
                
    def signin():    #third window
        def display(label):
                    label.pack()
                    root2.after(2000, destroy_widget, label)
        def destroy_widget(widget):
                    widget.destroy()
        def onclick_signin():
            if user_name_main.get()!="":
                if passw_main.get()!="":
                         conn = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                         cursor=conn.cursor()
                         username = user_name_main.get()
                         cursor.execute('SELECT user_name FROM logininfo WHERE user_name = %(username)s', { 'username' : username })
                         checkUsername = cursor.fetchone()
                         print(checkUsername)
                         conn.close()
                         if checkUsername != None:
                             conn = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                             cursor=conn.cursor()
                             password = passw_main.get()
                             cursor.execute('SELECT user_name FROM logininfo WHERE password = %(password)s', { 'password' : password })
                             checkPassword = cursor.fetchone()
                             print(checkPassword)
                             conn.close()
                             if checkPassword == checkUsername:
                                     messagebox.showinfo("DONE","Sign In Success")
                                     root2.destroy()
                                     
                                     root = Tk()                 #fourth window
                                     root.title("MP3 Player")
                                     frame1 = Frame(root)
                                     #menu = Menu(frame1)
                                     root.geometry("600x500+200+100")
                                     root.configure(background = "light green")
                                     
                                     root.filename=""
                                     root.playlist = []
                                     root.pauseFlag = False
                                     root.songAdded = False
                                     root.i = 0

                                     def song_saved(file):
                                         
                                         #file = root.filename

                                         if file!='':                      #saving song name and info
                                             conn = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                                             cursor=conn.cursor()
                                                         
                                             cursor.execute('SELECT song_name FROM songs WHERE song_name = %(song)s', { 'song' : file })
                                             checkFile = cursor.fetchone()
                                             print(checkFile)
                                             conn.close()
                                             if checkFile==None:
                                                 conn = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                                                 cursor=conn.cursor()
                                                 file = root.playlist[root.i]
                                                 num = 1
                                                 cursor.execute("insert into songs values('"+str(file)+"','"+str(num)+"')")
                                                 print("saved")
                                                 conn.commit()
                                                 conn.close()
                                             else:
                                                 conn = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                                                 cursor=conn.cursor()
                                                 file = root.playlist[root.i]
                                                 cursor.execute("select played from songs where song_name= %(song)s", {'song': file })
                                                 num = cursor.fetchone()
                                                 print(num)
                                                 num2 = num[0] + 1
                                                 cursor.execute('update songs set played = %(count)s where song_name = %(song)s' , {'count': num2, 'song': file})
                                                 print("count updated")
                                                 conn.commit()
                                                 conn.close()
                                         else:
                                             status.set("select track first")

                                     def openFile():
                                         root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select your track",filetypes = (("mp3 Music Files","*.mp3"),("m4a Music Files","*.m4a")))
                                         root.playlist.append(root.filename)
                                         root.songAdded = True
                                         if root.filename!='':
                                             print(" Added " + root.filename)
                                             status.set("Press Play")
                                         else:
                                             status.set("select track first")
                                             
                                     def playMusic():
                                         
                                         if(root.filename == ""):
                                             status.set("Add a track first")
                                         else:
                                             try:
                                                 if(root.pauseFlag == True):
                                                     pygame.mixer.music.unpause()
                                                     print("playing")
                                                     status.set("Playing " + root.filename)
                                                     
                                                 elif(root.pauseFlag == False):
                                                     
                                                     pygame.mixer.init()
                                                     pygame.mixer.music.load(root.filename)
                                                     pygame.mixer.music.play()
                                                     status.set("Playing " + root.filename)
                                                     print("playing")
                                                     song_saved(root.filename)
                                                     
                                             except:
                                                 status.set("cant load track")
                                                 
                                     def pauseMusic():
                                         if(root.filename == ""):
                                             status.set("Add a track first")
                                         else:
                                             try:
                                                 print("paused")
                                                 pygame.mixer.music.pause()                 
                                                 root.pauseFlag = True
                                                 status.set("Paused")
                                             except:
                                                 status.set("cant load track")
                                                 
                                     def stopMusic():
                                         if(root.filename == ""):
                                             status.set("Add a track first")
                                         else:
                                             print("stopped")
                                             pygame.mixer.music.fadeout(500)
                                             status.set("ended")
                                             root.pauseFlag = False
                                             
                                     def end():
                                         root.destroy()
                                         exit()
                                         
                                     def help_me():
                                         messagebox.showinfo("Help","Read the following: \n *Select an mp3 file from the 'Open File' Option \n *Press on 'Play' button to play"
                                                             "\n *Press on 'Pause' button to pause \n *Press on 'Stop' button to Stop"
                                                             "\n *Select new song only after stopping"
                                                             "\n Make sure filetype is MP3")
                                         
                                     def delete():   #to delete existing account    #fifth B
                                         root5=Tk()
                                         root5.title("deletion")
                                         root5.geometry("400x300+400+100")
                                         root5.configure(background = "light blue")
                                         
                                         def back():          #back button
                                             root5.destroy()
                                         def display(label):
                                             label.pack()
                                             root.after(2000, destroy_widget, label)
                                         def destroy_widget(widget):
                                             widget.destroy()

                                         def done():
                                             if user5.get()!='':
                                                 #if password5.get()!='':
                                                     if user5.get()==username:
                                                         #if password5.get()==password:
                                                             
                                                             con = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                                                             cursor=con.cursor()
                                                             cursor.execute('SELECT user_name FROM logininfo WHERE user_name = %(username)s', { 'username' : username })
                                                             checkuser5 = cursor.fetchone()
                                                             con.close()
                                                             if checkuser5 != None:
                                                                 
                                                                 conn = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                                                                 cursor=conn.cursor()                                                                         
                                                                 cursor.execute('DELETE FROM users WHERE username = %(user)s', { 'user' : username })
                                                                 conn.commit()
                                                                 conn.close()
                                                                 messagebox.showinfo("DONE","Deletion Successful")
                                                                 root5.destroy()
                                                                 root.destroy()
                                                                 
                                                             else:
                                                                 q1 = Label(root5,text = "username does not exist")
                                                                 display(q1)
                                                     else:
                                                         q2 = Label(root5,text = "wrong current username")
                                                         display(q2)
                                             else:
                                                 q3 = Label(root5,text = "please enter value first")
                                                 display(q3)

                                         #fifth B window        
                                         Label(root5,text="Delete Account",font=("Helvetica",14),fg="red",bg="white",width=110).pack(pady=20)
                                         Label(root5,text="Current Username*",font=("Helvetica",10),fg="blue",bg="light blue").pack()
                                         user5 = Entry(root5)
                                         user5.pack()
                                         #Label(root4,text="Current Password*",font=("Helvetica",10),fg="Blue",bg="light blue").pack()
                                         #password5 = Entry(root4)
                                         #password5.pack()
                                         Button(root5,text="Save Changes",fg="white",bg="red",font=("algerian",10),command=done).pack()
                                         Button(root5,text="Back",fg="white",bg="red",font=("algerian",10),command=back).pack(pady=5)
                                         root5.mainloop()
                                         
                                         
                                         
                                     def update():        #to update existing account info  #fifth A window
                                         root4=Tk()
                                         root4.title("updation")
                                         root4.geometry("600x400+400+100")
                                         root4.configure(background = "light blue")

                                         def display(label):
                                             label.pack()
                                             root.after(2000, destroy_widget, label)
                                         def destroy_widget(widget):
                                             widget.destroy()
                                             
                                         def back():        #back button
                                             root4.destroy()
                                             
                                         def okay():
                                             if user_name_cu.get()!='':
                                                 if passw_cu.get()!='':
                                                     if user_name_cu.get()==username:
                                                         if passw_cu.get()==password:
                                                             
                                                             u = username_new.get()
                                                             p = passw_new.get()
                                                             u1 = user_name_cu.get()
                                                             
                                                             if username_new.get()!='':
                                                                 if (len(username_new.get())) > 4:
                                                                     if (username_new.get().isalpha() == False) and (username_new.get().isdigit() == False):
                                                                         if len(username_new.get().split())==1:
                                                                             if passw_new.get()!='':
                                                                                 if (len(passw_new.get())) > 4:
                                                                                     if len(passw_new.get().split())==1:
                                                                                         
                                                                                         conn = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                                                                                         cursor=conn.cursor()
                                                                                         cursor.execute('SELECT username FROM users WHERE username = %(username)s', { 'username' : u })
                                                                                         check_user = cursor.fetchone()
                                                                                         conn.close()
                                                                                         
                                                                                         if check_user==None:
                                                                                             conn = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                                                                                             cursor=conn.cursor()
                                                                                             cursor.execute('SELECT password FROM users WHERE password = %(password)s', { 'password' : p })
                                                                                             check = cursor.fetchone()
                                                                                             conn.close()

                                                                                             if check==None:
                                                                                                 conn = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                                                                                                 cursor=conn.cursor()
                                                                                                 cursor.execute("update users set username=('"+str(u)+"'), password =('"+str(p)+"') where username=('"+str(u1)+"');")
                                                                                                 cursor.execute("update logininfo set password=('"+str(p)+"') where user_name=('"+str(u)+"');")
                                                                                                 conn.commit()
                                                                                                 conn.close()
                                                                                                 messagebox.showinfo("DONE","Updation Successful")
                                                                                                 messagebox.showinfo("ALERT","SIGN IN AGAIN")
                                                                                                 root4.destroy()
                                                                                                 root.destroy()
                                                                                             else:
                                                                                                 p5 = Label(root4, text = "password already taken")
                                                                                                 display(p5)
                                                                                         else:
                                                                                             v1 = Label(root4, text = "username already taken")
                                                                                             display(v1)
                                                                                     else:
                                                                                         c1 = Label(root4, text = "no space in password!")
                                                                                         display(c1)
                                                                                 else:
                                                                                     f1 = Label(root4, text = "password: atleast 5 digits!")
                                                                                     display(f1)    
                                                                             else:
                                                                                 
                                                                                 if username_new.get()!='':
                                                                                     if (len(username_new.get())) > 4:
                                                                                         if (username_new.get().isalpha() == False) and (username_new.get().isdigit() == False):
                                                                                             if len(username_new.get().split())==1:
                                                                                                 conn = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                                                                                                 cursor=conn.cursor()
                                                                                                 cursor.execute('SELECT username FROM users WHERE username = %(username)s', { 'username' : u })
                                                                                                 check_user = cursor.fetchone()
                                                                                                 conn.close()
                                                                                                 if check_user==None:
                                                                                                     conn = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                                                                                                     cursor=conn.cursor()
                                                                                                     cursor.execute("update users set username=('"+str(u)+"') where username=('"+str(u1)+"');")
                                                                                                     conn.commit()
                                                                                                     conn.close()
                                                                                                     messagebox.showinfo("DONE","Updation Successful")
                                                                                                     messagebox.showinfo("ALERT","SIGN IN AGAIN")
                                                                                                     root4.destroy()
                                                                                                     root.destroy()
                                                                                                 else:
                                                                                                     p = Label(root4, text = "username already taken")
                                                                                                     display(p)
                                                                                             else:
                                                                                                 g = Label(root4, text = "no space in username!")
                                                                                                 display(g)
                                                                                         else:
                                                                                             c2 = Label(root4, text = "username must be alphanumeric")
                                                                                             display(c2)
                                                                                     else:
                                                                                         c3 = Label(root4, text = "username: atleast 5 digits")
                                                                                         display(c3)
                                                                                 else:
                                                                                     None
                                                                         else:
                                                                             z1 = Label(root4, text = "no space in username!")
                                                                             display(z1)
                                                                     else:
                                                                         c4 = Label(root4, text = "username must be alphanumeric")
                                                                         display(c4)
                                                                 else:
                                                                     c5 = Label(root4,text = "username: atleast 5 digits")
                                                                     display(c5)
                                                             else:
                                                                 if passw_new.get()!='':
                                                                     if (len(passw_new.get())) > 4:
                                                                         if (len(passw_new.get().split()))==1:
                                                                             conn = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                                                                             cursor=conn.cursor()
                                                                             cursor.execute('SELECT password FROM users WHERE password = %(password)s', { 'password' : p })
                                                                             check_1= cursor.fetchone()
                                                                             conn.close()
                                                                             if check_1==None:
                                                                                 conn = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                                                                                 cursor=conn.cursor()
                                                                                 cursor.execute("update users set password =('"+str(p)+"') where username=('"+str(u1)+"');")
                                                                                 cursor.execute("update logininfo set password=('"+str(p)+"') where user_name=('"+str(u1)+"');")
                                                                                 conn.commit()
                                                                                 conn.close()
                                                                                 messagebox.showinfo("DONE","Updation Successful")
                                                                                 messagebox.showinfo("ALERT","SIGN IN AGAIN")
                                                                                 root4.destroy()
                                                                                 root.destroy()
                                                                             else:
                                                                                 ad = Label(root4, text = "password already taken!")
                                                                                 display(ad)
                                                                         else:
                                                                             ad1 = Label(root4, text = "no space in password!")
                                                                             display(ad1)
                                                                         
                                                                     else:
                                                                         c6 = Label(root4, text = "password: atleast 5 digits")
                                                                         display(c6)
                                                                 else:
                                                                     None            
                                                         else:
                                                             p1 = Label(root4,text = "wrong current username")
                                                             display(p1)
                                                     else:
                                                         p2 = Label(root4, text="wrong current username")
                                                         display(p2)
                                                 else:
                                                     p3 = Label(root4, text = "please enter current password")
                                                     display(p3)
                                             else:
                                                 p4 = Label(root4, text = "please enter current username")
                                                 display(p4)
                                                 
                                         #fifth A window
                                         Label(root4,text="Update Account Details",font=("Helvetica",14),fg="red",bg="white",width=110).pack(pady=20)
                                         Label(root4,text="Current Username*",font=("Helvetica",10),fg="blue",bg="light blue").pack()
                                         user_name_cu = Entry(root4)
                                         user_name_cu.pack()
                                         Label(root4,text="Current Password*",font=("Helvetica",10),fg="Blue",bg="light blue").pack()
                                         passw_cu = Entry(root4)
                                         passw_cu.pack()
                                         Label(root4,text="New Username",font=("Helvetica",10),fg="Blue",bg="light blue").pack()
                                         username_new =Entry(root4)
                                         username_new.pack()
                                         Label(root4,text="OR",font=("Helvetica",10),fg="Blue",bg="light blue").pack()
                                         Label(root4,text="New Password",font=("Helvetica",10),fg="Blue",bg="light blue").pack()
                                         passw_new =Entry(root4)
                                         passw_new.pack()                                     
                                         Button(root4,text="Save Changes",fg="white",bg="red",font=("algerian",10),command=okay).pack()
                                         Button(root4,text="Back",fg="white",bg="red",font=("algerian",10),command=back).pack(pady=5)                           
                                    
                                         root4.mainloop()
                                         
                                     #fourth window    
                                     #---------Creating Menus----------    
                                     label = LabelFrame(root,text="Menu",font=("times new roman",15,"bold"),bg="light green",fg="black",bd=5,relief=GROOVE)
                                     label.place(x=50,y=50,width=500,height=150)
                                     b_1 = Button(label,text="OPEN FILE",command=openFile,width=10,height=1,
                                                  font=("times new roman",12,"bold"),
                                                  fg="white",bg="green").grid(row=0,column=1,padx=30,pady=5)
                                     b_2 = Button(label,text="HELP",command=help_me,width=10,height=1,
                                                  font=("times new roman",12,"bold"),
                                                  fg="white",bg="green").grid(row=0,column=2,padx=30,pady=5)
                                     b_3 = Button(label,text="LOGOUT",command=end,width=10,height=1,
                                                  font=("times new roman",12,"bold"),
                                                  fg="white",bg="green").grid(row=0,column=3,padx=30,pady=5)
                                     b1 = Button(label,text="UPDATE ACC",command=update,width=12,height=1,
                                                 font=("times new roman",12,"bold"),
                                                 fg="white",bg="green").grid(row=1,column=1,padx=20,pady=5)
                                     b2 = Button(label,text="DELETE ACC",command=delete,width=12,height=1,
                                                 font=("times new roman",12,"bold"),
                                                 fg="white",bg="green").grid(row=1,column=2,padx=20,pady=5)
                                     
                                     #global username
                                     one = Label(root, text=(tuple(("Hello!",))+tuple(("Welcome,",)) + checkUsername),font=("times new roman",15,"bold"), bg="light green",fg="black")
                                     one.pack(fill=X)

                                     #---------Various Buttons----------
                                     buttonframe = LabelFrame(root,text="Control Panel",font=("times new roman",15,"bold"),bg="light green",fg="black",bd=5,relief=GROOVE)
                                     buttonframe.place(x=50,y=230,width=500,height=100)
                                     button1 = Button(buttonframe,text="PLAY",command=playMusic,width=6,height=1,
                                                                                                        font=("times new roman",16,"bold"),
                                                                                                        fg="white",bg="green").grid(row=0,column=2,padx=40,pady=5)
                                     button2 = Button(buttonframe,text="PAUSE",command=pauseMusic,width=6,height=1,
                                                      font=("times new roman",16,"bold"),
                                                      fg="white",bg="green").grid(row=0,column=1,padx=40,pady=5)
                                     button3 = Button(buttonframe,text="STOP",command=stopMusic,width=6,height=1,
                                                      font=("times new roman",16,"bold"),
                                                      fg="white",bg="green").grid(row=0,column=3,padx=40,pady=5)
                                     #-----------The status Bar--------------
                                     label2 = LabelFrame(root,text="Song Track",font=("times new roman",15,"bold"),bg="light green",fg="black",bd=5,relief=GROOVE)
                                     label2.place(x=50,y=360,width=500,height=100)
                                     track = StringVar()
                                     status = StringVar()
                                     songtrack = Label(label2,textvariable=track,width=20,font=("times new roman",20),bg="light green",fg="dark green").grid(row=0,column=0,padx=5,pady=5)
                                     trackstatus = Label(label2,textvariable=status,font=("times new roman",15),bg="light green",fg="dark green").grid(row=0,column=0,padx=100,pady=5)
                                     status.set("~LOOPMIX PLAYER~")

                                     root.mainloop()
                                     
                             else:
                                 b1 = Label(root2,text = "incorrect password")
                                 display(b1)
                                 #passw_main.delete(0,END)
                                     
                         else:
                             b2 = Label(root2,text = "username doesn't exist")
                             display(b2)
                             #user_name_main.delete(0,END)
                else:
                    b3 = Label(root2,text = "please enter all values")
                    display(b3)
            else:
                b4 = Label(root2,text = "please enter all values")
                display(b4)
    
        #third window                 
        root3.destroy()
        root2=Tk()
        root2.title("Sign In")
        root2.geometry("600x400+300+100")
        root2.configure(background = "light blue")
        Label(root2,text="Welcome to Loopmix MP3 Player",font=("Helvetica",17),fg="Red",width=110,bg="White").pack(pady=50)
        Label(root2,text="Sign In",font=("Helvetica",17),fg="White",width=110,bg="red").pack()
        user_name_main = StringVar()
        passw_main = StringVar()
        Label(root2,text="Username*",font=("Helvetica",14),fg="blue", bg="light blue").pack()
        user_name_main=Entry(root2, textvariable = user_name_main)
        user_name_main.pack()
        Label(root2,text="Password*",font=("Helvetica",14),fg="Blue", bg="light blue").pack()
        passw_main=Entry(root2, textvariable = passw_main)
        passw_main.pack()
        Button(root2,text="Sign in",fg="white",bg="red",font=("algerian",10),command=onclick_signin).pack()
        

        def adminlogin():
            def display(label):
                label.pack()
                root6.after(2000, destroy_widget, label)
            def destroy_widget(widget):
                widget.destroy()
                
            def login():
                if admin_username.get()=="admin":
                    if admin_password.get()=="00000":
                        root6.destroy()
                        win = Tk()
                        win.geometry("1000x350")
                        style = ttk.Style()
                        style.theme_use('clam')
                        tree = ttk.Treeview(win, column=("Name", "Gender", "Email","Username","Password"), show='headings', height=10)
                        tree.column("# 1", anchor=CENTER)
                        tree.heading("# 1", text="Name")
                        tree.column("# 2", anchor=CENTER)
                        tree.heading("# 2", text="Gender")
                        tree.column("# 3", anchor=CENTER)
                        tree.heading("# 3", text="Email")
                        tree.column("# 4", anchor=CENTER)
                        tree.heading("# 4", text="Username")
                        tree.column("# 5", anchor=CENTER)
                        tree.heading("# 5", text="Password")

                        conn = mysql.connector.connect(user="root", password='root', host='localhost', database="mp3player")
                        cursor=conn.cursor()
                        cursor.execute("select * from users")
                        store = cursor.fetchall()
                    
                        for i in store:
                            tree.insert('', 'end', text="1", values = i)
                        conn.close()
                        tree.pack()
                        win.mainloop()
                        
                    else:
                        d1 = Label(root6,text = "wrong password")
                        display(d1)
                else:
                    d2 = Label(root6,text = "wrong username")
                    display(d2)
                        
            root6=Tk()
            root6.title("Admin Login")
            root6.geometry("400x300+400+100")
            root6.configure(background = "light blue")
            Label(root6,text="Admin Sign In",font=("Helvetica",17),fg="White",width=110,bg="red").pack()
            admin_user = StringVar()
            admin_pass = StringVar()
            Label(root6,text="Username*",font=("Helvetica",14),fg="blue", bg="light blue").pack()
            admin_username=Entry(root6, textvariable = admin_user)
            admin_username.pack()
            Label(root6,text="Password*",font=("Helvetica",14),fg="blue", bg="light blue").pack()
            admin_password=Entry(root6, textvariable = admin_pass)
            admin_password.pack()
            Button(root6,text="Sign in",fg="white",bg="red",font=("algerian",10),command= login).pack()

            
        Button(root2,text="Admin Access",fg="white",bg="red",font=("algerian",10),command=adminlogin).pack()


  
    root1.destroy()
    root3=Tk()
    root3.title("Sign Up")
    root3.geometry("900x600+100+50")
    root3.configure(background = "light blue")
    Label(root3,text="LOOPMIX MP3 Player Sign Up",font=("Helvetica",17),fg="Red",width=110,bg="White").pack(pady=50)
    Label(root3,text="Sign Up",font=("Helvetica",17),fg="White",width=110,bg="red").pack()
    Label(root3,text="Name*",font=("Helvetica",14),fg="blue", bg="light blue",compound="left").pack()
    name=Entry(width=30)
    name.pack()
    Label(root3,text="Gender(M/F/NB)",font=("Helvetica",14),fg="blue",bg="light blue").pack()
    Gender=Entry(width=30)
    Gender.pack()
    Label(root3,text="Email*",font=("Helvetica",14),fg="Blue",bg="light blue").pack()
    email=Entry(width=30)
    email.pack()
    Label(root3,text="Username*",font=("Helvetica",14),fg="blue",bg="light blue",).pack()
    user_name=Entry(width=30)
    user_name.pack()
    Label(root3,text="Password*",font=("Helvetica",14),fg="Blue", bg="light blue").pack()
    passw=Entry(width=30)
    passw.pack()
    Button(root3,text="Sign up",fg="white",bg="red",font=("algerian",10),command=onclick_signup).pack()
    Label(root3,text="Already have an account?",font=("Helvetica",10),fg="BLACK",bg="light blue",compound="center").pack(pady=5)    
    Button(root3,text="Sign in",fg="white",bg="red",font=("algerian",10),command=signin).pack()

        
Button(root1,text="START LISTENING",font=("algerian",18),fg="white",bg="Orange",compound="center",command=signup).pack(pady=20)


root1.mainloop()
