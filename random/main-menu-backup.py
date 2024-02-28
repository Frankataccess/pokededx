#~~~~~~~~~~~~imports~~~~~~~~~~~~~~~~~
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#~~~~~~~~~~~~size variables~~~~~~~~~~~

# Window size
window_x = 300
window_y = 500

gif_x = 50
gif_y = 50

root = tk.Tk()
root.title("Main menu")
root.geometry(f"{window_x}x{window_y}")

#~~~~~~~~~~~~~image loaders~~~~~~~~~~~~~~

# Load and resize the Pokémon title image
pokemon_title_image = Image.open("International_Pokémon_logo.png")
pokemon_title_resized = pokemon_title_image.resize((window_x - 2 * gif_x, gif_y))
pokemon_title = ImageTk.PhotoImage(pokemon_title_resized)

# Load the Pikachu GIF
gif_file = "pika-chu.gif"
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

    loop = root.after(50, lambda: animation(current_frame))

#~~~~~~~~~~~~~~~~buttons~~~~~~~~~~~~~~~~~~~~~~~
# pokemon_button = (root,text = "Pokemon" )
# my_team_button = 
# account_button = 
# exit_button = 

#~~~~~~~~~~~~~~~~placements~~~~~~~~~~~~~~~~~~~

gif_label = tk.Label(root, image="")
gif_label.place(x=0, y=0)

pokemon_title_label = tk.Label(root, image=pokemon_title)
pokemon_title_label.place(x=gif_x, y=0)

gif_label_2 = tk.Label(root, image="")
gif_label_2.place(x=window_x - gif_x, y=0)  # Adjust the x-coordinate


#~~~~~~~~~~~~~~~run~~~~~~~~~~~~~~

animation()
root.mainloop()
