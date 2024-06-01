import tkinter as tk

def saludar():
    label.config(text="Hola Mundo")

root =tk.Tk()
root.title("Mi primera Aplicacion")
root.geometry("400x300")

label=tk.Label(root,text="Bienvenidos")
label.pack()
button= tk.Button(root, text="saludar", command=saludar)
button.pack()
root.mainloop()
