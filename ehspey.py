from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
import eyed3
import pygame
import time
import mutagen
from mutagen.mp3 import MP3

songDIRlist = []
songNAMElist = []

#RGB CONVERSION
def rgbConversion(rgb):
    return "#%02x%02x%02x" % rgb  

#THEME COLOURS
interfaceRGB = [128,0,0]
detailRGB = [128,128,0]
interface = rgbConversion((interfaceRGB[0],interfaceRGB[1],interfaceRGB[2]))
interfaceDark = rgbConversion((round(interfaceRGB[0]*0.8125),round(interfaceRGB[1]*0.8125),round(interfaceRGB[2]*0.8125)))
detail = rgbConversion((detailRGB[0],detailRGB[1],detailRGB[2]))
detailDark = rgbConversion((round(detailRGB[0]*0.8125),round(detailRGB[1]*0.8125),round(detailRGB[2]*0.8125)))

#ADD SONG
def addSong():
    global audio
    global songDIRlist
    global songNAMElist
    song = filedialog.askopenfilename(initialdir="music\\", title="Please select the song you wish to add.", filetypes=(("mp3 Files", "*.mp3"),))
    songStat = eyed3.load(f"{song}")
    songTitle = songStat.tag.title
    songListBox.insert(END, songTitle)
    songDIRlist.append(song)
    songNAMElist.append(songTitle)

#ADD SONGS
def addSongs():
    global songDIRlist
    global songNAMElist
    songs = filedialog.askopenfilenames(initialdir="music\\", title="Please select the songs you wish to add.", filetypes=(("mp3 Files", "*.mp3"),))
    for song in songs:
        songStat = eyed3.load(f"{song}")
        songTitle = songStat.tag.title
        songListBox.insert(END, songTitle)
        songDIRlist.append(song)
        songNAMElist.append(songTitle)

#REMOVE SONG
def removeSong():
    global songDIRlist
    global songNAMElist
    currentIndex = songListBox.curselection()
    songDIRlist.pop(currentIndex[0])
    songNAMElist.pop(currentIndex[0])
    songListBox.delete(ANCHOR)
    pygame.mixer.music.stop()

#REMOVE SONGS
def removeAll():
    global songDIRlist
    global songNAMElist
    songNAMElist.clear()
    songDIRlist.clear()
    songListBox.delete(0,END)
    pygame.mixer.music.stop()

#PLAY SELECTED SONG
def play():
    global songDIRlist
    global songNAMElist
    global paused
    global stopped
    currentSong = songListBox.get(ACTIVE)
    playlistIndex = songNAMElist.index(currentSong)
    paused = False
    stopped = False
    pygame.mixer.music.load(songDIRlist[playlistIndex])
    pygame.mixer.music.play(loops=0)
    currentRuntime()

#CURRENT RUNTIME
def currentRuntime():
    curRuntime = pygame.mixer.music.get_pos() / 1000
    if stopped == False:
        curRuntimeFormatted = time.strftime("%H:%M:%S", time.gmtime(curRuntime))
    else:
        curRuntimeFormatted = time.strftime("%H:%M:%S", time.gmtime(0))
    timestamp.config(text=curRuntimeFormatted)
    timestamp.after(1000, currentRuntime)

#STOP PLAYING CURRENT SONG
stopped = False
def stop():
    global stopped
    pygame.mixer.music.stop()
    songListBox.select_clear(ACTIVE)
    stopped = True

#PAUSE/UNPAUSE SELECTED SONG
paused = False
def pause():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

#PLAY NEXT SONG IN THE PLAYLIST
def nextSong():
    global songDIRlist
    global paused
    nextSong = songListBox.curselection()
    forward = nextSong[0]+1
    selectionSize = songListBox.size()
    songListBox.selection_clear(0,END)
    if forward <= selectionSize - 1:
        songListBox.select_set(forward)
        songListBox.activate(forward)
        pygame.mixer.music.load(songDIRlist[forward])
    else:
        songListBox.select_set(0)
        songListBox.activate(0)
        pygame.mixer.music.load(songDIRlist[0])
    pygame.mixer.music.play(loops=0)
    paused = False

#PLAY PREVIOUS SONG IN THE PLAYLIST
def previousSong():
    global songDIRlist
    global paused
    previousSong = songListBox.curselection()
    backward = previousSong[0]-1
    selectionSize = songListBox.size()
    selectionMax = selectionSize-1
    songListBox.selection_clear(0,END)
    if backward >= 0:
        songListBox.select_set(backward)
        songListBox.activate(backward)
        pygame.mixer.music.load(songDIRlist[backward])
    else:
        songListBox.select_set(selectionMax)
        songListBox.activate(selectionMax)
        pygame.mixer.music.load(songDIRlist[selectionMax])
    pygame.mixer.music.play(loops=0)
    paused = False

#SAVE PLAYLIST CONFIGURATION
def save():
    global playlistName
    global songDIRlist
    global songNAMElist
    file = open(f"playlists\\{playlistName}.sp", "w+")
    songDIRlistString = "x"
    songNAMElistString = "x"
    DIRdivide = "*"
    NAMEdivide = "*-*"
    x = 0
    for i in range(0,len(songDIRlist)):
        if x == 0:
            songDIRlistString = songDIRlist[0]
            x+=1
        else:
            songDIRlistString = songDIRlistString + DIRdivide + songDIRlist[x]
            x+=1
    y = 0
    for i in range(0,len(songNAMElist)):
        if y ==  0:
            songNAMElistString = songNAMElist[0]
            y+=1
        else:
            songNAMElistString = songNAMElistString + NAMEdivide + songNAMElist[y]
            y+=1
    file.write(f"{playlistName}\n{songDIRlistString}\n{songNAMElistString}")

