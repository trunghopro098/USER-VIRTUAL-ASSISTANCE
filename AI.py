import wikipedia
from gtts import gTTS
import playsound
import os
import speech_recognition as sr
import time
import datetime
import threading
import re
import json
import webbrowser
import requests
from youtube_search import  YoutubeSearch
import urllib.request as urllib2
import ctypes
from pygame import mixer
from tkinter import *
import GetAudio
wikipedia.set_lang('vi')
langguage = 'vi'

def Pauprgram():
    speak("Tạm biệt và hẹn gặp lại nha")
    print("stop")
    pau = threading.Thread(target=Pauprgram)
    pau.start()
def pause():
    speak("Chương trình của Loli tạm thời dừng lại!")
    # speak("Để tiếp tục với LoLi nhấn chữ ENTER nha ")
    return 0

#Chuyển giọng nói thành văn bản
# def get_audio():
#
#     ear_robot = sr.Recognizer()
#     with sr.Microphone() as source:#lắng nghe
#         # lablea = Label(UI.app,text="xin chao",bg="red").pack()
#         print("Loli : Đang nghe !--__--!")
#         # input("nhập vào mới nói : ")
#         audio = ear_robot.listen(source, phrase_time_limit= 3)
#         try:
#             text = ear_robot.recognize_google(audio ,language="vi-VN")
#             print("Toi : ", text)
#             return text
#         except:
#             print("Loli: Lỗi rồi.....")
#             return 0

def stop():
    speak("Cảm ơn bạn, hẹn gặp lại sau nha!")

def get_text():
    for i in range(3):
        text = GetAudio.get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Loli nghe không rỏ bạn nói, vui lòng nói lại cho mình đi!")
    time.sleep(3)
    stop()
    return 0

#Chuyển văn bản thành giongj nois
def speak(text):
    print("Loli: ", text)
# khoi tao van ban, ngôn ngử, tốc độ đọc , lưu file->dọc file-> xóa file
    tts = gTTS(text= text ,lang= langguage)
    tts.save("robot.mp3")
    playsound.playsound("robot.mp3", True)
    os.remove("robot.mp3")

def get_audio_TrainSlate():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        speak("loli đang nghe bạn nói !")
        print("Loli : Đang nghe !--__--!")
        audio = ear_robot.listen(source, phrase_time_limit= 3)
        try:
            text = ear_robot.recognize_google(audio ,language="vi-VN")
            print("Toi : ", text)
            return text
        except:
            print("Loli: Lỗi rồi.....")
            return 0
def hello():
    daytime = int(time.strftime("%H"))
    if 0 <= daytime <= 4:
        speak("Giờ này ngủ ngon lắm, sao bạn dạy sớm vậy, có phải nhớ tui không!")
    if 5 <= daytime <= 9:
        speak("Chúc bạn buổi sáng vui vẽ.")
    elif 10 <= daytime <= 12:
        speak("Chúc bạn buổi trưa vui vẻ.")
    elif 13 <= daytime <= 17:
        speak("Chúc bạn buổi chiều vui vẻ.")
    elif 17 < daytime <= 22:
        speak("Chúc bạn buổi tối vui vẻ.")
    elif 23 <= daytime <= 24:
        speak("Muộn rồi bạn nên đi ngủ xớm đi, mai mình gặp lại nha !")

def get_time(text):
    now = datetime.datetime.now()
    if 'giờ' in text:
        speak(f"Bây giờ là {now.hour} giờ {now.minute} phút {now.second} giây")
    elif "ngày" in text:
        speak(f'Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}')
    else:
        speak("Bé loli chưa hiểu ý bạn.")

def open_app(text):

    if "google" in text:
        speak("Mở google chrome")
        os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        # pause()
        speak("google đã mở, bạn muốn loli làm gì nữa !")
        return

    elif "word" in text:
        speak("mở microsoft word")
        os.startfile(r"C:\Users\Administrator\Desktop\Word 2013.lnk")

        speak("Microsoft Work đã mở, bạn muốn loli làm gì nữa !")
    elif "postman" in text:
        speak("Mở Postman")
        os.startfile(r"C:\Users\Administrator\Desktop\Postman.lnk")

        speak("Visua studio code đã mở, bạn muốn loli làm gì nữa !")
    elif "cốc cốc" in text:
        speak("mở Cốc cốc")
        os.startfile(r"C:\Users\Administrator\Desktop\Cốc Cốc.lnk")
        speak("cốc cốc đã mở, bạn muốn loli làm gì nữa !")

    else:
        speak("mở cái gì nói rõ lên, loli mới mở được chứ. Mệt cho cậu ghê.")

