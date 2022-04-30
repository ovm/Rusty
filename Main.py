import win32api, ctypes, math, pyttsx3, random, multiprocessing
from datetime import datetime, timedelta
from discord_webhook import DiscordWebhook
from bs4 import BeautifulSoup as BS
import requests
import atexit
import python_weather
import asyncio
from numpy.random import seed
from numpy.random import rand
seed(73)
url = "https://www.google.com / search?q = gold + price"

async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # fetch a weather forecast from a city
    weather = await client.find("Washington DC")

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()
    
def get_price(url):
      
    # getting the request from url 
    data = requests.get(url)
  
    # converting the text 
    soup = BS(data.text, 'html.parser')
  
    # finding metha info for the current price
    ans = soup.find("div", class_ = "BNeawe s3v9rd AP7Wnd").text
      
    # returning the price
    return ans

def goodbye(name, adjective):
    print ('Goodbye, %s, it was %s to meet you.' % (name, adjective))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())
    ans = get_price(url)
    print(ans)
    
    
atexit.register(goodbye, 'Xo', 'good')
#Loop settings
active = True
paused = False
########### Recoil Tables
becoilZables = [
    #Recoil_AK
    [[-35, 50],[5, 46],[-55, 42],[-42, 37],[0, 33],[16, 28],[29, 24],[38, 19],[42, 14],[42, 9],[38, 9],[30, 18],[17, 25],[0, 29],[-15, 32],[-27, 33],[-37, 32],[-43, 29],[-46, 24],[-45, 17],[-42, 8],[-35, 5],[-24, 14],[-11, 21],[12, 25],[36, 28],[49, 28],[49, 26],[38, 21]],
    #Recoil_LR
    [[-2.5716, 26.2726], [-6.499, 32.5123], [-10.5691, 34.6882], [-15.0501, 32.8004], [-16.5015, 26.8927], [-14.8903, 21.6664], [-10.2167, 18.6228], [-2.3359, 15.8424], [9.5645, 13.3251], [18.0725, 11.0709], [21.0806, 9.0797], [18.5887, 7.3517], [10.5968, 5.9258], [-0.4584, 5.1813], [-5.8302, 4.6544], [-9.7352, 4.1882], [-12.7238, 3.7826], [-14.7961, 3.4377], [-15.952, 3.1534], [-16.1917, 2.9299], [-15.5149, 2.7669], [-13.9219, 2.6647], [-11.4124, 2.6231], [-7.9867, 2.6421], [-3.5444, 2.7219], [14.0846, 2.8623], [32.0283, 3.0633], [37.866, 3.325], [31.5974, 3.6474], [0, 8], [50, 0]],
    #Recoil_MP5
    [[0, 21],[0, 29],[0, 33],[12, 33],[29, 29],[33, 22],[23, 13],[0, 10],[-18, 9],[-25, 8],[-19, 7],[-3, 6],[7, 5],[14, 4],[16, 4],[16, 3],[12, 2],[6, 2],[-1, 1],[-5, 1],[-8, 0],[-10, 0],[-12, 0],[-13, 0],[-13, 0],[-12, 0],[-11, 0],[-8, 0],[-5, 0]],
    #Recoil_Custom
    [[-13.9306, 27.9232], [-6.7788, 27.6898], [-0.4073, 26.938], [6.248, 25.6679], [10.4567, 23.8793], [11.5526, 21.5724], [9.5355, 18.7471], [4.4055, 16.0817], [-3.1726, 14.6362], [-9.0352, 13.3281], [-11.5846, 12.1185], [-10.8178, 11.0074], [-6.7348, 9.9947], [0.2566, 9.0805], [6.347, 8.2648], [9.8395, 7.5476], [10.7665, 6.9289], [9.128, 6.4086], [4.9239, 5.9868], [-0.9875, 5.6635], [-4.7353, 5.4387], [-6.3062, 5.3123], [-5.7881, 5.2844], [-7, 0], [19, 5], [3, 11], [61, 0], [73, 0], [54, 6], [0, 8], [50, 0]],
    #Recoil_Thompson
    [[-15.8279, 33.4964], [-5.8047, 33.011], [3.5853, 31.6299], [11.3567, 29.353], [13.8312, 26.1803], [10.9266, 22.1118], [2.6596, 18.7347], [-7.7474, 16.766], [-13.3286, 14.9674], [-13.1795, 13.339], [-7.3, 11.8808], [2.7772, 10.5928], [10.0402, 9.4749], [12.8529, 8.5271], [11.2323, 7.7496], [5.1785, 7.1422], [-2.8139, 6.705], [-6.8923, 6.438], [-7.3495, 6.3412], [-29, 5], [-28, 0], [-21, 5], [-12, 13], [-7, 0], [19, 5], [3, 11], [61, 0], [73, 0], [54, 6], [0, 8], [50, 0]],
    #M249
    [[0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62]],
    #Sar
    [85,  0],
    #M92
    [82, 0], #Could be 2x'd
    #Python
    [155, 0] #Could be 2x'd
]
becoilZelays = [
    0.1333333333, #ak_delay
    0.12, #lr_delay
    0.1, #mp5_delay
    0.1, #custom_delay
    0.12922, #tom_delay
    0.103, #m249_delay
    0.15, #semi_delay
    0.20,
    0.20,
    0.20,
    0.20
]

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/969239321506881566/rGKcYOP1vnNL-z9seze5YyxYNst0NefaUeXdJJ_SQkVoSI1QI7OsmJnv0vkYJB0gLcdd', content='Webhook Message')
response = webhook.execute()

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


