import tkinter as tk

window = tk.Tk()

greeting= tk.Label(text= "Hello, Tkinter")
greeting.pack()

clickable = tk.Button(text="BUTTON",foreground="red",background="black", width=100,height=10)
clickable.pack()

text_box = tk.Text(width=10,height=10)
text_box.pack()

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}
def button_click():
    print(button_click)

sunken_button = tk.Button(window, text="SUNKEN", relief="sunken", command=button_click)
raised_button = tk.Button(window, text="RAISED", relief="raised", command=button_click)
groove_button = tk.Button(window, text="GROOVE", relief="groove", command=button_click)

sunken_button.pack()
raised_button.pack()
groove_button.pack()


window.mainloop()