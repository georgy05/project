import json
import time
from threading import Thread
import winsound
preliminarycall=input("укажите полный путь к аудиофайлу (в формате .mp3) для предварительного звонка: ",)
lesstartcall=input("укажите полный путь к аудиофайлу (в формате .mp3) для звонка к началу урока: ",)
lesend=input("укажите полный путь к аудиофайлу (в формате .mp3) для звонка после окончания урока: ",)
timetable={
 "Monday":{
    "Lesson 1":{"preliminary":"Monday 08:29:00",
              "start":"Monday 08:30:00",
              "end":"Monday 09:15:00"},
    "Lesson 2":{"preliminary":"Monday 09:29:00",
              "start":"Monday 09:30:00",
              "end":"Monday 10:15:00"},
    "Lesson 3":{"preliminary":"Monday 10:34:00",
              "start":"Monday 10:35:00",
              "end":"Monday 11:20:00"},
    "Lesson 4":{"preliminary":"Monday 11:29:00",
              "start":"Monday 11:30:00",
              "end":"Monday 12:15:00"},
    "Lesson 5":{"preliminary":"Monday 12:34:00",
              "start":"Monday 12:35:00",
              "end":"Monday 13:20:00"},
    "Lesson 6":{"preliminary":"Monday 13:29:00",
              "start":"Monday 13:30:00",
              "end":"Monday14:15:00"},
    "Lesson 7":{"preliminary":"Monday 14:24:00",
              "start":"Monday 14:25:00",
              "end":"Monday 15:10:00"},
    "Lesson 8":{"preliminary":"Monday 15:19:00",
              "start":"Monday 15:20:00",
              "end":"Monday 16:05:00"},
    "Lesson 9":{"preliminary":"Monday 16:24:00",
              "start":"Monday 16:25:00",
              "end":"Monday 17:10:00"}
    },
 "Tuesday":{
    "Lesson 1":{"preliminary":"Tuesday 08:29:00",
              "start":"Tuesday 08:30:00",
              "end":"Tuesday 09:15:00"},
    "Lesson 2":{"preliminary":"Tuesday 09:29:00",
              "start":"Tuesday 09:30:00",
              "end":"Tuesday 10:15:00"},
    "Lesson 3":{"preliminary":"Tuesday 10:34:00",
              "start":"Tuesday 10:35:00",
              "end":"Tuesday 11:20:00"},
    "Lesson 4":{"preliminary":"Tuesday 11:29:00",
              "start":"Tuesday 11:30:00",
              "end":"Tuesday 12:15:00"},
    "Lesson 5":{"preliminary":"Tuesday 12:34:00",
              "start":"Tuesday 12:35:00",
              "end":"Tuesday 13:20:00"},
    "Lesson 6":{"preliminary":"Tuesday 13:29:00",
              "start":"Tuesday 13:30:00",
              "end":"Tuesday 14:15:00"},
    "Lesson 7":{"preliminary":"Tuesday 14:24:00",
              "start":"Tuesday 14:25:00",
              "end":"Tuesday 15:10:00"},
    "Lesson 8":{"preliminary":"Tuesday 15:19:00",
              "start":"Tuesday 15:20:00",
              "end":"Tuesday 16:05:00"},
    "Lesson 9":{"preliminary":"Tuesday 16:24:00",
              "start":"Tuesday 16:25:00",
              "end":"Tuesday 17:10:00"}
    },
 "Wednesday":{
    "Lesson 1":{"preliminary":"Wednesday 08:29:00",
              "start":"Wednesday 08:30:00",
              "end":"Wednesday 09:15:00"},
    "Lesson 2":{"preliminary":"Wednesday 09:29:00",
              "start":"Wednesday 09:30:00",
              "end":"Wednesday 10:15:00"},
    "Lesson 3":{"preliminary":"Wednesday 10:34:00",
              "start":"Wednesday 10:35:00",
              "end":"Wednesday 11:20:00"},
    "Lesson 4":{"preliminary":"Wednesday 11:29:00",
              "start":"Wednesday 11:30:00",
              "end":"Wednesday 12:15:00"},
    "Lesson 5":{"preliminary":"Wednesday 12:34:00",
              "start":"Wednesday 12:35:00",
              "end":"Wednesday 13:20:00"},
    "Lesson 6":{"preliminary":"Wednesday 13:29:00",
              "start":"Wednesday 13:30:00",
              "end":"Wednesday 14:15:00"},
    "Lesson 7":{"preliminary":"Wednesday 14:24:00",
              "start":"Wednesday 14:25:00",
              "end":"Wednesday 15:10:00"},
    "Lesson 8":{"preliminary":"Wednesday 15:19:00",
              "start":"Wednesday 15:20:00",
              "end":"Wednesday 16:05:00"},
    "Lesson 9":{"preliminary":"Wednesday 16:24:00",
              "start":"Wednesday 16:25:00",
              "end":"Wednesday 17:10:00"}
    },
 "Thursday":{
    "Lesson 1":{"preliminary":"Thursday 08:29:00",
              "start":"Thursday 08:30:00",
              "end":"Thursday 09:15:00"},
    "Lesson 2":{"preliminary":"Thursday 09:29:00",
              "start":"Thursday 09:30:00",
              "end":"Thursday 10:15:00"},
    "Lesson 3":{"preliminary":"Thursday 10:34:00",
              "start":"Thursday 10:35:00",
              "end":"Thursday 11:20:00"},
    "Lesson 4":{"preliminary":"Thursday 11:29:00",
              "start":"Thursday 11:30:00",
              "end":"Thursday 12:15:00"},
    "Lesson 5":{"preliminary":"Thursday 12:34:00",
              "start":"Thursday 12:35:00",
              "end":"Thursday 13:20:00"},
    "Lesson 6":{"preliminary":"Thursday 13:29:00",
              "start":"Thursday 13:30:00",
              "end":"Thursday 14:15:00"},
    "Lesson 7":{"preliminary":"Thursday 14:24:00",
              "start":"Thursday 14:25:00",
              "end":"Thursday 15:10:00"},
    "Lesson 8":{"preliminary":"Thursday 15:19:00",
              "start":"Thursday 15:20:00",
              "end":"Thursday 16:05:00"},
    "Lesson 9":{"preliminary":"Thursday 16:24:00",
              "start":"Thursday 16:25:00",
              "end":"Thursday 17:10:00"}
    },
 "Friday":{
    "Lesson 1":{"preliminary":"Friday 08:29:00",
              "start":"Friday 08:30:00",
              "end":"Friday 09:15:00"},
    "Lesson 2":{"preliminary":"Friday 09:29:00",
              "start":"Friday 09:30:00",
              "end":"Friday 10:15:00"},
    "Lesson 3":{"preliminary":"Friday 10:34:00",
              "start":"Friday 10:35:00",
              "end":"Friday 11:20:00"},
    "Lesson 4":{"preliminary":"Friday 11:29:00",
              "start":"Friday 11:30:00",
              "end":"Friday 12:15:00"},
    "Lesson 5":{"preliminary":"Friday 12:34:00",
              "start":"Friday 12:35:00",
              "end":"Friday 13:20:00"},
    "Lesson 6":{"preliminary":"Friday 13:29:00",
              "start":"Friday 13:30:00",
              "end":"Friday 14:15:00"},
    "Lesson 7":{"preliminary":"Friday 14:24:00",
              "start":"Friday 14:25:00",
               "end":"Friday 15:10:00"},
     "Lesson 8":{"preliminary":"Friday 15:19:00",
               "start":"Friday 15:20:00",
               "end":"Friday 16:05:00"},
     "Lesson 9":{"preliminary":"Friday 16:24:00",
               "start":"Friday 16:25:00",
               "end":"Friday 17:10:00"}
     },
     }
