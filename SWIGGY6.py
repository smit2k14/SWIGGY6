import requests
import json
import time
from gtts import gTTS
from pygame import mixer
#Enter your url here and enjoy your free offer!!
url = 'https://www.cricbuzz.com/match-api/21859/commentary.json'

tts = gTTS('Six Six Six')
tts.save('six.mp3')
tts = gTTS('You have run into an error. The API is not accepting calls. You need to run this code again.')
tts.save('error.mp3')
f = 0
c = time.time()
while True:
	try:
		current_scorecard = requests.get(url).json()['score']['prev_overs']
	except:
		mixer.init()
		mixer.music.load('error.mp3')
		mixer.music.play()	
		break
	for score in current_scorecard[-10:-1]:
		if score == '6':
			mixer.init()
			mixer.music.load('six.mp3')
			mixer.music.play()
			f = 1
			break
	if f == 1:
		break
	time.sleep(5*60)