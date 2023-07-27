import tkinter as tk
from pygame import mixer,time

class PlayMusic:
    def __init__(self):
        
        self.win=tk.Tk()
        self.win.geometry('500x500')
        self.win.title("SMASH MUSIC - MP3 PLAYER")
        
        self.lbl=tk.Label(self.win,text='enter your path',font=('Calibri',14,'bold')).grid(row=0,column=0)
        self.ent=tk.Entry(self.win,width=25)
        self.ent.grid(row=0,column=1)
        
        button1 = tk.Button( self.win, text = "  ▶  ", font=("Calibri",11),command=self.start).grid(row = 2,column = 1) 
        button2 = tk.Button( self.win, text = " ⏸ ", font=("Calibri",11),command=self.stop).grid(row = 2,column = 0) 
        button3 = tk.Button( self.win, text = "REPLAY", font=("Calibri",9)).grid(row = 1,column = 0) 
        button4 = tk.Button( self.win, text = "  ⏭  ", font=("Calibri",12)).grid(row = 1,column = 1) 
        button5 = tk.Button( self.win, text = "  ⏮  ", font=("Calibri",12)).grid(row = 1,column = 2) 
        button6= tk.Button( self.win, text = "EXIT", font=("Calibri",11)).place(x = 100, y= 100) 

        self.win.mainloop()

    def start(self):
        path = str(self.ent.get())
        mixer.init()
        mixer.music.set_volume(0.2)
        mixer.music.load(path)
        mixer.music.play()
        #while mixer.music.get_busy():
            #time.Clock().tick(1)

    def stop(self):
        mixer.music.stop()


PlayMusic()
