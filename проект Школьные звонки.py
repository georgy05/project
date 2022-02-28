import json
import time
from threading import Thread
import winsound
preliminary1=input("введите время предварительного звонка перед 1 уроком в формате 'чч:мм:сс' : ",)
lesstart1=input("введите время начала 1 урока в формате 'чч:мм:сс' : ",)
lesend1=input("введите время окончания 1 урока в формате 'чч:мм:сс' : ",)
preliminary2=input("введите время предварительного звонка перед 2 уроком в формате 'чч:мм:сс' : ",)
lesstart2=input("введите время начала 2 урока в формате 'чч:мм:сс' : ",)
lesend2=input("введите время окончания 2 урока в формате 'чч:мм:сс' : ",)
preliminary3=input("введите время предварительного звонка перед 3 уроком в формате 'чч:мм:сс' : ",)
lesstart3=input("введите время начала 3 урока в формате 'чч:мм:сс' : ",)
lesend3=input("введите время окончания 3 урока в формате 'чч:мм:сс' : ",)
preliminary4=input("введите время предварительного звонка перед 4 уроком в формате 'чч:мм:сс' : ",)
lesstart4=input("введите время начала 4 урока в формате 'чч:мм:сс' : ",)
lesend4=input("введите время окончания 4 урока в формате 'чч:мм:сс' : ",)
preliminary5=input("введите время предварительного звонка перед 5 уроком в формате 'чч:мм:сс' : ",)
lesstart5=input("введите время начала 5 урока в формате 'чч:мм:сс' : ",)
lesend5=input("введите время окончания 5 урока в формате 'чч:мм:сс' : ",)
preliminary6=input("введите время предварительного звонка перед 6 уроком в формате 'чч:мм:сс' : ",)
lesstart6=input("введите время начала 6 урока в формате 'чч:мм:сс' : ",)
lesend6=input("введите время окончания 6 урока в формате 'чч:мм:сс' : ",)
preliminary7=input("введите время предварительного звонка перед 7 уроком в формате 'чч:мм:сс' : ",)
lesstart7=input("введите время начала 7 урока в формате 'чч:мм:сс' : ",)
lesend7=input("введите время окончания 7 урока в формате 'чч:мм:сс' : ",)
preliminary8=input("введите время предварительного звонка перед 8 уроком в формате 'чч:мм:сс' : ",)
lesstart8=input("введите время начала 8 урока в формате 'чч:мм:сс' : ",)
lesend8=input("введите время окончания 8 урока в формате 'чч:мм:сс' : ",)
preliminary9=input("введите время предварительного звонка перед 9 уроком в формате 'чч:мм:сс' : ",)
lesstart9=input("введите время начала 9 урока в формате 'чч:мм:сс' : ",)
lesend9=input("введите время окончания 9 урока в формате 'чч:мм:сс' : ",)

preliminarycall=input("укажите полный путь к аудиофайлу (в формате .wav) для предварительного звонка: ",)
lesstartcall=input("укажите полный путь к аудиофайлу (в формате .wav) для звонка к началу урока: ",)
lesend=input("укажите полный путь к аудиофайлу (в формате .wav) для звонка после окончания урока: ",)

