import tkinter as tk

window = tk.Tk()

window.title("Snap Game")

window.geometry("500x500")
label = tk.Label(window, text="Hi", font=('Arial', 18))
label.pack()

window.mainloop()
