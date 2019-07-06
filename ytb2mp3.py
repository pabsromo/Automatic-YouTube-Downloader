# Pablo Romo
'''
Instructions:
1. Pick your YoutTube playlist to download and get it's link
2. Paste that link in the getPlaylistLinks function argument after railroad tracks
3. Run this script
4. Open the csv made of the names of all of the songs and add the metadata associated with each
5. Change the comments from mode 1 to mode 2 so that the metadata of the songs are changed according to the csv you just changed
'''

import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import os
from os import listdir
from os.path import isfile, join
import eyed3
import csv

#MODE 1 START

def getPlaylistLinks(url):
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    domain = 'https://www.youtube.com'
    for link in soup.find_all("a", {"dir": "ltr"}):
        href = link.get('href')
        if href.startswith('/watch?'):
            videos.append(domain + href)

#MODE 1 END

################################################################################

#MODE 1 START

videos = []
exists = False

# Fill the videos list with the links to be downloaded
getPlaylistLinks('https://www.youtube.com/playlist?list=PLU6vjRCwipddyONPM_xiOnk16tI0aLhWK')

for i in range(len(videos)):

    # Making the webdriver
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.implicitly_wait(50)
    driver.get('https://ytmp3.cc/')

    print(str(i) + '\n') # status

    dialog_box = driver.find_element_by_id('input')
    dialog_box.send_keys(videos[i])
    submit = driver.find_element_by_id('submit')
    submit.click()
    driver.implicitly_wait(90)
    down = driver.find_element_by_id('download')
    down.click()

time.sleep(600)
driver.close()

'''
# Get list of downloaded files from the current directory
path = 'C:\Users\Pablo Romo\Downloads'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
print(onlyfiles)
'''

# Get list of downloaded files from the specified directory no matter current location
# Rememebr that to see current directory use os.getcwd()
os.chdir("/mnt/c/Users/Pablo Romo/Downloads")
onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
print(onlyfiles)

#MODE 1 END

# ADD FUNCTIONALITY TO CREATE CSV OR EXCEL FILE OF THE LIST OF THE SONGS IN THE DOWNLOADS directory
# Use xlsxwriter python module
#   Look here for the documentation: https://xlsxwriter.readthedocs.io/

#MODE 2 START

# ADD FUNCTIONALITY TO CHANGE THE SONG METADATA ACCORDING TO THE NEWLY CHANGED CSV OR EXCEL FILE THAT WAS PREVIOUSLY CREATED

#MODE 2 END

'''
os.chdir(path)

# Load csv of song metadata
with open("Songs to be added.csv", "rb") as f:
    reader - csv.reader(f)
    meta = list(reader)

# Go through the numbered mp3s and give them the correct metadata from csv
i = 1
for filename in os.listdir(path):
        if filename.find("mp3") != -1 :
            audiofile = eyed3.load(filename)
            audiofile = eyed3.title = list[i][0]
            audiofile = eyed3.artist = list[i][1]
            audiofile = eyed3.album = list[i][2]
            audiofile.tag.save()
'''

# Useful Links and things:
# https://stackoverflow.com/questions/9567069/python-selenium-webdriver-checking-element-exists

# To use to change the metadata of the mp3 file
#   https://eyed3.readthedocs.io/en/latest/

# Renaming multiple files using python
#   https://www.geeksforgeeks.org/rename-multiple-files-using-python/

# An example of a YouTube downloader
#   https://www.geeksforgeeks.org/python-program-to-download-complete-youtube-playlist/

# Importing csv to list
#   https://stackoverflow.com/questions/24662571/python-import-csv-to-list

'''
# Rename the downloaded mp3s in list to a numbered format
# Thought I needed this but I realized that I don't and so I put this here
# because it is still pretty useful to know how to do something like this.
i = 0
os.chdir(path)
for filename in os.listdir(path):
        if filename.find("mp3") != -1 :
            print(filename)
            dst = "song" + str(i) + ".mp3"
            src = filename

            os.rename(src, dst)
            i += 1
'''

# For the libmagic error with eyed3
#   https://stackoverflow.com/questions/46518690/pip-installing-eyed3-module-failed-to-find-libmagic

# Remember that to use selenium you need to have chromedriver in the C:\Windows\System32 folder if it needs to be updated
