import tkinter as tk

def show_window():
    root = tk.Tk()
    root.title("pyiba GUI")
    root.geometry("400x300")
    label = tk.Label(root, text="pyiba GUI ウィンドウ", font=("Arial", 16))
    label.pack(pady=40)
    root.mainloop()
