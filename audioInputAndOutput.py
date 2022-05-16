# Reading and Printing weather report of a given city. Taking city name as voice input.

# import speech_recognition as sr
# import requests
# import pyaudio
# import pyttsx3
# r = sr.Recognizer()
# # audio = ''

# with sr.Microphone() as source:
# with sr.AudioFile('sampleAudio.MP3') as source:
	# r.adjust_for_ambient_noise(source)
	# print("say something!")
	# audio = r.listen(source)
	# r.runAndWait()
	# print(temp := r.recognize_google(audio))

	# print(temp := (eval(requests.get("https://api.openweathermap.org/data/2.5/weather?q=" 
	# 	+ r.recognize_google(audio) + 
	# 	"&appid=e6b7427f8bf97526adf2869093c7509c&units=metric").text)['main']['temp']))
# engine = pyttsx3.init()
# # # text = r.recognize_google(audio)
# engine.say(temp)
# engine.runAndWait()
# input("")

# print((city := input("Enter City Name to find temperature:")), 
	# eval(requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + 
	# 	"&appid=e6b7427f8bf97526adf2869093c7509c&units=metric").text)['main']['temp'])

import speech_recognition as sr
import requests
import pyaudio
import pyttsx3
r = sr.Recognizer()
# audio = ''

with sr.Microphone() as source:
# with sr.AudioFile('sampleAudio.MP3') as source:
	r.adjust_for_ambient_noise(source)
	# print("say something!")
	audio = r.listen(source)
	# r.runAndWait()
	print(temp := (eval(requests.get("https://api.openweathermap.org/data/2.5/weather?q=" 
		+ r.recognize_google(audio) + 
		"&appid=e6b7427f8bf97526adf2869093c7509c&units=metric").text)['main']['temp']))
def speak(temp):
	engine = pyttsx3.init()
	# # text = r.recognize_google(audio)
	engine.say(temp)
	engine.runAndWait()
	# print(temp := r.recognize_google(audio))
speak(temp)
