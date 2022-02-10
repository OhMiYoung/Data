import requests
import json
import os

kakao_account = '28140c3c1a4e7f4179173101e436eed3'

if kakao_account in [None, '']:
    raise Exception('Kakao account invalid')

stt_url = 'https://kakaoi-newtone-openapi.kakao.com/v1/recognize'
stt_headers = {
    'Content-Type': 'application/octet-stliream',
    'Authorization': 'KakaoAK ' + kakao_account
}

os.system('arecord -D plughw:1,0 -c2 -r 16000 -f S32_LE -d 5 -t wav -q -vv -V streo stream.raw; sox stream.raw -c 1 -b 16 stream.wav')

with open('stream.wav', 'rb') as f:
    stt_data = f.read()

stt_res = requests.post(stt_url, headers=stt_headers, data=stt_data)
# print(stt_res.text)

result_json_string = stt_res.text[stt_res.text.index('{"type":"finalResult"'):stt_res.text.rindex('}')+1]

# print(result_json_string)
result = json.loads(result_json_string)
# print(result)
print(result['value'])
