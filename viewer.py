from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learn to Code at Codemy.com")
root.iconbitmap("images/python.ico")

load = Image.open("images/oreo.jpg")
width, height = load.size
new_width = int(width * 0.10)
new_height = int(height * 0.10)
resized_image1 = load.resize((new_width, new_height), Image.Resampling.LANCZOS)

load = Image.open("images/snow.jpg")
width, height = load.size
new_width = int(width * 0.10)
new_height = int(height * 0.10)
resized_image2 = load.resize((new_width, new_height), Image.Resampling.LANCZOS)

load = Image.open("images/disney.jpg")
width, height = load.size
new_width = int(width * 0.10)
new_height = int(height * 0.10)
resized_image3 = load.resize((new_width, new_height), Image.Resampling.LANCZOS).rotate(-90, Image.NEAREST, expand = 1)

load = Image.open("images/plastic1.jpg")
width, height = load.size
new_width = int(width * 0.10)
new_height = int(height * 0.10)
resized_image4 = load.resize((new_width, new_height), Image.Resampling.LANCZOS)

load = Image.open("images/plastic2.jpg")
width, height = load.size
new_width = int(width * 0.10)
new_height = int(height * 0.10)
resized_image5 = load.resize((new_width, new_height), Image.Resampling.LANCZOS)

my_img1 = ImageTk.PhotoImage(resized_image1)
my_img2 = ImageTk.PhotoImage(resized_image2)
my_img3 = ImageTk.PhotoImage(resized_image3)
my_img4 = ImageTk.PhotoImage(resized_image4)
my_img5 = ImageTk.PhotoImage(resized_image5)

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    
    if image_number == 5:
         button_forward = Button(root, text=">>", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    
    if image_number == 1:
         button_back = Button(root, text="<<", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()