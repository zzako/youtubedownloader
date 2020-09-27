
from tkinter import *

from pytube import YouTube


root = Tk()
def download():
   try:
       myVar.set("Downloading...")
       root.update()
       YouTube(link.get()).streams.get_highest_resolution().download()
       link.set("Complete")
   except Exception as e:
      myVar.set("Error")
      root.update()
      link.set("Check your link")

def downloadAudio():
          try:
              myVar.set("Downloading...")
              root.update()
              YouTube(link.get()).streams.get_audio_only().download()
              link.set("Complete")
          except Exception as e:
              myVar.set("Error")
              root.update()
              link.set("Check your link")



myVar = StringVar()
myVar.set("Enter link Below:")
Entry(root, textvariable=myVar, width=40).pack(pady=10)
link = StringVar()
Entry(root, textvariable=link, width=40).pack(pady=10)
b = Button(root,
         text="Download Highest Quality",
         command=download,
           width=20)
b.pack(side=RIGHT)

b1 = Button(root ,
             text= "Download Audio Only",
             command=downloadAudio,
             width=20)
b1.pack(side=RIGHT)
root.configure(background='#000000')
root.mainloop()