# mở website
def Open_website(text):
    # tìm kiếm trong chuổi nếu trong tẽxt cso chữ mở  (biểu thưc chính qui-gồm http or .vn....) tham số
    reg_ex = re.search('mở (.+)',text)
    # nếu reg_ẽ khác 0 hay có giá trị
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.'+ domain
        speak("Đang mở trang web bạn yêu cầu!")
        webbrowser.open(url)
        speak("bạn cần loli giúp gì nữa không!")
        return True
    else:
        return False
# Open_website("mở youtube.com")
# tìm kiếm trên google
def open_google_and_search(text):
    # split cắt chuỏi theo từ
    search_for = str(text).split('kiếm',1)[1]
    url = f'https://www.google.com/search?q={search_for}'
    webbrowser.get().open(url)
    speak('Đây là thông tin bạn cần tìm')
    speak("bạn cần mình giúp gì nữa không!")

def open_google_and_search1():
    speak("Bạn cần tìm kiếm gì trên google ?")
    search = str(get_text()).lower()
    url = f'https://www.google.com/search?q={search}'
    webbrowser.get().open(url)
    speak('Đây là thông tin bạn cần tìm')
    speak("bạn cần mình giúp gì nữa không!")

def open_google_map():
    # split cắt chuỏi theo từ
    # find_way = str(text).split('đường ',1)[1]
    speak("bạn muốn tìm đường nào ?")
    find_way = get_text()
    url = f'https://www.google.com/maps/place/{find_way}'
    webbrowser.get().open(url)
    speak('Đây là thông tin bạn cần tìm')
    speak("bạn cần mình giúp gì nữa không!")

def open_google_map1(text):
    # split cắt chuỏi theo từ
    # find_way = str(text).split('đường ',1)[1]

    find_way = str(text).split("đường",1)[1]
    url = f'https://www.google.com/maps/place/{find_way}'
    webbrowser.get().open(url)
    speak('Đây là thông tin bạn cần tìm')
    speak("bạn cần mình giúp gì nữa không!")
# open_google_map("đường hùng vương thành phố tam kỳ")
def play_Youtube():
    speak("bạn muốn tìm gì trên youtube !")
    search = get_text()
    while True:
        result = YoutubeSearch(search, max_results=10).to_dict()
        if result:
            break
    print(result)
    url = f'https://www.youtube.com'+result[0]['url_suffix']
    print("link youtube \t",url)
    webbrowser.get().open(url)
    speak("Đây là kết quả bạn cần tìm")
    speak("bạn cần loli giúp gì nữa không")
# play_Youtube()

def change_wellpaper ():
    api_key = "gYc9AhZ6wMoFd0U_soEAyH7VKdLHiRZxM88LxUWuxPQ"

    url = 'https://api.unsplash.com/photos/random?client_id=' + \
          api_key  # pic from unspalsh.com
    # duyệt web ẩn không hiển thị như open(url)
    f = urllib2.urlopen(url)
    # đọc dử liệu trong web
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']
    # Location where we download the image to.
    urllib2.urlretrieve(photo, r"D:\pythonW\a.png")
    image = os.path.join(r"D:\pythonW\a.png")

    ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 3)
    speak("Hình nền máy tính bạn đã được thay đổi. Bạn xem có đẹp không nha ?")

# change_wellpaper()
def current_weather():

    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    # Đường dẫn trang web để lấy dữ liệu về thời tiết
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"

    # lưu tên thành phố vào biến city
    city = get_text()
    # nếu biến city != 0 và = False thì để đấy ko xử lí gì cả
    if not city:
        pass
    # api_key lấy trên open weather map
    api_key = "2c7c85350294ff16545481df0989c649"
    # tìm kiếm thông tin thời thời tiết của thành phố
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    # truy cập đường dẫn của dòng 188 lấy dữ liệu thời tiết
    response = requests.get(call_url)
    # lưu dữ liệu thời tiết dưới dạng json và cho vào biến data
    data = response.json()
    print('Thời tiết\n', data)
    # kiểm tra nếu ko gặp lỗi 404 thì xem xét và lấy dữ liệu
    if data["cod"] != "404":
        # lấy value của key main
        city_res = data["main"]

        # nhiệt độ hiện tại
        current_temperature = city_res["temp"]
        # áp suất hiện tại
        current_pressure = city_res["pressure"]
        # độ ẩm hiện tại
        current_humidity = city_res["humidity"]
        # thời gian mặt trời
        suntime = data["sys"]
        # 	lúc mặt trời mọc, mặt trời mọc
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        # lúc mặt trời lặn
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        # thông tin thêm
        wthr = data["weather"]
        # mô tả thời tiết
        weather_description = wthr[0]["description"]
        # Lấy thời gian hệ thống cho vào biến now
        now = datetime.datetime.now()
        # hiển thị thông tin với người dùng
        content = f"""
        Thời tiết ở thành phố {city}  ngày {now.day} tháng {now.month} năm {now.year}
        Mặt trời mọc vào {sunrise.hour} giờ {sunrise.minute} phút
        Mặt trời lặn vào {sunset.hour} giờ {sunset.minute} phút
        Nhiệt độ trung bình là {current_temperature} độ C
        Áp suất không khí là {current_pressure} héc tơ Pascal
        Độ ẩm là {current_humidity}%
        """
        speak(content)
        speak("bạn cần loli giúp gì nữa không ?")
    else:
        # nếu tên thành phố không đúng thì nó nói dòng dưới 227
        speak("Không tìm thấy địa chỉ của bạn")

