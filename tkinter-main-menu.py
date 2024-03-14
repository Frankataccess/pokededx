#~~~~~~~~~~~~imports~~~~~~~~~~~~~~~~~
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from settings import *

def main_menu_run ():

    #~~~~~~~~~~~~size variables~~~~~~~~~~~


    main_menu = tk.Tk()
    main_menu.title("Main menu")
    main_menu.geometry(f"{window_x}x{window_y}")

    #~~~~~~~~~~~~~image loaders~~~~~~~~~~~~~~

    # Load and resize the Pokémon title image
    pokemon_title_image = Image.open(file_path + "International_Pokémon_logo.png")
    pokemon_title_resized = pokemon_title_image.resize((window_x - 2 * gif_x, gif_y))
    pokemon_title = ImageTk.PhotoImage(pokemon_title_resized)

    # Load the Pikachu GIF
    gif_file = (file_path + "pika-chu.gif")
    info = Image.open(gif_file)
    frames = info.n_frames

    photoimage_objects = []
    for i in range(frames):
        info.seek(i)
        resized_image = info.resize((gif_x, gif_y))
        obj = ImageTk.PhotoImage(resized_image)
        photoimage_objects.append(obj)

    #~~~~~~~~~~~~~animation~~~~~~~~~~~~~~~~~~~~~

    def animation(current_frame=0):
        global loop
        image = photoimage_objects[current_frame]

        gif_label.configure(image=image)
        gif_label_2.configure(image=image)  # Update gif_label_2 with the current frame
        current_frame = (current_frame + 1) % frames

        loop = main_menu.after(50, lambda: animation(current_frame))

    #~~~~~~~~~~~~~~title~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    title = tk.Label(main_menu,text="Main Menu", font=custom_font,height=20,width=20,)


    #~~~~~~~~~~~~~~~~button functions~~~~~~~~~~~~~~
    def pokemon_menu():
        main_menu.quit()

    def  my_team_menu ():
        main_menu.quit

    def account_menu ():
        main_menu.quit()

    def exit_command():
        main_menu.quit()

    #~~~~~~~~~~~~~~~~buttons~~~~~~~~~~~~~~~~~~~~~~~
    pokemon_button = tk.Button(main_menu,text = "Pokemon", relief= "raised", command= pokemon_menu, width= button_x, height=button_y, bg = "blue" )
    my_team_button = tk.Button(main_menu,text = "My Team", relief= "raised", command= my_team_menu, width= button_x, height=button_y,bg = "yellow")
    account_button = tk.Button(main_menu,text = "Account", relief= "raised", command= account_menu, width= button_x, height=button_y, bg = "green")
    exit_button = tk.Button(main_menu,text = "Exit", relief= "raised", command= exit_command, width= button_x, height=button_y ,bg = "pink" )

    #~~~~~~~~~~~~~~~~placements~~~~~~~~~~~~~~~~~~~

    gif_label = tk.Label(main_menu, image="")
    gif_label.place(x=0, y=0) 

    pokemon_title_label = tk.Label(main_menu, image=pokemon_title)
    pokemon_title_label.place(x=gif_x, y=0)

    gif_label_2 = tk.Label(main_menu, image="")
    gif_label_2.place(x=window_x - gif_x, y=0)  # Adjust the x-coordinate

    title.place(x = (window_x - (gif_x * 4))  / 2, y = -(0.5 * window_y) + gif_y + 20)

    pokemon_button.place(x= (window_x - (gif_x * 4)) / 2 , y= 100)
    my_team_button.place(x= (window_x - (gif_x * 4)) / 2 ,y=100 + (button_y * 2))
    account_button.place(x= (window_x - (gif_x * 4)) / 2 ,y=1)
    exit_button.place(x= (window_x - (gif_x * 2)) / 2 + 20 ,y=1)

    #~~~~~~~~~~~~~~~run~~~~~~~~~~~~~~

    animation()
    main_menu.mainloop()

main_menu_run()