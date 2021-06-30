import webbrowser as web
import time
import pyautogui as pg

def getTimeAndExecute(meeting_time,link):
    t = time.localtime()
    current_time = time.strftime('%H:%M',t)
    while current_time!=meeting_time:
        t = time.localtime()
        current_time = time.strftime('%H:%M',t)
    joinMeeting(link)

    

def joinMeeting(link):
    web.open(link)
    time.sleep(30)               #waiting for the page to open
    pg.hotkey('ctrl','d')           #turn off mic
    time.sleep(2.5)
    pg.hotkey('ctrl','e')           #turn off camera
    time.sleep(2.5)
    pg.moveTo(930,316)
    pg.click()
    time.sleep(2.5)
    pg.moveTo(930,458)
    pg.click()

def admitEntry():
    time.sleep(2.5)
    pg.moveTo(847,198)
    while True:
        time.sleep(5)
        pg.click(847,198)



#joinMeeting('https://meet.google.com/vzc-kdyo-ggy')
time.sleep(4)
meeting_time = pg.prompt('Enter the meeting time.\nFormate should be in HH:MM (24hr)')
link = pg.prompt('Enter or paste the meeting link and press enter.')
host = pg.confirm("Are you the host of this meeting?\n'If yes then the participants will be admited automatically'\nIf yes then click 'OK' otherwise 'Cancel'")
getTimeAndExecute(meeting_time,link)
if host=='OK':
    admitEntry()
