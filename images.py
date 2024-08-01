from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to Code at Codemy.com")
root.iconbitmap("images/python.ico")

load = Image.open("images/oreo.jpg")
width, height = load.size
new_width = int(width * 0.25)
new_height = int(height * 0.25)
resized_image = load.resize((new_width, new_height), Image.Resampling.LANCZOS)

my_img = ImageTk.PhotoImage(resized_image)
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()