import tkinter as tk

main_menu = tk.Tk()


pikachu_gif =tk.PhotoImage(file= "pikachu-wave.gif")

main_menu_title = tk.Label(image=pikachu_gif,text="Pokedex Main-Menu", bg="black", fg= "red" )
main_menu_title.pack()

main_menu.mainloop()