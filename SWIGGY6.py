import requests
import json
import time
from pygame import mixer
#Enter your url here and enjoy your free offer!!
url = 'https://www.cricbuzz.com/match-api/21859/commentary.json'

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
