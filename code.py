from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import subprocess
#time.sleep(120)
if datetime.datetime.now().time().hour==7:
    time.sleep(10)
    browser = webdriver.Chrome()
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day=datetime.datetime.today().weekday()
    # browser.get('http://gaana.com/playlist/gaana-dj-everyday-bhakti-'+days[day])
    browser.get('http://gaana.com/playlist/gaana-dj-shailputri-pratham-navratra')
    time.sleep(10)
    play = browser.find_element_by_id('p-list-play_all')
    play.click()
else:
    subprocess.Popen(['notify-send' , "not now"])