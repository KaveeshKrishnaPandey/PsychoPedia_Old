import tkinter as tk
from tkinter import BOTH, messagebox as tmg
from turtle import left
from PIL import ImageTk, Image
import os

os.chdir("D:\ABHI\Programming\Comfest")

root = tk.Tk()

def article1():
    root = tk.Tk()
    root.title("Articles")
    root.geometry('600x150')
    root.minsize(600,300)
    root.config(bg='light yellow')

    def adhd():
        root = tk.Tk()
        root.title("ADHD")
        root.geometry('600x150')
        root.minsize(600,300)
        root.config(bg='light yellow')

        with open('.\\Data\\ADHD.txt') as f:
            adhd = f.read()

        f1 = tk.Frame(root, bg='light yellow')
        f2 = tk.Frame(f1, bg='light yellow')

        f1.pack(side='top')
        f2.pack(side='top')

        l1 = tk.Label(f2, bg='light green', text=adhd)

        l1.pack(side='left', expand=True, fill='both')

        root.mainloop()


    def anxiety():
        root = tk.Tk()
        root.title("Anxiety Disorder")
        root.geometry('600x150')
        root.minsize(600,300)
        root.config(bg='light yellow')

        with open('.\\Data\\Anxiety Disorder.txt') as f:
            adhd = f.read()

        f1 = tk.Frame(root, bg='light yellow')
        f2 = tk.Frame(f1, bg='light yellow')

        f1.pack(side='top')
        f2.pack(side='top')

        l1 = tk.Label(f2, bg='light green', text=adhd)

        l1.pack(side='left', expand=True, fill='both')

        root.mainloop()

    def bipolar():
        root = tk.Tk()
        root.title("Bipolar Disorder")
        root.geometry('600x150')
        root.minsize(600,300)
        root.config(bg='light yellow')

        with open('.\\Data\\bipolar disorder.txt') as f:
            adhd = f.read()

        f1 = tk.Frame(root, bg='light yellow')
        f2 = tk.Frame(f1, bg='light yellow')

        f1.pack(side='top')
        f2.pack(side='top')

        l1 = tk.Label(f2, bg='light green', text=adhd)

        l1.pack(side='left', expand=True, fill='both')

        root.mainloop()

    def clinical():
        root = tk.Tk()
        root.title("Clinical Depressions")
        root.geometry('600x150')
        root.minsize(600,300)
        root.config(bg='light yellow')

        with open('.\\Data\\Clinical Depressions.txt') as f:
            adhd = f.read()

        f1 = tk.Frame(root, bg='light yellow')
        f2 = tk.Frame(f1, bg='light yellow')

        f1.pack(side='top')
        f2.pack(side='top')

        l1 = tk.Label(f2, bg='light green', text=adhd)

        l1.pack(side='left', expand=True, fill='both')

        root.mainloop()

    def ptsd():
        root = tk.Tk()
        root.title("Post-Traumatic Stress Disorder (PTSD)")
        root.geometry('600x150')
        root.minsize(600,300)
        root.config(bg='light yellow')

        with open('Data\\Post-Traumatic Stress Disorder (PTSD).txt') as f:
            adhd = f.read()

        f1 = tk.Frame(root, bg='light yellow')
        f2 = tk.Frame(f1, bg='light yellow')

        f1.pack(side='top')
        f2.pack(side='top')

        l1 = tk.Label(f2, bg='light green', text=adhd)

        l1.pack(side='left', expand=True, fill='both')

        root.mainloop()

    def schizophrenia():
        root = tk.Tk()
        root.title("Schizophrenia")
        root.geometry('600x150')
        root.minsize(600,300)
        root.config(bg='light yellow')

        with open('.\\Data\\Schizophrenia.txt') as f:
            adhd = f.read()

        f1 = tk.Frame(root, bg='light yellow')
        f2 = tk.Frame(f1, bg='light yellow')

        f1.pack(side='top')
        f2.pack(side='top')

        l1 = tk.Label(f2, bg='light green', text=adhd)

        l1.pack(side='left', expand=True, fill='both')

        root.mainloop()


    backGround = ImageTk.PhotoImage(Image.open('.\\backgrounds\\background_02.png').resize((300,300), Image.ANTIALIAS))

    f1 = tk.Frame(root, bg='light yellow')
    f2 = tk.Frame(f1, bg='light yellow')
    f3 = tk.Frame(f1, bg='light yellow')
    f4 = tk.Label(f1, bg='light yellow')

    f1.pack(side='top')
    f2.pack(side='top')
    f3.pack(side='top')
    f4.pack(side='left', expand=True, fill='both')

    l1 = tk.Label(f2, text="Diseases", bg='light green')
    b1 = tk.Button(f2, text="Anxiety Disorder", bg='light blue', command=anxiety)
    b2 = tk.Button(f2, text="ADHD", bg='light blue', command=adhd)
    b3 = tk.Button(f2, text="bipolar disorder", bg='light blue', command=bipolar)
    b4 = tk.Button(f3, text="Clinical Depressions", bg='light blue', command=clinical)
    b5 = tk.Button(f3, text="Post-Traumatic Stress Disorder", bg='light blue', command=ptsd)
    b6 = tk.Button(f3, text="Schizophrenia", bg='light blue', command=schizophrenia)
    l2 = tk.Label(f4, image=backGround, bg='gray')

    l1.pack(side='top', padx=5, pady=5)
    b1.pack(side='left', padx=5, pady=5)
    b2.pack(side='left', padx=5, pady=5)
    b3.pack(side='left', padx=5, pady=5)
    b4.pack(side='left', padx=5, pady=5)
    b5.pack(side='left', padx=5, pady=5)
    b6.pack(side='left', padx=5, pady=5)
    l2.pack(side='top', padx=5, pady=5)


    root.mainloop()

