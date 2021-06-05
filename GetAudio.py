
import speech_recognition as sr
def get_audio():

    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:#lắng nghe
        # lablea = Label(UI.app,text="xin chao",bg="red").pack()
        print("Loli : Đang nghe !--__--!")
        # input("nhập vào mới nói : ")
        audio = ear_robot.listen(source, phrase_time_limit= 3)
        try:
            text = ear_robot.recognize_google(audio ,language="vi-VN")
            print("Toi : ", text)
            return text
        except:
            print("Loli: Lỗi rồi.....")
            return 0