#LOAD PLAYLIST CONFIGURATION
def load():
    global playlistName
    global songDIRlist
    global songNAMElist
    songDIRlist.clear()
    songNAMElist.clear()
    songListBox.delete(0,END)
    configurePath = filedialog.askopenfilename(initialdir="playlists\\", title="Please select the playlist you wish to load.", filetypes=(("sp Files", "*.sp"),))
    configure = open(configurePath, "r")
    settings = []
    settings = configure.readlines()
    playlistName = settings[0]
    songDIRlistMash = settings[1]
    songNAMElistMash = settings[2]
    songNAMElist = songNAMElistMash.split("*-*")
    songDIRlist = songDIRlistMash.split("*")
    playlistTitle.configure(text=playlistName)
    x = 0
    while x < len(songNAMElist):
        songListBox.insert(END, songNAMElist[x])
        x += 1

root = Tk()
root.title("Ehspey")
#root.iconbitmap("PATH TO ICON HERE")
root.geometry("500x360")
root.configure(bg=detail)

#INITIALISE PYGAME MIXER
pygame.mixer.init()

#RENAME PLAYLIST FUNCTION
playlistName = "Playlist"
def renamePlaylist():
    global playlistNameInput
    global playlistName
    playlistName = playlistNameInput.get()
    playlistTitle.configure(text=playlistName)

#CREATE PLAYLIST NAME
playlistTitle = Label(root, text="Playlist", bg=detail, fg=interface, font=(16))
playlistTitle.pack()

#CREATE PLAYLIST NAMING INPUT
playlistNameInput = Entry(root, width=32, bg=interface, fg=detail)
playlistNameInput.focus_set()
playlistNameInput.pack()

#STYLE TTK BUTTON
style=ttk.Style()
style.theme_use("alt")
style.configure("TButton", background=interface, foreground=detail)
style.map("TButton", background=[("active",interface)])

#CREATE PLAYLIST NAMING CONFIRMATION BUTTON
ttk.Button(root, width=32, text="Confirm rename", command=renamePlaylist, ).pack(pady=4)

#CREATE PLAYLIST BOX
songListBox = Listbox(root, bg=interface, fg=detail, width=60, selectbackground=detail, selectforeground=interface, borderwidth=0)
songListBox.pack(pady=16)

#DEFINE CONTROL BUTTONS
backButtonIMG = PhotoImage(file="images/backwardButton.png")
forwardButtonIMG = PhotoImage(file="images/forwardButton.png")
playButtonIMG = PhotoImage(file="images/playButton.png")
pauseButtonIMG = PhotoImage(file="images/pauseButton.png")
stopButtonIMG = PhotoImage(file="images/stopButton.png")

#CREATE CONTROL BUTTONS FRAME
controlsFrame = Frame(root, bg=detail)
controlsFrame.pack()

#CREATE CONTROL BUTTONS
backButton = Button(controlsFrame, image=backButtonIMG, borderwidth=0, bg=detail, activebackground=detail, command=previousSong)
forwardButton = Button(controlsFrame, image=forwardButtonIMG, borderwidth=0, bg=detail, activebackground=detail, command=nextSong)
playButton = Button(controlsFrame, image=playButtonIMG, borderwidth=0, bg=detail, activebackground=detail, command=play)
pauseButton = Button(controlsFrame, image=pauseButtonIMG, borderwidth=0, bg=detail,activebackground=detail, command=pause)
stopButton = Button(controlsFrame,image=stopButtonIMG, borderwidth=0, bg=detail, activebackground=detail, command=stop)

backButton.grid(row=0, column=0, padx=4)
forwardButton.grid(row=0, column=1, padx=4)
playButton.grid(row=0, column=2, padx=4)
pauseButton.grid(row=0, column=3, padx=4)
stopButton.grid(row=0, column=4, padx=4)

#CREATE TIMESTAMP
timestamp = Label(root, text="", bd=1, relief=GROOVE, anchor=CENTER, bg=interface, fg=detail, width=16)
timestamp.pack(side=BOTTOM, ipady=4)

#CREATE MENU
menu = Menu(root)
root.config(menu=menu)

#CREATE ADD SONG MENU
addSongMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Add", menu=addSongMenu)
addSongMenu.add_command(label="Add a song to playlist", command=addSong)
addSongMenu.add_command(label="Add multiple songs to playlist", command=addSongs)

#CREATE REMOVE SONG MENU
removeSongMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Remove", menu=removeSongMenu)
removeSongMenu.add_command(label="Remove a song from playlist", command=removeSong)
removeSongMenu.add_command(label="Remove all songs from playlist", command=removeAll)

#SAVE/LOAD MENU
saveLoadMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Save/Load", menu=saveLoadMenu)
saveLoadMenu.add_command(label="Save your current playlist", command=save)
saveLoadMenu.add_command(label="Load a playlist", command=load)

#MAINLOOP
root.mainloop()