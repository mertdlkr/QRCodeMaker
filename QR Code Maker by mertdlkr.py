import qrcode
from tkinter import *
from PIL import Image, ImageTk


def generate_qr():
    data = entry.get()
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")
    img = Image.open("qr_code.png")
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img


def exit_button():
    root.quit()


root = Tk()
root.geometry("650x600")
root.minsize(500, 550)
root.title("QR Code Generator by mertdlkr")
root.configure(background="red")

label = Label(root, text="Enter the link:", font=("Arial", 25))
label.pack()

entry = Entry(root, width=35)
entry.pack(pady=20)

button = Button(root, text="Generate QR Code", command=generate_qr)
button.pack()


button4 = Button(
    root,
    command=exit_button,
    text="Exit",
    font=("Arial"),
    bg="black",
    fg="white",
).pack(pady=30)

qr_label = Label(root)
qr_label.pack()

root.mainloop()