timetable={
 "Понедельник":{ 
    "1 урок":{"предварительный":preliminary1,
              "начало":lesstart1,
              "конец":lesend1}, 
    "2 урок":{"предварительный":preliminary2,
              "начало":lesstart2,
              "конец":lesend2}, 
    "3 урок":{"предварительный":preliminary3,
              "начало":lesstart3,
              "конец":lesend3}, 
    "4 урок":{"предварительный":preliminary4,
              "начало":lesstart4,
              "конец":lesend4}, 
    "5 урок":{"предварительный":preliminary5,
              "начало":lesstart5,
              "конец":lesend5}, 
    "6 урок":{"предварительный":preliminary6,
              "начало":lesstart6,
              "конец":lesend6}, 
    "7 урок":{"предварительный":preliminary7,
              "начало":lesstart7,
              "конец":lesend7}, 
    "8 урок":{"предварительный":preliminary8,
              "начало":lesstart8,
              "конец":lesend8}, 
    "9 урок":{"предварительный":preliminary9,
              "начало":lesstart9,
              "конец":lesend9}, 
    },
 "Вторник":{
   "1 урок":{"предварительный":preliminary1,
              "начало":lesstart1,
              "конец":lesend1}, 
    "2 урок":{"предварительный":preliminary2,
              "начало":lesstart2,
              "конец":lesend2}, 
    "3 урок":{"предварительный":preliminary3,
              "начало":lesstart3,
              "конец":lesend3}, 
    "4 урок":{"предварительный":preliminary4,
              "начало":lesstart4,
              "конец":lesend4}, 
    "5 урок":{"предварительный":preliminary5,
              "начало":lesstart5,
              "конец":lesend5}, 
    "6 урок":{"предварительный":preliminary6,
              "начало":lesstart6,
              "конец":lesend6}, 
    "7 урок":{"предварительный":preliminary7,
              "начало":lesstart7,
              "конец":lesend7}, 
    "8 урок":{"предварительный":preliminary8,
              "начало":lesstart8,
              "конец":lesend8}, 
    "9 урок":{"предварительный":preliminary9,
              "начало":lesstart9,
              "конец":lesend9}, 
    },
 "Среда":{ 
   "1 урок":{"предварительный":preliminary1,
              "начало":lesstart1,
              "конец":lesend1}, 
    "2 урок":{"предварительный":preliminary2,
              "начало":lesstart2,
              "конец":lesend2}, 
    "3 урок":{"предварительный":preliminary3,
              "начало":lesstart3,
              "конец":lesend3}, 
    "4 урок":{"предварительный":preliminary4,
              "начало":lesstart4,
              "конец":lesend4}, 
    "5 урок":{"предварительный":preliminary5,
              "начало":lesstart5,
              "конец":lesend5}, 
    "6 урок":{"предварительный":preliminary6,
              "начало":lesstart6,
              "конец":lesend6}, 
    "7 урок":{"предварительный":preliminary7,
              "начало":lesstart7,
              "конец":lesend7}, 
    "8 урок":{"предварительный":preliminary8,
              "начало":lesstart8,
              "конец":lesend8}, 
    "9 урок":{"предварительный":preliminary9,
              "начало":lesstart9,
              "конец":lesend9}, 
    },
 "Четверг":{ 
    "1 урок":{"предварительный":preliminary1,
              "начало":lesstart1,
              "конец":lesend1}, 
    "2 урок":{"предварительный":preliminary2,
              "начало":lesstart2,
              "конец":lesend2}, 
    "3 урок":{"предварительный":preliminary3,
              "начало":lesstart3,
              "конец":lesend3}, 
    "4 урок":{"предварительный":preliminary4,
              "начало":lesstart4,
              "конец":lesend4}, 
    "5 урок":{"предварительный":preliminary5,
              "начало":lesstart5,
              "конец":lesend5}, 
    "6 урок":{"предварительный":preliminary6,
              "начало":lesstart6,
              "конец":lesend6}, 
    "7 урок":{"предварительный":preliminary7,
              "начало":lesstart7,
              "конец":lesend7}, 
    "8 урок":{"предварительный":preliminary8,
              "начало":lesstart8,
              "конец":lesend8}, 
    "9 урок":{"предварительный":preliminary9,
              "начало":lesstart9,
              "конец":lesend9}, 
    },
 "Пятница":{
    "1 урок":{"предварительный":preliminary1,
              "начало":lesstart1,
              "конец":lesend1}, 
    "2 урок":{"предварительный":preliminary2,
              "начало":lesstart2,
              "конец":lesend2}, 
    "3 урок":{"предварительный":preliminary3,
              "начало":lesstart3,
              "конец":lesend3}, 
    "4 урок":{"предварительный":preliminary4,
              "начало":lesstart4,
              "конец":lesend4}, 
    "5 урок":{"предварительный":preliminary5,
              "начало":lesstart5,
              "конец":lesend5}, 
    "6 урок":{"предварительный":preliminary6,
              "начало":lesstart6,
              "конец":lesend6}, 
    "7 урок":{"предварительный":preliminary7,
              "начало":lesstart7,
              "конец":lesend7}, 
    "8 урок":{"предварительный":preliminary8,
              "начало":lesstart8,
              "конец":lesend8}, 
    "9 урок":{"предварительный":preliminary9,
              "начало":lesstart9,
              "конец":lesend9}, 
    }
   }
def soundpreliminary ():
    winsound.PlaySound(preliminarycall, winsound.SND_FILENAME)
def soundstart ():
    winsound.PlaySound(lesstartcall, winsound.SND_FILENAME)   
def soundend ():
    winsound.PlaySound(lesendcall, winsound.SND_FILENAME)    
while True:
    named_tuple = time.localtime()
    time_string = time.strftime("%H:%M:%S", named_tuple)
    print(time_string)
    print(timetable["Понедельник"]["1 урок"]["предварительный"])
    time.sleep(1)
    if time_string == (timetable["Понедельник"]["1 урок"]["предварительный"]) or time_string == (timetable["Понедельник"]["2 урок"]["предварительный"]) or time_string == (timetable["Понедельник"]["3 урок"]["предварительный"]) or time_string == (timetable["Понедельник"]["4 урок"]["предварительный"]) or time_string == (timetable["Понедельник"]["5 урок"]["предварительный"]) or time_string == (timetable["Понедельник"]["6 урок"]["предварительный"]) or time_string == (timetable["Понедельник"]["7 урок"]["предварительный"]) or time_string == (timetable["Понедельник"]["8 урок"]["предварительный"]) or time_string == (timetable["Понедельник"]["9 урок"]["предварительный"]):
        th=Thread(target=soundpreliminary)
        th.start()    
    if  time_string == (timetable["Понедельник"]["1 урок"]["начало"]) or time_string == (timetable["Понедельник"]["2 урок"]["начало"]) or time_string == (timetable["Понедельник"]["3 урок"]["начало"]) or time_string == (timetable["Понедельник"]["4 урок"]["начало"]) or time_string == (timetable["Понедельник"]["5 урок"]["начало"]) or time_string == (timetable["Понедельник"]["6 урок"]["начало"]) or time_string == (timetable["Понедельник"]["7 урок"]["начало"]) or time_string == (timetable["Понедельник"]["8 урок"]["начало"]) or time_string == (timetable["Понедельник"]["9 урок"]["начало"]):
        th=Thread(target=soundstart)
        th.start()
    if  time_string == (timetable["Понедельник"]["1 урок"]["конец"]) or time_string == (timetable["Понедельник"]["2 урок"]["конец"]) or time_string == (timetable["Понедельник"]["3 урок"]["конец"]) or time_string == (timetable["Понедельник"]["4 урок"]["конец"]) or time_string == (timetable["Понедельник"]["5 урок"]["конец"]) or time_string == (timetable["Понедельник"]["6 урок"]["конец"]) or time_string == (timetable["Понедельник"]["7 урок"]["конец"]) or time_string == (timetable["Понедельник"]["8 урок"]["конец"]) or time_string == (timetable["Понедельник"]["9 урок"]["конец"]):
        th=Thread(target=soundend)
        th.start()           