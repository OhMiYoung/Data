import requests
import json
import os

kakao_account = '28140c3c1a4e7f4179173101e436eed3'
tts_filename = '/home/pi/tts.mp3'
volume = -500

if kakao_account in [None, '']:
    raise Exception('Kakao account invalid')

tts_url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
tts_headers = {
    'Content-Type': 'application/xml',
    'Authorization': 'KakaoAK ' + kakao_account
}

say_word = '서울로봇고 오미영입니다 '

tts_string = '<speak><voice name="WOMAN_DIALOG_BRIGHT">  {} </voice></speak>'.format(say_word)  
# MAN_READ_CALM, WOMAN_READ_CALM, MAN_DIALOG_BRIGHT, WOMAN_DIALOG_BRIGHT

print(tts_string)
tts_res = requests.post(tts_url, headers=tts_headers, data=tts_string.encode('utf-8'))

with open(tts_filename, 'wb') as f:
    f.write(tts_res.content)

os.system(f'omxplayer -o local --vol {volume} {tts_filename}')