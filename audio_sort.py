from email.mime import base
import os
from glob import glob
from posixpath import split
import random
import shutil
from turtle import onclick
import numpy as np
from pydub import AudioSegment
import array as arr
import matplotlib.pyplot as plt
from moviepy.editor import *

Data_in = "C:\\Users\\czuni\\Downloads\\lombardgrid\\"
Data_out = "C:\\Users\\czuni\\Downloads\\GRID\\"

base_audio_dir = os.path.join(Data_in,'audio\\')
base_video_dir = os.path.join(Data_in,'front\\')
base_audio_dir = glob(os.path.join(base_audio_dir, '*.wav'))
base_video_dir = glob(os.path.join(base_video_dir, '*.mov'))
print(base_audio_dir)
print(base_video_dir)

for s in base_audio_dir:
    name = s.split('\\')[6]
    name_split = name.split('_')
    folder = name_split[0]
    wrong = len(name_split)<4
    Data_out_as = Data_out+folder+'\\audio\\'
    if not os.path.isdir(Data_out_as):
        os.makedirs(Data_out_as)
    Data_out_vs = Data_out+folder+'\\video\\'
    if not os.path.isdir(Data_out_vs):
        os.makedirs(Data_out_vs)
    
    try:
        name_video_in = Data_in+'front\\'+name.split('.')[0]+'.mov'
        clip = VideoFileClip(name_video_in)
    except:
        wrong=0


    if wrong:
#       guardar audio
        name_audio_out = Data_out_as+name
        s1 = AudioSegment.from_file(s)
        s1.export(name_audio_out,format='wav')
        
#       guardar video
        name_video_in = Data_in+'front\\'+name.split('.')[0]+'.mov'
        name_video_out = Data_out_vs+name.split('.')[0]+'.mov'
    
        clip = VideoFileClip(name_video_in)
        clip.write_videofile(name_video_out, codec = "libx264") 

        print(name_audio_out+'  '+ name_video_out)
#clip = VideoFileClip("C:\\Users\\czuni\\Downloads\\lombardgrid\\front\\s55_p_lgwb7p.mov")
#clip.write_videofile("C:\\Users\\czuni\\Downloads\\lombardgrid\\s55_p_lgwb7p.mov", codec = "libx264")