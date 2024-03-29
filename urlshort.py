import pyperclip
import pyshorteners
from tkinter import *

root =Tk()
root.geometry("400x200")
root.title("Short Your URL")
root.configure(bg="#54ff95")
url = StringVar()
url_address = StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root, text="My Short URL", font="poppins").pack(fill=X)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generated", command = urlshortener).pack(pady=5)
Entry(root, textvariable = url_address).pack(pady=5)
Button(root, text="Copy URL", command = copyurl).pack(pady=5)

root.mainloop()
