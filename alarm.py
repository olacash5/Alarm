import datetime
import winsound

alarm_hour = int(input('what hour do you want to wake up?'))
alarm_minute = int (input('what minute do you want to get up?'))
am_pm = str(input('am or pm'))

if am_pm == 'pm':
    alarm_hour = alarm_hour + 12

while(1 == 1):
    if alarm_hour == datetime.datetime.now().hour and alarm_minute == datetime.datetime.now().minute:
        print('wake up man')
        break
    for i in range(2):
        winsound.Beep(3000,200)
        datetime.datetime.now()

print('alarm turned off')