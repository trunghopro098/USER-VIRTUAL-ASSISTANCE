import pyttsx3
import playsound
import os
from gtts import gTTS


def reading(b,L):

    print("Loli: ", b)
    # khoi tao van ban, ngôn ngử, tốc độ đọc , lưu file->dọc file-> xóa file
    tts = gTTS(text=b, lang=L, slow=False)
    tts.save("robot.mp3")
    # playsound.playsound("abc.mp4", True)
    playsound.playsound("robot.mp3", True)
    os.remove("robot.mp3")
# reading('xin chào',"vi")

def SpeakEnligsh(b):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    engine.setProperty('voices', voices[1].id)
    engine.setProperty('volume', volume - 0.0)
    engine.setProperty('rate', rate - 50)

    engine.say(b)
    engine.runAndWait()
