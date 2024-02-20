import json
import requests
import speech_recognition as sr
import pyttsx3
import time
import os
import pywhatkit

while True:
    # initialize recognizer class (for recognizing the speech)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # change index to change voices
    r = sr.Recognizer()

    # Reading Microphone as source
    with sr.Microphone() as source:
        print("Say 'max' to activate.")
        audio = r.listen(source)
        print("end recording")

    # recoginize_google() method to recognize the speech
    try:
        text = r.recognize_google(audio)
        text = text.lower()
        print(text)
        if text.find("max") != -1:
            print("Activated.")
            search = text.replace('max', '')
            if search.find('play') != -1:
                song = search.replace('play', '')
                pywhatkit.playonyt(song)
                engine.say('playing ' + song)
                engine.runAndWait()
            else:
                print("User: " + search)
            # Define the endpoint
                endpoint = "https://api.openai.com/v1/completions"

            # Define the headers
                headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer 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",
            }

            # Define the data
                data = {
                "model": "text-davinci-003",
                "prompt": search,
                "temperature": 0,
                "max_tokens": 1024,
            }

            # Send the request
                response = requests.post(endpoint, json=data, headers=headers)
            # print(response.json())
                result = response.json()["choices"][0]["text"]

            # Print the result
                print("MAX:" + result)
            # Code for running the assistant
                engine.say(result)
                engine.runAndWait()
        else:
            print("Incorrect activation phrase.")
    except:
        print("Sorry, I did not get that.")
