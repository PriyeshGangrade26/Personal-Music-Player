#Importing Necessary Modules
import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

#creating window (interface) for player
musicplayer = tkr.Tk()


#adding title for interface
musicplayer.title("Music Player")


#setting dimensions of tkinter window
musicplayer.geometry('650x550')


#Asking for music directory
directory = askdirectory()

#Setting Music Directory to the Current Working Directory
os.chdir(directory)

#Creating our Song List
songlist = os.listdir()
#Creating the Playlist
playlist = tkr.Listbox(musicplayer, font ="Cambria 14 bold", bg="black", fg="white", selectmode = tkr.SINGLE)

#Addding songs from songlist to playlist
for item in songlist:
    pos=0
    playlist.insert(pos, item)
    pos = pos + 1
#initialising Modules 
pygame.init()
pygame.mixer.init()



def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def ExitMusicPlayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()



# Creating Buttons
Button1 = tkr.Button(musicplayer, width=5, height=1, font="Cambria 20 bold", text="Play Music", command=play, bg="lime green", fg="black")

Button3 = tkr.Button(musicplayer, width=5, height=1, font="Cambria 16 bold", text="Pause Music", command=pause, bg="yellow", fg="black")

Button4 = tkr.Button(musicplayer, width=5, height=1, font="Cambria 16 bold", text="Resume Music", command=resume, bg="skyblue", fg="black")

Button2 = tkr.Button(musicplayer, width=5, height=1, font="Cambria 20 bold", text="Stop Music", command=ExitMusicPlayer, bg="red", fg="black")

Button1.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
Button2.pack(fill="x")

playlist.pack(fill="both", expand="yes")

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="Helvetica 12 bold", textvariable=var)

songtitle.pack()
musicplayer.mainloop()