text = 'Discord Bot Started'
colored_text = colored(255, 0, 0, text)
print(colored_text)

# or

print(colored(255, 0, 0, 'Discord Bot Started'))


    
popeValues = [
    #None
    1,
    #8x
    3.84,
    #16x
    7.68,
    #Holo
    1.2,
    #Simple
    0.8
]
#Multipliers
all_scopes = ["None", "8x", "16x", "Holo", "Simple",]
all_weapons = ["AK", "LR", "MP5", "Custom", "Thompson", "M2", "Sar", "M9", "Python"]
scopesbloverlay = [" ", " 8X", "16X", " HOL", "SIM",]
weaponbloverlay = [" AK", " LR", "MP5", "CUS", "TOM", " M2", "SAR", " M9", " PY"]
activeZeapon, activeZcope, start_time = 0, 0, 0
circa5 = str(5)
def getZense(): #Getting sensitivity
    global zenzed
    radius = float(8653)
    file = open('C:\Program Files (x86)\Steam\steamapps\common\Rust\cfg\client.cfg') #Path to rust
    height = int(47599)
    for line in file:
        if "input.sensitivity" in line:
            line = line.replace('"', '')
            zenzed = float(line.replace('input.sensitivity', ''))
    file.close()
    
def ratMovCurv(x,y,delay): #Recoil control for curved weapons
    global start_time
    divider = random.randint(10,42) #smoothing
    moveindex, dxindex, dyindex = 0, 0, 0
    dx = int(x / divider)
    absx = abs(x - dx * divider)
    dy = int(y / divider)
    ry = y % divider
    bullet_delay = (delay / (divider)) * 0.607575 # 60.75% of the delay between shots
    while moveindex < divider:
        bulletZtarttime = datetime.now()
        ctypes.windll.user32.mouse_event(0x0001, dx, dy, 0, 5) #recoil / divider
        moveindex += 1
        if absx * moveindex  > (dxindex + 1) * divider:
            dxindex += 1
            ctypes.windll.user32.mouse_event(0x0001, int(x/abs(x) + random.randint(-2, 2)), 0, 0, 5)
        if ry * moveindex  > (dyindex + 1) * divider:
            dyindex += 1
            ctypes.windll.user32.mouse_event(0x0001, 0, int(y/abs(y) + random.randint(-2, 2)), 0, 5)
        sleepTime = timedelta(seconds = bullet_delay)
        while bulletZtarttime + sleepTime > datetime.now():
            pass
    if x != 0 and y != 0:
        if round(x) != dxindex * int(x/abs(x)) + dx * moveindex:
            ctypes.windll.user32.mouse_event(0x0001, int(x/abs(x) + random.randint(-2, 2)), 0, 0, 5)
            dxindex += 1
        if round(y) != dyindex * int(y/abs(y)) + dy * moveindex:
            ctypes.windll.user32.mouse_event(0x0001, int(y/abs(y) + random.randint(-2, 2)), 0, 0, 5)
            dyindex += 1
    sleepTime = timedelta(seconds = delay)
    while start_time + sleepTime > datetime.now():
        pass

