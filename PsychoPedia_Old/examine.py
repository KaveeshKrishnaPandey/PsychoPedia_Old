import tkinter as tk
    
root = tk.Tk()

# Window Settings
root.geometry('800x400+563+313')
root.minsize(800,400)
root.maxsize(800,400)
root.title('Know about your Disease')
root.config(bg='gray', highlightbackground='gray', highlightthickness=10)

behavioural = tk.BooleanVar
difficulty_focusing = tk.BooleanVar
anger = tk.BooleanVar

# Frames
f1 = tk.Frame(root, bg='light gray')
f2 = tk.Frame(f1, bg='light gray')
f3 = tk.Frame(f1, bg='light gray')

f1.pack(side='top')
f2.pack(side='top', fill='x')
f1.pack(side='top')


l1 = tk.Label(f2, text='Find Your Disease')

l2 = tk.Label(f2, text='Do you have Behavioural issues?')
b1 = tk.Button(f2, text='Yes')
b2 = tk.Button(f2, text='No')

l1.pack(side='top', fill='x', padx=5, pady=5)
l2.pack(side='top', fill='x', padx=5, pady=5)
b1.pack(side='left', padx=5, pady=5)
b2.pack(side='left', padx=5, pady=5)

root.mainloop()