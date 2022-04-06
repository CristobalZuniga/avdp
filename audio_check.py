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

base_speakers = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55]
#base_speakers = [2,3,4]#,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55]
data_dir =  "C:/Users/czuni/source/repos/DPRNN-Pytorch-master/GRID"
data_dir_out =  "C:/Users/czuni/source/repos/DPRNN-Pytorch-master/GRID_f"

name = []
size = []

 


for s in base_speakers:
    base_audio_dir = os.path.join(data_dir,'s'+str(s),'audio\\')
    out_audio_dir = os.path.join(data_dir_out,'s'+str(s),'audio\\')
    base_video_dir = os.path.join(data_dir,'s'+str(s),'video\\')
    out_video_dir = os.path.join(data_dir_out,'s'+str(s),'video\\')
    if not os.path.isdir(out_audio_dir):
        os.makedirs(out_audio_dir)
    if not os.path.isdir(out_video_dir):
        os.makedirs(out_video_dir)
    print(base_audio_dir)
    base_speech_list = glob(os.path.join(base_audio_dir, '*.wav'))
    for base_Speech in base_speech_list:
        s1 = AudioSegment.from_file(base_Speech)
        s1 = s1[:2000]
        
        if len(s1.get_array_of_samples())>=32000:
            name_out = out_audio_dir+base_Speech.split('\\')[3]
            s1.export(name_out,format='wav')
            
            vname_in = base_video_dir+base_Speech.split('\\')[3].split('.')[0]+'.mov'
            vname_out = out_video_dir+base_Speech.split('\\')[3].split('.')[0]+'.mov'
            my_clip = VideoFileClip(vname_in)
            video = my_clip.subclip(0,2)
            video.write_videofile(vname_out, codec = "libx264") 
        

            name.append(base_Speech)
            size.append(len(np.array(s1.get_array_of_samples())))

print(size)
print(len(size))     
plt.hist(size,10)
plt.show()