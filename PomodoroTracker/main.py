from tkinter import *


FontName = "Courier "

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224)
canvas.create_image(103, 112, image=tomato_img)
canvas.create_text(103, 130, text="00:00", fill="White", font=(FontName, 35, "bold"))

canvas.pack()

window.mainloop()