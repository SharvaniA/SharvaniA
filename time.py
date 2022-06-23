import pyttsx3
import time
# d = time.strftime("%b %d %Y")
# print(d)
# print(t)
def speak(t):
	engine = pyttsx3.init()
	engine.say(t)
	engine.runAndWait()
while(1):
	t = time.strftime("%I:%M %p")
	speak(t)
	time.sleep(300)
	