#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests

#Audio
from pydub import AudioSegment

#OS, TIME
import time
import os


# In[2]:


def get_audio_source(list_item):
    return list_item.find_element_by_xpath("span/audio/a").get_attribute('href')


# In[3]:


def get_label(list_item):
    label = list_item.get_attribute("innerHTML")
    closing_tag = "</span> "
    return label[label.find(closing_tag)+len(closing_tag):]


# In[4]:


def download_file_from_url(url,full_location):
    audio_file = requests.get(file_url)
    with open(full_location, 'wb') as download_file:
        download_file.write(audio_file.content)


# In[5]:


def convert_mp3_to_wav(mp3_file_location,wave_file_dest):
    sound = AudioSegment.from_mp3(mp3_file_location)
    sound.export(wave_file_dest, format="wav")


# In[11]:


chrome_driver = r"E:\Projects\Dota2 Reponses Extractor\chromedriver.exe"
URL = "https://dota2.gamepedia.com/Earthshaker/Responses"
download_folder = r"E:\Projects\Dota2 Reponses Extractor\wavs"
target_hero = "EarthShaker"
transcript_file = 'transcript.csv'


# In[7]:


chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : download_folder}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)


# In[8]:


browser.get(URL)


# In[9]:


list_items = browser.find_elements_by_xpath("//li[span[audio]]")


# In[10]:


for list_item in list_items:
    #print(list_item.get_attribute('innerHTML'))
    file_url = get_audio_source(list_item)
    #print(file_url)

    label = get_label(list_item)
    #print(label)
    name = label
    location = f'.//mp3s/{name}.mp3'
    
    try:
        download_file_from_url(file_url,location)
    except:
        continue

