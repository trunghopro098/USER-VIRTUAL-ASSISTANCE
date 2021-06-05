from tkinter import *
import tkinter.ttk as CB
from PIL import ImageTk,Image
import threading
import AI
import AI1
from  googletrans import *
import speech_recognition as sr
import googletrans
import json


# Lấy tên ngôn ngữ và mã nn gán vào mảng LanguageJSon và codeLanguageJson

Language = googletrans.LANGUAGES
b = json.dumps(Language)
obj = json.loads(b)
LanguageJson = []
CodeLanguageJson = []
for i in obj:
    LanguageJson.append(obj[i])
    CodeLanguageJson.append(i)
print(Language)
print(LanguageJson)
print(CodeLanguageJson)

#

# Hàm chuyển đổi vị trí sang mã nn trong mảng
def KnowLanguage(codeLan):
    U =""
    for i in range(0, len(CodeLanguageJson)):
        if (codeLan==i):
            U = CodeLanguageJson[i]
            print("c2", U)
    return U

# Chuyển đổi vị trí thành mã ngôn ngữ
def KnowLanguageTranslated(codeLan1):
    L=""
    for i in range(0, len(CodeLanguageJson)):
        if (codeLan1==i):
            L = CodeLanguageJson[i]
            print("c1",L)
    return L

def clear():
    Text1.delete(1.0, END)
    Text2.delete(1.0, END)

def translates():
    try:
        n = combb1.get()
        n1 = combb2.get()
        q = 0
        q1 = 0
        for i in range(0, len(LanguageJson)):
            if( n ==LanguageJson[i]):
                print(i)
                q = i
                print("test index",q)
        for j in range(0, len(LanguageJson)):
            if (n1 == LanguageJson[j]):
                print(j)
                q1 = j
                print("test index",q1)
        Input = Text1.get(1.0,END)
        # print(Input)
        t = Translator()
        a = t.translate(Input, src=KnowLanguageTranslated(q), dest=KnowLanguageTranslated(q1))
        b = a.text
        Text2.delete(1.0,END)
        Text2.insert(END,b)
    except:
        AI.speak("Chưa nhập vào text mà dịch cái gì ông!")
# đọc ngôn ngữ của text 2
def read_Tran():
    try:
        n1 = combb2.get()
        q1 = 0
        for j in range(0, len(LanguageJson)):
            if (n1 == LanguageJson[j]):
                print(j)
                q1 = j
        AI1.reading(Text2.get(1.0, END),KnowLanguageTranslated(q1))
    except:
       AI1.SpeakEnligsh("Sorry!my wife don't understand")
testthrr = threading.Thread(target=read_Tran)

def get_audio_TrainSlate():
    n1 = combb1.get()
    q1 = 0
    for j in range(0, len(LanguageJson)):
        if (n1 == LanguageJson[j]):
            print(j)
            q1 = j
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        AI.speak("loli đang nghe bạn nói !")
        print("Loli : Đang nghe !--__--!")
        audio = ear_robot.listen(source, phrase_time_limit= 6)
        try:
            text = ear_robot.recognize_google(audio ,language=KnowLanguageTranslated(q1))
            print("Toi : ", text)
            return text
        except:
            print("Loli: Lỗi rồi.....")
            return 0

def listenTranSlate():
    Text1.delete(1.0, END)
    a = get_audio_TrainSlate()
    Text1.insert(END,a)
    print(a)
    # translator = Translator()
    # dt = translator.detect(a)
    # print(dt)
    translates()

def listenTranSlate1(a):
    AI.speak("bạn muốn mình phiên dich từ nào?")
    Text1.delete(1.0, END)
    Text1.insert(END, a)
    print(a)
    translator = Translator()
    dt = translator.detect(a)
    print(dt)
    translates()

def ReadAgain():
    try:
        n1 = combb1.get()
        q1 = 0
        for j in range(0, len(LanguageJson)):
            if (n1 == LanguageJson[j]):
                print(j)
                q1 = j
        AI1.reading(Text1.get(1.0, END), KnowLanguageTranslated(q1))
    except:
        AI1.SpeakEnligsh("Sorry!my wife don't understand")


def Pauprogram():
    AI.speak("loli không nói nữa")
    return 0
#