def runArticle():
    article1()

root.title('Mentle Health')
# root.iconbitmap('.\\Paint.ico') 
root.geometry('600x150')
root.minsize(600,500)
root.maxsize(600,500)
root.config(bg='light blue')

# Images
article = ImageTk.PhotoImage(Image.open(".\\icons\\article.png").resize((100,100), Image.ANTIALIAS))
news = ImageTk.PhotoImage(Image.open('.\\icons\\newspaper.png').resize((100,100), Image.ANTIALIAS))
motivation = ImageTk.PhotoImage(Image.open('.\\icons\\fire.png').resize((100,100), Image.ANTIALIAS))
fyd = ImageTk.PhotoImage(Image.open('.\\icons\\checklist.png').resize((100,100), Image.ANTIALIAS))
kayd = ImageTk.PhotoImage(Image.open('.\\icons\\newspaper.png').resize((100,100), Image.ANTIALIAS))
backGround = ImageTk.PhotoImage(Image.open('.\\backgrounds\\BACKGROUND_01.png').resize((300,300), Image.ANTIALIAS))

# Frames
f1 = tk.Frame(root, bg='light blue')
f2 = tk.Frame(f1, bg='light blue', borderwidth=1, relief="ridge")
f3 = tk.Frame(f1, bg='light blue', borderwidth=1, relief="ridge")
f3 = tk.Frame(f1, bg='light blue', borderwidth=1, relief="ridge")
f4 = tk.Frame(root, bg='light blue')

f1.pack(side='top', fill='x')
f2.pack(side='left', padx=5, pady=5)
f3.pack(side='left', padx=5, pady=5)
f4.pack(side='top', padx=5, pady=5)

# Widgets
l1 = tk.Label(f2, text='Education Section', bg='light blue')
b1 = tk.Button(f2, image=article, command=runArticle)
b2 = tk.Button(f2, image=news)
b3 = tk.Button(f2, image=motivation)

l2 = tk.Label(f3, text='Examine Section', bg='light blue')
b4 = tk.Button(f3, image=fyd)
b5 = tk.Button(f3, image=news)
l3 = tk.Label(f4, image=backGround)

l1.pack(side='top', padx=5, pady=5)
b1.pack(side='left', padx=5, pady=5)
b2.pack(side='left', padx=5, pady=5)
b3.pack(side='left', padx=5, pady=5)

l2.pack(side='top', padx=5, pady=5)
b4.pack(side='left', padx=5, pady=5)
b5.pack(side='left', padx=5, pady=5)
l3.pack(side='top')

root.mainloop()