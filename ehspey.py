#EHSPEY

#IMPORTS

import playsound
from playsound import playsound

def ultQuery():
    wants = input("Enter command here => ")
    action,specializer,unique = wants.split(" ")
    if action.lower() == "play":
        if specializer.lower() == "song":
            if unique.lower() == "overlook":
                playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\1.wav")
                ultQuery()
            elif unique.lower() == "hound dog":
                playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\2.wav")
                ultQuery()
            elif unique.lower() == "lucky sevens":
                playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\3.wav")
                ultQuery()
            elif unique.lower() == "call it a reraise":
                playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\4.wav")
                ultQuery()
            elif unique.lower() == "skullheart duskwalk":
                playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\5.wav")
                ultQuery()
            elif unique.lower() == "path of the righteous man":
                playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\6.wav")
                ultQuery()

def querySong():
    song = input("Enter the name of the song you would like to play => ")
    if song.lower() == "lovecraft":
        playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\10.wav")
        querySong()
    elif song.lower() == "path of the righteous man":
        playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\6.wav")
        querySong()
    elif song.lower() == "fraudulent quartet":
        playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\7.wav")
        querySong()
    elif song.lower() == "intermission: mimesiswing":
        playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\8.wav")
        querySong()
    elif song.lower() == "dismantled":
        playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\9.wav")
        querySong()
    elif song.lower() == "money for nothing":
        playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\11.wav")
        querySong()
    elif song.lower() == "disciplinary action":
        playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\12.wav")
        querySong()
    elif song.lower() == "guess my name":
        playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\13.wav")
        querySong()
    elif song.lower() == "made for spades":
        playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\14.wav")
        querySong()
    elif song.lower() == "pale imitation":
        playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\15.wav")
        querySong()
    elif song.lower() == "bonus: dear pesky shufflers":
        playsound("C:\\Users\\David Kelley\\Desktop\\ehspey\\music\\dead shufflers - anything goes\\16.wav")
        querySong()
    else:
        querySong()

querySong()