import tkinter as tk
from PIL import Image, ImageTk

class Main_Menu:
    def __init__(self):
        root = tk.Tk()
        root.title("Displaying Resized GIF")

        file = "pika-chu.gif"
        info = Image.open(file)

        frames = info.n_frames  # number of frames

        photoimage_objects = []
        for i in range(frames):
            info.seek(i)
            resized_image = info.resize((20, 20))  # Change the dimensions as needed
            obj = ImageTk.PhotoImage(resized_image)
            photoimage_objects.append(obj)


    def animation(self,photoimage_objects,gif_label,frames,root,animation,current_frame=0):
        global loop
        image = photoimage_objects[current_frame]

        gif_label.configure(image=image)
        current_frame = current_frame + 1

        if current_frame == frames:
            current_frame = 0

        loop = root.after(50, lambda: animation(current_frame))





    gif_label = tk.Label(root, image="")
    gif_label.pack()


    animation()
    root.mainloop()