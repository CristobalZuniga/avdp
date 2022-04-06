# Python program to read
# json file

import av_speech_enhancement
import mixed_speech_generator
import os
import json
import dlib
import tensorflow as tf
print(tf.__version__)
print(dlib.__version__)
#with open(r'C:\Users\czuni\source\repos\audio_visual_speech_enhancement\lombardgrid\json\s2.json') as f:
#  data = json.load(f)
#a = []
#for data_aux in data:
#  a.append(data_aux.get('SPKR')+"_"+data_aux.get('COND')+'_'+data_aux.get('UTTERANCE'))
#print(a)

#av_speech_enhancement.py mixed_speech_generator --data_dir "C:\Users\czuni\source\repos\audio_visual_speech_enhancement\lombardgrid/" --base_speaker_ids a --audio_dir "C:\Users\czuni\source\repos\audio_visual_speech_enhancement\lombardgrid/audio/"	--dest_dir "C:\Users\czuni\source\repos\audio_visual_speech_enhancement\lombardgrid/Out"	--num_samples 0	--num_mix 2	--num_mix_speakers 2

a = []
for i in range(2,56):
  file = 'C:/Users/czuni/source/repos/audio_visual_speech_enhancement/lombardgrid/json/s'+str(i)+'.json'
  with open(file) as f:
    data = json.load(f)
  for data_aux in data:
    a.append(data_aux.get('SPKR')+"_"+data_aux.get('COND')+'_'+data_aux.get('UTTERANCE'))

#print(a)

#execfile("python av_speech_enhancement.py mixed_speech_generator --data_dir 'C:/Users/czuni/source/repos/audio_visual_speech_enhancement/lombardgrid/' --base_speaker_ids a --audio_dir 'C:/Users/czuni/source/repos/audio_visual_speech_enhancement/lombardgrid/audio/' --dest_dir 'C:/Users/czuni/source/repos/audio_visual_speech_enhancement/lombardgrid/Out/' --num_samples 0 --num_mix 2")
#mixed_speech_generator --data_dir 'C:/Users/czuni/source/repos/audio_visual_speech_enhancement/lombardgrid/' --base_speaker_ids a --audio_dir 'C:/Users/czuni/source/repos/audio_visual_speech_enhancement/lombardgrid/audio/' --dest_dir 'C:/Users/czuni/source/repos/audio_visual_speech_enhancement/lombardgrid/Out/' --num_samples 0 --num_mix 2
#mixed_speech_generator('C:/Users/czuni/source/repos/audio_visual_speech_enhancement/lombardgrid/', a, 'C:/Users/czuni/source/repos/audio_visual_speech_enhancement/lombardgrid/audio/', 'C:/Users/czuni/source/repos/audio_visual_speech_enhancement/lombardgrid/Out/' , 0 , 2)
#python av_speech_enhancement.py mixed_speech_generator --data_dir 'C:/Users/czuni/source/repos/audio_visual_speech_enhancement/lombardgrid/' --base_speaker_ids a --audio_dir 'C:/Users/czuni/source/repos/audio_visual_speech_enhancement/lombardgrid/audio/' --dest_dir 'C:/Users/czuni/source/repos/audio_visual_speech_enhancement/lombardgrid/Out/' --num_samples 0 --num_mix 2
