import webbrowser as web
import time
import pyautogui as pg

def getTimeAndExecute(meeting_time,link):
    '''This function gets the time and repetedly checks it with the given time and executes further at correct time'''
    t = time.localtime()                        #time object
    current_time = time.strftime('%H:%M',t)     #Device current time
    while current_time!=meeting_time:           #to check the current time and given time repetedly
        t = time.localtime()
        current_time = time.strftime('%H:%M',t)
    joinMeeting(link)

    

def joinMeeting(link):
    '''This function is for joining the user to the meeting'''
    web.open(link)                      #opens the meeting link
    joinButton = getJoinButtonCoords()  #geting the coordinates of the join/ask to join button
    pg.hotkey('ctrl','d')               #turn off mic
    time.sleep(2.5)
    pg.hotkey('ctrl','e')               #turn off camera
    time.sleep(2.5)
    pg.click(joinButton)                #click on the join button
    #pg.moveTo(930,316)
    #pg.click()
    #time.sleep(2.5)
    #pg.moveTo(930,458)
    #pg.click()
    

def getJoinButtonCoords():
    '''This function mainly focuses on clicking the join/ask to join button wherever it appears'''
    while True:
        joinButtonCoords = pg.locateCenterOnScreen('img/joinButton.png')
        askToJoinButtonCoords = pg.locateCenterOnScreen('img/asktojoinbutton.png')
        if joinButtonCoords:
            return joinButtonCoords
        if askToJoinButtonCoords:
            return askToJoinButtonCoords
        
        
            
    

def admitEntry():
    time.sleep(2.5)
    admitButton = pg.locateCenterOnScreen('img/admitButton.PNG')
    if admitButton:
        pg.click(admitButton)
    admitEntry()



#joinMeeting('https://meet.google.com/vzc-kdyo-ggy')
time.sleep(4)
meeting_time = pg.prompt('Enter the meeting time.\nFormate should be in HH:MM (24hr)')
link = pg.prompt('Enter or paste the meeting link and press enter.')
host = pg.confirm("Are you the host of this meeting?\n'If yes then the participants will be admited automatically'\nIf yes then click 'OK' otherwise 'Cancel'")
getTimeAndExecute(meeting_time,link)
if host=='OK':
    admitEntry()
