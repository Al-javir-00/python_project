import tkinter as t
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text = "type",src="English",dest="Benglie"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans_1 = trans.translate(text,src = src1,dest = dest1)
    return trans_1.text

def data():
    sx = combo.get()
    dy = combo_1.get()
    msg = s.get("1.0",'end-1c')
    textget = change(text = msg, src = sx, dest=dy) 
    s_1.delete("1.0",'end-1c')
    s_1.insert('end-1c', textget)



a = t.Tk()
a.title("Translator")
a.geometry("500x800")
#a.config(bg="white")
i = t.PhotoImage(file = "i.png")
l = t.Label(image=i)
l.pack()

#a.wm_attributes('-transparentcolor','white')
l = t.Label(a,text="Tanslator",font=("Time New Roman",20, "bold"))
l.place(x = 80,y = 15,height=100,width=300)

f = t.Frame(a).pack(side="bottom")

l_2 = t.Label(a,text="Source",font=("Time New Roman",15),bg="white",fg="red")
l_2.place(x = 40,y = 120,height=25,width=70)

s = t.Text(f,font=("Time New Roman",20),wrap="word",bg="red",fg= "white")
s.place(x=38, y=150,height=80,width=420)

list_t = list(LANGUAGES.values())
combo = ttk.Combobox(f,values=list_t)
combo.place(x = 39, y= 240,height=30,width=80)
combo.set("english")

combo_1 = ttk.Combobox(f,values=list_t)
combo_1.place(x = 379, y= 240,height=30,width=80)
combo_1.set("bengali")

b_1 = t.Button(f,text ="Tanslate",command=data)
b_1.place(x = 180, y= 240,height=30,width=80)






l_3 = t.Label(a,text="you",font=("Time New Roman",15),bg="white",fg="red")
l_3.place(x = 30,y = 420,height=25,width=70)

s_1 = t.Text(f,font=("Time New Roman",20),wrap="word",bg="red",fg="white")
s_1.place(x=38, y=460,height=90,width=420)

b_e = t.Button(a,text="Press for Exit",width=30,height=1,command=a.destroy,bg="white",fg="red")
b_e.place(x = 180, y = 700, height=40, width=100)


a.mainloop()