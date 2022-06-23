import speech_recognition as sr
import requests
import pyaudio
import pyttsx3
import time

class person:  
	name = ''  
	def setName(self, name):  
		self.name = name 

r = sr.Recognizer()
# audio = ''
def speak(audio_string):
	engine = pyttsx3.init()
	engine.say(audio_string)
	engine.runAndWait()

def record_audio(ask=False):  
	with sr.Microphone() as source: # microphone as source  
		r.adjust_for_ambient_noise(source)
		if ask:  
			speak(ask)  
		print("Speak something...")
		audio = r.listen(source)  # listen for the audio via source 
		voice_data = ''  
		try:
			voice_data = r.recognize_google(audio)  # convert audio to text  
		except sr.UnknownValueError: # error: recognizer does not understand  
			speak('I did not get that')
		except sr.RequestError:
			speak('Sorry, the service is down') # error: recognizer is not connected  
			print(f">> {voice_data.lower()}") # print what user said  
		return voice_data.lower()
def respond(voice_data):
	speak('How can I help you?')
time.sleep(1)  

person_obj = person()  
while(1):  
	voice_data = record_audio() # get the voice input  
	respond(voice_data) # respond  