def current_weather1(text):
    # speak("Bạn muốn xem thời tiết ở đâu ạ.")
    # Đường dẫn trang web để lấy dữ liệu về thời tiết
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"

    # lưu tên thành phố vào biến city
    city = str(text).split("tiết ",1)[1]
    # nếu biến city != 0 và = False thì để đấy ko xử lí gì cả
    print(city)
    if not city:
        pass
    # api_key lấy trên open weather map
    api_key = "2c7c85350294ff16545481df0989c649"
    # tìm kiếm thông tin thời thời tiết của thành phố
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    # truy cập đường dẫn của dòng 188 lấy dữ liệu thời tiết
    response = requests.get(call_url)
    # lưu dữ liệu thời tiết dưới dạng json và cho vào biến data
    data = response.json()
    print('Thời tiết\n', data)
    city_res1 = data["weather"]
    print(city_res1)
    # kiểm tra nếu ko gặp lỗi 404 thì xem xét và lấy dữ liệu
    if data["cod"] != "404":
        # lấy value của key main
        city_res = data["main"]
        # nhiệt độ hiện tại
        current_temperature = city_res["temp"]
        # áp suất hiện tại
        current_pressure = city_res["pressure"]
        # độ ẩm hiện tại
        current_humidity = city_res["humidity"]
        # thời gian mặt trời
        suntime = data["sys"]
        # 	lúc mặt trời mọc, mặt trời mọc
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        # lúc mặt trời lặn
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        # thông tin thêm
        wthr = data["weather"]
        # mô tả thời tiết
        weather_description = wthr[0]["description"]
        # Lấy thời gian hệ thống cho vào biến now
        now = datetime.datetime.now()
        # hiển thị thông tin với người dùng
        content = f"""
        Thời tiết ở thành phố {city}  ngày {now.day} tháng {now.month} năm {now.year}
        Mặt trời mọc vào {sunrise.hour} giờ {sunrise.minute} phút
        Mặt trời lặn vào {sunset.hour} giờ {sunset.minute} phút
        Nhiệt độ trung bình là {current_temperature} độ C
        Áp suất không khí là {current_pressure} héc tơ Pascal
        Độ ẩm là {current_humidity}%
        """
        speak(content)
        speak("bạn cần loli giúp gì nữa không ?")
    else:
        # nếu tên thành phố không đúng thì nó nói dòng dưới 227
        speak("Không tìm thấy địa chỉ của bạn")

# current_weather1("thời tiết Đà Nẵng")
# current_weather()
# open_google_and_search('tìm kiếm đua thuyền')
def music_google():
    speak("bạn muốn mình hát về chủ đề nào")
    a = get_text()
    if ("rap" in a) or ("đọc rap" in a):
        mixer.init()
        mixer.music.load(r"C:\Users\Administrator\PycharmProjects\DoAnCS5\rap1.mp3")  # Music file can only be MP3
        mixer.music.play()
        # Then start a infinite loop
        time.sleep(22)
        speak("Bạn muốn loli làm gì nữa không ")
    elif ("sinh nhật" in a):
        mixer.init()
        mixer.music.load(r"C:\Users\Administrator\PycharmProjects\DoAnCS5\sn1.mp3")  # Music file can only be MP3
        mixer.music.play()
        # Then start a infinite loop
        time.sleep(15)
        speak("Bạn muốn loli làm gì nữa không ")
    else:
        mixer.init()
        mixer.music.load(r"C:\Users\Administrator\PycharmProjects\DoAnCS5\nono.mp3")  # Music file can only be MP3
        mixer.music.play()
        time.sleep(13)
        speak("Bạn muốn loli làm gì nữa không ")

