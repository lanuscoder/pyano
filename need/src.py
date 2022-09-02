from tkinter import *
from pygame import mixer
tk = Tk()
tk.geometry("310x520")
fr1 = Frame(tk)
fr1.place(x =0,y=0)
list = ['Db','Eb']
list2 = ['Gb','Ab','Bb']
for i in 'CDEFGAB':
    def C(x = i):
        mixer.init()
        mixer.music.load(x + '4.mp3')
        mixer.music.play()
    b = Button(fr1,text = i,
                               height = 5,
                               width = 50,
                               bg ="white",
                               anchor = "w",command=C)
    b.pack()
x1 = 120
y1 = 58
for i in list:
    def C(x = i):
        mixer.init()
        mixer.music.load(x + '4.mp3')
        mixer.music.play()
    c = Button(tk,text = i,
                        height = 2,
                        width = 30,
                        bg = 'black',
                        fg = 'white',anchor ='w',
                        command = C)
    c.place (x = x1, y = y1)
    y1 = y1 + 75
x2 = 120
y2 = 283
for i in list2:
    def C(x = i):
        mixer.init()
        mixer.music.load(x + '4.mp3')
        mixer.music.play()
    c = Button(tk,text = i,
                        height = 2,
                        width = 30,
                        bg = 'black',
                        fg = 'white',anchor ='w',
                        command = C)
    c.place (x = x2, y = y2)
    y2 = y2 + 75
tk.mainloop()