"""
Speech Recognition

text2emotion
"""

import speech_recognition as sr
import text2emotion as te

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak Anything: ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))

        emotions = te.get_emotion(text)
        print(emotions)

    except:
        print('Sorry could not recognize speech')

