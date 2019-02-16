from tkinter import *
from tkinter import ttk
import speech_recognition as sr
from time import ctime
import time
from gtts import gTTS
import webbrowser
from pygame import mixer

def speak(reply,i):
	print(reply)
	txt2spch=gTTS(text=reply, lang='en')
	txt2spch.save("mp3/audio"+str(i)+".mp3")
	mixer.init()
	mixer.music.load("mp3/audio"+str(i)+".mp3")
	mixer.music.play()

def record():
	voice_in=sr.Recognizer()    
	with sr.Microphone() as source:
		print("Say Something!")
		audio=voice_in.listen(source, timeout=None)	
	command_in=" "
	try:
		command_in=voice_in.recognize_google(audio)
		print("You said: "+command_in)
	except sr.UnknownValueError:
		print("Sorry!! Your Command cannot be recognised!")
	except sr.RequestError:
		print("Sorry!! Couldn't request result from google services!!")
	else:
		pass

	return command_in
	
def vega(command_in,i):
	msg="Speak again please"
	if "what time is it" in command_in:
		msg="The time is: "+ctime()
	
	if "how are you" in command_in:
		msg="I am fine!"

	if "who are you" in command_in:
		msg="I am VEGA. I am a voice assistant designed using python."

	if "search video" in command_in:
		command_in=command_in.split(" ")
		vid=""
		for i in range(2, len(command_in)):
			vid+=command_in[i]+" "
		msg="searching youtube for video named "+vid
		url="https://www.youtube.com/results?search_query="+vid
		webbrowser.open(url)

	if "open" in command_in:
		command_in=command_in.split(" ")
		webpage=command_in[1]
		msg="loading "+webpage
		url="http://"+webpage
		webbrowser.open(url)

	if "where is" in command_in:
		command_in=command_in.split(" ")
		location=""
		for i in range(2, len(command_in)):
			location+=command_in[i]
		msg="Locating "+location+" on google maps"
		url="https://www.google.nl/maps/place/"+location


	speak(msg,i)

class VEGA:
	def __init__(self, master):
		self.label=Label(root,text="Command")
		self.label.grid(row=0,column=0)
		self.entry=Entry(root, width=50)
		self.entry.grid(row=0, column=1)
		self.micButton=Button(master,image=photo,command=self.vega_start)
		self.micButton.grid(row=0,column=4)
		self.searchButton= Button(master, text='Search', width=10, command=self.search)
		self.searchButton.grid(row=0, column=3)
	def vega_start(self):
		i=0
		speak("Hi, How can i help you?",i)
		while 1:
			i=i+1
			voice_in=record()
			vega(voice_in,i)
	def search(self):
		webbrowser.open('http://google.com/search?q='+self.entry.get())

root=Tk()
root.title("VEGA Virtual Assistant")
root.iconbitmap('mic.ico')
photo=PhotoImage(file='mic.png').subsample(30,30)
VEGA(root)
root.mainloop()