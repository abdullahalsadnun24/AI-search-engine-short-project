import json
import requests
import speech_recognition as sr
import  pyttsx3
import pywhatkit
import time
import os
from tkinter import *
# Define the endpoint
endpoint = "https://api.openai.com/v1/completions"
# Define the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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",
}
#
# GUI
root = Tk()
root.title("AI Search Engine")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # change index to change voices
def talk(text):
    engine.say(text)
    engine.runAndWait()

def remove_at(i, s):
    return s[:i] + s[i+1:]
# Send function
def send():
	search=e.get()
	send = "\n\nYou -> " + e.get()
	txt.insert(END, "\n" + send)
	if search.find('play') != -1:
		song = search.replace('play', '')
		txt.insert(END, "\n" + 'MAX-> playing ' + song)
		pywhatkit.playonyt(song)
		talk('playing ' + song)
	else:
		data = {
			"model": "text-davinci-003",
			"prompt": search,
			"temperature": 0,
			"max_tokens": 1024,
		}
		response = requests.post(endpoint, json=data, headers=headers)
		result = response.json()["choices"][0]["text"]
		result = remove_at(1, result)
		result = remove_at(0, result)
		txt.insert(END, "\n" +"Max->"+result)
		##talk(result)
	e.delete(0, END)

def maxai():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Speaking....")
		audio = r.listen(source)
		print("Recording ended...")
	try:
		text = r.recognize_google(audio)
		text = text.lower()
		txt.insert(END, "\n" + "\nYou -> "+text)
		print(text)
		if text.find('play') != -1:
			song = text.replace('play', '')
			txt.insert(END, "\n" + 'MAX-> playing ' + song)
			talk('playing ' + song)
			pywhatkit.playonyt(song)

		else:
			data = {
				"model": "text-davinci-003",
				"prompt": text,
				"temperature": 0,
				"max_tokens": 1024,
			}
			response = requests.post(endpoint, json=data, headers=headers)
			result = response.json()["choices"][0]["text"]
			result = remove_at(1, result)
			result = remove_at(0, result)
			txt.insert(END, "\n" +"Max->" + result)
			talk(result)


	except:
		print("Couldn't understand")
lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="MAX", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=70)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=1)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=60)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)
micr = Button(root, text="Speak", font=FONT_BOLD, bg=BG_GRAY,
			command=maxai).grid(row=3, column=0)
root.mainloop()