def main_brain():
    global name
    speak("Xin chào. Mình tên là loli. Bạn tên là gì ?")
    name =get_text()
    if name:

        speak(f"Chào bạn {name} Bạn cần mình giúp gì") #f=> thay thế cho format
        while True:
            text = get_text()
            if not text: #nếu text kg có giá trị thì dừng chương trình
                break
            elif "chào" in text:
                hello()

            elif ("tạm biệt" in text) or ("hẹn gặp lại" in text):
                stop()
                break

            elif ('hiện tại' in text) or ("hôm nay" in text) or("bây giờ" in text):
                get_time(text)

            elif "mở" in text:
                if '.' in text:
                    Open_website(text)
                else:
                    open_app(text)
            elif 'tìm kiếm' in text:
                if  str(text).split("kiếm",1)[1] == '':
                    open_google_and_search1()
                else:
                    open_google_and_search(text)
            # elif 'dịch từ' in text:
            #     if str(text).split("từ",1)[1] == '':
            #         UITEXT.listenTranSlate1()
            #     else:
            #         UITEXT.listenTranSlate1(text)
            elif ('thời tiết' in text):
                if  str(text).split('tiết',1)[1] == "":
                    current_weather()
                else:
                    current_weather1(text)
            elif("tìm đường" in text):
                if str(text).split('đường',1)[1] == "":
                    open_google_map()
                else:
                    open_google_map1(text)
            elif ("tìm trên youtube" in text) or ('youtube' in text):
                play_Youtube()
            elif ('thay đổi hình nền' in text) or ("hình nền" in text):
                speak("bạn muốn thay đổi hình nền động hay tĩnh!")
                a = get_text()
                if ('động' in a) or ('hình nền động' in a):
                    os.startfile(r"C:\Users\Administrator\AppData\Local\Programs\PUSH Entertainment\Video Wallpaper\pushvideowallpaper.exe")
                    speak("đã thay đổi hình nền, bạn muốn loli làm gì nữa không !")

                else:
                    change_wellpaper()
                    speak("bạn muốn loli làm gì nữa không !")

            elif ("hát bài" in text) or ("hát" in text):
                music_google()

            elif ("tạm dừng" in text) or ("chờ" in text):
                 time.sleep(15)
                 speak(f'Bạn {name} ơi bạn cần mình giúp gì không ?')

            elif  ("không cần" in text) or ('không' in text):
                speak(f"Chào {name},hẹn gặp lại sau nha!")
                print('stop')
                return
            else:
                speak("CHức năng chưa đươc cài đặt, ông có thể cài đặt cho tui không")


# main_brain()
# mainT = threading.Thread(target=main_brain)
def continu():
    if name:
        speak(f"{name} muốn mình giúp gì!")
        while True:
            text = get_text()
            if not text: #nếu text kg có giá trị thì dừng chương trình
                break
            elif "chào" in text:
                hello()

            elif ("tạm biệt" in text) or ("hẹn gặp lại" in text):
                stop()
                break

            elif ('hiện tại' in text) or ("hôm nay" in text) or("bây giờ" in text):
                get_time(text)

            elif "mở" in text:
                if '.' in text:
                    Open_website(text)
                else:
                    open_app(text)
            elif 'tìm kiếm' in text:
                if  str(text).split("kiếm",1)[1] == '':
                    open_google_and_search1()
                else:
                    open_google_and_search(text)
            # elif 'dịch từ' in text:
            #     if str(text).split("từ",1)[1] == '':
            #         UITEXT.listenTranSlate1()
            #     else:
            #         UITEXT.listenTranSlate1(text)
            elif ('thời tiết' in text):
                if  str(text).split('tiết',1)[1] == "":
                    current_weather()
                else:
                    current_weather1(text)
            elif("tìm đường" in text):
                if str(text).split('đường',1)[1] == "":
                    open_google_map()
                else:
                    open_google_map1(text)
            elif ("tìm trên youtube" in text) or ('youtube' in text):
                play_Youtube()
            elif ('thay đổi hình nền' in text) or ("hình nền" in text):
                speak("bạn muốn thay đổi hình nền động hay tĩnh!")
                a = get_text()
                if ('động' in a) or ('hình nền động' in a):
                    os.startfile(r"C:\Users\Administrator\AppData\Local\Programs\PUSH Entertainment\Video Wallpaper\pushvideowallpaper.exe")
                    speak("đã thay đổi hình nền, bạn muốn loli làm gì nữa không !")

                else:
                    change_wellpaper()
                    speak("bạn muốn loli làm gì nữa không !")

            elif ("hát bài" in text) or ("hát" in text):
                music_google()

            elif ("tạm dừng" in text) or ("chờ" in text):
                 time.sleep(15)
                 speak(f'Bạn {name} ơi bạn cần mình giúp gì không ?')

            elif  ("không cần" in text) or ('không' in text):
                speak(f"Chào {name}, hẹn gặp lại sau nha!")
                print('stop')
                return
            else:
                speak("CHức năng chưa đươc cài đặt, bạn có thể cài đặt cho tui không")
    else:
        speak("bạn chưa bắt đầu, hãy nhấn nút start")

# mainT = threading.Thread(target=main_brain())
# mainContinues = threading.Thread(target=continu())