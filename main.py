import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
from random import randint


r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio , language='tr-TR')
        except sr.UnknownValueError:
            speak('Anlayamadım Lütfen Tekrar Edin')
        except sr.RequesrError:
            speak('Sistem Çalışmıyor')
        return voice

def response(voice):
    if 'aç' in voice:
        open = record('Neyi açmamı istersin')
        url = 'https://www.instagram.com'
        webbrowser.get().open(url)
    if 'Seni kim yarattı' in voice:
        speak('Yaratmak Allaha mahsustur beni oluşturan ise Sefer Kalkandır')
    if 'Senin adın ne' in voice:
        speak('Benim adım Pars')
    if 'nasılsın' in voice:
        speak('Teşekkür Ederim İyiyim Sen Nasılsın')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search = record('Ne Aramak istiyorsun')
        url = 'https://www.google.com/search?q=' +search
        webbrowser.get().open(url)
        speak(search + 'İçin Bulduklarım')
    if 'tamamdır' in voice:
        speak('Görüşürüz')
        sys.exit()

def speak(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)



def speak(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)



speak('Nasıl Yardımcı Olabilirim')
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)
