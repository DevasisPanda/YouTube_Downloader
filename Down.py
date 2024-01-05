import tkinter
import customtkinter
from pytube.__main__ import YouTube

def startDownload():
    try:
       ytLink=link.get()
       ytObject = YouTube(ytLink)
       video = ytObject.streams.get_lowest_resolution()
       video.download()
    except:
       print("Youtube link is invalid")
    print("Download Complete!")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app=customtkinter.CTk()
app.geometry("720X400")
app.title("Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)
#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()
#DownLoad Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10,pady=10)


app.mainloop()