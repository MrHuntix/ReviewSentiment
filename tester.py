import reccomenderModule as rm
from tkinter import *
from tkinter import filedialog

win = Tk()

def fileopen():
    file=filedialog.askopenfilename(parent=win,title="choose a file")
    s=""
    try:
        textread= [line for line in open(file,"r").readlines()]
        for i in textread:
            #s=s+i
            t1.insert("1.0",i)
    except :
        pass

def review():
   # f=open("ss.txt","r").read()
    
    out=""
    f=t1.get("1.0",END)
    p_c=0
    n_c=0
    words=[]
    positive_text=["good","great","excellent","satisfied","happy","easy","stylish","sleek","classic","well","compact","beautiful",
                   "excusite","improvement","definitely","absolutely","certainly","fantastic","marvelous","excellent","cool",
                   "helpful","enjoy","enjoyed","positive","happy","excited"
                   ]
    for review in f.split("\n"):
        if review=="":
            pass
        else:
            sentiment=rm.PosOrNeg(review)
            out=out+review+": "+sentiment+"\n"
            #print(review+": ",sentiment)
            if sentiment=="pos":
                words=[w for w in review.split() if w.lower() in positive_text ]
                p_c+=1
            else:
                n_c+=1

    out=out+"Positive reviews:"+str(p_c)+"\n"+"Negative reviews:"+str(n_c)+"\n"
    #print("Positive reviews:",p_c)
    #print("Negative reviews:",n_c)
    if p_c>n_c:
        out=out+"overall sentiment is positive"+"\n"
        #print("overall sentiment is positive")
    elif p_c<n_c:
        out=out+"overall sentiment is negative"+"\n"
        #print("overall sentiment is negative")
    else:
        out=out+"neutral feelings"+"\n"
        #print("neutral feelings")

    for i in words:
        out=""+"\n"+out+i+","

    t2.insert("1.0",out)

def clear():
    print("clear is pressed")
    t2.delete("1.0",END)
    t1.delete("1.0",END)
browse = Button(win, text="Browse",command = fileopen)
t1 = Text(win, width=150, height=5)
submit= Button(win, text='Submit', command = review)
clear=Button(win,text='Clear', command= clear)
t2 = Text(win, width=150, height=30)

t1.grid(row=0,column=0,columnspan=50)
browse.grid(row=7,column=0,columnspan=8)
submit.grid(row=7,column=10,columnspan=8)
clear.grid(row=7,column=20,columnspan=8)
t2.grid(row=10,column=0,columnspan=50)
win.mainloop()
