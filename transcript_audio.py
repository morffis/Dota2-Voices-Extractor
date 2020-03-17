#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import os
import csv


# In[2]:


def append_transcript(filename, transcript, transcript_path):
    row = f'{filename[:-4]}|{transcript}'
    with open(transcript_path,'a', newline='') as transcript_file:
        writer = csv.writer(transcript_file)
        writer.writerow([row])


# In[3]:


wav_folder = './/wavs'
transcript_path = 'transcript.csv'
target_hero = "EarthShaker"


# In[4]:


counter = 0
for file in os.listdir(wav_folder):
#file = os.listdir(wav_folder)[0]
    counter += 1
    target_filename = f'{target_hero}-{str(counter).zfill(4)}.wav'
    label = file[:-4]

    append_transcript(target_filename,label,transcript_path)

    #renaming the file
    old_file = os.path.join(wav_folder, file)
    new_file = os.path.join(wav_folder, target_filename)
    os.rename(old_file, new_file)


# In[5]:


#A better time will present itself..wav

