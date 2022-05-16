# Reading and Printing the meaning of a word using Dictionary API.

# print((wordToSearch := str(input("Enter a word find its meaning: "))), (dict := eval(requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + wordToSearch).text)))(answer := ['meanings' for i in dict.values()])
# import requests
# print((wordToSearch := str(input("Enter a word find its meaning: "))),
#  (dict := eval(requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"
#   + wordToSearch).text)[0]['meanings'][0]['definitions'][0]['definition']))

import requests
import vlc


print("The meaning of", (wordToSearch := str(input("Enter a word find its meaning:"))), "is {0:s}"
	.format((dictionaryapi := eval(requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"
  + wordToSearch).text))[0]['meanings'][0]['definitions'][0]['definition']))

indexForAudio = 0
if ((dictionaryapi)[0]['phonetics'][0]['audio']) == '':
	indexForAudio += 1
	media = vlc.MediaPlayer("{0:s}" .format((dictionaryapi)[0]['phonetics'][indexForAudio]['audio']))
	media.play()
	input("Enter")
else:
	media = vlc.MediaPlayer("{0:s}" .format((dictionaryapi)[0]['phonetics'][0]['audio']))
	media.play()
	input("Enter")

# import requests
# import vlc


# print("The meaning of", (wordToSearch := str(input("Enter a word find its meaning:"))), "is {0:s}"
# 	.format((dictionaryapi := eval(requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"
#   + wordToSearch).text))[0]['meanings'][0]['definitions'][0]['definition']))

# indexForAudio = 0
# if ((dictionaryapi)[0]['phonetics'][0]['audio']) == '':
# 	indexForAudio += 1
# 	media = vlc.MediaPlayer("{0:s}" .format((dictionaryapi)[0]['phonetics'][indexForAudio]['audio']))
# 	media.play()
# 	input("Enter")
# else:
# 	media = vlc.MediaPlayer("{0:s}" .format((dictionaryapi)[0]['phonetics'][0]['audio']))
# 	media.play()
# 	input("Enter")

# indexForExample = 0
# if ((dictionaryapi)[0]['meanings'][0]['definitions'][0]['example']) is None:
# 	indexForExample += 1
# 	print("Example: {0:s}" .format((dictionaryapi)[0]['meanings'][0]['definitions'][indexForExample + 1]['example']))
# else:
# 	print("Example: {0:s}" .format((dictionaryapi)[0]['meanings'][0]['definitions'][0]['example']))



# import requests
# import webbrowser


# print("The meaning of", (wordToSearch := str(input("Enter a word find its meaning:"))), "is {0:s}"
# 	.format((dictionaryapi := eval(requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"
#   + wordToSearch).text))[0]['meanings'][0]['definitions'][0]['definition']))

# indexForAudio = 0
# if ((dictionaryapi)[0]['phonetics'][0]['audio']) == '':
# 	indexForAudio += 1
# 	webbrowser.open("{0:s}" .format((dictionaryapi)[0]['phonetics'][indexForAudio]['audio']))
# else:
# 	webbrowser.open("{0:s}" .format((dictionaryapi)[0]['phonetics'][0]['audio']))

# indexForExample = 0
# if ((dictionaryapi)[0]['meanings'][0]['definitions'][0]['example']) is None:
# 	indexForExample += 1
# 	print("Example: {0:s}" .format((dictionaryapi)[0]['meanings'][0]['definitions'][indexForExample + 1]['example']))
# else:
# 	print("Example: {0:s}" .format((dictionaryapi)[0]['meanings'][0]['definitions'][0]['example']))