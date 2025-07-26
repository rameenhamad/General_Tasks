import time

# In aruments by using '\r' keeps cruser to begining of current line

# By For Loop
sec = int(input("enter sec: "))
for x in range(sec,0,-1):
    seconds = x % 60
    minute = int((x/60) % 60)
    hour = int(x / 3600)
    print(f"{hour:02}:{minute:02}:{seconds:02}", end='\r')
    time.sleep(1)
print('time up')

# # By While Loop
# sec = int(input("enter sec: "))
# while sec>0:
#     seconds = int(sec % 60)
#     minute = int((sec/60) % 60)
#     hour = int(sec / 3600)
#     print(f"{hour:00}:{minute:00}:{seconds:00}", end='\r')
#     time.sleep(1)
#     sec -= 1
# print("time up")

# # By Function
# def conver_time(sec):
#     while True:
#         seconds = int(sec % 60)
#         minute = int((sec/60) % 60)
#         hour = int(sec / 3600)
#         form = '{:02d}:{:02d}:{:02d}'.format(hour,minute,seconds)
#         print(form, end='\r')
#         # print(f"{hour:00}:{minute:00}:{seconds:00}")
#         time.sleep(1)
#         sec -= 1
# sec = int(input("enter sec: "))
# conver_time(sec)
# print("time up")  