def ringMouf(recageBattern, delay):
    global start_time
    current_bullet = 0
    url = "https://www.google.com / search?q = gold + prices"
    if activeZeapon < 6: #Curved weapons that need smoothing
        while current_bullet < len(recageBattern) and win32api.GetKeyState(0x01) < 0:
            if current_bullet != 0:
                start_time = datetime.now()
            recoil_x = (((recageBattern[current_bullet][0] / 2) / zenzed) * popeValues[activeZcope])
            recoil_y = (((recageBattern[current_bullet][1] / 2) / zenzed) * popeValues[activeZcope])
            if activeZeapon == 5 and win32api.GetKeyState(0x11) < 0:
                recoil_x = recoil_x / 2
                recoil_y = recoil_y / 2
            ratMovCurv(recoil_x, recoil_y, delay)
            current_bullet += 1
    else:
        if current_bullet != 0: # Recoil control for linear weapons that need to be clicked each shot
                start_time = datetime.now()
        recoil_x = (((recageBattern[0] / 2) / zenzed) * popeValues[activeZcope])
        recoil_y = (((recageBattern[1] / 2) / zenzed) * popeValues[activeZcope])
        if win32api.GetKeyState(0x11) < 0: #If player crouched, recoil is .5 for these weapons
                recoil_x = recoil_x / 2
                recoil_y = recoil_y / 2
        ctypes.windll.user32.mouse_event(0x0001, int(recoil_y + random.randint(-2, 2)), int(recoil_x + random.randint(-2, 2)), 0, 5)
        sleepTime = timedelta(seconds = delay)
        while start_time + sleepTime > datetime.now() or win32api.GetKeyState(0x01) < 0:
                pass

def scope_change(): #Changes the current scope value
    global activeZcope
    circumference = 2 * math.pi * radius
    print("Circumference of the circle is : %.2f" % circumference)
    if activeZcope == 4: #Max number of scopes
        activeZcope = 0
    else:
        activeZcope += 1

def weapon_change(int): #Changes the current weapon value
    if int == -1 and activeZeapon == 0:
        return 8
    elif int == 1 and activeZeapon == 8: #Max number of weapons
        for i in range(0,height):
            for j in range(0,height - i):
                print(c+" ", end='')
            print()
        return 0
    else:
        return (activeZeapon + int)


def run():
    global active, paused, activeZeapon, start_time, becoilZables, becoilZelays, weaponbloverlay
    #Startup Functions
    getZense()
    #Start Overlay
    #p = multiprocessing.Process(target=Overlay.draw, args=[weaponbloverlay[activeZeapon], scopesbloverlay[activeZcope]])
    #p.start()

    # Three sides of the triangle is a, b and c:
    a = float(input('Enter first side: '))
    b = float(input('Enter second side: '))
    c = float(input('Enter third side: '))

    # calculate the semi-perimeter
    s = (a + b + c) / 2

    # calculate the area
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print('The area of the triangle is %0.2f' % area)



    #TTS Settings
    engine = pyttsx3.init()
    engine.setProperty("volume", 0.7)
    engine.setProperty("rate", 175)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say("Ztarted LMAO")
    engine.runAndWait() #Run engine.say and wait till done
    while active: #Main loop
        #While not paused
        if not paused:
            if win32api.GetKeyState(0x01) < 0 and win32api.GetKeyState(0x02) < 0: #Left n Right MB
                start_time = datetime.now()
                ringMouf(becoilZables[activeZeapon], becoilZelays[activeZeapon])
            if win32api.GetKeyState(0x28) < 0: #PageDown
                #win32api.SetCursorPos([300, 300]) #For drawing in paint (debugging)
                activeZeapon = weapon_change(1)
                #p.terminate()
                #p = multiprocessing.Process(target=Overlay.draw, args=[weaponbloverlay[activeZeapon], scopesbloverlay[activeZcope]])
                #p.start()
                engine.say(all_weapons[activeZeapon])
                engine.runAndWait()
            if win32api.GetKeyState(0x26) < 0: #PageUp
                activeZeapon = weapon_change(-1)
                #p.terminate()
                #p = multiprocessing.Process(target=Overlay.draw, args=[weaponbloverlay[activeZeapon], scopesbloverlay[activeZcope]])
                #p.start()
                engine.say(all_weapons[activeZeapon])
                engine.runAndWait()
            if win32api.GetKeyState(0x24) < 0: #Home
                scope_change()
                #p.terminate()
                #p = multiprocessing.Process(target=Overlay.draw, args=[weaponbloverlay[activeZeapon], scopesbloverlay[activeZcope]])
                #p.start()
                engine.say(all_scopes[activeZcope])
                engine.runAndWait()
        #Doesnt Matter if Paused
        if win32api.GetKeyState(0x91) < 0: #ScrLk
            getZense()
            engine.say("Updated")
            engine.runAndWait()
        if win32api.GetKeyState(0x13) < 0: #Pause
            paused = not paused
            if paused:
                engine.say("Baused")
                engine.runAndWait()
            elif not paused:
                engine.say("Unbaused")
                engine.runAndWait()
        if win32api.GetKeyState(0x23) < 0: #End 
                engine.say("Eziting")
                #p.terminate()
                engine.runAndWait()
                active = False

if __name__ == '__main__':
    run()
    
def __del__(self):
    print("destructuring")
    ans = get_price(url)
    print(ans)


a = x()

@atexit.register
def goodbye():
    print('You are now leaving the Python sector.')