def sound ():
    winsound.PlaySound('C:\\Users\\rezik\\Downloads\\export (1).WAV', winsound.SND_FILENAME)
def soundpreliminary ():
    playSound(preliminarycall)
def soundstart ():
    playSound(lesstartcall)   
def soundend ():
    playSound(lesendcall)    
while True:
        named_tuple = time.localtime()
        time_string = time.strftime("%A %H:%M:%S", named_tuple)
        print(time_string)
        time.sleep(1)
        if time_string == (timetable["Monday"]["Lesson 1"]["end"]) or time_string == (timetable["Monday"]["Lesson 2"]["end"]) or time_string == (timetable["Monday"]["Lesson 3"]["end"]) or time_string == (timetable["Monday"]["Lesson 4"]["end"]) or time_string == (timetable["Monday"]["Lesson 5"]["end"]) or time_string == (timetable["Monday"]["Lesson 6"]["end"]) or time_string == (timetable["Monday"][ "Lesson 7"]["end"]) or time_string == (timetable["Monday"]["Lesson 8"]["end"]) or time_string == (timetable["Monday"]["Lesson 9" ]["end"]):
         th=Thread(target=soundend)
         th.start()
        elif time_string == (timetable["Tuesday"]["Lesson 1"]["end"]) or time_string == (timetable["Tuesday"]["Lesson 2"]["end"]) or time_string == (timetable["Tuesday"]["Lesson 3"]["end"]) or time_string == (timetable["Tuesday"]["Lesson 4"]["end"]) or time_string == (timetable["Tuesday"]["Lesson 5"]["end"]) or time_string == (timetable["Tuesday"]["Lesson 6"]["end"]) or time_string == (timetable["Tuesday"][ "Lesson 7"]["end"]) or time_string == (timetable["Tuesday"]["Lesson 8"]["end"]) or time_string == (timetable["Tuesday"]["Lesson 9" ]["end"]):
          th=Thread(target=soundend)
          th.start()
        elif time_string == (timetable["Wednesday"]["Lesson 1"]["end"]) or time_string == (timetable["Wednesday"]["Lesson 2"]["end"]) or time_string == (timetable["Wednesday"]["Lesson 3"]["end"]) or time_string == (timetable["Wednesday"]["Lesson 4"]["end"]) or time_string == (timetable["Wednesday"]["Lesson 5"]["end"]) or time_string == (timetable["Wednesday"]["Lesson 6"]["end"]) or time_string == (timetable["Wednesday"][ "Lesson 7"]["end"]) or time_string == (timetable["Wednesday"]["Lesson 8"]["end"]) or time_string == (timetable["Wednesday"]["Lesson 9" ]["end"]):
         th=Thread(target=soundend)
         th.start()
        elif time_string == (timetable["Thursday"]["Lesson 1"]["end"]) or time_string == (timetable["Thursday"]["Lesson 2"]["end"]) or time_string == (timetable["Thursday"]["Lesson 3"]["end"]) or time_string == (timetable["Thursday"]["Lesson 4"]["end"]) or time_string == (timetable["Thursday"]["Lesson 5"]["end"]) or time_string == (timetable["Thursday"]["Lesson 6"]["end"]) or time_string == (timetable["Thursday"][ "Lesson 7"]["end"]) or time_string == (timetable["Thursday"]["Lesson 8"]["end"]) or time_string == (timetable["Thursday"]["Lesson 9" ]["end"]):
         th=Thread(target=soundend)
         th.start()
        elif time_string == (timetable["Friday"]["Lesson 1"]["end"]) or time_string == (timetable["Friday"]["Lesson 2"]["end"]) or time_string == (timetable["Friday"]["Lesson 3"]["end"]) or time_string == (timetable["Friday"]["Lesson 4"]["end"]) or time_string == (timetable["Friday"]["Lesson 5"]["end"]) or time_string == (timetable["Friday"]["Lesson 6"]["end"]) or time_string == (timetable["Friday"][ "Lesson 7"]["end"]) or time_string == (timetable["Friday"]["Lesson 8"]["end"]) or time_string == (timetable["Friday"]["Lesson 9" ]["end"]):
         th=Thread(target=soundend)
         th.start()    
        elif time_string == (timetable["Monday"]["Lesson 1"]["preliminary"]) or time_string == (timetable["Monday"]["Lesson 2"]["preliminary"]) or time_string == (timetable["Monday"]["Lesson 3"]["preliminary"]) or time_string == (timetable["Monday"]["Lesson 4"]["preliminary"]) or time_string == (timetable["Monday"]["Lesson 5"]["preliminary"]) or time_string == (timetable["Monday"]["Lesson 6"]["preliminary"]) or time_string == (timetable["Monday"][ "Lesson 7"]["preliminary"]) or time_string == (timetable["Monday"]["Lesson 8"]["preliminary"]) or time_string == (timetable["Monday"]["Lesson 9" ]["preliminary"]):
         th=Thread(target=soundpreliminary)
         th.start()
        elif time_string == (timetable["Tuesday"]["Lesson 1"]["preliminary"]) or time_string == (timetable["Tuesday"]["Lesson 2"]["preliminary"]) or time_string == (timetable["Tuesday"]["Lesson 3"]["preliminary"]) or time_string == (timetable["Tuesday"]["Lesson 4"]["preliminary"]) or time_string == (timetable["Tuesday"]["Lesson 5"]["preliminary"]) or time_string == (timetable["Tuesday"]["Lesson 6"]["preliminary"]) or time_string == (timetable["Tuesday"][ "Lesson 7"]["preliminary"]) or time_string == (timetable["Tuesday"]["Lesson 8"]["preliminary"]) or time_string == (timetable["Tuesday"]["Lesson 9" ]["preliminary"]):
         th=Thread(target=soundpreliminary)
         th.start()
        elif time_string == (timetable["Wednesday"]["Lesson 1"]["preliminary"]) or time_string == (timetable["Wednesday"]["Lesson 2"]["preliminary"]) or time_string == (timetable["Wednesday"]["Lesson 3"]["preliminary"]) or time_string == (timetable["Wednesday"]["Lesson 4"]["preliminary"]) or time_string == (timetable["Wednesday"]["Lesson 5"]["preliminary"]) or time_string == (timetable["Wednesday"]["Lesson 6"]["preliminary"]) or time_string == (timetable["Wednesday"][ "Lesson 7"]["preliminary"]) or time_string == (timetable["Wednesday"]["Lesson 8"]["preliminary"]) or time_string == (timetable["Wednesday"]["Lesson 9" ]["preliminary"]):
         th=Thread(target=soundpreliminary)
         th.start()
        elif time_string == (timetable["Thursday"]["Lesson 1"]["preliminary"]) or time_string == (timetable["Thursday"]["Lesson 2"]["preliminary"]) or time_string == (timetable["Thursday"]["Lesson 3"]["preliminary"]) or time_string == (timetable["Thursday"]["Lesson 4"]["preliminary"]) or time_string == (timetable["Thursday"]["Lesson 5"]["preliminary"]) or time_string == (timetable["Thursday"]["Lesson 6"]["preliminary"]) or time_string == (timetable["Thursday"][ "Lesson 7"]["preliminary"]) or time_string == (timetable["Thursday"]["Lesson 8"]["preliminary"]) or time_string == (timetable["Thursday"]["Lesson 9" ]["preliminary"]):
         th=Thread(target=soundpreliminary)
         th.start()
        elif time_string == (timetable["Friday"]["Lesson 1"]["preliminary"]) or time_string == (timetable["Friday"]["Lesson 2"]["preliminary"]) or time_string == (timetable["Friday"]["Lesson 3"]["preliminary"]) or time_string == (timetable["Friday"]["Lesson 4"]["preliminary"]) or time_string == (timetable["Friday"]["Lesson 5"]["preliminary"]) or time_string == (timetable["Friday"]["Lesson 6"]["preliminary"]) or time_string == (timetable["Friday"][ "Lesson 7"]["preliminary"]) or time_string == (timetable["Friday"]["Lesson 8"]["preliminary"]) or time_string == (timetable["Friday"]["Lesson 9" ]["preliminary"]):
         th=Thread(target=soundpreliminary)
         th.start()  
        elif time_string == (timetable["Monday"]["Lesson 1"]["start"]) or time_string == (timetable["Monday"]["Lesson 2"]["start"]) or time_string == (timetable["Monday"]["Lesson 3"]["start"]) or time_string == (timetable["Monday"]["Lesson 4"]["start"]) or time_string == (timetable["Monday"]["Lesson 5"]["start"]) or time_string == (timetable["Monday"]["Lesson 6"]["start"]) or time_string == (timetable["Monday"][ "Lesson 7"]["start"]) or time_string == (timetable["Monday"]["Lesson 8"]["start"]) or time_string == (timetable["Monday"]["Lesson 9" ]["start"]):
         th=Thread(target=soundstart)
         th.start()
        elif time_string == (timetable["Tuesday"]["Lesson 1"]["start"]) or time_string == (timetable["Tuesday"]["Lesson 2"]["start"]) or time_string == (timetable["Tuesday"]["Lesson 3"]["start"]) or time_string == (timetable["Tuesday"]["Lesson 4"]["start"]) or time_string == (timetable["Tuesday"]["Lesson 5"]["start"]) or time_string == (timetable["Tuesday"]["Lesson 6"]["start"]) or time_string == (timetable["Tuesday"][ "Lesson 7"]["start"]) or time_string == (timetable["Tuesday"]["Lesson 8"]["start"]) or time_string == (timetable["Tuesday"]["Lesson 9" ]["start"]):
         th=Thread(target=soundstart)
         th.start()
        elif time_string == (timetable["Wednesday"]["Lesson 1"]["start"]) or time_string == (timetable["Wednesday"]["Lesson 2"]["start"]) or time_string == (timetable["Wednesday"]["Lesson 3"]["start"]) or time_string == (timetable["Wednesday"]["Lesson 4"]["start"]) or time_string == (timetable["Wednesday"]["Lesson 5"]["start"]) or time_string == (timetable["Wednesday"]["Lesson 6"]["start"]) or time_string == (timetable["Wednesday"][ "Lesson 7"]["start"]) or time_string == (timetable["Wednesday"]["Lesson 8"]["start"]) or time_string == (timetable["Wednesday"]["Lesson 9" ]["start"]):
         th=Thread(target=soundstart)
         th.start()
        elif time_string == (timetable["Thursday"]["Lesson 1"]["start"]) or time_string == (timetable["Thursday"]["Lesson 2"]["start"]) or time_string == (timetable["Thursday"]["Lesson 3"]["start"]) or time_string == (timetable["Thursday"]["Lesson 4"]["start"]) or time_string == (timetable["Thursday"]["Lesson 5"]["start"]) or time_string == (timetable["Thursday"]["Lesson 6"]["start"]) or time_string == (timetable["Thursday"][ "Lesson 7"]["start"]) or time_string == (timetable["Thursday"]["Lesson 8"]["start"]) or time_string == (timetable["Thursday"]["Lesson 9" ]["start"]):
         th=Thread(target=soundstart)
         th.start()
        elif time_string == (timetable["Friday"]["Lesson 1"]["start"]) or time_string == (timetable["Friday"]["Lesson 2"]["start"]) or time_string == (timetable["Friday"]["Lesson 3"]["start"]) or time_string == (timetable["Friday"]["Lesson 4"]["start"]) or time_string == (timetable["Friday"]["Lesson 5"]["start"]) or time_string == (timetable["Friday"]["Lesson 6"]["start"]) or time_string == (timetable["Friday"][ "Lesson 7"]["start"]) or time_string == (timetable["Friday"]["Lesson 8"]["start"]) or time_string == (timetable["Friday"]["Lesson 9" ]["start"]):
         th=Thread(target=soundstart)
         th.start()        
         