import tkinter as tk

from PIL import Image, ImageTk

window = tk.Tk()
window.title("Hello world")
window.geometry("300x300")

label = "Guess who?"

def showImage():
  person = text.get("1.0", "end")
  if person.lower().strip() == "mo":
    canvas.itemconfig(container, image = mo)
  if person.lower().strip() == "charlotte":
    canvas.itemconfig(container, image = charlotte)
  elif person.lower().strip() == "gerald":
    canvas.itemconfig(container, image = gerald)
  elif person.lower().strip() == "katie":
    canvas.itemconfig(container, image = katie)
  else:
    canvas.pack_forget()
    Warning.pack()
    return
  Warning.pack_forget()
  canvas.pack()


hello = tk.Label(text=label)
hello.pack()

Warning = tk.Label(text="Unable to find this user")
text = tk.Text(window, height = 1, width = 30)
text.pack()
button = tk.Button(text = "Find", command = showImage)
button.pack()

canvas = tk.Canvas(window, width = 300, height = 150)
canvas.pack()
charlotte = ImageTk.PhotoImage(Image.open ("Guess Who/charlotte.jpg"))
gerald = ImageTk.PhotoImage(Image.open ("Guess Who/gerald.jpg"))
katie = ImageTk.PhotoImage(Image.open ("Guess Who/katie.jpg"))
mo = ImageTk.PhotoImage(Image.open ("Guess Who/mo.jpg"))
container = canvas.create_image(150,1,image = mo)


tk.mainloop()


