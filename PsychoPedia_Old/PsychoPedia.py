import tkinter as tk
from PIL import ImageTk, Image
import webbrowser


def article():
    root = tk.Tk()
    root.iconbitmap('.\\icons\\icon.ico')
    root.title("PsychoPedia")
    root.geometry('600x550')
    root.minsize(600,550)
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

    def motivate():
        webbrowser.open('https://www.youtube.com/c/SandeepSeminars')

    def about():
        root = tk.Tk()
        root.title("About Us")
        root.geometry('600x150')
        root.minsize(600,300)
        root.config(bg='light yellow')

        with open('.\\Data\\About.txt') as f:
            adhd = f.read()

        f1 = tk.Frame(root, bg='light yellow')
        f2 = tk.Frame(f1, bg='light yellow')

        f1.pack(side='top')
        f2.pack(side='top')

        l1 = tk.Label(f2, bg='light green', text=adhd)

        l1.pack(side='left', expand=True, fill='both')

        root.mainloop()


    backGround = ImageTk.PhotoImage(Image.open('.\\backgrounds\\background_01.png').resize((300,300), Image.ANTIALIAS))

    f1 = tk.Frame(root, bg='light yellow')
    f2 = tk.Frame(f1, bg='light yellow')
    f3 = tk.Frame(f1, bg='light yellow')
    f4 = tk.Label(f1, bg='light yellow')

    f1.pack(side='top')
    f2.pack(side='top')
    f3.pack(side='top')
    f4.pack(side='left', expand=True, fill='both')

    main_menu = tk.Menu(root)
    m1 = tk.Menu(main_menu)
    m1.add_command(label='About', command=about)
    root.config(menu=main_menu)
    main_menu.add_cascade(label='File', menu=m1)

    l1 = tk.Label(f2, text="Diseases", bg='light green')
    b1 = tk.Button(f2, text="Anxiety Disorder", bg='light blue', command=anxiety)
    b2 = tk.Button(f2, text="ADHD", bg='light blue', command=adhd)
    b3 = tk.Button(f2, text="bipolar disorder", bg='light blue', command=bipolar)
    b4 = tk.Button(f3, text="Clinical Depressions", bg='light blue', command=clinical)
    b5 = tk.Button(f3, text="Post-Traumatic Stress Disorder", bg='light blue', command=ptsd)
    b6 = tk.Button(f3, text="Schizophrenia", bg='light blue', command=schizophrenia)
    l2 = tk.Label(f4, image=backGround, bg='gray')
    b7 = tk.Button(f4, text="Find Motivation Here (make sure you are connected to the internet)", bg='light blue', command=motivate)

    l1.pack(side='top', padx=5, pady=5)
    b1.pack(side='left', padx=5, pady=5)
    b2.pack(side='left', padx=5, pady=5)
    b3.pack(side='left', padx=5, pady=5)
    b4.pack(side='left', padx=5, pady=5)
    b5.pack(side='left', padx=5, pady=5)
    b6.pack(side='left', padx=5, pady=5)
    l2.pack(side='top', padx=5, pady=5)
    b7.pack(side='bottom', padx=5, pady=5)

    root.mainloop()

article()