def create_Continue():
    if(btnStart['bg'] == 'green'):
        btnStart['bg'] = '#F6000B'
        btnStart['text'] = 'CONTINUE'
        btnStart['command'] = AI.main_brain()
        return
    if(btnStart['bg'] == '#F6000B'):
        btnStart['command'] = AI.continu()
        return





app = Tk()
app.title("VKU.UDN.VN-KHOA CÔNG NGHỆ THÔNG TIN - TRUYỀN THÔNG ĐẠI HỌC VIỆT-HÀN")

app.geometry('1135x520+100+20')
app.resizable(False, False)
image2 =Image.open('logo2.jpg')
reder = ImageTk.PhotoImage(image2)
img = Label(app, image= reder).place(x=0, y=0)
# Khung Chức năng
lb = Label(app, text = "VIRTUAL ASSISTANT USERS", fg= "red",font= "Time 24 bold" ,bg ='#F0F0F0')
lb.place(x= 350, y = 85)
labelframe=LabelFrame(app,fg = '#F7961E',font= "Time 8 bold",width=1100,
             height=360,highlightcolor="yellow",
             highlightbackground="#C1DD00",highlightthickness=5)
labelframe.place(x = 20, y = 140)

labelframe__la=LabelFrame(labelframe,text="VIRTUAL ASSISTANT USERS",fg = 'red',font= "Time 8 bold",width=200,
             height=300,highlightcolor="yellow",
             highlightbackground="red",highlightthickness=1)
labelframe__la.place(x = 20, y = 25)
btnStart = Button(labelframe__la, text = "START",width = 15,height = 2 ,bg = "green", fg = "white",command=create_Continue, relief = 'raised',borderwidth =5)
btnStart.place(x= 32,y=60)



labelframeTrain=LabelFrame(labelframe,text="LANGUAGE TRANSLATION",fg = 'red',font= "Time 8 bold",width=830,
             height=300,highlightcolor="yellow",
             highlightbackground="red",highlightthickness=1)
labelframeTrain.place(x = 240, y = 25)

combb1 = CB.Combobox(labelframeTrain, width = 30, height = 9, font = "Time 10 bold",state = "readonly")
combb1['values'] = (LanguageJson)
combb1.current(101)
combb1.place(x= 10, y = 20)
# lbChange= Label(app,text = "TRANSLATE", bg = "#837FCD",fg = "#19B3ED" , font = "Time 11 bold")
# lbChange.place(x = 430, y = 170)
combb2 = CB.Combobox(labelframeTrain, width = 30, height = 9, font = "Time 10 bold",state = "readonly")
combb2['values'] = (LanguageJson)
combb2.current(21)
combb2.place(x= 580, y = 20)
btnClearT = Button(labelframeTrain, text = "CLEAR TEXT", font = "Time 10 bold", bg = "red", fg = "white", command=lambda: clear()).place(x= 414, y= 20)

btnTranslate = Button(labelframeTrain, text = "TRANSLATE", font = "Time 10 bold", bg = "green", fg = "white", command = translates).place(x= 320, y= 20)

Text1 = Text(labelframeTrain, width = 36, height = 7 , font="time 15", fg = "black")
Text1.place(x = 10,y = 65 )
Text2 =  Text(labelframeTrain, width = 36, height = 7 , font="time 15", fg = "black")
Text2.place(x= 414, y =65)


image3 =Image.open('microphone_24px.png')
micro = ImageTk.PhotoImage(image3)
image4 =Image.open('high_volume_24px.png')
highvolume = ImageTk.PhotoImage(image4)

lblMicro = Label(labelframeTrain,bg ="white", width = "35", text = "", font ="Time 15")
lblMicro.place(x = 19, y =230)
ButMicro = Button(labelframeTrain, text = "microphone", image = micro, command = listenTranSlate)
ButMicro.place(x =10,y = 230)
Buttreadagain = Button(labelframeTrain, text = "Listen", image = highvolume,command=lambda: ReadAgain())
Buttreadagain.place(x =40,y = 230)

lblMicro = Label(labelframeTrain,bg ="white", width = "35", text = "", font ="Time 15")
lblMicro.place(x = 423, y =230)
Buthighvolume = Button(labelframeTrain, text = "Listen", image = highvolume, command=lambda: read_Tran())
Buthighvolume.place(x =414,y = 230)

app.mainloop()