import tkinter as tk

def yes():
    global yes
    root.destroy()

    yes = tk.Tk()
    yes.title("")

    yes = tk.Label(yes, text="Oh, Good to know", font=("Arial",50), fg="red")
    yes.pack(pady=10)

def maybe():
    global maybe
    root.destroy()

    maybe = tk.Tk()
    maybe.title("")

    maybe = tk.Label(maybe, text="ಥ_ಥ", font=("Arial",100), fg="red")
    maybe.pack(pady=10)

def no():
    global no
    root.destroy()

    no = tk.Tk()
    no.title("")

    no = tk.Label(no, text="Exactly, I don't too", font=("Arial",50), fg="red")
    no.pack(pady=10)

root = tk.Tk()
root.title("Choice")
root.geometry("500x350")

Choice = tk.Label(root, text="I've played this game before", font=("Arial", 25), bg="lightgray", relief="ridge", bd=10)
Choice.pack(pady=20)

but1 = tk.Button(root, text="Yes, I do", font=("Arial", 20), relief="raised", bd=5, cursor="hand2", command=yes)
but2 = tk.Button(root, text="Maybe", font=("Arial", 20), relief="raised", bd=5, cursor="hand2", command=maybe)
but3 = tk.Button(root, text="No, I don't", font=("Arial", 20), relief="raised", bd=5, cursor="hand2", command=no )
but1.pack(pady=10, anchor="e", padx=10)
but2.pack(pady=10, anchor="e", padx=10)
but3.pack(pady=10, anchor="e", padx=10)

root.mainloop()