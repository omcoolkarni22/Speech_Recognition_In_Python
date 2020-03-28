import speech_recognition as sr

r = sr.Recognizer()
a = sr.AudioFile('harvard.wav')

print("***Recognizing***")

with a as source:
    au = r.record(source)

s = r.recognize_google(au)

print(s)
